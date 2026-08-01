# -*- coding: utf-8 -*-
{
    'name': "Employee Loan management",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'product',
    'summary': 'employee loan management',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': True,
    'depends': ['base','hr'],
    'data':[
            "data/sequence_data.xml",
            "security/ir.model.access.csv",
            "views/employee_loan_views.xml",
            "views/employee_menu.xml",
       "views/employee_loan_line_views.xml",



    ],
}
