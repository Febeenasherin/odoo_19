# -*- coding: utf-8 -*-
{
    'name': "restricted vendor",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'sales',
    'summary': 'restricted vendor',
    'description': """  restricted vendor""",
    'website': 'http://www.cybrosys.com',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'purchase'],
    'data':[
                "views/res_partner_views.xml",
                "views/purchase_order_views.xml",
     ],
}

