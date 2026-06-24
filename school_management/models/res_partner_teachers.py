# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartnerTeachers(models.Model):
    _inherit = 'res.partner'

    partner =  fields.Selection([('teacher', 'Teacher'), ('student', 'Student')], string="Partner")
