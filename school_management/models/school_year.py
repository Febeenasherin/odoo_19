# -*- coding: utf-8 -*-
from odoo import fields, models


class SchoolYear(models.Model):
    """ school year """
    _name = 'school.year'
    _description = 'School Year'

    name=fields.Char(string='Name')




