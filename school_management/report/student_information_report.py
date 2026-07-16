# -*- coding: utf-8 -*-
from odoo import  models, fields
from odoo.exceptions import UserError


class ReportSchoolInformationTemplate(models.AbstractModel):
    """ students leaves"""

    _name = 'report.school_management.student_information_template'

    def _get_report_values(self, docids, data=None):

        student_ids = data.get('ids',[])

        docs = self.env['school.students'].browse(student_ids)

        if not docs:
            raise UserError("No leaves found")

        return {
            'docs': docs,
        }
