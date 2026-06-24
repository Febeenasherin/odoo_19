# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartnerOfficeStaff(models.Model):
    """partner selection"""
    _inherit = 'res.partner'

    partner = fields.Selection([('student', 'Student'), ('office staff', 'Office Staff'), ('teacher', 'Teacher')], string="Partner")