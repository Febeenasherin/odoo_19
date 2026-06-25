# -*- coding: utf-8 -*-
from odoo import fields, models, api
from datetime import timedelta


class SchoolLeaves(models.Model):
    """ students leaves"""
    _name = "school.leaves"
    _description = "School Leaves"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    student_id = fields.Many2one('school.students', string="Students")
    class_id = fields.Many2one('school.class', string="Class")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    total_date = fields.Integer(string="Total Date", compute='_compute_total_date')
    half_day = fields.Datetime(string="Half Day")
    reason = fields.Char(string="Reason")


    @api.depends('start_date', 'end_date')
    def _compute_total_date(self):
        """ calculate total date excluding saturday and sunday"""
        print('self',self)
        for rec in self:
            if rec.start_date and rec.end_date not in [5,6]:
                total = rec.end_date - rec.start_date
                rec.total_date = total.days+1
            else:
                rec.total_date = 0

    
