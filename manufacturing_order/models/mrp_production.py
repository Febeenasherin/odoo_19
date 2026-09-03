# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MrpProductionExt(models.Model):
    _name = 'mrp.production.ext'

    name = fields.Char(string='name')
    product_id = fields.Many2one(comodel_name='product.product', compute='_compute_product_id', readonly=False,)
    bom_id = fields.Many2one(comodel_name='mrp.bom', )
    planned_date = fields.Date(string="Planned Date")
    quantity = fields.Float(string="Quantity")
    state = fields.Selection([
        ('draft', 'Draft'),('done', 'Done'),


    ])
    bom_component = fields.Char(string='Bom Component')
    material_line_ids = fields.One2many(comodel_name='mrp.production.material.line', inverse_name='production_id')

    @api.model_create_multi
    def create(self, vals_list):
        """ sequence"""

        print("self", self, vals_list)
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals["name"] = self.env['ir.sequence'].next_by_code('name') or 'New'

        return super(MrpProductionExt, self).create(vals_list)

    @api.onchange('product_id', 'bom_id', 'quantity')
    def _onchange_product_id(self):
        print("dd")

        # def _onchange_bom_id(self):
        #     # products = self.env['simple.production'].search([])
            #
        self.material_line_ids = [(5, 0, 0)]
            #     print(self.production_line_ids)

        values = []



        for line in self.bom_id.bom_line_ids:
            print("line", line.product_id.id)

            # if not self.bom_id.bom_line_ids:
            #     raise ValidationError("Bom line not available")

            quantity = line.product_qty * self.quantity
            print("quantity", quantity)
            values.append((0, 0, {
                    'product_id': line.product_id.id,
                    'required_qty': line.product_qty * self.quantity,
                    'available_qty': line.product_id.qty_available,
                }))

            self.material_line_ids = values

            print(values)

    # @api.depends('product_id')
    # def _compute_product_id(self):
    #     print("hgh")
    #     # for production in self:
    #     #     bom = production.product_id
    #     #     if bom and (not production.bom_id
    #     #             or bom.bom_id and bom.bom_id != production.bom_id
    #     #         ):
    #     #             production.bom_id = bom.id
    #
    #     for production in self:
    #         bom = production.bom_id
    #         if bom and (
    #                 not production.product_id
    #                 or bom.product_id and bom.product_id != production.product_id
    #         ):
    #             production.product_id = bom.product_id











