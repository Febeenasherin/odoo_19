# -*- coding: utf-8 -*-
from odoo import fields, models


class ProjectTask(models.Model):
    _name = 'project.task.template'



    name = fields.Char(required=True)
    project_id = fields.Many2one(comodel_name='project.project')




    def create_project_task(self):

        self.env['project.task'].create({
            'name': self.name,
            'project_id': self.project_id.id,
        })

        print("project",self.project_id)
