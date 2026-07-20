# -*- coding: utf-8 -*-
from odoo import  models
from datetime import date
from odoo.exceptions import UserError


class StudentInformationReport(models.AbstractModel):
    """ students leaves"""

    _name = 'report.school_management.student_information_template'

    def _get_report_values(self, docids, data=None):

        dep = self.env['student.information'].browse(docids)

        sql = """
        SELECT s.admission,s.first_name,c.name_class,s.email,d.name from school_students as s
        left join school_department as d on s.department_id = d.id join school_class as c on s.class_id = c.id  WHERE 1=1
        """

        if dep.department_id:
            sql += f" AND s.department_id = '{dep.department_id.id}'"

            print("dep,")

        if dep.class_id:
            sql += f"AND s.class_id= '{dep.class_id.id}'"




        self.env.cr.execute(sql)
        result = self.env.cr.fetchall()
        print(result)

        

        return {
            'docs': result,
            'print_date' : date.today(),
            'department' : dep.department_id.name if dep.department_id else "",
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
