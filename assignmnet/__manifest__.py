# -*- coding: utf-8 -*-
{
    'name': "approve product",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'website': 'https://www.cybrosys.com',
    'category': 'Approval',
    'summary': 'Approval Block',
    'description': """approval block """,
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'purchase', 'sale_management'],
    'data':[
        "security/ir.model.access.csv",

        "views/puchase_order.xml",
        "views/customer_views.xml",
        "views/product_product_views.xml",

    ],
}

