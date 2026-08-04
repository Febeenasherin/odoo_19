# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import base64

from odoo.tests import result


class WebsiteMain(http.Controller):
    """ website"""
    # registration

    @http.route(['/website/student/list'], type='http', auth="public", website=True)
    def student_list(self, **kw):
        students = request.env['school.students'].sudo().search([])

        return request.render('school_management.student_register_list_template',
                              {'students': students})

    @http.route(['/website/student/form'], type='http', auth="public", website=True)
    def student_form(self, **kw):
        classes = request.env['school.class'].sudo().search([])



        return request.render('school_management.student_register_form_template',
                              {'classes': classes})

    # student form view
    @http.route(['/website/student/form/view/<int:student_id>'], type='http', auth="public", website=True)

    def student_form_view(self, student_id, **kw):
        student = request.env['school.students'].sudo().browse(student_id)

        return request.render('school_management.student_form_view_template',
                          {'students': student})

    @http.route(['/website/student/create'], type='http', auth="public", methods=['POST'], website=True, csrf=True)
    def create_student(self, **post):

        image_encode = False
        image = post.get('image')
        if image:
            image_encode = base64.b64encode(image.read())

        request.env['school.students'].sudo().create({
            'image' : image_encode,
            'first_name': post.get('first_name'),
            'last_name': post.get('last_name'),
            'email': post.get('email'),
            'phone_no': post.get('phone_no'),
            'gender': post.get('gender'),
            'class_id': post.get('class_id'),
            'status' : 'registration'
            # 'customer_rank': 1,
        })

        request.env['school.students'].sudo().write( {'status': 'registration'})
        return request.render('school_management.student_success_template')



    # leave request
    @http.route(['/website/leave/form'], type='http', auth="public", website=True)
    def customer_form(self, **kw):
        leave = request.env['school.students'].sudo().search([])
        classes = request.env['school.class'].sudo().search([])

        return request.render('school_management.leave_form_template',
                              {'leave': leave,
                               'classes': classes})


    @http.route(['/website/leave/create'], type='http', auth="public", methods=['POST'], website=True, csrf=True)
    def create_customer(self, **post):
        request.env['school.leaves'].sudo().create({
            'student_id': post.get('student_id'),
            'start_date': post.get('start_date'),
            'end_date': post.get('end_date'),
            'class_id': post.get('class_id'),
            'reason': post.get('reason'),
            #     'customer_rank': 1,
        })
        return request.render('school_management.student_leave_template')


    # student leave create

    @http.route(['/website/student/leave/form'], type='http', auth="public", website=True)
    def student_own_form(self, **kw):
        student = request.env['school.students'].sudo().search([('user_id', '=', request.env.user.id)],limit=1)
        classes = request.env['school.class'].sudo().search([])

        return request.render('school_management.student_leave_form_template',
                              {'student': student,
                               'classes': classes
                             })


    @http.route(['/website/student/leave/create'], type='http', auth="public", methods=['POST'], website=True, csrf=True)
    def create_student_own(self, **post):
        student = request.env['school.students'].sudo().search([('user_id', '=', request.env.user.id)])
        # user_name = request.env.user.name if request.env.user.id else 'Guest'
        request.env['school.leaves'].sudo().create({
            'student_id': student.id,
            'class_id': post.get('class_id'),
            'start_date': post.get('start_date'),
            'end_date': post.get('end_date'),
            'reason': post.get('reason'),
            #     'customer_rank': 1,
        })
        return request.render('school_management.portal_student_leave_template')



    # latest event

    @http.route('/get_events', auth="public", type='jsonrpc',website=True)
    def get_events(self):

        """Get the website categories for the snippet."""



        events = request.env['school.events'].sudo().search([], order='start_date desc', limit=4)

        # image_encode = False
        # image = events.image
        # if image:
        #     image_encode = base64.b64encode(image.read())

        result = []
        for event in events:
            result.append({
                'id': event.id,
                'name': event.name,
                'start_date': event.start_date,
                'end_date': event.end_date,
                'venue': event.venue,
                'image' : event.image,
            })


        values = {
            'event': events,
        }
        # print("val",values)
        print("event",result)
        # print("image",event.image)
        return result
        # return request.render('school_management.latest_event', values)

    @http.route(['/website/event/form/view/<int:event_id>'], type='http', auth="public", website=True)
    def student_form_view(self, event_id, **kw):
        event = request.env['school.events'].sudo().browse(event_id)

        print("eve", event)
        print(event.name)

        return request.render('school_management.event_form_view_template',
                              {'event': event})




    # @http.route(['/website/students/events/<int:event_id>'], auth="public", type='jsonrpc', website=True)
    # def latest_event(self, event_id, **kw):
    #     event = request.env['school.events'].sudo().search([()] , order = 'start_date desc', limit=4)
    #
    #     print("eve",event)
    #
    #     return request.render('school_management.school_event_template',
    #                           {'event': event})








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