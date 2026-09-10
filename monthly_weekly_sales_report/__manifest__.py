# -*- coding: utf-8 -*-
{
    'name': "Monthly Weekly sale  Report",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'sales',
    'summary': 'monthy or weekly sale report report',
    'description': """ weekly monthly sale report """,
    'website': 'http://www.cybrosys.com',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'sale_management'],
    'data':[
            "security/ir.model.access.csv",
            "views/monthly_weekly_sale_report_views.xml",
            "/home/cybrosys/odoo-19/custom/monthly_weekly_sales_report/data/ir_cron_data.xml",
     ],
}

