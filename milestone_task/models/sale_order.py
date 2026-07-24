# -*- coding: utf-8 -*-
from odoo import fields, models


class SalesOrder(models.Model):
    _inherit = "sale.order"


    def project_create(self):
        if not self.project_id:
            self.project_id = self.env['project.project'].create({'name': self.name})
        for line in self.order_line:
            task_ids = self.project_id.task_ids
            main_task = task_ids.filtered(lambda task: task.name == f"Milestone {line.milestone}")
            if not main_task:
                main_task = task_ids.create({'name': f"Milestone {line.milestone}", 'project_id': self.project_id.id})
            child_task_ids = main_task.child_ids
            child_task = child_task_ids.filtered(
                lambda task: task.name == f"Milestone {line.milestone} - {line.product_template_id.display_name}")
            if not child_task:
                child_task_ids.create({'name': f'Milestone {line.milestone} - {line.product_template_id.display_name}',
                                       'project_id': self.project_id.id, 'parent_id': main_task.id, })