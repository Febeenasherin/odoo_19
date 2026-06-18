from odoo import fields,models


class SchoolDepartment(models.Model):
    _name = 'school.department'
    _description = 'School Department details'

    name = fields.Char(string='Department')
    dep_partner= fields.Many2one('res.partner',string='Head of Department', index=True)

