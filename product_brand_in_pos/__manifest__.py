# -*- coding: utf-8 -*-
{
    'name': "Product Brand in POS",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'Brand',
    'summary': 'product brand in pos',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': True,
    'depends': ['base', 'point_of_sale'],
    'data':[
            "views/product_template.xml",

      ],

    'assets': {
            'point_of_sale._assets_pos': [
                "product_brand_in_pos/static/src/xml/pos_order_line.xml"
            ]
    },

}