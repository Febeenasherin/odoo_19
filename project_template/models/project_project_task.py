# -*- coding: utf-8 -*-
from odoo import fields, models



class ProjectProjectTask(models.Model):
    _name = 'project.project.task'


    name = fields.Char(string='Name')
    milestone = fields.Many2one('project.milestone', string='Milestone')
    assigners = fields.Many2many('res.users', string='Assigners')
    customer = fields.Many2one('res.partner', string='Customer')
    project_id = fields.Many2one('project.template', string='Project')