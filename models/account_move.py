# -*- coding: utf-8 -*-
#############################################################################
#    ElitBuzz Technologies Ltd.(<https://elitbuzz-bd.com>)
#    Author: Hasinur Arefin Shawon
#############################################################################
from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    property_order_id = fields.Many2one('property.sale', string="Property Order ID",
                                        help='The corresponding property ''sale order')