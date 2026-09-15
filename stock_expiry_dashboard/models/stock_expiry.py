# -*- coding: utf-8 -*-
from itertools import count

from odoo import fields, models, api
from datetime import date, timedelta


class StockExpiry(models.Model):
    _name = "stock.expiry"



    count_expiring = fields.Integer('Expiry Count', )
    no_already_expired = fields.Integer('Already Expired')
    total_expired = fields.Integer('Total Expired')


    @api.model
    def stock_expiration(self):

        for stock in self:
            print('working')
            stock.count_expiring = 0
        # product = self.env['product.template'].search([('use_expiration_date', '=', True)])
        # for pro in product:
        #
        #     exp_date = pro.expiration_time
        #     print("time",exp_date)
        #
            move = self.env['stock.move.line'].search([])



            for line in move:

                lot_no = line.lot_name
                print("lot_no", lot_no)

                # if stock.expired == 'current_week':

                if lot_no:
                    today = date.today()

                    start_date = today - timedelta(days=today.weekday())
                    print("start_date", start_date)
                    end_date = start_date + timedelta(days=6)
                    print("end_date", end_date)

                    expiry_date = line.expiration_date
                    print("expiry_date", expiry_date)
                    ex_date = expiry_date.date()
                    print("ex_date", ex_date)

                    if ex_date >= start_date and expiry_date.date() <= end_date:
                        stock.count_expiring += 1


                







                        # print("count_expiring", self.count_expiring)
