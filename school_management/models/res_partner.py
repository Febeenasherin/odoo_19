# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    partner = fields.Selection([('teacher', 'Teacher'), ('student', 'Student'), ('office staff', 'Office staff')], string="Partner", ondelete="cascade")
    start_id = fields.Many2one('school.events', string="Start Task", compute="_compute_start_id")




    #
    # def _compute_start_id(self):
    #     target_alert_date = self.start_id - datetime.timedelta(days=2)
    #
    #
    #     records_to_process = self.env['school.events'].search([
    #     ('start_id', '=', target_alert_date),])
    #
    # # Execute your specific business automation logic
    #     for record in records_to_process:
    #         record.message_post(body="Reminder: This task is due in 2 days!")

    # @api.model
    # def send_student_homework_reminder(self):
    #         template = self.env.ref(
    #             'school_events.email_template_eventt',
    #             raise_if_not_found=False
    #         )
    #         if not template:
    #             return
    #         students = self.search([('partner', '=', 'student,teacher'),
    #             ('email', '!=', False)
    #         ])
    #         for student in students:
    #             template.send_mail(partner, force_send=True)

