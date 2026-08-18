# -*- coding: utf-8 -*-
from odoo import fields, models, api
import base64

from odoo.tools.mimetypes import guess_mimetype
from odoo.exceptions import ValidationError


class   PurchaseOrder(models.Model):
    _inherit = "purchase.order"


    attachment_ids = fields.Many2many('ir.attachment', string='Attachments')



    def button_confirm(self):
        """ button click before attaching file, raise validation error """
        for order in self:

            value = self.env['ir.config_parameter'].sudo().get_param(
                            'mandatory_attachment_before_confirming_purchase_order.attachment'
                        )

            print(value)

            attachments = self.env['ir.attachment'].search([
                ('res_model', '=', 'purchase.order'),
                ('res_id', '=', order.id)

            ])


            count = len(attachments)
            print(count,"count")
            if count == 0 and value == 'True':
                raise ValidationError("You must attach a document before confirming this purchase order.")

            # attachments = self.env['ir.attachment'].search([('res_model', '=', 'purchase.order'),
            #     ('res_id', '=', order.id)])

            if attachments.mimetype not in ('image/jpeg','application/pdf') and value == 'True':
                    raise ValidationError("You must attach pdf/png")




        return super().button_confirm()




