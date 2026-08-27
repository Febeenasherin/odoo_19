# -*- coding: utf-8 -*-
from odoo import fields, models, api
import base64


class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    @api.model
    def send_Daily_Attendance_report(self):
    #     # Get all teachers with email
    #      = self.search([
    #         ('education_role', '=', 'teacher'),
    #         ('email', '!=', False)
    #     ])
    #     if not teachers:
    #         return
    #     # Get email template
        template = self.env.ref(
            'day_wise_attendance_report.email_template_attendance_report',
            raise_if_not_found=False
        )

        print("template",template)
        if not template:
            return
    #     # Get report action
        report_action = self.env.ref(
            'day_wise_attendance_report.action_report_attendance_template',
            raise_if_not_found=False
        )
        print("report",report_action)
        # if not report_action:
        #     return
    #     # Get all student.performance records
        records = self.env['hr.attendance'].search([])
        print("record",records)
    #     # Generate PDF once
        pdf_content, _ = report_action._render_qweb_pdf(report_action.id, records.ids)
        print("pdf",pdf_content)
        pdf_base64 = base64.b64encode(pdf_content)
    #     # Create attachment
        attachment = self.env['ir.attachment'].create({
            'name': 'Student_Performance_Report.pdf',
            'type': 'binary',
            'datas': pdf_base64,
            'res_model': 'hr.attendance',
        })

        print("attachment",attachment)
    #     # Send email to each teacher
    #     for teacher in teachers:
    #         template.send_mail(
    #             teacher.id,
    #             email_values={'attachment_ids': [(4, attachment.id)]},
    #             force_send=True
    #         )
