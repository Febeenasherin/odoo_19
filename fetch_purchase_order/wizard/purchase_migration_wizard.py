# -*- coding: utf-8 -*-
from odoo import fields, models, api
import xmlrpc.client
import ssl
import requests

from odoo.exceptions import ValidationError


class PurchaseMigrationWizard(models.TransientModel):
    _name = "purchase.migration.wizard"


    url = fields.Char(string="url", default="http://127.0.0.1:8069",required=True)
    database = fields.Char(string="database",)
    username = fields.Char(string="username",)
    password = fields.Char(string="password",)


    def import_purchase_order_action(self):
        print("self")

        # common = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/common")
        # print("common", common)
        #
        # uid = common.authenticate(self.database, self.username, self.password, {})
        # print("uid", uid)
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
                                        'fields' : ['id', 'name', 'partner_id', 'date_order', 'amount_total']
                                         })
        print(f"Fetched {len(purchase_order)} customers from Odoo 16")

        self.env['purchase.migration'].search([])

        for record in purchase_order:
            print(record)