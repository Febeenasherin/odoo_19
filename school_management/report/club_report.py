# -*- coding: utf-8 -*-
from odoo import  models
from odoo.exceptions import ValidationError
from datetime import date


class ClubReport(models.AbstractModel):
    """ students leaves"""

    _name = 'report.school_management.clubs_data_template'

    def _get_report_values(self, docids, data=None):

        clubs = self.env['school.club.data'].browse(docids)

        sql = """
               SELECT s.first_name,s.admission,c.name_class from school_students as s JOIN school_class as c on s.class_id = c.id 
               JOIN school_clubs_school_students_rel as r on s.id = r.school_students_id JOIN school_clubs as sc on sc.id = r.school_clubs_id WHERE 1=1 """

        event_sql =  """
               SELECT e.name,e.venue,e.start_date,e.end_date from school_events as e WHERE 1=1 """

        # Find students in the club
        if clubs.club_id:
            sql += f" AND sc.id = '{clubs.club_id.id}'"
            event_sql += f" AND e.club_id = '{clubs.club_id.id}'"

        if clubs.student_id:
            sql += f"AND s.id = '{clubs.student_id.id}'"

        self.env.cr.execute(sql)
        students = self.env.cr.fetchall()



        self.env.cr.execute(event_sql)
        event = self.env.cr.fetchall()

        if not students:
            raise  ValidationError ("not found")

        return {
            'print_date': date.today(),
            'club_name' : clubs.club_id.name if clubs.club_id else '',
            'student_name' :
                clubs.student_id.first_name if clubs.student_id else '',
            'event' : event,
            'students' : students,


        }

            
            
            















