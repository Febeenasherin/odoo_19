# -*- coding: utf-8 -*-
from odoo import fields, models


class SalesOrder(models.Model):
    """ create project"""
    _inherit = "sale.order"


    def action_project_create(self):
        """for creating project.and main task and parent task.create project with sale order name, main task with
        milestone,and subtask created using product"""
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
                                       'project_id': self.project_id.id, 'parent_id': main_task.id,
                                       'line_id': line.id
                                       })


            print("line",line.id)



    def action_update_project(self):
        """for updating created task.update created subtask."""

        task_ids= self.project_id.task_ids
        print("task",task_ids)


        for line in self.order_line:



            child_task = task_ids.child_ids.filtered(lambda task: task.line_id == line)
            print("child",child_task)

            main_task = task_ids.filtered(lambda t:not t.parent_id and t.name == f"Milestone {line.milestone}")
            # print("parent",task_ids.parent_id)
            print("pare",main_task)
            if not main_task:
                main_task = task_ids.create({'name': f"Milestone {line.milestone}", 'project_id': self.project_id.id})

            if child_task:
                old_parent = child_task.parent_id
                child_task.write({
                    'name': f"Milestone {line.milestone} - {line.product_template_id.display_name}",
                    'parent_id': main_task.id,
                        })

                if old_parent and not old_parent.child_ids:
                    old_parent.unlink()

            else:
                main_task.child_task.create({
                'name': f'Milestone {line.milestone} - {line.product_template_id.display_name}',
                'project_id': self.project_id.id, 'parent_id': main_task.id,
                'line_id': line.id
                })

        return True
