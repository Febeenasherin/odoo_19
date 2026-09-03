# -*- coding: utf-8 -*-
from psycopg2._psycopg import cursor

from odoo import fields, models, api
import xmlrpc.client
import ssl
import requests


from odoo.exceptions import ValidationError


class PurchaseMigrationWizard(models.TransientModel):
    _name = "purchase.migration.wizard"


    url = fields.Char(string="Url", default="http://127.0.0.1:8069",required=True)
    database = fields.Char(string="Database",)
    username = fields.Char(string="Username",)
    password = fields.Char(string="Password",)


    def import_purchase_order_action(self):
        """ fetch purchase order data from odoo 16 db to odoo 19 db"""
        print("self")


        url_db1 = "http://127.0.0.1:8069"

        # cert_path = requests.get('https://odoo.lvh.me', verify=False)
        # print("cert_path", cert_path)


        common = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/common")
        print("common", common)

        uid = common.authenticate(self.database, self.username, self.password, {})
        print("uid", uid)
        version_db = common.version()
        print("version",version_db)

        models = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/object")
        print("object", models)

        purchase_order = models.execute_kw(self.database, uid, self.password, 'purchase.order', 'search_read',
                                           [[]], {
                                        'fields' : ['id', 'name', 'partner_id', 'date_order', 'amount_total' , 'order_line',]
                                         })

        print("order:", purchase_order)
        print(f"Fetched {len(purchase_order)} customers from Odoo 16")


        #19

        # url_dest = "http://localhost:8019"
        # db_dest = "aug19"
        # user_dest = "1"
        # pwd_dest = "1"
        # common_dest = xmlrpc.client.ServerProxy(f"{url_dest}/xmlrpc/2/common")
        # uid_dest = common_dest.authenticate(db_dest, user_dest, pwd_dest, {})
        # models_dest = xmlrpc.client.ServerProxy(f"{url_dest}/xmlrpc/2/object")

        # models_dest.execute_kw(db_dest, uid_dest, pwd_dest, 'purchase.order', 'create',)

        # self.env['purchase.migration'].search([]).unlink()

        for record in purchase_order:
            print(record,"rec")
            # partner = record.get('partner_id')
            # name = partner[1]


            # new = {
            #     'name': record.get('name'),
            #                 'partner_id': name,
            #                 'date_order': record.get('date_order'),
            #                 'amount_total': record.get('amount_total'),
            #             }
            #
            # models_dest.execute_kw(db_dest, uid_dest, pwd_dest, 'purchase.order', 'create', [new])


            partner = record.get('partner_id')
            print(partner,"partner_id")

            if partner:
                vendor_name = partner[1]
                print(id(vendor_name))

                currnt_pro = self.env['product.product'].search([('name', '=', vendor_name)], limit=1)
                print("current", currnt_pro)


                order = self.env['purchase.order'].create({
                    # 'old_id': record.get('id'),
                    'name': record.get('name'),
                    'partner_id': vendor_name,
                    'date_order': record.get('date_order'),
                    'amount_total': record.get('amount_total'),
                })

            print(order)



        # order line

            line_ids = record.get('order_line')
            # #
            # #
            # #
            orders = models.execute_kw(self.database, uid, self.password, 'purchase.order.line', 'read',
                                           [line_ids], {
                                               'fields': ['product_id', 'product_qty', 'price_unit', 'price_subtotal',]
                                           })
            print("orderline",orders)
            for line in orders:
                print("line",line)
                product = line.get('product_id')
                print(product,"product")


                if product:
                    pro = product[1]
                    print("name", pro)
                    # prod = product[1]
                    liness = self.env['purchase.order.line'].create({
                        'order_id': order.id,
                        'product_id' : pro,
                        'product_qty' : line.get('product_qty'),
                        'price_unit': line.get('price_unit'),
                        'price_subtotal' : line.get('amount_total'),})

                    print("lines", liness)



            #
            # return {
            #     'type': 'ir.actions.act_window',
            #     'name': 'po order',
            #     'res_model': 'purchase.migration.line',
            #     'view_mode': 'list',
            #     'target': 'current',
            # }



        return {
                'type': 'ir.actions.act_window',
                'name': 'po order',
                'res_model': 'purchase.order',
                'view_mode': 'list,form',
                'target': 'current',
            }

