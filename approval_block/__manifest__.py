# -*- coding: utf-8 -*-
{
    'name': "Approval block",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'website': 'https://www.cybrosys.com',
    'category': 'Approval',
    'summary': 'Approval Block',
    'description': """approval block """,
    'sequence': 10,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'purchase'],
    'data':[
        "data/approval_block_data.xml",
        "security/ir.model.access.csv",
        "views/approval_block_views.xml",
        "views/approval_block_menu_views.xml",
        "views/purchase_order_views.xml",
    ],
}

