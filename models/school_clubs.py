# -*- coding: utf-8 -*-

from odoo import fields,models

class SchoolClubs(models.Model):
    """school clubs"""
    _name = 'school.clubs'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Club Name')
    student_id = fields.Many2one('school.students',string='Student')

    event_count = fields.Integer(string='Event Count', compute='_compute_event_count')

    def _compute_event_count(self):
        for event in self:
            event_count = self.env['school.events'].search_count([('name', '=' , event.name)])
            event.event_count = event_count


    def action_open_events(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Open Events',
            'res_model': 'school.events',
            'domain': [('name' ,'=' , self.name)],
            'view_mode': 'list',
            'target': 'new',


        }