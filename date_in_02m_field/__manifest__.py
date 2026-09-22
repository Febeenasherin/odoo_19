# -*- coding: utf-8 -*-
{
    'name': "Date in O2M field",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'Project',
    'summary': 'date in o2m field',
    'description': """date in o2m field""",
    'website': 'http://www.cybrosys.com',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'project'],
    'data':[
            "security/ir.model.access.csv",
            "views/project_date_line_views.xml",
            "views/project_project_views.xml",
     ],
}

