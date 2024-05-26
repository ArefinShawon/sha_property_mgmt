# -*- coding: utf-8 -*-
#############################################################################
#    ElitBuzz Technologies Ltd.(<https://elitbuzz-bd.com>)
#    Author: Hasinur Arefin Shawon
#############################################################################
{
    'name': "Advanced Property Management | Real Estate",
    'version': '16.0.1.0.0',
    'category': 'Industries',
    'summary': """Manage your properties sale""",
    'description': """The module makes it simple for you to manage
     your properties""",
    'author': "ElitBuzz Technologies Ltd.",
    'company': 'ElitBuzz Technologies Ltd.',
    'maintainer': 'ElitBuzz Technologies Ltd.',
    'sequence': 0,
    'price': '0.0',
    'currency': 'USD',
    'website': 'https://elitbuzz-bd.com',
    'depends': ['base', 'mail', 'sale_management'],
    'data': [
        'security/user_groups.xml',
        'security/property_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/property_property_views.xml',
        'views/property_category_view.xml',
        'views/property_facility_views.xml',
        'views/property_tag_views.xml',
        'views/property_commision_views.xml',
        'views/property_sale_views.xml',
        'views/property_search_pannel_views.xml',
        'views/res_partner_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
