# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    partner = fields.Selection([('teacher', 'Teacher'), ('student', 'Student'), ('office staff', 'Office staff')], string="Partner")
