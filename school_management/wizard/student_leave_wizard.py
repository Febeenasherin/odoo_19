# -*- coding: utf-8 -*-
from odoo import fields, models, api

from odoo.exceptions import ValidationError


class StudentLeaveWizard(models.TransientModel):
    """student information report"""
    _name = "student.leave.wizard"
    _description = "Student Leave Wizard"

    filter_type = fields.Selection([('day', 'Day'),
                                    ('week', 'Week'), ('month', 'Month'), ('custom', 'Custom')], string='Filter Type', )

    start_date = fields.Date()
    end_date = fields.Date()
    student_id = fields.Many2one('school.students', string='Student',
                                 domain="[('id', 'in', student_ids)]", store=True)
    student_ids = fields.Many2many('school.students', compute="_compute_student")

    # student_id = fields.Many2one(related='class_id.student_id', string='Student')
    class_id = fields.Many2one('school.class', string='Class', readonly=False)

    @api.constrains('start_date', 'end_date')
    def _end_date(self):
        for rec in self:
            if rec.start_date and rec.end_date:
                if rec.end_date <= rec.start_date:
                    raise ValidationError("end date greater than start date")

    @api.onchange('student_id')
    def _onchange_student_id(self):
        """ selecting student auto_fill class"""
        for rec in self:
            if rec.student_id:
                rec.class_id = rec.student_id.class_id

    @api.depends('class_id')
    def _compute_student(self):
        """ when selecting class ,only list students name based on class"""

        print("kk", self)

        classes = self.env['school.students']
        for stud in self:

            if stud.class_id:
                stud.student_ids = classes.search([('class_id', '=', stud.class_id)])

            else:
                stud.student_ids = classes.search([])

    def action_print(self):
        """ print student leave report"""

        return self.env.ref('school_management.action_report_school_leave').report_action(self)

# elif self.filter_type == 'week':
#     week_start = today - timedelta(days=today.weekday())
#     week_end = week_start + timedelta(days=6)
#
#     domain += [('start_date', '<=', week_start), ('end_date', '>=', week_end)]
#
# elif self.filter_type == 'month':
#     month_start = today - timedelta(days=today.month)
#
#     domain += [('start_date', '<=', month_start), ('end_date', '>=', month_start)]
#
# elif self.filter_type == 'custom':
#     domain +=[('start_date', '=', self.start_date), ('end_date', '=', self.end_date)]
