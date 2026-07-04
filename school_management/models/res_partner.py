# -*- coding: utf-8 -*-
from odoo import fields, models



class ResPartner(models.Model):
    """ add field partner to contact form"""
    _inherit = 'res.partner'

    partner = fields.Selection([('teacher', 'Teacher'), ('student', 'Student'), ('office staff', 'Office staff')], string="Partner", ondelete="cascade")






