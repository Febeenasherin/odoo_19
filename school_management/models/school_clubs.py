# -*- coding: utf-8 -*-
from odoo import fields, models


class SchoolClubs(models.Model):
    """school clubs"""
    _name = 'school.clubs'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Club Name')
    student_ids = fields.Many2many('school.students', 'club_ids', string='Student', compute='_compute_student_ids')
    event_ids = fields.One2many('school.events','club_id', string='Event')
    event_count = fields.Integer(string='Event Count', compute='_compute_event_count')

    def _compute_event_count(self):
        """it usd for total count of event ,itss used for smart button"""
        for rec in self:
            rec.event_count = len(rec.event_ids)

    def action_open_events(self):
        """ smart button in club form view"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Events',
            'res_model': 'school.events',
            'domain': [('club_id' ,'=' , self.id)],
            'view_mode': 'list,form',
            }

    def _compute_student_ids(self):
        """this function used for list student under that club in club form view"""
        for club in self:
            club.student_ids=self.env['school.students'].search([('club_ids' , 'in' , club.id)])
