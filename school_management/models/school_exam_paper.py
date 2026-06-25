# -*- coding: utf-8 -*-
from odoo import fields, models


class SchoolExamPaper(models.Model):
    _name = 'school.exam.paper'
    _description = 'School Exam Paper'

    exam_id = fields.Many2one('school.exam', string='Exam')
    subject_id = fields.Many2one('school.subject', string='Subject')
    pass_mark = fields.Integer(string='Pass Mark')
    max_mark = fields.Integer(string='Max Mark')
