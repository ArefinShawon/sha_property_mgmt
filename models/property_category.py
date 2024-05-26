# -*- coding: utf-8 -*-
#############################################################################
#    ElitBuzz Technologies Ltd.(<https://elitbuzz-bd.com>)
#    Author: Hasinur Arefin Shawon
#############################################################################
from odoo import fields, models, api


class PropertyKatha(models.Model):
    _name = 'property.katha'
    _description = "Property Measurement in Katha"
    _inherit = ['mail.thread']
    _rec_name = 'property_size'

    sequence = fields.Integer()
    property_size = fields.Char(string="Property Size", compute='_compute_property_katha')
    property_katha = fields.Char(string="Property Katha", required=True, tracking=True)
    property_sqft1 = fields.Char(string="Width", tracking=True)
    property_sqft2 = fields.Char(string="Length", tracking=True)

    @api.onchange('property_katha', 'property_sqft1', 'property_sqft2')
    def _compute_property_katha(self):
        for rec in self:
            if rec.property_katha and rec.property_sqft1 and rec.property_sqft2:
                rec.property_size = f"{rec.property_katha} Katha ({rec.property_sqft1}' X {rec.property_sqft2}')"
            else:
                rec.property_size = rec.property_katha


class PropertyBlock(models.Model):
    _name = 'property.block'
    _description = "Property Measurement in Block"
    _inherit = ['mail.thread']
    _rec_name = 'property_block'

    sequence = fields.Integer()
    property_block = fields.Char(string="Block", required=True, tracking=True)


class PropertyTag(models.Model):
    _name = 'property.tag'
    _description = 'Property Tag'
    _rec_name = 'tag'

    tag = fields.Char(string='Tag', required=True, help='Name of the tag')
