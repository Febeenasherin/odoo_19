# -*- coding: utf-8 -*-
from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = 'project.project'


    # task_id = fields.Many2one(
    #     'project.template',
    #     string='Task',
    # )


    def create_project_template(self):
        for rec in self:

            template = self.env['project.template'].create({
                'name' : rec.name,
                'partner_id' : rec.partner_id.id,
            })



        tasks = self.task_ids
        print(tasks)

        for task in tasks:

            self.env['project.project.task'].create({
                'project_id' : template.id,
                'name' : task.name,


            })


        return {
            'type': 'ir.actions.act_window',
            'name': 'project',
            'res_model': 'project.template',
            'view_mode': 'form',
            'res_id': template.id,
        }

