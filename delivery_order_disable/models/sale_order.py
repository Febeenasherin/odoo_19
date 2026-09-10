# -*- coding: utf-8 -*-
from exceptions import ValidationError

from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = "sale.order"


    def _action_confirm(self):

        # self.picking_ids.unlink()
        # print("dsds",self.picking_ids)

        return super(SaleOrder, self)._action_confirm







    def action_delivery(self):
        print("gg")


        order = self.order_line._action_launch_stock_rule()
        print("order",order)

        return order















        # new = self.picking_ids
        # print("new",new)
        # if self.picking_ids:
        #     print("hh",self.picking_ids)
        #     return self.action_view_delivery()
        #
        #
        # if not self.order_line:
        #     raise ValidationError("select product")
        #
        # if self.picking_ids:
        #     print("hh",self.picking_ids)
        #     return self.action_view_delivery()
        # deliv = super().action_view_delivery

        # return self._get_action_view_picking(self.picking_ids)




