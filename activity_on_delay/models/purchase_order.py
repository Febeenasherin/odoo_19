# -*- coding: utf-8 -*-
from odoo import fields, models, api
from datetime import date,datetime
from datetime import timedelta

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'


    # def _create_activity(self):
    #     order = self.search([])
    #     print(order)
    #     today = date.today()
    #     print(today)
    #     for rec in order:
    #         print(rec.date_planned.date())
    #         if rec.date_planned.date() == today and rec.receipt_status == 'pending':
    #             # ac = super().create(vals)
    #             activity_type = self.env.ref('mail.mail_activity_data_todo')
    #             self.env['mail.activity'].create({
    #                 'activity_type_id': activity_type.id,
    #                 'res_model_id': self.env['ir.model']._get_id('purchase.order'),
    #                 'res_id': rec.id,
    #                 'user_id': rec.user_id.id,
    #                 'date_deadline': fields.Date.today(),
    #                 'summary': 'Review Sales Order',
    #             })
    #
    #             return
    #             # activity = self.env['mail.activity.schedule'].create({
    #             #     ''
    #             # })



    @api.model
    def create(self, vals):
        order = self.search([])
        today = datetime.today()
        yesterday = today - timedelta(days=1)
        print(yesterday)
        for rec in order:
            # print(rec.date_planned.date())
            print("fff",rec.date_planned < today and rec.receipt_status == 'pending')
            if rec.date_planned < today and rec.receipt_status == 'pending':
                activity = super().create(vals)
                activity_type = rec.env.ref('mail.mail_activity_data_call')
                self.env['mail.activity'].create({
                'activity_type_id': activity_type.id,
                'res_model_id': self.env['ir.model']._get_id('purchase.order'),
                'res_id': activity.id,
                'user_id': activity.user_id.id or self.env.user.id,
                'date_deadline': fields.Date.today() + timedelta(days=2),
                'summary': 'Follow-up with vendor',
            })
                return activity
    # @api.model
    # def create_mail(self):
    #     order = self.search([])
    #     today = date.today()
    #     for rec in order:
    #         # print(rec.date_planned.date())
    #         if rec.date_planned.date() == today and rec.receipt_status == 'pending':
    #
    #             emails = self.env.user.id
    #             template = self.env.ref('activity_on_delay.email_template_purchase')
    #
    #
    #             template.send_mail(rec.id, force_send=True, email_values={'email_to': emails,
    #                                                                 })

