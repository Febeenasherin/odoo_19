# -*- coding: utf-8 -*-
{
    'name': "restrict_delete_product",
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
    'depends': ['base', 'sale_management'],
    'data':[
                "data/sequence.xml",

                "views/product_category_views.xml",

    ],
}

