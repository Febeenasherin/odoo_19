# -*- coding: utf-8 -*-
{
    'name': "School_Management",
    'version': "19.0.1.0.0",
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
    'depends': ['base','mail',],
    'data':["security/ir.model.access.csv",
        "views/school_students_view.xml",
        "views/school_department_views.xml",
        "views/school_class_views.xml",
        "views/school_subject_views.xml",
        "data/sequence_data.xml",
        "data/school_class_data.xml",
        "data/school_department_data.xml",
        "data/school_subject_data.xml",
        "data/admission_no_data.xml",
        "views/school_year_views.xml",
        "views/school_clubs_views.xml",
        "views/school_events_views.xml",
        "views/student_menu_views.xml",

        ],


    # 'post_init_hook': 'create_default_department',
    # 'post_init_hook':'create_default_class',
    #





}   