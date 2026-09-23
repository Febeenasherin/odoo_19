# -*- coding: utf-8 -*-
{
    'name': "CRM Dashboard",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'CRM',
    'summary': 'crm Dashboard',
    'description': """crm dashboard""",
    'website': 'http://www.cybrosys.com',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'crm'],
    'data':[
            "views/dashbooard_views.xml",
     ],

    'assets': {
        'web.assets_backend': [
            'crm_dashboard/static/src/js/crm_dashboard.js',
            'crm_dashboard/static/src/xml/crm_dashboard.xml',
   ],
},
}

