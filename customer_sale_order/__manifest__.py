# -*- coding: utf-8 -*-
{
    'name': "Customer sale order",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'sale',
    'summary': 'sale order',
    'description': """sale order""",
    'website': 'http://www.cybrosys.com',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'contacts', 'sale_management','purchase'],
    'data':[
            "security/ir.model.access.csv",
            "data/ir_cron_data.xml",
            "views/res_partner.xml",
            "views/product_product_views.xml",
            "views/purchase_order_histor_views.xml",
            "views/menu_vies.xml",

     ],
}

