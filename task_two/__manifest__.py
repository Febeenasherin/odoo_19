# -*- coding: utf-8 -*-
{
    'name': "order quantity",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'product',
    'summary': 'ordered',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': True,
    'depends': ['base', 'contacts', 'sale_management'],
    'data':[
           "views/res_partner_views.xml",
        '/home/cybrosys/odoo-19/custom/task_two/views/sale_order_views.xml',

    ],
    }