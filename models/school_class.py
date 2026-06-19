
from odoo import fields,models


class SchoolClass(models.Model):
    _name ='school.class'
    _description ='School class details'

    _unique_name = models.Constraint('UNIQUE(name_class)', 'class must be unique!')
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name_class= fields.Char(string='Name')
    school_dep= fields.Many2one('school.department',string='Department')
    head_dep =fields.Many2one(related='school_dep.dep_partner',string='Head department')
