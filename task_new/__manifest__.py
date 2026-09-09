# -*- coding: utf-8 -*-
{
    'name': "Update delivery",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'sale',
    'summary': 'sale_order',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': True,
    'depends': ['base','sale_management'],
    'data':[
        "/home/cybrosys/odoo-19/custom/task_new/security/ir.model.access.csv",

       "data/action_update_delivery.xml",
        "/home/cybrosys/odoo-19/custom/task_new/wizard/sale_order_wizard_vies.xml",



    ],
}
