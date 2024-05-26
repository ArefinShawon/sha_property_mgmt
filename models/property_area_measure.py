# -*- coding: utf-8 -*-
#############################################################################
#    ElitBuzz Technologies Ltd.(<https://elitbuzz-bd.com>)
#    Author: Hasinur Arefin Shawon
#############################################################################
from odoo import fields, models, api


class PropertyAreaMeasure(models.Model):
    _name = 'property.area.measure'
    _description = 'Property Area Measurement'

    name = fields.Char(string='Section', required=True,
                       help='Name of the room or section')
    length = fields.Float(string='Length(ft)', help='The length of the room')
    width = fields.Float(string='Width(ft)', help='The width of the room')
    height = fields.Float(string='Height(ft)', help='The height of the room')
    area = fields.Float(string='Area(ft²)', compute='_compute_area',
                        help='The total area of the room')
    property_id = fields.Many2one('property.property', string='Property',
                                  help='The corresponding property')

    @api.depends('length', 'width', 'height')
    def _compute_area(self):
        for rec in self:
            rec.area = rec.length * rec.width
