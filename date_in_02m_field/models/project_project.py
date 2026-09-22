# -*- coding: utf-8 -*-
from odoo import fields, models
from datetime import datetime
import calendar


class ProjectProject(models.Model):
    _inherit = 'project.project'


    date_ids = fields.One2many('project.date.line','project_id',string='Date')


    def action_schedule_date(self):
        print("work")


        year = datetime.now().year
        print(year)
        current_calender = calendar.calendar(year)
        print(current_calender)

        # for dates in current_calender:
        #     print(dates)
        date = datetime.now()

        months = list(calendar.month_name)[1:]
        print(months)

        # month = date.strftime('%B')
        # print(month,"months")

        today = date.today().month
        print(today)

        # for line in months:
        val = []
        count = 0

        for month in range(today,13):

            if month == today:
                start_date = date.today()

            else:

                start_date = datetime(year,month,1).date()

            end_date = calendar.monthrange(year, month)
            print(start_date,"start_date")

            last_day_date = datetime(year, month, end_date[1])
            print(last_day_date,"last_day_date")

            # self.env['project.date.line'].create({
            #     'project_id': self.id,
            #     'month': start_date.strftime('%B'),
            #     'year': year,
            #     'from_date': start_date,
            #     'to_date': last_day_date
            #
            # })

            values = {
                'project_id': self.id,
                'month': start_date.strftime('%B'),
                'year': year,
                'from_date': start_date,
                'to_date': last_day_date,
            }

            val.append(values)
            #
            print("vals",val)

            self.date_ids = []

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









