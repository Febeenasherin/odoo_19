# -*- coding: utf-8 -*-
from odoo import fields, models



class ProjectProject(models.Model):
    """inherit product template"""
    _name = 'project.template'



    name = fields.Char(string="Project Name")
    partner_id = fields.Many2one('res.partner')



    def create_project(self):

        print("ddd")

        self.env['project.project'].create({
            'name': self.name,
            'partner_id': self.partner_id.id,

        })



    # def action_open_tasks(self):
    #
    #     return {    #
    #     }
