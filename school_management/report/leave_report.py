# -*- coding: utf-8 -*-


from odoo import  models, fields
from datetime import date, timedelta
from odoo.exceptions import UserError


class LeaveReport(models.AbstractModel):
    """ students leaves"""

    _name = 'report.school_management.leave_information_template'

    def _get_report_values(self, docids, data=None):


        leave = self.env ['student.leave.wizard'].browse(docids)


        sql = """
        SELECT s.admission, s.first_name, c.name_class, l.start_date, l.end_date, l.total_date,
        l.reason FROM school_leaves as l JOIN school_students as s on l.student_id = s.id 
        JOIN school_class as c on l.class_id = c.id WHERE 1=1"""

        if leave.class_id:
            sql += f" AND l.class_id = '{leave.class_id.id}'"

            print("class",sql)

        if leave.student_id:
            sql+= f" AND l.student_id = '{leave.student_id.id}'"

            print("student",sql)

        today = date.today()

        if leave.filter_type == 'day':
            sql +=  f" AND '{today}' BETWEEN l.start_date AND l.end_date "

            print("day",sql)

        elif leave.filter_type == 'week':
            week_start = today - timedelta(days=today.weekday())
            week_end = week_start + timedelta(days=6)

            sql += f" AND l.start_date >= '{week_start}' AND l.start_date <= '{week_end}'"

            print("week",sql)

        elif leave.filter_type == 'month':
            month_start = today.replace(day=1)
            next_month = month_start + timedelta(days=32)
            month_end = next_month - timedelta(days=1)

            sql +=  f" AND l.start_date >= '{month_start}' AND l.start_date < '{month_end}'"

        elif leave.filter_type == 'custom':
            if leave.start_date:

                sql += f" AND l.start_date >= '{leave.start_date}'"

            if  leave.end_date:

                sql += f" AND l.end_date <= '{leave.end_date}'"


            # if leave.start_date and leave.end_date:
            #
            #     sql += f"AND l.start_date BETWEEN '{leave.start_date}' AND '{leave.end_date}'"

        self.env.cr.execute(sql)
        result = self.env.cr.fetchall()


        print("query",sql)
        print("r",result)
        print("result",len(result))

        if not result:
            raise UserError("No leaves found")

        # data = {'report': result}
        return {
            # 'doc_ids': leave,
            # 'doc_model': 'school.leave.wizard',
            'print_date': date.today(),
            'type' : leave.filter_type,
            'docs' : result,
            # 'class_name' : leave.class_id.name_class if leave.class_id else '',
            # 'student_name' : leave.student_id.first_name if leave.student_id else '',
            }











    #     leave_ids = data.get('ids',[])
    #
    #     docs = self.env['school.leaves'].browse(leave_ids)
    #
    #     if not docs:
    #         raise UserError("No leaves found")
    #
    #     return {
    #         'docs': docs,
    #     }

     #
     # def action_print(self):
     #
     #      query = """ select s."""



