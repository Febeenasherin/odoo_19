# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.release import product_name


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    bom_product_ids = fields.Many2many(related='website_id.bom_product_ids',string='Products',readonly=False)

    @api.model
    def get_values(self):
        #     """Get the values from settings."""


        # product = self.env['product.template'].search(['product_id', '=', self.id])
        # print("product",product)

        selected_product = self.bom_product_ids
        print("hhhh",selected_product)

        bom = self.env['mrp.bom'].sudo().search([('product_tmpl_id', '=', self.bom_product_ids)], )
        print("bom", bom)


        # bom = False
        # if selected_product:
        #     bom = self.env['mrp.bom'].sudo().search([('product_tmpl_id', '=', self.id)], )
        #     print("bom", bom)

        res = super(ResConfigSettings, self).get_values()
        return res
