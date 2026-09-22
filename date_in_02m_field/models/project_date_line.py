# -*- coding: utf-8 -*-
from odoo import fields, models


class ProjectDateLine(models.Model):
    _name = 'project.date.line'


    month = fields.Char(string='Month')
    year = fields.Char(string='Year')
    from_date = fields.Date(string='From Date')
    to_date = fields.Date(string='To Date')
    project_id = fields.Many2one('project.project', string='Project')