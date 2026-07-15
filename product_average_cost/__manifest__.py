# -*- coding: utf-8 -*-
{
    'name': "product_average_cost",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'product',
    'summary': 'average cost of products',
    'description': """vendor product average cost """,
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'purchase', 'sale'],
    'data':[
        "views/product_product_views.xml",
        "views/product_template_views.xml",
        "views/product_average_cost_menu.xml",
        "wizard/sale_order_wizard_views.xml",


    ],
}

