# -*- coding: utf-8 -*-
from odoo import fields, models


class SalesOrderRevision(models.Model):
    _name = 'sale.order.revision'



    revision_no = fields.Integer(string="Revision Number")
    modified_on = fields.Datetime(string="Date and Time")
    modified_by = fields.Many2one(comodel_name='res.users', string="User")
    revision_note = fields.Text(string="Revision Note")
    sale_id = fields.Many2one(comodel_name='sale.order', string="Sale Order")
