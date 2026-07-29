# -*- coding: utf-8 -*-
{
    'name': "milestone_task",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'Task',
    'summary': 'automatic add delivery product',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': True,
    'depends': ['base', 'purchase', 'sale_management', 'project'],
    'data':[

        "views/sale_order_views.xml",



    ],
}
