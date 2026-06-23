# -*- coding: utf-8 -*-

from odoo import fields,models

class SchoolEvents(models.Model):
    _name = 'school.events'
    _description = 'School Events'

    name = fields.Char(string='Event Name')
    venue = fields.Text(string='Venue')
    club_id = fields.Many2one('school.clubs', string='Club')
