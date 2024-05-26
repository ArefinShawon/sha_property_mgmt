# -*- coding: utf-8 -*-
#############################################################################
#    ElitBuzz Technologies Ltd.(<https://elitbuzz-bd.com>)
#    Author: Hasinur Arefin Shawon
#############################################################################
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    blacklisted = fields.Boolean(string='Blacklisted', default=False,
                                 help='Is this contact a blacklisted contact or not')

    def action_add_blacklist(self):
        self.blacklisted = True

    def action_remove_blacklist(self):
        self.blacklisted = False
