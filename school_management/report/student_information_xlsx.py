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


class StudentInformation(models.TransientModel):
    _inherit = 'student.information'

    def student_report_excel(self):
        sql = """
                SELECT d.name,c.name_class,s.first_name,s.last_name,s.reg_no,s.email,s.phone_no from school_students as s
                left join school_department as d on s.department_id = d.id join school_class as c on s.class_id = c.id  WHERE 1=1
                """

        if self.department_id:
            sql += f" AND s.department_id = '{self.department_id.id}'"

            print("dep,")

        if self.class_id:
            sql += f"AND s.class_id= '{self.class_id.id}'"

        sql += f" ORDER BY c.name_class,s.first_name "

        self.env.cr.execute(sql)
        students = self.env.cr.fetchall()
        print(students)

        grouped_students = {}
        for student in students:
            class_name = student[1]
            if class_name in grouped_students:
                grouped_students[class_name].append(student)
            else:
                grouped_students[class_name] = [student]

            print("class", class_name)
            print("st", student)
            print("grp", grouped_students[class_name])
            print([student])
            print(grouped_students[class_name])
            print("dd", grouped_students)

        if not students:
            raise ValidationError("No leaves found")

        data = {
                # 'docs': students,
                'print_date': date.today(),
                'department': self.department_id.name if self.department_id else '',
                'grouped_students': grouped_students,
                'class' : self.class_id,
            }

        return {
            'type': 'ir.actions.report',
            'data': {'model': 'student.information',
                     'options': json.dumps(data, default=json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Students Report',
                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, data, response):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format(
            {'font_size': '12px', 'align': 'left', 'bold': True, })
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '20px'})
        txt = workbook.add_format({'font_size': '13px', 'align': 'left'})

        headings = workbook.add_format(
            {'bold': True, 'font_size': '11px', 'align': 'center', 'font_color': 'white', 'bg_color': 'black'})
        # sub_title = workbook.add_format({'bold': True, 'font_color': 'white', 'font_size': '15px'})

        sheet.merge_range('A2:D3', 'STUDENTS REPORT', head)
        sheet.write('A5', 'Print Date', cell_format)
        sheet.write('B5', data['print_date'], txt)

        if data['department']:
            sheet.write('C5', 'Department', cell_format)
            sheet.write('D5', data['department'], txt)


        sheet.set_column('A:A', 20)
        sheet.set_column('B:B', 20)
        sheet.set_column('C:C', 20)
        sheet.set_column('D:D', 20)
        sheet.set_column('E:E', 20)
        sheet.set_column('F:F', 20)
        sheet.set_column('G:G', 20)

        row = 6
        col = 0
        seriel = 1

        for rec, val in data['grouped_students'].items():
            print("hh", rec)
            print("ww", rec[0])
            print("val", val)
            sheet.write(row, 0, 'Class', cell_format)

            sheet.write(row, 1, rec, txt)

            row +=2

            sheet.write(row, col, 'Sl.no', headings)
            col +=1
            sheet.write(row, col, 'Registration no', headings)
            col+=1
            sheet.write(row, col, 'First Name', headings)
            col+=1
            sheet.write(row, col, 'Last name', headings)
            col+=1

            # sheet.write(row, col, 'Department', headings)
            # col+=1
            sheet.write(row, col, 'Email', headings)
            col+=1
            sheet.write(row, col, 'Phone no', headings)



            col =0
            for stud in val:
                row += 1
                sheet.write(row, col, seriel, txt)
                col+=1
                sheet.write(row, col, stud[4], txt)
                col+=1
                sheet.write(row, col, stud[2], txt)
                col+=1
                sheet.write(row, col, stud[3], txt)
                col+=1

                # sheet.write(row, col, stud[0], txt)
                # col+=1
                sheet.write(row, col, stud[5], txt)
                col+=1
                sheet.write(row, col, stud[6], txt)
                seriel +=1
                row+=1
                col = 0

                if data['class']:
                    sheet.write('C7', 'Department', cell_format)
                    sheet.write('D7', stud[0], txt)


            seriel = 1


            row +=3
            col=0

        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
