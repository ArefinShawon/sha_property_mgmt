# -*- coding: utf-8 -*-
#############################################################################
#    ElitBuzz Technologies Ltd.(<https://elitbuzz-bd.com>)
#    Author: Hasinur Arefin Shawon
#############################################################################
from odoo import fields, models


class PropertyCommission(models.Model):
    _name = 'property.commission'
    _description = 'Property Commission'

    name = fields.Char(string='Commission Name', help="Name of commission plan", required=True)
    commission_type = fields.Selection([('fixed', 'Fixed'),
                                        ('percentage', 'Percentage')],
                                       string='Commission Type', required=True,
                                       help='The type of the commission either fixed or a percentage')
    commission = fields.Float(string='Commission Rate', help="Commission calculating value.")
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
