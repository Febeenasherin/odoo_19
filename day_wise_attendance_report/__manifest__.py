# -*- coding: utf-8 -*-
{
    'name': "Daily Attendance Report",
    'version': "19.0.1.0.0",
    'license':"LGPL-3",
    'author': "Cybrosys Techno Solutions",
    'category': 'Attendance',
    'summary': 'daily attendance report',
    'description': """sale order""",
    'website': 'http://www.cybrosys.com',
    'sequence': 2,
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'hr_attendance'],
    'data':[

            "/home/cybrosys/odoo-19/custom/day_wise_attendance_report/data/email_template.xml",
            "/home/cybrosys/odoo-19/custom/day_wise_attendance_report/data/ir_cron_data.xml",
            "views/hr_attendance_views.xml",

            "/home/cybrosys/odoo-19/custom/day_wise_attendance_report/report/attendance_report.xml",
            "/home/cybrosys/odoo-19/custom/day_wise_attendance_report/report/ir_action_report.xml",
     ],
}

