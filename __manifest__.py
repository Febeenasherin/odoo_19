# -*- coding: utf-8 -*-
{
    'name': "School_Management",
    'version': "19.0.1.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'website': 'https://www.cybrosys.com',
    'category': '   Education',
    'summary': 'School Management',
    'description': """manage student,subject,department""",
    'sequence': 10,
    'application': True,
    'installable': True,
    'auto_install': True,
    'data':["security/ir.model.access.csv",
        "views/action_view_students.xml",
        "views/action_dep.xml",
        "views/action_class.xml",
        "views/action_sub.xml",
        "data/sequence.xml",
        "views/action_year.xml",
        "views/student_menu.xml",

]


}