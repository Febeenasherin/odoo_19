# -*- coding: utf-8 -*-
from odoo import fields, models



class ProjectProject(models.Model):
    """inherit product template"""
    _name = 'project.template'



    name = fields.Char(string="Project Name")
    partner_id = fields.Many2one('res.partner')
    project_manager = fields.Many2one('res.users', string='Project Manager')
    company_id = fields.Many2one('res.company',string='Company')
    task_ids = fields.One2many('project.project.task','project_id', string='Tasks')



    def create_project(self):

        print("ddd")

        project = self.env['project.project'].create({
            'name': self.name,
            'partner_id': self.partner_id.id,
            'user_id' : self.project_manager.id,

        })


        tasks = self.task_ids
        print("nnn",tasks)

        for task in tasks:

            self.env['project.task'].create({
            'name': task.name,
            'user_ids': task.assigners,
            'partner_id': self.partner_id.id,
            'project_id': project.id,

            })


        return  {
            'type' : 'ir.actions.act_window',
            'name' : 'project',
            'res_model': 'project.project',
            'view_mode': 'form',
            'res_id': project.id,

        }








    # def action_open_tasks(self):
    #
    #     return {    #
    #     }
