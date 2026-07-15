# -*- coding: utf-8 -*-
from odoo import  models, fields
from datetime import timedelta, date


class SchoolLeaves(models.Model):
    """ students leaves"""
    _inherit = "school.leaves"


    leave_id = fields.Many2one('student.leave.wizard', string="Leave")
    filter_type = fields.Selection(related="leave_id.filter_type", string="Filter")









