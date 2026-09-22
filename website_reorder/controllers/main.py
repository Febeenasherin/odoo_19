# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class WebsiteReorder(http.Controller):
    """website reorder product"""
    @http.route(['/my/orders/<int:order_id>/reorder'], type='http', auth='public', website=True)


    def reorder(self, order_id, **kw):
        """user can reorder sale order product when clicking button"""

        sale_order = request.env['sale.order'].browse(order_id)
        print(sale_order)

        cart = request.cart
        print("cart", cart)

        for line in sale_order.order_line:
            print(line)
            product_id = line.product_id.id
            print(product_id)
            add_qty = line.product_uom_qty
            print(add_qty)

            cart._cart_add(product_id=product_id,
                           add_qty=add_qty, )

        return request.redirect('/shop/cart')
