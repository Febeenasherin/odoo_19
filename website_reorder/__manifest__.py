# -*- coding: utf-8 -*-
{
    'name': "Website Reorder",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'Order',
    'summary': 'reorder product from sale order',
    'description': """reorder the same product in sale order""",
    'website': 'http://www.cybrosys.com',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'website', 'website_sale',],
    'data':[

            "views/sale_order_portal_views.xml",
            "views/portal_my_orers_views.xml",
     ],
}

