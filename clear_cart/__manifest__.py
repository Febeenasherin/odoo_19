# -*- coding: utf-8 -*-
{
    'name': "clear_cart",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'sale',
    'summary': 'clear website sale cart',
    'description': """clear cart""",
    'website': 'http://www.cybrosys.com',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'website', 'website_sale',],
    'data':[
            "views/website_sale.xml",

     ],
}

