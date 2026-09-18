# -*- coding: utf-8 -*-
{
    'name': "Daily work report tracker",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'sale',
    'summary': 'work report',
    'description': """daily work report""",
    'website': 'http://www.cybrosys.com',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'contacts','hr'],
    'data':[
            "security/ir.model.access.csv",
            "data/alias.xml",
            "views/hr_employee_views.xml",
            "views/work_report_view.xml",
            "views/daily_work_report_menu.xml",
     ],
}

