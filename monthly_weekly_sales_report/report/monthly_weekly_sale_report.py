# -*- coding: utf-8 -*-
from odoo import fields, models, api
from datetime import timedelta, date
import base64


class MonthlyWeeklySalesReport(models.Model):
    _name = 'monthly.weekly.sales.report'



    customer_ids = fields.Many2many('res.partner', string='Customers')
    sale_team_id = fields.Many2one('crm.team', string='Sales Team')
    filter_type = fields.Selection([('week', 'Week'), ('month', 'Month'), ('custom', 'Custom')],
                                   string='Filter Type', default='week')

    start_date = fields.Date(string="Date from")
    end_date = fields.Date(string="To")
    is_active = fields.Boolean(string="Sended")
    type =   fields.Selection([('normal', 'Normal'), ('detailed', 'Detailed')], string='Type')

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
            # print("selected", sale.customer_ids)
            # if sale.customer_ids in order.partner_id:
            #     customer = sale.customer_ids
            #     print("custmr order", customer)

            # customer = orders.partner_id == sale.customer_ids
            # print(customer)

            if sale.filter_type == 'week':
                week_start = today - timedelta(days=today.weekday())
                week_end = week_start + timedelta(days=6)

                start_date = week_start
                end_date = week_end

            elif sale.filter_type == 'month':

                month_start = today.replace(day=1)
                next_month = (month_start + timedelta(days=32)).replace(day=1)
                month_end = next_month - timedelta(days=1)

                start_date = month_start
                end_date = month_end

                print("month strt",sale.start_date)
                print("month end",sale.end_date)

            else:
                start_date = sale.start_date
                end_date = sale.end_date


            for customer in sale.customer_ids:

                if not customer.email:
                    continue

                sale_order = self.env['sale.order'].search([('partner_id', '=', customer.id), ('state', 'in', 'sale'),
                                                            ('date_order', '>=', start_date), ('date_order', '<=', end_date),
                                                            ('team_id', '=', record.sale_team_id.id)])


                print("sale order",sale_order)


                # for order in sale_order:
                #     sales_orders =
                # if customer not in sale_order:
                #     continue
                # print("customer", customer)
                # print("sale", sale_order)

                # if sale.sale_team_id:

#                     sale_order.append('team_id', '=', sale.id)


#                     print("all orders",sale_order)

                # Get report action
                report_action = self.env.ref(
                    'monthly_weekly_sales_report.action_sale_report_template',
                    raise_if_not_found=False
                )
                print("report", report_action)

                pdf_content, _ = report_action._render_qweb_pdf("monthly_weekly_sales_report.sale_report",
                                                                res_ids=sale.ids,
                                                                data = {
                                                                    'sale_order_id' : sale_order.ids,
                                                                    'customer_id' : customer.id,
                                                                    'start_date' : start_date,
                                                                    'end_date' : end_date,
                                                                })

                template = self.env.ref('monthly_weekly_sales_report.template_sales_report',

                )
                print("template",template)

                pdf_base64 = base64.b64encode(pdf_content)
                # #     # Create attachment
                attachment = self.env['ir.attachment'].create({
                    'name': 'Sale_Report.pdf',
                    'type': 'binary',
                    'datas': pdf_base64,
                    'mimetype': 'application/pdf',
                })

                # for rec in user:
                if template:
                    template.send_mail(
                    customer.id,
                        force_send=True,

                        email_values={'attachment_ids': [(4, attachment.id)],
                                      'email_to': customer.email,
                                      'body_content': f"<p>Hello {today}</p>", }

                    )



                    record.write({
                        'is_active' : True,
                    })








