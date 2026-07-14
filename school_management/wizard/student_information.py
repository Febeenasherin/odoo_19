# -*- coding: utf-8 -*-
from odoo import fields, models, api


class StudentInformation(models.TransientModel):
    _name = 'student.information'
    _inherit = 'school.students'

