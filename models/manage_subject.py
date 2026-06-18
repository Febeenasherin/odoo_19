from odoo import fields,models

class Manage_Subjects(models.Model):
    _name = 'school.subject'


    name = fields.Char(string='Subject')
    school_dep= fields.Many2one('school.department',string='Head of Department')