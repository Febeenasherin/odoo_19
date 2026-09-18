# -*- coding: utf-8 -*-
from odoo import fields, models, api, _



class WorkReport(models.Model):

    _name = 'work.report'
    _inherit = ['mail.thread', 'mail.activity.mixin']



    name = fields.Char(string='Subject')
    date = fields.Date(string='Date')
    employee_name = fields.Many2one('hr.employee', string='Employee Name')
    report = fields.Html(string='Report')

    @api.model
    def message_new(self, msg_dict, custom_values=None):
        print(self)
        print("working")
        if custom_values is None:
            custom_values = {}
            defaults = {
            'name': msg_dict.get('subject') or _("No Subject"),
            # 'email_from': msg_dict.get('from'),
            # 'partner_id': msg_dict.get('author_id', False),
            }

            subject = msg_dict.get('subject')
            print(defaults)
            email_from = msg_dict.get('from')
            print('from', email_from)


            self.create({
            'name' : subject
            })




        return super(WorkReport, self).message_new(msg_dict, custom_values=defaults)




    # def fetch_mail(self):








