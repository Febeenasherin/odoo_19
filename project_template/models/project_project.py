# -*- coding: utf-8 -*-
from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = 'project.project'


    def create_project_template(self):
        for rec in self:

            self.env['project.template'].create({
                'name' : rec.name,
                'partner_id' : rec.partner_id.id,
            })

