# -*- coding: utf-8 -*-
from odoo import fields, models, api


class MonthlyWeeklySalesReport(models.TransientModel):
    _name = 'monthly.weekly.sales.report'



    customer_ids = fields.Many2many('res.partner', string='Customers')
    sale_team_id = fields.Many2one('crm.team', string='Sales Team')
    filter_type = fields.Selection([('week', 'Week'), ('month', 'Month'), ('custom', 'Custom')], string='Filter Type', )

    start_date = fields.Date(string="Date from")
    end_date = fields.Date(string="To")