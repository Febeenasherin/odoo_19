# -*- coding: utf-8 -*-
from odoo import fields, models


class SchoolExamPaper(models.Model):
    """child model of school exam.for showing exams in list view inside exam form view"""
    _name = 'school.exam.paper'
    _description = 'School Exam Paper'

    exam_id = fields.Many2one('school.exam')
    subject_id = fields.Many2one('school.subject', string='Subject', required=True)
    class_id = fields.Many2one('school.class', string='Class')
    pass_mark = fields.Integer(string='Pass Mark')
    max_mark = fields.Integer(string='Max Mark')
