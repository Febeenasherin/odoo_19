# -*- coding: utf-8 -*-
from openpyxl.worksheet import related

from odoo import fields, models, api
from datetime import timedelta


class SchoolLeaves(models.Model):
    """ students leaves"""
    _name = "school.leaves"
    _description = "School Leaves"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    student_id = fields.Many2one('school.students', string="Students", required=True)
    class_id = fields.Many2one(related='student_id.class_id', string="Class", required=True)
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    total_date = fields.Integer(string="Total Date", readonly=True, compute='_compute_total_day')
    half_day = fields.Boolean(string="Half Day")
    afternoon = fields.Selection([('fornoon', 'Fornoon'), ('afternoon', 'Afternoon')], default='fornoon', string="Half Day")
    reason = fields.Char(string="Reason")


    @api.depends('start_date', 'end_date')
    # def _compute_total_date(self):
    #     for rec in self:
    #         if rec.start_date and rec.end_date:
    #             rec.total_date = ((rec.end_date - rec.start_date).days+1)
    #             # print("dd",rec.total_date)
    #             print("dd", rec.end_date.weekday())

        # for i in range(rec.total_date):
        #     count=0
        #     day = rec.start_date + timedelta(days=1)
        #     if day.weekday() in (5,6):
        #         count += 1
        #
        #     print(count)
        #     rec.total_date = (rec.total_date - count)


    def _compute_total_day(self):
        for rec in self:
            rec.total_date = 0
            # print("dd",rec.end_date.weekday())

        # for i in range(rec.total_date.isformat()):
        #     print("dd",i)


            if rec.start_date and rec.end_date:
                start = rec.start_date
                end = rec.end_date
                current = start
                day = 0
                while (current <= end):

                    print("date",current)
                    if current.weekday() not in [5, 6]:
                        day+=1

                    current += timedelta(days=1)

                rec.total_date = day














    
