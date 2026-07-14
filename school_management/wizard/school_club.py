# -*- coding: utf-8 -*-
from odoo import fields, models, api


class SchoolClubData(models.TransientModel):
    _name = 'school.club.data'
    _inherit = 'school.clubs'

    def club_data(self):
        return {'type': 'ir.actions.act_window',}
