# -*- coding: utf-8 -*-
from odoo import fields, models, api

class ProjectTaskStage(models.Model):
    _inherit = 'project.task.type'



    default_duration = fields.Integer(string="duration", default=1)


