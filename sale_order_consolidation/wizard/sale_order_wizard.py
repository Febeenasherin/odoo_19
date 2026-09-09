# -*- coding: utf-8 -*-
from odoo import fields, models, api
import xmlrpc.client
from odoo.exceptions import ValidationError


class SaleOrderWizard(models.TransientModel):
    _name = "sale.order.wizard"


    # customer_id = fields.Many2one('res.partner', string="Customer")

    sale_order_ids = fields.Many2many('sale.order')
    dominating_order_id =  fields.Many2one('sale.order')
    partner_id = fields.Many2one('res.partner')




    def action_merge(self):
        orders = self.dominating_order_id
        partner = self.partner_id.id
        sale_order = self.sale_order_ids
        print("order",orders)
        print("partner",partner)
        print("sale_order",sale_order)


        first_order = sale_order[0]
        print("first_ord",first_order)
        other_order = sale_order[1:]
        print("other_ord",other_order)


        first_pro = first_order.order_line.mapped("product_id")
        print("first_pro",first_pro)

        others = sale_order - orders
        print("others",others)
        count = 0

        for order in others:
            for line in order.order_line:
                print("line",line)
                products = orders.filtered(lambda p: p.order_line.product_id == line.product_id)
                print("products",products)
                if products:
                    orders.order_line.product_uom_qty += line.product_uom_qty

                else :
                    print("jj")
                    orders = line.copy({
                        'order_id' :  self.dominating_order_id.id,
                    })
                    print("orders",orders)
                count += 1
            print("count",count)


        return {
            'name': 'Dominating orders',
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'view_mode': 'form',
            'res_id': orders.id,
            'target': 'current',

        }

        # for order in self:
        #     not_choose = order not in orders
        #     for line in not_choose:
        #             orders.write({
        #             'order_id': orders,
        #                 'order_line': [fields.Command.create({
        #                     'product_id': line.product_id.id,
        #                     'product_uom_qty': line.product_uom_qty,
        #                 })]
        #             })

        # for order in sale_order:
        #     print("order",order)
        #     new = sale_order.order_line.mapped('product_id')
        #     print("new",new)
        #
        # for order in self:
        #     if order.id != orders:
        #
        #
        #
        #
        #     for rec in other_order.order_line:
        #         if prod in rec:
        #             product = rec
        #             print("product",product)








                # prod = product
                # # if product in order.order_line.product_id:
                # #     print("rttg",order.order_line.product_uom_qty)
                # if prod == order.order_line.product_id:
                #     print("sdd",product.name)





            # if len(product) == 0:
            #     product.append(order_line)
            #
            # elif  order_line in product:
            #     product.append(order_line)
            #
            # else :
            #     pro.append(order_line)
            #
            #
            # print("same",product)
            # print("diff",pro)
            #
            #
            # new_order = self.env['sale.order'].write({
            #
            #     'partner_id': partner,
            #     'name' : orders,
            #     'order_line': [fields.Command.create
            #         ({
            #             'product_id': product[0] and pro,
            #             'product_uom_qty': 1,
            #         }),
            #     ]
            # })
            #
            #
            # print("new_order",new_order)
            #
            #
            # return new_order









    # def action_order_sale(self):
    #     print("jjj")
    #
    #
    #
    #
    #     return {
    #                 'type': 'ir.actions.act_window',
    #                 'name': 'dominating order',
    #                 'res_model': 'sale.order.wizard',
    #                 'view_mode': 'form',
    #                 'target': 'new',
    #             }

