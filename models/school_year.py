from odoo import fields, models

class SchoolYear(models.Model):
    _name = 'school.year'
    _description = 'School Year'


    name=fields.Char(string='Name')