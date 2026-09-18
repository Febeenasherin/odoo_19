# -*- coding: utf-8 -*-


from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"


    restricted_partner = fields.Boolean(related="partner_id.restricted", readonly=True)
    value = fields.Integer(related="partner_id.restricted_count", readonly=True)
    show_warning = fields.Char(string='warning message', readonly=True, compute='_order_restrict_warning', store=True)




    @api.depends("partner_id",'restricted_partner','value')

    def _order_restrict_warning(self):

        print("work")


        order = self.order_line

        len_of_order = len(order)
        print("len_of_order",len_of_order)

        if self.partner_id.restricted:
            print("val",self.partner_id.restricted)
            count = self.value
            print("count",count)
            if count < len_of_order:
                # raise ValidationError("Purchase Order less than restrict value")
                self.show_warning = f"this order can only select {self.value} items"





