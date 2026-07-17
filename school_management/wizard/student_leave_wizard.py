# -*- coding: utf-8 -*-
from odoo import fields, models, api
from datetime import date, timedelta



class StudentLeaveWizard(models.TransientModel):
    """student information report"""
    _name = "student.leave.wizard"
    _description = "Student Leave Wizard"


    filter_type = fields.Selection([('day', 'Day'),
    ('week', 'Week'), ('month', 'Month'), ('custom', 'Custom')], string='Filter Type',)

    start_date = fields.Date()
    end_date = fields.Date()
    student_id = fields.Many2one('school.students', string='Student')

    # student_id = fields.Many2one(related='class_id.student_id', string='Student')
    class_id = fields.Many2one(related='student_id.class_id', string='Class', readonly=False)



    def action_print(self):
        """report show ,is the student name is selected it show that student leave information.
        if class is selected ,show leave based on class.if the day selected show today leaves,or week selected show weekly report,
        or month selected show monthly, if custom selected show leave based on we selected date range."""


        # domain = []
        #
        # if self.student_id:
        #     domain.append(('student_id', '=', self.student_id.id))
        #
        #
        #
        # print("domain", domain)
        #
        # if self.class_id:
        #     domain.append(('class_id', '=', self.class_id.id))
        #
        # today = date.today()
        # if self.filter_type == 'day':
        #     domain += [('start_date', '=', today)]
        #
        #     print(domain)
        #
        # elif self.filter_type == 'week':
        #     week_start = today - timedelta(days=today.weekday())
        #     week_end = week_start + timedelta(days=6)
        #
        #     domain += [('start_date', '>=', week_start), ('start_date', '<=', week_end)]
        #
        #     print(domain)
        #
        # elif self.filter_type == 'month':
        #     month_start = today.replace(day=1)
        #
        #     domain += [('start_date', '>=', month_start), ('start_date', '<=', today)]
        #
        #     print("month",domain)
        #
        # elif self.filter_type == 'custom':
        #
        #     domain +=[('start_date', '>=', self.start_date)]
        #     domain += [('end_date', '<=', self.end_date)]
        #
        #     print("custom",domain)
        #
        # leave_info = self.env['school.leaves'].search(domain)
        #
        # print("info",leave_info)

        # return self.env.ref('school_management.action_report_school_leave').report_action(self,data = {'ids' : leave_info.ids})



        return self.env.ref('school_management.action_report_school_leave').report_action(self)














 # elif self.filter_type == 'week':
        #     week_start = today - timedelta(days=today.weekday())
        #     week_end = week_start + timedelta(days=6)
        #
        #     domain += [('start_date', '<=', week_start), ('end_date', '>=', week_end)]
        #
        # elif self.filter_type == 'month':
        #     month_start = today - timedelta(days=today.month)
        #
        #     domain += [('start_date', '<=', month_start), ('end_date', '>=', month_start)]
        #
        # elif self.filter_type == 'custom':
        #     domain +=[('start_date', '=', self.start_date), ('end_date', '=', self.end_date)]

