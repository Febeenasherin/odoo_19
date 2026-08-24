# -*- coding: utf-8 -*-
{
    'name': "Remove orderlines pos",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'POS',
    'summary': 'remove order line when clicking button',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': True,
    'depends': ['base', 'point_of_sale'],
    'data':[


      ],

    'assets': {
            'point_of_sale._assets_pos': [

                "remove_orderline_pos/static/src/xml/pos_orderline_views.xml",
                "remove_orderline_pos/static/src/js/pos_orderline.js",
                "remove_orderline_pos/static/src/xml/remove_orderline.xml",
            ]
    },

}