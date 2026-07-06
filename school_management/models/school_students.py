# -*- coding: utf-8 -*-
from odoo import fields, models, api
from datetime import date


class SchoolStudents(models.Model):
    """school student registration"""
    _name = 'school.students'
    _description = 'School Students details'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'first_name'

    _unique_name = models.Constraint('UNIQUE(aadhaar_no)', 'aadhaar number must be unique!')

    sequence = fields.Char(string='Registration No', copy=False, readonly=True, default='New')
    first_name = fields.Char(string="First Name", required=True ,help='enter first name')
    last_name = fields.Char(string="Last Name", required=True,  help='enter last name')
    father_name = fields.Char(string="Father Name", help='enter father name')
    mother_name = fields.Char(string="Mother Name", help='enter mother name')

    street = fields.Char(string="Street")
    city = fields.Char(string="City")
    country_id = fields.Many2one('res.country', string="Country")
    same_as_communication = fields.Boolean(string="Same As Communication")
    email = fields.Char(string="Email", help='enter email', required=True)
    phone_no = fields.Char(string="Phone Number", required=True, help='enter phone number')
    dob = fields.Date(string="DOB", help='select DOB')
    student_age = fields.Integer(string="Age" , compute='_compute_student_age', store=True)

    gender = fields.Selection([('m','male'),('f','female')], string="Gender")
    registration_date = fields.Date(string="Registration Date", required=True, default=fields.Date.today , help='enter registration date')
    image = fields.Image(string= "image", help='upload image')
    school_id = fields.Many2one('school.department', string='Head of Department', help='select department')
    document = fields.Binary(string="Document")
    aadhaar_no = fields.Char(string="Aadhaar no", help='enter Aadhaar no')
    company_id = fields.Many2one('res.company', string='School', tracking=True, default= lambda self: self.env.company)
    admission = fields.Char(string='Admission no', readonly=True)
    status = fields.Selection([("draft","Draft"),("registration","Registration")], default='draft', string="Status")
    previous_department_id = fields.Many2one('school.department',string='Previous Department')
    previous_class_id = fields.Many2one('school.class' , string='Previous Class')
    club_ids = fields.Many2many('school.clubs', string='Club')
    class_id = fields.Many2one('school.class', string='Class')
    exam_ids = fields.Many2many('school.exam')
    attendance = fields.Selection([('present', 'Present'), ('absent', 'Absent')], default='present', string="Attendance")
    user_id = fields.Many2one('res.users', string='User')

    # sequence
    @api.model_create_multi
    def create(self, vals_list):
        """add sequence number"""
        print("self",self)
        for vals in vals_list:
            if vals.get('sequence' , 'New') == 'New':
                vals["sequence"] = self.env['ir.sequence'].next_by_code('sequencecode')  or 'New'

        return super(SchoolStudents, self).create(vals_list)

    # button registration
    def action_registration(self):
        """change status inro registration"""
        print("self",self)
        self.status = 'registration'

        self.admission = self.env['ir.sequence'].next_by_code('admissioncode')


     #  age calculation
    @api.depends('dob')
    def _compute_student_age(self):
        """ calculate age of student based on date of birth"""
        print("nn",self)
        for record in self:
            if record.dob:
                today = date.today()
                birth = record.dob
                record.student_age = today.year - birth.year
            else:
                record.student_age = 0


    def _create_user(self):
        print("working...")
        for student in self:
            if not student.user_id:
                if student.status == 'registration':
                    user= self.env['res.users'].create({
                        "name":student.first_name,
                        "email":student.email,
                        "login":student.email,
                        "password":"demo123",
                        "company_id":student.company_id.id,

                    })
                    student.user_id = user.id
                    print("created", user)


