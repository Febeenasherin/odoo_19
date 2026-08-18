# -*- coding: utf-8 -*-
from odoo import fields, models, api
import base64
from odoo.exceptions import UserError
from odoo.tools.mimetypes import guess_mimetype
from odoo.exceptions import ValidationError


class   PurchaseOrder(models.Model):
    _inherit = "purchase.order"


    attachment_ids = fields.Many2many('ir.attachment', string='Attachments')



    def button_confirm(self):
        for order in self:

            value = self.env['ir.config_parameter'].sudo().get_param(
                            'mandatory_attachment_before_confirming_purchase_order.attachment'
                        )

            print(value)

            attachment_count = self.env['ir.attachment'].search([
                ('res_model', '=', 'purchase.order'),
                ('res_id', '=', order.id)

            ])


            count = len(attachment_count)
            if count == 0 and value == 'True':
                raise UserError("You must attach a document before confirming this purchase order.")

            attachments = self.env['ir.attachment'].search([('res_model', '=', 'purchase.order'),
                ('res_id', '=', order.id)])

            if attachments not in ('image/jpeg','application/pdf'):
                raise ValidationError("You must attach pdf/png")




        return super().button_confirm()


    # attach_file = fields.Binary("Attach File", attachment=True, compute="_compute_attach_file")
    # file = fields.Char("File")

    # attachment_ids = fields.Many2many(
    #
    #     'ir.attachment',
    #
    #     'purchase_order_attachment_rel',
    #
    #     'purchase_id', 'attachment_id',
    #
    #     string='Attachments'
    #
    # )





    # def _compute_attach_file(self):
    #     print("hh")
    #
    #
    #     value = self.env['ir.config_parameter'].sudo().get_param(
    #             'mandatory_attachment_before_confirming_purchase_order.attachment'
    #         )
    #
    #     print(value)
    #
    #
    #     for order in self:
    #         order.attach_file = value == 'True'
    #
    #
    #     # if value == 'True':
    #
    # def button_confirm(self):
    #     # Call the attachment helper method before confirming the PO
    #     self._attach_pdf_to_chatter()
    #     return super().button_confirm()
    #
    # def _attach_pdf_to_chatter(self):
    #     for order in self:
    #         # 1. Generate QWeb PDF report or use existing binary data
    #         pdf_content, _ = self.env['ir.actions.report'].sudo()._render_qweb_pdf(
    #             'purchase.report_purchase_quotation', order.id
    #         )
    #
    #         # 2. Create the attachment record linked to the purchase order
    #         attachment = self.env['ir.attachment'].create({
    #             'name': f"Quotation_{order.name}.pdf",
    #             'type': 'binary',
    #             'datas': base64.b64encode(pdf_content),
    #             'res_model': 'purchase.order',
    #             'res_id': order.id,
    #             'mimetype': 'application/pdf',
    #         })
    #
    #         # 3. Post a message in chatter with the attachment
    #         order.message_post(
    #             body="A pre-confirmation PDF document has been attached.",
    #             attachment_ids=[attachment.id]
    #         )



        # def button_confirm(self):
        #     # Call the attachment helper method before confirming the PO
        #     self._attach_pdf_to_chatter()
        #     return super().button_confirm()
        #
        # def _attach_pdf_to_chatter(self):
        #     for order in self:
        #         # 1. Generate QWeb PDF report or use existing binary data
        #         pdf_content, _ = self.env['ir.actions.report'].sudo()._render_qweb_pdf(
        #             'purchase.report_purchase_quotation', order.id
        #         )
        #
        #         # 2. Create the attachment record linked to the purchase order
        #         attachment = self.env['ir.attachment'].create({
        #             'name': f"Quotation_{order.name}.pdf",
        #             'type': 'binary',
        #             'datas': base64.b64encode(pdf_content),
        #             'res_model': 'purchase.order',
        #             'res_id': order.id,
        #             'mimetype': 'application/pdf',
        #         })
        #
        #         # 3. Post a message in chatter with the attachment
        #         order.message_post(
        #             body="A pre-confirmation PDF document has been attached.",
        #             attachment_ids=[attachment.id]
        #         )

    # def action_file(self):
    #     print("action")

