# -*- coding: utf-8 -*-
from odoo import fields, models

class SchoolSubjects(models.Model):
    """ school subject """
    _name = 'school.subject'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _unique_name = models.Constraint('UNIQUE(name_sub)', 'Subject must be unique!')

    name_sub = fields.Char(string='Subject')
    school_id = fields.Many2one('school.department', string='Head of Department')
