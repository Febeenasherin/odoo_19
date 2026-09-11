# -*- coding: utf-8 -*-
from odoo import models


class SleReport(models.AbstractModel):
    _name = 'report.monthly_weekly_sales_report.sale_report'

    def _get_report_values(self, docids, data=None):

        record = self.env['monthly.weekly.sales.report'].browse(docids)
        print("record:",record)

        customer =self.env['res.partner'].browse(data.get('customer_id'))
        print("customer:",customer)

        sale_order = self.env['sale.order'].browse(data.get('sale_order_id'))
        print("sale_order:",sale_order)

        return {
            'docs' : record,
            'doc_ids' : docids,
            'doc_model' : 'monthly.weekly.sales.report',
            'sale_orders' : sale_order,
            'customer' : customer,
            'start_date' : data.get('start_date'),
            'end_date' : data.get('end_date'),

        }


