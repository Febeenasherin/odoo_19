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
    'depends': ['base', 'mrp'],
    'data':[
            "security/ir.model.access.csv",
            "views/simple_production.xml",
            "views/simple_production_line_view.xml",
            "views/menu.xml",
    ],
    }