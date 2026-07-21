# -*- coding: utf-8 -*-
from odoo import fields, models, api
from datetime import timedelta, date


class StudentInformation(models.TransientModel):
    """student information wizard"""
    _name = 'student.information'

    #
    # filter_type = fields.Selection([('class', 'Class'), ('department', 'Department')], default='class')
    class_id = fields.Many2one('school.class')
    department_id = fields.Many2one('school.department')

    def action_print_student_information(self):
        """ show report of students based on class and department"""


        return self.env.ref('school_management.action_report_student').report_action(self)





    # domain = []
        #
        # if self.class_id:
        #     domain += [('class_id', 'in', self.class_id.id)]
        #
        #     print("class",domain)
        #
        #
        # if self.department_id:
        #     domain += [('department_id', 'in', self.department_id.id)]
        #
        #     print("dep",domain)
        #
        # student_info = self.env['school.students'].search(domain)
        #
        # print("info", student_info)



