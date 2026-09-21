# -*- coding: utf-8 -*-
from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    revision_ids = fields.One2many('sale.order.revision', 'sale_id', string='Revisions')

    revision_count = fields.Integer(compute='_compute_revision_count')

    @api.depends('revision_ids')
    def _compute_revision_count(self):
        for rec in self:

           rec.revision_count = len(rec.revision_ids)

    def action_open_revision(self):

        """ smart button in club form view"""
        print("done")
        for rec in self:
            print("records",rec)

            return {
            'type': 'ir.actions.act_window',
            'name': 'Sale order Revision',
            'res_model': 'sale.order.revision',
            'domain': [('sale_id' ,'=' , rec.id)],
            'view_mode': 'list',
                }



    def write(self, vals):
        print("values", vals)

        for rec in self:
            note =" "


            if rec.state == 'sent':

                if 'state' in vals:
                    state=vals['state']
                    note = f"state changed to {state}"


                # if rec.partner_id:
                #     partner = vals['partner_id']
                #     note = f"partner changed to {partner}"






                new = self.env['sale.order.revision'].create({
                        'sale_id': self.id,
                        'revision_no' : len(rec.revision_ids)+1,
                        'revision_note' : note
                    })
                print("new",new)



                    # if 'state' in vals:
                    #     print("changed")
                    #     state = vals[line]zz
                    #     print("state",state)
                    #
                    #     note = f"state is changed {self.state}"
                    #     print("note",note)


        return super().write(vals)






