# -*- coding: utf-8 -*-
#############################################################################
#    ElitBuzz Technologies Ltd.(<https://elitbuzz-bd.com>)
#    Author: Hasinur Arefin Shawon
#############################################################################
from odoo import models, fields, api, _


class PropertyProperty(models.Model):
    _name = 'property.property'
    _description = "Property Model"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "code"

    plot_name = fields.Char(string="Plot", compute='_compute_plot_name')
    code = fields.Char(string="Reference", readonly=True, default=lambda self: _("New"))
    plot_number = fields.Char(string="Plot Number", required=True, copy=False)
    state = fields.Selection([
        ("draft", "Draft"),
        ("available", "Available"),
        ("sold", "Sold")
    ], required=True, string="Status", default="draft")
    street = fields.Text(string="Address")
    company_id = fields.Many2one("res.company", string="Property Management Company",
                                 default=lambda self: self.env.company)
    currency_id = fields.Many2one("res.currency", string="Currency", related="company_id.currency_id")
    image = fields.Binary(string="Image", help="Image of the property")
    landlord_id = fields.Many2one("res.partner", string="LandLord", help="The owner of the property")
    description = fields.Html(string="Description", help="A brief description about the property")
    responsible_id = fields.Many2one("res.users", string="Responsible Person")
    property_type = fields.Selection([
        ("land", "Land"),
        ("residential", "Residential"),
        ("commercial", "Commercial"),
        ("industry", "Industry"),
    ], string="Type", help="The type of the property", default="land")
    property_block_ids = fields.Many2one('property.block', string="Block")
    property_size_ids = fields.Many2one('property.katha', string="Katha")
    land_name = fields.Char(string="Land Name", help="The name of the land")
    usage = fields.Char(string="Used For", help="For what purpose is this property used for")
    property_image_ids = fields.One2many("property.image", "property_id", string="Property Images")
    area_measurement_ids = fields.One2many("property.area.measure", "property_id", string="Area Measurement")
    total_sq_feet = fields.Float(string="Total Square Feet", compute="_compute_total_sq_feet")
    facilities_ids = fields.Many2many('property.facility', string="Facilities")
    nearby_connectivity_ids = fields.One2many("property.nearby.connectivity", "property_id",
                                              string="Nearby Connectives")
    property_tags = fields.Many2many("property.tag", string="Property Tags")
    attachment_id = fields.Many2one("ir.attachment", string="Attachment")
    unit_price = fields.Monetary(string="Sales Price", currency_field='currency_id')
    sale_id = fields.Many2one("property.sale", string="Sale Order", tracking=True)

    is_installment_payment = fields.Boolean(string="Installment Payment", help="Payments are made in installment")
    monthly_or_yearly = fields.Selection([('monthly', 'Monthly'),
                                          ('yearly', 'Yearly')],
                                         string="Monthly / Yearly",
                                         help="Automatically selects the Contract Period",
                                         tracking=True)
    no_of_months = fields.Integer(string="Number of Months")
    no_of_years = fields.Integer(string="Number of Years")
    no_of_installments = fields.Integer(string="Number of Installments", compute='_compute_installments', store=True)
    amount_per_installment = fields.Float(string="Amount Per Installment", compute='_compute_installments', store=True)

    @api.model
    def create(self, vals):
        if vals.get("code", "New") == "New":
            vals["code"] = (
                    self.env["ir.sequence"].next_by_code("property.property") or "New"
            )
        res = super(PropertyProperty, self).create(vals)
        return res

    @api.onchange('plot_number', 'property_block_ids', 'property_size_ids')
    def _compute_plot_name(self):
        for rec in self:
            if rec.plot_number and rec.property_block_ids and rec.property_size_ids:
                rec.plot_name = f"{rec.property_block_ids.property_block} - {rec.property_size_ids.property_size} - Plot {rec.plot_number} "
            else:
                rec.plot_name = rec.plot_number

    def _compute_total_sq_feet(self):
        for rec in self:
            rec.total_sq_feet = sum(rec.mapped("area_measurement_ids").mapped("area"))

    def action_available(self):
        self.state = "available"

    def action_draft(self):
        self.state = "draft"

    def action_property_sale_view(self):
        return {
            "name": "Property Sale: " + self.code,
            "view_mode": "tree,form",
            "res_model": "property.sale",
            "type": "ir.actions.act_window",
            "res_id": self.sale_id.id,
        }

    @api.depends('unit_price', 'no_of_months', 'no_of_years')
    def _compute_installments(self):
        for record in self:
            if record.no_of_months or record.no_of_years:
                record.no_of_installments = record.no_of_months or record.no_of_years
                if record.unit_price:
                    record.amount_per_installment = record.unit_price / record.no_of_installments
            else:
                record.no_of_installments = 0
                record.amount_per_installment = 0.00
