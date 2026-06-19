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
    'depends': ['mail',],
    'data':["security/ir.model.access.csv",
        "views/school_students_view.xml",
        "views/school_department_view.xml",
        "views/school_class_view.xml",
        "views/school_subject_view.xml",
        "data/sequence_data.xml",
        "views/school_year_view.xml",
        "views/student_menu_view.xml",

]
}   