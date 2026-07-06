# -*- coding: utf-8 -*-
from odoo import fields, models


class SchoolExam(models.Model):
    """ exams for students"""
    _name = 'school.exam'
    _description = 'School Exam'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    class_id = fields.Many2one('school.class', string='Class', required=True)
    # subject_id = fields.Many2one('school.subject', string='Subject')
    paper_ids = fields.One2many('school.exam.paper', 'exam_id')
    start_date = fields.Datetime(string='Start Date')
    end_date = fields.Datetime(string='End Date')
    user_id = fields.Many2one('res.users', string='User')


    def action_exam(self):
        """ adding exam for students while clicking add button"""

        for student in self.class_id.student_ids:
            student.exam_ids = [(self.id)]
        print(self.class_id.student_ids)

        # students = self.env['school.students'].search([('class_id', '=', self.class_id.id)])
        #
        # for rec in students:
        #     rec.exam_ids = [(self.id)]








