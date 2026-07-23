# -*- coding: utf-8 -*-
from xlrd import sheet


from datetime import date, timedelta

from odoo.addons.test_convert.tests.test_env import record
from odoo.exceptions import ValidationError
import io
import json
import xlsxwriter
from odoo import models
from odoo.tools import json_default


class LeaveReport(models.TransientModel):
    _inherit = 'student.leave.wizard'

    def leave_report_excel(self):

        sql = """
        SELECT s.admission, s.first_name, c.name_class, l.start_date, l.end_date, l.total_date,
        l.reason FROM school_leaves as l JOIN school_students as s on l.student_id = s.id 
        JOIN school_class as c on l.class_id = c.id WHERE 1=1"""

        if self.class_id:
            sql += f" AND s.class_id = '{self.class_id.id}'"

            print("class", sql)

        if self.student_id:
            sql += f" AND l.student_id = '{self.student_id.id}'"

            print("student", sql)

        today = date.today()

        if self.filter_type == 'day':
            sql += f" AND '{today}' BETWEEN l.start_date AND l.end_date "

            print("day", sql)


        elif self.filter_type == 'week':
            week_start = today - timedelta(days=today.weekday())
            week_end = week_start + timedelta(days=6)

            sql += f" AND l.start_date >= '{week_start}' AND l.start_date <= '{week_end}'"

            print("week", sql)

        elif self.filter_type == 'month':
            month_start = today.replace(day=1)
            next_month = (month_start + timedelta(days=32)).replace(day=1)
            month_end = next_month - timedelta(days=1)

            sql += f" AND l.start_date >= '{month_start}' AND l.start_date < '{month_end}'"

        elif self.filter_type == 'custom':
            if self.start_date and self.end_date:
                sql += f"AND l.start_date <= '{self.end_date}' AND l.end_date >= '{self.start_date}'"
            elif self.start_date:

                sql += f" AND l.start_date >= '{self.start_date}'"

        elif self.end_date:

            sql += f" AND l.end_date <= '{self.end_date}'"

        self.env.cr.execute(sql)
        result = self.env.cr.fetchall()

        print("query", sql)
        print("r", result)
        print("result", len(result))

        if not result:
            raise ValidationError("No leaves found")

        data = {
            'print_date' : date.today(),
            'student' : self.student_id.first_name if self.student_id else 'All',
            'class' : self.class_id.name_class if self.class_id else 'All',
            'type': self.filter_type if self.filter_type else '',
            'd_from' : date.today() if self.filter_type =='day' else '',
            'd_to' : date.today() if self.filter_type == 'day' else '',
            'w_from': today - timedelta(days=today.weekday()),
            'w_to': today - timedelta(days=today.weekday()) + timedelta(days=6),
            'm_from': today.replace(day=1),
            'm_to': (today.replace(day=1) + (timedelta(days=32))).replace(day=1) - timedelta(days=1),
            'c_from': self.start_date,
            'c_to': self.end_date,
            'stud' : self.student_id,
            'classes' : self.class_id,
            'records' : result,

            }

        return {
            'type': 'ir.actions.report',
            'data': {'model': 'student.leave.wizard',
                     'options': json.dumps(data,default=json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Leave Report',
                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, data, response):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format(
            {'font_size': '12px', 'align': 'left', 'bold': True,})
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '20px'})
        txt = workbook.add_format({'font_size': '13px', 'align': 'center'})

        headings = workbook.add_format({'bold': True, 'font_size': '11px', 'align': 'center', 'font_color': 'white', 'bg_color': 'black'})
        sheet.merge_range('A2:F3', 'Leave Report', head)

        if  data['student']:
            sheet.write('A4', 'Student:', cell_format)
            sheet.write('B4', data['student'], txt)

        if  data['student'] and  data['class']:
            sheet.write('C4', 'Class', cell_format)
            sheet.write('D4', data['class'], txt)

        if data['type']:
            sheet.write('C8', 'Type', cell_format)
            sheet.write('D8', data['type'], txt)
        sheet.write('A8', 'Print Date', cell_format)
        sheet.write('B8', data['print_date'], txt)

        if data['type'] == 'day':

            sheet.write('A6', 'From', cell_format)
            sheet.write('B6', data['d_from'], txt)
            sheet.write('C6', 'To', cell_format)
            sheet.write('D6', data['d_to'], txt)

        if data['type'] == 'week':
            sheet.write('A6', 'From', cell_format)
            sheet.write('B6', data['w_from'], txt)
            sheet.write('C6', 'To', cell_format)
            sheet.write('D6', data['w_to'], txt)


        if data['type'] == 'month':
            sheet.write('A6', 'From', cell_format)
            sheet.write('B6', data['m_from'], txt)
            sheet.write('C6', 'To', cell_format)
            sheet.write('D6', data['m_to'], txt)

        if data['type'] == 'custom':
            sheet.write('A6', 'From', cell_format)
            sheet.write('B6', data['c_from'], txt)
            sheet.write('C6', 'To', cell_format)
            sheet.write('D6', data['c_to'], txt)





        sheet.set_column('A:A', 20)
        sheet.set_column('B:B', 20)
        sheet.set_column('C:C', 20)
        sheet.set_column('D:D', 20)
        sheet.set_column('E:E', 20)
        sheet.set_column('F:F', 20)
        sheet.set_column('G:G', 20)
        sheet.set_column('H:H', 20)

        row = 9
        col = 0


        sheet.write(row,col,'SL.no',headings)
        col+=1
        sheet.write(row,col,'Admission no',headings)
        col+=1
        if data['type'] and data['class']:

            sheet.write(row,col,'First Name',headings)
            col+=1

        if not data['class']:
            sheet.write(row,col,'Class',headings)
            col+=1
        sheet.write(row,col,'Start Date',headings)
        col+=1
        sheet.write(row,col,'End Date',headings)
        col+=1
        sheet.write(row,col,'Total Date',headings)
        col+=1
        sheet.write(row,col,'Reason',headings)

        col=0
        seriel = 1

        print("rec",data['records'])
        print("data",data)

        for rec in data['records']:
            row += 1
            sheet.write(row,col,seriel, txt)
            col+=1
            sheet.write(row,col, rec[0],txt)
            col+=1
            if data['type'] and data['class']:
                sheet.write(row,col, rec[1],txt)
                col+=1
            if data['type']:
                sheet.write(row,col, rec[2],txt)
                col+=1
            sheet.write(row,col, rec[3],txt)
            col+=1
            sheet.write(row,col, rec[4],txt)
            col+=1
            sheet.write(row,col, rec[5],txt)
            col+=1
            sheet.write(row,col, rec[6],txt)

            col = 0
            seriel += 1

        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
