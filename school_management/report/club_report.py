# -*- coding: utf-8 -*-
from odoo import  models, fields
from odoo.exceptions import UserError


class ClubReport(models.AbstractModel):
    """ students leaves"""

    _name = 'report.school_management.clubs_data_template'

    def _get_report_values(self, docids, data=None):

        clubs = slef.env['school.club.data'].browse(docids)

        sql = """
               SELECT , s.first_name, c.name_class, e.name, , l.total_date,
               l.reason FROM school_leaves as l JOIN school_students as s on l.student_id = s.id 
               JOIN school_class as c on l.class_id = c.id WHERE 1=1"""






        # club_ids = data.get('ids',[])
        #
        # docs = self.env['school.clubs'].browse(club_ids)
        #
        # if not docs:
        #     raise UserError("No leaves found")
        #
        # return {
        #     'docs': docs,
        # }






