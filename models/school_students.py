from datetime import date

from odoo import fields,models,api


class SchoolStudents(models.Model):
    _name = 'school.students'
    _description = 'School Students details'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'first_name'
    _unique_name = models.Constraint('UNIQUE(aadhaar_no)', 'aadhaar number must be unique!')

    sequence = fields.Char(string='Reference', required=True, copy=False, readonly=True, default=lambda self: 'New')
    first_name = fields.Char(string="First Name",required=True ,help='enter first name')
    last_name = fields.Char(string="Last Name",required=True,  help='enter last name')
    father_name = fields.Char(string="Father Name",help='enter father name')
    mother_name = fields.Char(string="Mother Name",required=True, help='enter mother name')
    personal_information=fields.Text(string="Personal InformationS",required=True,help='enter personal information')
    communication_address=fields.Text(string="Communication Address",required=True,help='enter communication address')
    street=fields.Char(string="Street")
    city=fields.Char(string="City")
    country_id=fields.Many2one('res.country',string="Country")
    same_as_communication=fields.Boolean(string="Same As Communication")
    email=fields.Char(string="Email",help='enter email')
    phone_no=fields.Char(string="Phone Number",required=True, help='enter phone number')
    dob=fields.Date(string="DOB",help='select DOB')
    student_age=fields.Integer(string="Age" ,compute='_compute_student_age', store=True)
    gender=fields.Selection([('m','male'),('f','female')],string="Gender")
    registration_date=fields.Date(string="Registration Date",required=True, help='enter registration date')
    image= fields.Image(string= "image",help='upload image')
    school_id=fields.Many2one('school.department', string='Head of Department', help='select department')
    tc=fields.Image(string='TC')
    aadhaar_no=fields.Char(string="Aadhaar no",help='enter Aadhaar no')
    company_id = fields.Many2one('res.company', string='multi_school', tracking=True)
    admission = fields.Char(string='Admission no')
    status=fields.Selection([("draft","Draft"),("registration","Registration")], default='draft', string="Status"   )

    # sequence
    def  create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['sequence']=self.env['ir.sequence'].next_by_code('sequence') or 'New'
        return super(SchoolStudents, self).create(vals)


    # button
    def registration(self):
        self.status='registration'

    #  age calculation

    @api.depends('dob')
    def _compute_student_age(self):
        for record in self:
            if record.dob:
                today = date.today()
                birth = record.dob
                record.student_age = today.year - birth.year
            else:
                record.student_age = 0




