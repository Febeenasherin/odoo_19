# -*- coding: utf-8 -*-
from odoo import fields, models


class SchoolExam(models.Model):
    """ exams for students"""
    _name = 'school.exam'
    _description = 'School Exam'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    class_id = fields.Many2one('school.class', string='Class', required=True)
    # subject_id = fields.Many2one('school.subject', string='Subject')
    paper_ids = fields.One2many('school.exam.paper', 'exam_id')
    start_date = fields.Datetime(string='Start Date')
    end_date = fields.Datetime(string='End Date')


    def action_exam(self):
        """ adding exam for students while clicking add button"""
        students = self.env['school.students'].search([('class_id', '=', self.class_id.id)])

        for rec in students:
            rec.exam_ids = [(self.id)]





