# -*- coding: utf-8 -*-
{
    'name': "Restrict delivery",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'Attendance',
    'summary': 'restrict delivery',
    'description': """sale order""",
    'website': 'http://www.cybrosys.com',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'sale_management'],
    'data':[

            "views/sale_order_views.xml",
     ],
}

