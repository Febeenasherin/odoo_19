# -*- coding: utf-8 -*-
{
    'name': "Mandatory Attachment Before Confirming Purchase Order",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'purchase',
    'summary': 'mandatory attachment',
    'description': """mandatory attachment""",
    'website': 'http://www.cybrosys.com',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'purchase'],
    'data':[
            "views/res_config_settings_views.xml",
            "views/purchase_order_view.xml",

     ],
}

