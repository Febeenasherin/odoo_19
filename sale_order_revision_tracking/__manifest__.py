# -*- coding: utf-8 -*-
{
    'name': "Sale order revision tracking",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'sale',
    'summary': 'restrict user in sale',
    'description': """saleorder revision tracking""",
    'website': 'http://www.cybrosys.com',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'sale_management'],
    'data':[
            "security/ir.model.access.csv",
            "views/sale_order_views.xml",
            "views/sale_order_revision_views.xml",
     ],
}

