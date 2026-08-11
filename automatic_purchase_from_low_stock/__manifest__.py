# -*- coding: utf-8 -*-
{
    'name': "Automatic purchase from low stock",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'product',
    'summary': 'automatic purchase product from low stock',
    'description': """automatic purchse product""",
    'website': 'http://www.cybrosys.com',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'stock', 'purchase',],
    'data':[
            "/home/cybrosys/odoo-19/custom/automatic_purchase_from_low_stock/data/ir_cron_data.xml",

     ],
}

