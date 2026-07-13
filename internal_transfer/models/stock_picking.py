# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError


class StockPicking(models.Model):
    """ inherit stock picking (inventory)"""
    _inherit = 'stock.picking'


    def button_validate(self):
        """ while clicking validate transfer created user ,the user cant valid that transfer.only another user can valid that transfer"""
        # for picking in self:

        if self.picking_type_id.code == 'internal':
            if  self.create_uid.id == self.env.user.id:
                    raise UserError("Only another user can validate internal transfers.")

                # print(self.env.user.id)


        return super(StockPicking, self).button_validate()
























