# -*- coding: utf-8 -*-
import email
from odoo import fields, models, api
from datetime import date, timedelta



class SchoolEvents(models.Model):
    """ event """
    _name = 'school.events'
    _description = 'School Events'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Event Name')
    venue = fields.Html('Venue')
    club_id = fields.Many2one('school.clubs', string='Club')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Datetime(string='End Date')
    image = fields.Image(string="image")
    status = fields.Selection([("new", "New"), ("ongoing", "Ongoing"), ("completed", "Completed")],
                              default='new', string="Status")
    active = fields.Boolean(string='active', default=True)

    def ongoing(self):
        """change status into ongoing"""
        print("self",self)
        self.status = 'ongoing'


    def completed(self):
        """change status into completed"""
        print("self",self)
        self.status = 'completed'

        for record in self:
            record.write({'active': False})


    @api.model
    def _auto_send_email(self):
        """ automatically send email to employees ,email send 2 day before starting event"""
        print("working")
        reminder_date = date.today() + timedelta(days=2)


        events = self.search([('start_date', '=', reminder_date)])
        employee = self.env['res.partner'].search([('email','!=' ,False), ('partner','=' ,('teacher','office staff','student'))])

        template = self.env.ref('school_management.email_template_event')
        emails =  employee.mapped('email')

        for event in events:

            template.send_mail(event.id,force_send=True,email_values={'email_to':emails [0],
                                                                      'email_cc':emails [1:]})

        print("emp",employee.mapped('name'))
        print("temp",template)
        print("events",events)





