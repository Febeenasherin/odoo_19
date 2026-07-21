# -*- coding: utf-8 -*-
from odoo import  models
from datetime import date
from odoo.exceptions import ValidationError


class StudentInformationReport(models.AbstractModel):
    """ student information """

    _name = 'report.school_management.student_information_template'

    def _get_report_values(self, docids, data=None):
        """ get student department information and class wise information when clicking print-trigger """

        dep = self.env['student.information'].browse(docids)

        sql = """
        SELECT d.name,c.name_class,s.first_name,s.last_name,s.reg_no,s.email,s.phone_no from school_students as s
        left join school_department as d on s.department_id = d.id join school_class as c on s.class_id = c.id  WHERE 1=1
        """

        if dep.department_id:
            sql += f" AND s.department_id = '{dep.department_id.id}'"

            print("dep,")

        if dep.class_id:
            sql += f"AND s.class_id= '{dep.class_id.id}'"

        sql += f" ORDER BY c.name_class,s.first_name"


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

            print("class",class_name)
            print("st",student)
            print("grp",grouped_students[class_name])
            print([student])
            print(grouped_students[class_name])
            print("dd",grouped_students)

            if not grouped_students:
                raise ValidationError("No leaves found")


        return {
            'docs': students,
            'print_date' : date.today(),
            'department' : dep.department_id.name if dep.department_id else "",
            'grouped_students' : grouped_students,
        }






        # student_ids = data.get('ids',[])
        #
        # docs = self.env['school.students'].browse(student_ids)
        #
        # if not docs:
        #     raise UserError("No leaves found")
        #
        # return {
        #     'docs': docs,
        # }
