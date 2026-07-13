# -*- coding: utf-8 -*-
{
    'name': "Vendor_product_list",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'Product',
    'summary': 'Vendor product list',
    'description': """vendor product list""",
    'sequence': 10,
    'application': True,
    'installable': True,
    'auto_install': True,
    'depends': ['base','purchase',],
    'data':[

        "views/purchase_order_views.xml",

    ],
}


