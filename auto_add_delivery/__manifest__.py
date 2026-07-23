# -*- coding: utf-8 -*-
{
    'name': "auto_add_delivery",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'product',
    'summary': 'automatic add delivery product',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'purchase', 'sale'],
    'data':[
            "data/sale_order_data.xml",



    ],
}
