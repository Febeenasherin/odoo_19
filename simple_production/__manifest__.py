# -*- coding: utf-8 -*-
{
    'name': "Simple production",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'product',
    'summary': 'simple production',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': True,
    'depends': ['base', 'mrp', 'stock'],
    'data':[
            "security/ir.model.access.csv",
            "views/simple_production.xml",
            "data/sequence_data.xml",
            "views/simple_production_line_view.xml",
            "views/production_order_views.xml",
            "views/production_order_line_views.xml",
            "views/menu.xml",
    ],
    }