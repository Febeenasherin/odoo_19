# -*- coding: utf-8 -*-
from odoo import fields, models, api
from datetime import date,datetime
from datetime import timedelta

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'



    @api.model
    def create_mail(self):
        order = self.search([('receipt_status', '=', 'pending'),('state', '=', 'purchase')])
        today = date.today()
        manager = self.env.ref('purchase.group_purchase_manager')
        # manager = manager
        print(manager)
        user = self.env['res.users'].search([('group_ids', '=', manager.id)],limit=1)
        print(user,"user")


        print(today)
        for rec in order:
            print("records",rec)
            print(rec.date_planned.date() < today,"today")
            # print("fff",rec.date_planned < today and rec.receipt_status == 'pending')
            if rec.date_planned.date() < today:
                # activity = super().create(vals)
                actitvity = self.env['mail.activity'].search([('res_model_id', '=', 'res.partner'),('res_id', '=', rec.partner_id.id)])

                if not actitvity:
                    activity_type = rec.env.ref('mail.mail_activity_data_call')
                    self.env['mail.activity'].create({
                    'activity_type_id': activity_type.id,
                    'res_model_id': self.env['ir.model']._get_id('res.partner'),
                    'res_id': rec.partner_id.id,
                    'partner_id': rec.partner_id.id,
                    'date_deadline': fields.Date.today() + timedelta(days=2),
                    'summary': (f'Follow-up with {rec.name}'),
            })

                    rec.message_post(
                    body=(f"the {rec.name} has been delayed. please follow with {rec.partner_id.name}") ,
                    message_type="comment",
                    subtype_xmlid="mail.mt_comment",
                    partner_ids =  [user.id],
                )






            # if rec.date_planned.date() < today:
            #     # activity = super().create(vals)
            #     actitvity = self.env['mail.activity'].search(
            #         [('res_model_id', '=', 'purchase.order'), ('res_id', '=', rec.id)])
            #
            #     if not actitvity:
            #         activity_type = rec.env.ref('mail.mail_activity_data_call')
            #         self.env['mail.activity'].create({
            #             'activity_type_id': activity_type.id,
            #             'res_model_id': self.env['ir.model']._get_id('purchase.order'),
            #             'res_id': rec.id,
            #             'user_id': rec.user_id.id,
            #             'date_deadline': fields.Date.today() + timedelta(days=2),
            #             'summary': 'Follow-up with vendor',
            #         })
            #
            #         rec.message_post(
            #             body=(f"the {rec.name} has been delayed. please follow with {rec.partner_id.name}"),
            #             message_type="comment",
            #             subtype_xmlid="mail.mt_comment",
            #             partner_ids=[user.id],
            #         )



