# -*- coding: utf-8 -*-
from odoo import  models, fields
from odoo.exceptions import UserError


class ClubReport(models.AbstractModel):
    """ students leaves"""

    _name = 'report.school_management.clubs_data_template'

    def _get_report_values(self, docids, data=None):

        club_ids = data.get('ids',[])

        docs = self.env['school.clubs'].browse(club_ids)

        if not docs:
            raise UserError("No leaves found")

        return {
            'docs': docs,
        }






