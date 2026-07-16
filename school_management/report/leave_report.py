# -*- coding: utf-8 -*-
from odoo import  models, fields
from odoo.exceptions import UserError


class SchoolLeaves(models.AbstractModel):
    """ students leaves"""

    _name = 'report.school_management.leave_information_template'
    #
    # def _get_report_values(self, docids, data=None):
    #
    #     leave_ids = data.get('ids',[])
    #
    #     docs = self.env['school.leaves'].browse(leave_ids)
    #
    #     if not docs:
    #         raise UserError("No leaves found")
    #
    #     return {
    #         'docs': docs,
    #     }


     def action_print(self):

          self.env.cr.execute(""""""



