# -*- coding: utf-8 -*-
from odoo import fields, models, api
import base64
from datetime import datetime,time,timedelta


class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    @api.model
    def send_Daily_Attendance_report(self):

        today = datetime.now()
        print("today",today)
        start_date = datetime.combine(today, time.min)
        print("start_date",start_date)

        tomorrow = today + timedelta(days=1)

        end_date = datetime.combine(tomorrow, time.max)
        print("end_date",end_date)

        template = self.env.ref(
            'day_wise_attendance_report.email_template_attendance_report',

        )

        print("template",template)
        rec = self.search([('check_in' , '>=', start_date), ('check_in' , '<', end_date)])
        print("rec",rec)

        employees = self.env['hr.employee'].search([('active', '=', True)])
        print("employees",employees)

        emp_present = rec.mapped('employee_id')
        print("emp_present",emp_present)


    # #     # Get report action
        report_action = self.env.ref(
            'day_wise_attendance_report.action_report_attendance_template',
            raise_if_not_found=False
        )
        print("report",report_action)

        pdf_content, _ = report_action._render_qweb_pdf("day_wise_attendance_report.attendance_report", res_ids=rec.ids)
        print("pdf",pdf_content)
        pdf_base64 = base64.b64encode(pdf_content)
    # #     # Create attachment
        attachment = self.env['ir.attachment'].create({
            'name': 'Student_Performance_Report.pdf',
            'type': 'binary',
            'datas': pdf_base64,
            'mimetype': 'application/pdf',
        })
    #
        print("attachment",attachment)

        managers = self.env.ref("hr.group_hr_manager")
        print("manager",managers)
        user = self.env['res.users'].search([('group_ids', '=', managers.id)], limit=1)
        print(user, "user")
    #     # Send email to each teacher
        for users in user:
            template.send_mail(
                user.id,
                force_send=True,

                email_values={'attachment_ids': [(4, attachment.id)],
                              'email_to' : users.email,
                              'body_content': f"<p>Hello {today}</p>",}

            )
