# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MrpProductionMaterialLine(models.Model):
    _name = 'mrp.production.material.line'


    production_id = fields.Many2one('mrp.production.ext',)
    product_id = fields.Many2one('product.product',)
    required_qty = fields.Float('Required Qty')
    available_qty = fields.Float('Available Qty')
    consumed_qty = fields.Float('Consumed Qty')

    is_material_available = fields.Boolean('Material Available')

    # @api.onchange('product_id', 'bom_id')
    # def _onchange_product_id(self):
    #     print("dd")
    #
    #     for line in self:
    #
    #         bom = self.env['mrp.bom'].search([('product_id', '=', line.product_id.id)])
    #         print("bom",bom)
    #
    #         if bom:
    #             for bom_line in self.product_id:
    #                 print("bom_line",bom_line)



    # def compute_available_qty(self):








