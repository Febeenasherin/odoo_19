# -*- coding: utf-8 -*-
from odoo import fields, models


class SchoolClass(models.Model):
    """school class"""
    _name ='school.class'
    _description ='School class details'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name_class'

    _unique_name = models.Constraint('UNIQUE(name_class)', 'class must be unique!')

    name_class = fields.Char(string='Name')
    school_id = fields.Many2one('school.department', string='Department')
    head_id = fields.Many2one(related='school_id.dep_id', string='Head department')
    company_id = fields.Many2one('res.company', string='multi_school', tracking=True)
