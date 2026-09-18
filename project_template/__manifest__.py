# -*- coding: utf-8 -*-
{
    'name': "Project template",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'project',
    'summary': 'average cost of products',
    'description': """project and task template""",
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'project'],
    'data':[

            "security/ir.model.access.csv",
            "security/group.xml",
            "views/project_template_views.xml",
            "views/project_task_template_views.xml",
            "views/project_task_views.xml",
            "views/project_project_views.xml",
            "views/project_project_task_views.xml",

            "views/project_project_menu.xml",

    ],
}

