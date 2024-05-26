# -*- coding: utf-8 -*-
#############################################################################
#    ElitBuzz Technologies Ltd.(<https://elitbuzz-bd.com>)
#    Author: Hasinur Arefin Shawon
#############################################################################
from odoo import fields, models


class PropertyFacility(models.Model):
    _name = 'property.facility'
    _description = 'Property Facility'
    _rec_name = 'facility'

    facility = fields.Char(string='Facility', required=True, help='Facilities of the property')


class PropertyNearbyConnectivity(models.Model):
    _name = 'property.nearby.connectivity'
    _description = 'Property Nearby Connectivity'

    name = fields.Char(string="Name", required=True, help='Name of the nearby connectivity for the property')
    direction = fields.Selection([('north', 'North'), ('south', 'South'),
                                  ('east', 'East'), ('west', 'West')],
                                 string='Direction', help='To which direction is the nearby connectivity')
    kilometer = fields.Float(string="Kilometer", required=True,
                             help='The distance between the property and nearby connectivity in kilometers')
    property_id = fields.Many2one('property.property', string="Property Name", help='The related property')
