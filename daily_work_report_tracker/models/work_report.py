# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from odoo.exceptions import UserError
from datetime import datetime, date


class WorkReport(models.Model):

    _name = 'work.report'
    _inherit = ['mail.thread', 'mail.activity.mixin']



    name = fields.Char(string='Subject')
    date = fields.Date(string='Date')
    employee_id = fields.Many2one('hr.employee', string='Employee Name')
    report = fields.Html(string='Report')

    @api.model
    def message_new(self, msg_dict, custom_values=None):
        print(self)
        print("working")
        # super(WorkReport, self).message_new(msg_dict)

        subject = msg_dict.get('subject')
        print("subject", subject)
        email_from = msg_dict.get('from')
        print('from', email_from)
        body = msg_dict.get('body')
        print('body', body)

        part = subject.split('_', 2)
        print("split", part)

        if len(part) != 3:
            raise UserError('Invalid subject format')

        sub = part[0].strip()
        print("sub", sub)
        date = part[1].strip()
        emp_name = part[2].strip()

        real_date = datetime.strptime(date, '%d %b %Y').date()
        print("real_date", real_date)


        employee = self.env['hr.employee'].search([('name', '=', emp_name)], limit=1)
        if not employee:
            raise UserError('Employee not found')

        # if custom_values is None:
        #     custom_values = {}

        values = {
            'name': subject,
            'date': real_date,
            'employee_id': employee.id,
            'report': body,
            # 'partner_id': msg_dict.get('author_id', False),
            }

        # self.env['hr.employee'].create(values)


        print(values)
        print("name", values['name'])

        new = self.env['work.report'].create(values)
        print(new)





        return new



    # def fetch_mail(self):








