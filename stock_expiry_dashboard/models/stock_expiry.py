# -*- coding: utf-8 -*-


from odoo import fields, models, api
from datetime import date, timedelta


class StockExpiry(models.Model):
    _name = "stock.expiry"



    count_expiring = fields.Integer('Expiry Count', )
    no_already_expired = fields.Integer('Already Expired')
    total_expired = fields.Integer('Total Expired')


    @api.model
    def stock_expiration(self):

        lot = self.env['stock.lot']


        today = date.today()

        start_date = today - timedelta(days=today.weekday())
        print("start_date", start_date)
        end_date = start_date + timedelta(days=6)
        print("end_date", end_date)

        expiring_count = lot.search([('expiration_date', '>=', start_date),('expiration_date', '<=', end_date)])
        print("expiring_count", expiring_count)


        expired = lot.search([('expiration_date', '<=', today)])
        print("expired", expired)

        value = 0.0

        for lots in expired:

            quantity = lots.product_qty * lots.product_id.lst_price
            # total = sum(quantity)
            print("quantity", quantity)
            # print("total", total)
            value += quantity




        return {
            'current_week' : len(expiring_count),
            'expired' : len(expired),
            'total_value' : value,
        }

