# -*- coding: utf-8 -*-
from odoo import fields, models


class SchoolEvents(models.Model):
    """ event """
    _name = 'school.events'
    _description = 'School Events'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Event Name')
    venue = fields.Html('Venue')
    club_id = fields.Many2one('school.clubs', string='Club')
    start_date = fields.Datetime(string='Start Date')
    end_date = fields.Datetime(string='End Date')
    image = fields.Image(string="image")
    status = fields.Selection([("new", "New"), ("ongoing", "Ongoing"), ("completed", "Completed")],
                              default='new', string="Status")

    def ongoing(self):
        """change status into ongoing"""
        print("self",self)
        self.status = 'ongoing'


    def completed(self):
        """change status into completed"""
        print("self",self)
        self.status = 'completed'

