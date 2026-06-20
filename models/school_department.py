# -*- coding: utf-8 -*-
from odoo import fields,models


class SchoolDepartment(models.Model):
    """ school department """
    _name = 'school.department'
    _description = 'School Department details'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _unique_name = models.Constraint('UNIQUE(name)', 'class must be unique!')

    name = fields.Char(string='Department')
    dep_partner= fields.Many2one('res.partner',string='Head of Department', index=True)
