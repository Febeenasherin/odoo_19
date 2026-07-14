# -*- coding: utf-8 -*-
from odoo import fields, models, api


class StudentLeaveWizard(models.TransientModel):
    _name = "student.leave.wizard"
    _description = "Student Leave Wizard"
    _inherit = "school.leaves"

    def action_leave(self):
        return {'type': 'ir.actions.act_window'}
