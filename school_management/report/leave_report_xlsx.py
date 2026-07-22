# -*- coding: utf-8 -*-
from xlrd import sheet

from odoo import models
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
        sheet.merge_range('A4:A5', 'Student:', cell_format)
        sheet.merge_range('B4:B5', data['student'], txt)
        sheet.merge_range('C4:C5', 'Class', cell_format)
        sheet.merge_range('D4:D5', data['class'], txt)
        sheet.merge_range('E4:E5', 'Type', cell_format)
        sheet.merge_range('F4:F5', data['type'], txt)

        if data['type'] == 'day':

            sheet.merge_range('A6:A7', 'From', cell_format)
            sheet.merge_range('B6:B7', data['d_from'], txt)
            sheet.merge_range('C6:C7', 'To', cell_format)
            sheet.merge_range('D6:D7', data['d_to'], txt)

        if data['type'] == 'week':
            sheet.merge_range('A6:A7', 'From', cell_format)
            sheet.merge_range('B6:B7', data['w_from'], txt)
            sheet.merge_range('C6:C7', 'To', cell_format)
            sheet.merge_range('D6:D7', data['w_to'], txt)


        if data['type'] == 'month':
            sheet.merge_range('A6:A7', 'From', cell_format)
            sheet.merge_range('B6:B7', data['m_from'], txt)
            sheet.merge_range('C6:C7', 'To', cell_format)
            sheet.merge_range('D6:D7', data['m_to'], txt)

        if data['type'] == 'custom':
            sheet.merge_range('A6:A7', 'From', cell_format)
            sheet.merge_range('B6:B7', data['c_from'], txt)
            sheet.merge_range('C6:C7', 'To', cell_format)
            sheet.merge_range('D6:D7', data['c_to'], txt)





        sheet.set_column('A:A', 20)
        sheet.set_column('B:B', 20)
        sheet.set_column('C:C', 20)
        sheet.set_column('D:D', 20)
        sheet.set_column('E:E', 20)
        sheet.set_column('F:F', 20)
        sheet.set_column('G:G', 20)

        row = 9
        col = 0



        sheet.write(row,col,'Admission no',headings)

        sheet.write(row,col+1,'First Name',headings)

        sheet.write(row,col+2,'Class',headings)
        sheet.write(row,col+3,'Start Date',headings)
        sheet.write(row,col+4,'End Date',headings)
        sheet.write(row,col+5,'Total Date',headings)
        sheet.write(row,col+6,'Reason',headings)

        print("rec",data['records'])
        print("data",data)

        for rec in data['records']:
            row += 1

            sheet.write(row,col, rec[0],txt)
            sheet.write(row,col+1, rec[1],txt)
            sheet.write(row,col+2, rec[2],txt)
            sheet.write(row,col+3, rec[3],txt)
            sheet.write(row,col+4, rec[4],txt)
            sheet.write(row,col+5, rec[5],txt)
            sheet.write(row,col+6, rec[6],txt)

        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
