# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import ValidationError

class EmployeeLoan(models.Model):
    _name = 'employee.loan'

    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(copy=False, required=True, default='New')
    employee_id = fields.Many2one('hr.employee',string="Employee ID")
    loan_amount = fields.Float(string="Loan Amount")
    installment_count = fields.Integer(string="Installment Count",default=1)
    start_date = fields.Date(string="Start Date")
    state= fields.Selection([('draft','Draft'),('approved','Approved'),('ongoing','Ongoing'),('paid','Paid')],string="State", default='draft')
    loan_line_ids = fields.One2many('employee.loan.line', 'loan_id', string="Loan Lines")
    installment_amount = fields.Integer(string="Installment Amount")
    loan_date = fields.Datetime(string="Loan Date")
    total_payable = fields.Float(string="Total Payable", compute="_compute_total_payable")

    @api.model_create_multi
    def create(self, vals_list):

        print("self", self, vals_list)
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':

                vals["name"] = self.env['ir.sequence'].next_by_code('name') or 'New'

        return super(EmployeeLoan, self).create(vals_list)




    @api.onchange('loan_amount','installment_count')
    def _onchange_installment_count(self):
        for rec in self:

            amount = rec.loan_amount / rec.installment_count
            rec.installment_amount = amount

    @api.depends('loan_amount')
    def _compute_total_payable(self):
        for record in self:
            line = record.loan_line_ids
            print("line",line)
            amount=0
            record.total_payable=0
            for rec in line:
                record.total_payable += rec.amount + amount


    def action_approve(self):
        if self.loan_amount > 0:

            self.state = 'approved'

        else:
            raise ValidationError("Loan amount must be above zero")






