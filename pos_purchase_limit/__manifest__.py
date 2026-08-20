# -*- coding: utf-8 -*-
{
    'name': "POS Purchase Limit",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'product',
    'summary': 'set limit of purchase product',
    'description': """purchase limit""",
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'point_of_sale', 'contacts'],
    'data':[
        "views/res_partner_views.xml",

    ],
}

