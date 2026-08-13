# -*- coding: utf-8 -*-
{
    'name': "Material Request",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'Material Request',
    'summary': 'material request',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': True,
    'depends': ['base', 'purchase', 'contacts', 'stock'],
    'data':[
            "security/material_request_group.xml",
            "security/ir.model.access.csv",

            "views/material_request_views.xml",
            "views/material_request_line.xml",
            "views/matterial_request_menu_views.xml",
      ],
}
