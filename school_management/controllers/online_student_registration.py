# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class WebsiteStudentRegistrationForm(http.Controller):

    @http.route(['/website/student/list'], type='http', auth="public", website=True)
    def customer_form(self, **kw):
        students = request.env['school.students'].sudo().search([])

        return request.render('school_management.student_register_list_template',
                              {'students': students})

    @http.route(['/website/student/form'], type='http', auth="public", website=True)
    def customer_form(self, **kw):
        classes = request.env['school.class'].sudo().search([])


        return request.render('school_management.student_register_form_template',
                              {'classes': classes})



    @http.route(['/website/student/create'], type='http', auth="public", methods=['POST'], website=True, csrf=True)
    def create_student(self, **post):
        request.env['school.students'].sudo().create({
            'image' : post.get('image'),
            'first_name': post.get('first_name'),
            'last_name': post.get('last_name'),
            'email': post.get('email'),
            'phone_no': post.get('phone_no'),
            'gender': post.get('gender'),
            'class_id': post.get('class_id'),
            # 'customer_rank': 1,
        })
        return request.render('school_management.student_success_template')





    # @http.route(['/website/form/submit'], type='http', auth='public', website=True)
    # def file_upload(self, redirect=None, **kw):
    #     current_partner = request.env.user.partner_id
    #     uploaded_file = kw.get('att')
    #     if uploaded_file:
    #         file_name = uploaded_file.filename
    #         file_content = uploaded_file.read()
    #         attachment = request.env['ir.attachment'].sudo().create({
    #             'name': file_name,
    #             'type': 'binary',
    #             'datas': base64.b64encode(file_content),
    #         #     'res_model': 'res.partner',
    #         #     'res_id': current_partner.id,
    #         })
    #         current_partner.sudo().write({
    #             'attachment_ids': [(4, attachment.id)],
    #         })
    #     return request.redirect(redirect or '/')