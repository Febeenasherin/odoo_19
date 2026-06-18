
from odoo import fields,models


class SchoolClass(models.Model):
    _name ='school.class'
    _description ='School class details'


    name= fields.Char(string='Name')
    school_dep= fields.Many2one('school.department',string='Head of Department')