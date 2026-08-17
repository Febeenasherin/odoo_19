# -*- coding: utf-8 -*-
{
    'name': "Import Lot and Serial Number",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'lot or serial number',
    'summary': 'lot or serial number',
    'description': """import excel sheet""",
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'stock',],
    'data':[
            "security/ir.model.access.csv",

            "wizard/wizard_views.xml"


    ],
}