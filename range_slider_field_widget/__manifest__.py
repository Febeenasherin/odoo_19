# -*- coding: utf-8 -*-
{
    'name': "Range slider field widget",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'tool',
    'summary': 'add field slider widget',
    'description': """sale order""",
    'website': 'http://www.cybrosys.com',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'demo': ['Demo'],
    'depends': ['base', 'product'],

    'data':[

            "security/ir.model.access.csv",
            "views/slider_widget_views.xml",
            "views/menu.xml",
     ],
    'assets': {
        'web.assets_backend': [
            "range_slider_field_widget/static/src/xml/slider_widget.xml",
             "range_slider_field_widget/static/src/js/slider_widget.js",
        ],


   },
}

