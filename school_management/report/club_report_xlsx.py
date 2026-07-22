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


class ClubReportXLSX(models.TransientModel):
    _inherit = "school.club.data"

    def club_report_excel(self):
        sql = """
                      SELECT s.first_name,s.admission,c.name_class,sc.name from school_students as s JOIN school_class as c on s.class_id = c.id 
                      JOIN school_clubs_school_students_rel as r on s.id = r.school_students_id JOIN school_clubs as sc on sc.id = r.school_clubs_id WHERE 1=1 """

        event_sql = """
                      SELECT e.name,e.venue,e.start_date,e.end_date,sc.name from school_events as e join school_clubs as sc on e.club_id = sc.id WHERE 1=1 """

        # Find students in the club
        if self.club_id:
            sql += f" AND sc.id = '{self.club_id.id}'"
            event_sql += f" AND e.club_id = '{self.club_id.id}'"

        if self.student_id:
            sql += f"AND s.id = '{self.student_id.id}'"


        self.env.cr.execute(sql)
        clubs = self.env.cr.fetchall()
        print("students", clubs)

        self.env.cr.execute(event_sql)
        event = self.env.cr.fetchall()

        if not clubs:
            raise ValidationError("not found")

        data = {
            'print_date' : date.today(),
            # 'club_name': self.club_id.name if self.club_id else '',
            'student_name':
                self.student_id.first_name if self.student_id else '',
            'event': event,
            'clubs': clubs,
        }

        return {
            'type': 'ir.actions.report',
            'data': {'model': 'school.club.data',
                     'options': json.dumps(data, default=json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Club Report',
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
        sub_title = workbook.add_format({'bold': True, 'font_color': 'white', 'font_size': '15px'})


        sheet.merge_range('A2:D3', 'CLUB REPORT', head)
        sheet.merge_range('A4:A5', 'Print Date', cell_format)
        sheet.merge_range('B4:B5', data['print_date'], txt)
        # sheet.merge_range('G4:G5', 'Club', cell_format)
        # sheet.merge_range('H4:H5', data['club_name'], txt)
        sheet.merge_range('A6:A7', 'Student Name', cell_format)
        sheet.merge_range('B6:B7', data['student_name'], txt)
        # sheet.merge_range('C6:C7', 'From', cell_format)
        # sheet.merge_range('D6:D7', data['d_from'], txt)
        # sheet.merge_range('E6:E7', 'To', cell_format)
        # sheet.merge_range('F6:F7', data['d_to'], txt)

        sheet.set_column('A:A', 20)
        sheet.set_column('B:B', 20)
        sheet.set_column('C:C', 20)
        sheet.set_column('D:D', 20)


        row = 9
        col = 0

        sheet.write(row,col,'Admission no',headings)
        sheet.write(row,col+1,'First Name',headings)
        sheet.write(row,col+2,'Class',headings)
        sheet.write(row,col+3,'Club',headings)

        #
        # print("rec",data['records'])
        # print("data",data)
        #
        for rec in data['clubs']:
            row+=1
            print("gg",rec)
            sheet.write(row,col, rec[1],txt)
            sheet.write(row,col+1, rec[0],txt)
            sheet.write(row,col+2, rec[2],txt)
            sheet.write(row,col+3, rec[3],txt)






        row +=2

        sheet.merge_range('C20:D20', 'Events', sub_title)

        sheet.set_column('C:C', 20)
        sheet.set_column('D:D', 20)
        sheet.set_column('E:E', 20)
        sheet.set_column('F:F', 20)
        sheet.set_column('G:G', 20)

        row += 8
        col = 0

        sheet.write(row, col, 'Club name', headings)
        sheet.write(row, col + 1, 'Event name', headings)
        sheet.write(row, col + 2, 'Venue', headings)
        sheet.write(row, col + 3, 'Start date', headings)
        sheet.write(row, col + 4, 'End date', headings)

        for rec in data['event']:
            row+=1
            print("gg",rec)
            sheet.write(row,col, rec[4],txt)
            sheet.write(row,col+1, rec[0],txt)
            sheet.write(row,col+2, rec[1],txt)
            sheet.write(row,col+3, rec[2],txt)
            sheet.write(row,col+4, rec[3],txt)




        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()