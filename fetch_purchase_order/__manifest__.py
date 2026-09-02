# -*- coding: utf-8 -*-
{
    'name': "Fetch Purchase order",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'Attendance',
    'summary': 'migrate purchase order from odoo16 to odoo19',
    'description': """migrate purchase order""",
    'website': 'http://www.cybrosys.com',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'purchase'],
    'data':[
        "security/ir.model.access.csv",
        "wizard/purchase_migraton_wizard_views.xml",
        "/home/cybrosys/odoo-19/custom/fetch_purchase_order/views/purchase_order_views.xml",
     ],
}

