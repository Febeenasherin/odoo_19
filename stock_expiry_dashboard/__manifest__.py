# -*- coding: utf-8 -*-
{
    'name': "Stock Expiry Dashboard",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'dashboard',
    'summary': 'stock expiry dashboard',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': True,
    'depends': ['base', 'stock'],
    'data':[
                "security/ir.model.access.csv",
                "views/stock_expiry_views.xml",
    ],

#     'assets': {
#         'web.assets_backend': [
#                     "stock_expiry_dashboard/static/src/js/dashboard.js",
#                     "stock_expiry_dashboard/static/src/xml/dashboard.xml",
#    ],
# },
    }