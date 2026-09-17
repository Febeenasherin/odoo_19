# -*- coding: utf-8 -*-
{
    'name': "Multi-step approve for Vendor bill",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'internal transfer',
    'summary': 'Multistep approve for vendor bill',
    'description': """mullti step approve for vendor bill""",
    'website': 'http://www.cybrosys.com',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'purchase','account'],
    'data':[

            "security/group_rule.xml",
            "views/account_move_views.xml",

     ],
}

