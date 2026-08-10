# # -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class ClearCart(http.Controller):

    @http.route(['/cart/'], type='http', auth='public', website=True)

    def clear(self):
       order= request.cart

       product = order.order_line.unlink()
       print(order)
       print(product)




       return request.redirect('/shop')