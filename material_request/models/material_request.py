# -*- coding: utf-8 -*-
from odoo import fields, models, api
from datetime import date

from odoo.exceptions import ValidationError


class MaterialRequest(models.Model):
    """school student registration"""
    _name = 'material.request'

    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(copy=False, required=True, default='New')
    requested_id = fields.Many2one('res.users', string='Requested by', default=lambda self: self.env.user.id, readonly=True)
    state = fields.Selection([('draft', 'Draft'), ('requested', 'Requested'), ('first_approval', 'First Approval'),
                              ('second_approval', 'Approved'), ('reject', 'Rejected')], default='draft')

    requested_date = fields.Date('Requested date',default=date.today(), readonly=True)
    request_line_ids = fields.One2many('material.request.line', 'request_id',)


    purchase_order_ids = fields.One2many('purchase.order','material_purchase_id' ,string='Purchase Orders' ,readonly=True)
    purchase_count = fields.Integer('Purchase Order Count', compute='_compute_purchase_count', store=True)

    internal_transfer_ids = fields.One2many('stock.picking', 'material_internal_id', string='Internal Transfers' ,readonly=True)
    internal_count = fields.Integer('Internal Transfers Count', compute='_compute_count', store=True)

    @api.depends('purchase_order_ids')
    def _compute_purchase_count(self):
        print("working compute")
        for record in self:
            record.purchase_count = len(record.purchase_order_ids)
            print(record.purchase_count,"count")

    @api.depends('internal_transfer_ids')
    def _compute_count(self):
        for record in self:
            record.internal_count = len(record.internal_transfer_ids)
            print(record.internal_count,"count")



    @api.model_create_multi

    def create(self, vals_list):
        """ sequence"""

        print("self", self, vals_list)
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals["name"] = self.env['ir.sequence'].next_by_code('name') or 'New'

        return super(MaterialRequest, self).create(vals_list)

    def action_request(self):
        if not self.env.user._has_group('material_request.group_material_user'):
            raise ValidationError("only user can create request")

        print("button request")
        self.state = 'requested'

    def action_first_approve(self):
        if not self.env.user._has_group('material_request.group_material_manager'):
            raise ValidationError("only manager can approve")
        self.state = 'first_approval'

    def action_second_approve(self):
        if not self.env.user._has_group('material_request.group_material_head'):
            raise ValidationError("only head can approve")
        self.state = 'second_approval'


        internal = self.env['stock.picking.type'].search([('code', '=', 'internal')])
        print("internal", internal)


        for line in self.request_line_ids:
            if line.request_type == 'purchase order':
                for vendor in line.vendor_ids:
                    rfq = self.env['purchase.order'].create({
                        'partner_id': vendor.id,
                        'material_purchase_id' : self.id,
                        'order_line' : [fields.Command.create({
                            'product_id': line.product_id.id,
                            'name' : line.product_id.name,
                            'product_qty': line.product_qty,
                        })]
                    })

                    print("rfq", rfq)


            if line.request_type == 'internal transfer':
                transfer = self.env['stock.picking'].create({
                    'partner_id': self.requested_id.id,
                    'picking_type_id': internal.id,
                    'location_id' : line.source_id.id,
                    'location_dest_id' : line.destination_id.id,
                    'material_internal_id' : self.id,
                    'move_ids' : [fields.Command.create({
                        'product_id': line.product_id.id,
                        'product_uom_qty': line.product_qty,
                    })]
                })

                print(transfer,"internal")


    def action_reject(self):
        if not self.env.user._has_group('material_request.group_material_head'):
            raise ValidationError("only head can reject")
        self.state = 'reject'



    def action_open_purchase(self):
        """ smart button in club form view"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Purchase Order',
            'res_model': 'purchase.order',
            'domain': [('material_purchase_id' ,'=' , self.id)],
            'view_mode': 'list,form',
            }


    def action_open_internal(self):
        """ smart button in club form view"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Internal Transfer',
            'res_model': 'stock.picking',
            'domain': [('material_internal_id' ,'=' , self.id)],
            'view_mode': 'list,form',
            }




# 'domain': [('id' ,'in' , self.purchase_order_ids.ids)],