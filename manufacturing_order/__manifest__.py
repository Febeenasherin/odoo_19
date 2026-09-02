# -*- coding: utf-8 -*-
{
    'name': "Manufaccturing Order",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'Manufacturing order',
    'summary': 'manufacturing order',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': True,
    'depends': ['base', 'mrp', 'contacts', 'stock'],
    'data':[
        "/home/cybrosys/odoo-19/custom/manufacturing_order/security/ir.model.access.csv",
        "/home/cybrosys/odoo-19/custom/manufacturing_order/data/sequence_data.xml",
        "/home/cybrosys/odoo-19/custom/manufacturing_order/views/mrp_production_views.xml",
        "/home/cybrosys/odoo-19/custom/manufacturing_order/views/production_menu.xml",
      ],
}
