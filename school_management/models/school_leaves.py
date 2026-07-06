# -*- coding: utf-8 -*-
from openpyxl.worksheet import related

from odoo import fields, models, api
from datetime import timedelta, date


class SchoolLeaves(models.Model):
    """ students leaves"""
    _name = "school.leaves"
    _description = "School Leaves"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'student_id'


    student_id = fields.Many2one('school.students', string="Students", required=True)
    class_id = fields.Many2one(related='student_id.class_id', string="Class")
    start_date = fields.Date(string="Start Date", default=fields.Date.today)
    end_date = fields.Date(string="End Date", default=fields.Date.today)
    total_date = fields.Float(string="Total Date", readonly=True, compute='_compute_total_day')
    half_day = fields.Boolean(string="Half Day")
    afternoon = fields.Selection([('fornoon', 'Fornoon'), ('afternoon', 'Afternoon')], default='fornoon', string="Half Day")
    reason = fields.Char(string="Reason")


    @api.depends('start_date', 'end_date', 'half_day')
    def _compute_total_day(self):
        """ for calculate the total days of leave excluding sunday and saturday.if enable half day the total day set 0.5"""
        for rec in self:
            if rec.start_date and rec.end_date:
                current = rec.start_date
                day = 0
                while (current <= rec.end_date):

                    print("date",current)
                    if current.weekday() not in [5, 6]:
                        day+=1

                    current += timedelta(days=1)

                if rec.half_day:
                    day -=0.5
                rec.total_date = day

    def update_attendance(self):
        """ mark attendance absent or present .if the student taken leave today,mark absent """
        today = date.today()
        students = self.search([('start_date', '<=', today), ('end_date', '>=' , today)]).mapped('student_id')
        self.env['school.students'].search([]).write({'attendance': 'present'})
        students.attendance = 'absent'
        print("stu",students)











    
