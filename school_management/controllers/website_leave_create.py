# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class WebsiteCustomerForm(http.Controller):
    @http.route(['/website/leave/form'], type='http', auth="public", website=True)
    def customer_form(self, **kw):
        leave= request.env['school.leaves'].sudo().search([])


        return request.render('school_management.leave_form_template',
                              {'leave':leave})
    @http.route(['/website/leave/create'], type='http', auth="public", methods=['POST'], website=True, csrf=True)
    def create_customer(self, **post):
        request.env['school.leaves'].sudo().create({
            'student_id': post.get('student_id.first_name'),
            'start_date': post.get('start_date'),
            'end_date': post.get('end_date'),
        #     'customer_rank': 1,
        })
        return request.render('custom_module_name.student_leave_template')
