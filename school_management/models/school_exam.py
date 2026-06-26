# -*- coding: utf-8 -*-
from odoo import fields, models


class SchoolExam(models.Model):
    """ exams for students"""
    _name = 'school.exam'
    _description = 'School Exam'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    class_id = fields.Many2one('school.class', string='Class')
    # subject_id = fields.Many2one('school.subject', string='Subject')
    paper_ids = fields.One2many('school.exam.paper', 'exam_id', string='Exams')
    start_date = fields.Datetime(string='Start Date')
    end_date = fields.Datetime(string='End Date')

    def action_exam(self):
        students = self.env['school.students'].search([('class_id', '=', self.class_id.id)])

        for rec in students:
            rec.exam_ids = [(self.id)]





