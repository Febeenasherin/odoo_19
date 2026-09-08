# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployee(models.Model):
    _inherit = "hr.employee"


    level_id  = fields.Many2one('employee.level',string="Employee Level")
    salary = fields.Float(string="Salary", related="level_id.salary")

    is_highest = fields.Boolean(string="Highest", compute="_compute_is_highest", store=True)



    def action_promote(self):
        print("print")

        next_level = self.env['employee.level'].search([('ref_no', '>', self.level_id.ref_no)], order='ref_no asc', limit=1)
        print(next_level)

        if next_level:
            self.write({
                'level_id': next_level.id,
                'salary': next_level.salary,
            })

    @api.depends('level_id')
    def _compute_is_highest(self):



        highest = self.env['employee.level'].search([], order='ref_no desc', limit=1)
        print(highest)

        for employee in self:

            employee.is_highest = (employee.level_id == highest)







