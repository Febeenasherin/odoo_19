# -*- coding: utf-8 -*-
from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"



    def create_project_task_template(self):

        print(self)

        print("dsd",self.project_id)
        print("ss",self.project_id.name)

        for rec in self:

            self.env["project.task.template"].create({
            'name' : rec.name,
            'project_id' : rec.project_id.id,
            })