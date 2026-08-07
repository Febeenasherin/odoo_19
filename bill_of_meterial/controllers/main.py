# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Main(http.Controller):

    @http.route(['/bom/product/<int:product_id>'], type='http', auth="public",  website=True)
    def website_bom_product(self,product_id):
        print("working")

        product = request.env['product.template'].sudo().browse(product_id)

        # print(product.name)
        selected_product = request.website.bom_product_ids
        print(selected_product)
        bom = False
        if product in selected_product:
            bom = request.env['mrp.bom'].sudo().search([('product_tmpl_id', '=', product.id)],)
            print("bom",bom)

        # bom = request.env['mrp.bom'].sudo().search([('product_tmpl_id','=',product.id)])
        # print(bom)

        return request.render('bill_of_meterial.bom_product_view_template', {
                        'bom' : bom,
        })


