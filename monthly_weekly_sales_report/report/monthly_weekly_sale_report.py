# -*- coding: utf-8 -*-
from odoo import fields, models, api
from datetime import timedelta, date


class MonthlyWeeklySalesReport(models.Model):
    _name = 'monthly.weekly.sales.report'



    customer_ids = fields.Many2many('res.partner', string='Customers')
    sale_team_id = fields.Many2one('crm.team', string='Sales Team')
    filter_type = fields.Selection([('week', 'Week'), ('month', 'Month'), ('custom', 'Custom')], string='Filter Type', )

    start_date = fields.Date(string="Date from")
    end_date = fields.Date(string="To")

    @api.model
    def send_Daily_sale_report(self):

        record = self.env['monthly.weekly.sales.report'].search([])
        print("rec",record)

        orders = self.env['sale.report'].search([])
        print("report",orders)
        today = date.today()
        customer = self.env['sale.report'].search([('partner_id', '=', self.customer_ids.ids)])
        print("customer", customer)
        print("sale", self.customer_ids)
        # for order in orders:
        for sale in record:
            print("selected", sale.customer_ids)
            if sale.customer_ids in order.partner_id:
                customer = sale.customer_ids
                print("custmr order", customer)

            # customer = orders.partner_id == sale.customer_ids
            # print(customer)

            if sale.filter_type == 'week':
                week_start = today - timedelta(days=today.weekday())
                week_end = week_start + timedelta(days=6)

                sale.start_date = week_start
                sale.end_date = week_end
