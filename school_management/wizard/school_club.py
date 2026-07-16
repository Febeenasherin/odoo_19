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
        domain=[]

        if self.club_id:
            domain.append(('id', '=', self.club_id.id))

            print("club",domain)

        if self.student_id:
            domain += [('student_ids', 'in', self.student_id.id)]

            print("stud",domain)

        club_info = self.env['school.clubs'].search(domain)

        print("info", club_info)

        return self.env.ref('school_management.action_report_club').report_action(self,data={'ids': club_info.ids})





