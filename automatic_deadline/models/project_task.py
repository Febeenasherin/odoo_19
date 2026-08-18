# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import fields, models, api


class ProjectTask(models.Model):
    _inherit = 'project.task'


    def write(self, vals):
        print("working")

        if 'stage_id' in vals:
            print(vals,"values")
            stage = self.env['project.task.type'].browse(vals['stage_id'])

            print(stage,"stage")

            date = stage.default_duration
            print(date,"date")



            if stage.default_duration:
                print("hhh")
                vals['date_deadline'] = fields.Date.today() + timedelta(days=date)

                print(self.date_deadline,"date")

        return super().write(vals)
