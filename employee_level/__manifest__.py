# -*- coding: utf-8 -*-
{
    'name': "Employee level",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'employee',
    'summary': 'daily attendance report',
    'description': """sale order""",
    'website': 'http://www.cybrosys.com',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'hr'],
    'data':[
            "security/ir.model.access.csv",
            "views/employee_level_views.xml",

            "views/employee_menu_views.xml",
            "views/hr_employee_views.xml",


     ],
}

