# # -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class ClearCart(http.Controller):
   # clear cart when clicking button
    @http.route(['/cart/'], type='http', auth='public', website=True)

    def clear(self):
       order= request.cart
       print(request)

       product = order.order_line.unlink()
       print(order)
       print(product)

       qty = request.session['website_sale_cart_quantity']
       print(qty)
       request.session['website_sale_cart_quantity'] = 0


       # request.session.get('website_sale_cart_quantity')
       # self.cart_quantity = 0




       return request.redirect('/shop/cart')