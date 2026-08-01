# -*- coding: utf-8 -*-
from odoo import fields, models


class EmployeeLoanLine(models.Model):
    _name = "employee.loan.line"

    loan_id = fields.Many2one('employee.loan', string="Loan")
    date = fields.Date(string="Date")
    amount = fields.Float(string="Amount")
    paid = fields.Boolean(string="Paid")
