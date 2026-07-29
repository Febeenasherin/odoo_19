# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/hello-odoo', type='http', auth='public', website=True)
    def hello_page(self, **kwargs):
        """
        This controller handles the request for the /hello-odoo page.
        It renders a QWeb template and passes a dynamic value.
        """
        user_name = request.env.user.name if request.env.user.id else 'Guest'

        return request.render('custom_web_page.hello_page_template', {
            'user_name': user_name,
        })
