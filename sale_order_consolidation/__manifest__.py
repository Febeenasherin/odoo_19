# -*- coding: utf-8 -*-
{
    'name': "Sale order consolidation",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'Task',
    'summary': 'automatic add delivery product',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': True,
    'depends': ['base','sale_management'],
    'data':[

        "/home/cybrosys/odoo-19/custom/sale_order_consolidation/security/ir.model.access.csv",
            "data/ir_cron_data.xml",
        # "/home/cybrosys/odoo-19/custom/sale_order_consolidation/views/sale_order_views.xml",
        "/home/cybrosys/odoo-19/custom/sale_order_consolidation/wizard/sale_order_views.xml",
    "/home/cybrosys/odoo-19/custom/sale_order_consolidation/wizard/sale_order_wizard_vies.xml",],
}
