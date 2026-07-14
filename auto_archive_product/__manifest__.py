# -*- coding: utf-8 -*-
{
    'name': "auto_archive_product",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'product',
    'summary': 'auto archive product',
    'description': """auto archive product""",
    'website': 'http://www.cybrosys.com',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'purchase', 'sale',],
    'data':[
        "data/ir_cron_data.xml",

     ],
}

