# -*- coding: utf-8 -*-
from odoo import fields, models


class SchoolClubData(models.TransientModel):
    """club data wizard"""
    _name = 'school.club.data'

    club_id = fields.Many2one('school.clubs', string='Club')
    student_id = fields.Many2one('school.students', string='Student')


    def action_club_print(self):
        """for print report"""
        return self.env.ref('school_management.action_report_club').report_action(self)

    def club_excel(self):
        self.ensure_one()
        return self.club_report_excel()





