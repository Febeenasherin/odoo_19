# -*- coding: utf-8 -*-
{
    'name': "Bill of Materials in Cart",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'product',
    'summary': 'bill of meterials',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': True,
    'depends': ['base','website', 'website_sale', 'mrp'],
    'data':[
            "views/website_menu.xml",
            "views/website_template.xml",


   ],
}
