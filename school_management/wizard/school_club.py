# -*- coding: utf-8 -*-
from datetime import date

from odoo import fields, models, api




class SchoolClubData(models.TransientModel):
    """club data wizard"""
    _name = 'school.club.data'

    club_id = fields.Many2one('school.clubs', string='Club')
    student_id = fields.Many2one('school.students', string='Student')


    def action_club_print(self):
        """for getting report, if the club is selected it show the club name and including student name,"""
        

        return self.env.ref('school_management.action_report_club').report_action(self)





