# -*- coding: utf-8 -*-
from odoo import fields, models, api


class EmployeeLevel(models.Model):
    _name = 'employee.level'
    _rec_name = 'level'


    level = fields.Char('Level', required=True)
    salary = fields.Float('Salary', required=True)
    ref_no = fields.Integer('No', required=True)