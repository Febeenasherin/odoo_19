# -*- coding: utf-8 -*-
from odoo import fields, models
from datetime import datetime, timedelta
import calendar


class ProjectProject(models.Model):
    _inherit = 'project.project'


    date_ids = fields.One2many('project.date.line','project_id',string='Date')


    def action_schedule_date(self):
        print("work")
        current_month = datetime.today().month

        val = []
        for month in range(current_month,13):

            start_date = datetime.today() if month == current_month else datetime(datetime.today().year,month,1).date()
            end_date = calendar.monthrange(datetime.today().year, month)
            last_day_date = datetime(datetime.today().year, month, end_date[1])

            values = {
                'month': start_date.strftime('%B'),
                'year': datetime.today().year,
                'from_date': start_date,
                'to_date': last_day_date,
            }

            val.append(fields.Command.create(values))


        self.date_ids = val
        print(self.date_ids)















            # val.append((0, 0, values))

            # self.production_line_ids = values

        # records = self.env['project.date.line'].create([
        #     {'date_ids': [fields.Command.create({val})]},])

        # self.date_ids = [fields.Command.create[(0, 0 {val})]]

        # rec = self.env['project.date.line'].create(val)
        # print(rec)

        # return rec




            # self.date_ids=[fields.Command.create({
            #     'month': start_date.strftime('%B'),
            #     'year': year,
            #     'from_date': start_date,
            #     'to_date': last_day_date,
            # }),]





            # print(self.date_ids)









