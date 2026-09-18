# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class FetchMail(models.Model):
    _inherit = 'fetchmail.server'



    @api.model
    def fetch_mail(self,msg, custom_values=None):
        print("mcm")






        # if custom_values is None:
        #         custom_values = {}
        #         # defaults = {
        #         #     'name': msg.get('subject') or _("No Subject"),
        #         #     # 'email_from': msg_dict.get('from'),
        #         #     # 'partner_id': msg_dict.get('author_id', False),
        #         # }
        #
        #         subject = msg.get('subject')
        #         # print(defaults)
        #         email_from = msg.get('from')
        #         print('from', email_from)
        #
        #         self.create({
        #             'name': subject
        #         })