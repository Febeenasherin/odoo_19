
from odoo import fields,models


class SchoolStudents(models.Model):
    _name = 'school.students'
    _description = 'School Students details'

    sequence = fields.Char(string='Reference', required=True, copy=False, readonly=True,default=lambda self: 'New')
    First_name = fields.Char(string="First Name",required=True)
    Last_name = fields.Char(string="Last Name",required=True)
    Father_name = fields.Char(string="Father Name",required=True)
    Mother_name = fields.Char(string="Mother Name",required=True)

    personal_information=fields.Text(string="Personal InformationS",required=True)
    Communication_address=fields.Text(string="Communication Address",required=True)
    street=fields.Char(string="Street")
    city=fields.Char(string="City")
    country_id=fields.Many2one('res.country',string="Country")
    same_as_communication=fields.Boolean(string="Same As Communication")

    Email=fields.Char(string="Email",required=True)
    phone_no=fields.Char(string="Phone Number",required=True)
    DOB=fields.Date(string="DOB",required=True)
    Gender=fields.Selection([('m','Male'),('f','Female')],string="Gender",required=True)
    Registration_date=fields.Date(string="Registration Date",required=True)
    image= fields.Image(string= "image",required=True)
    school_dep = fields.Many2one('school.department', string='Head of Department')
    TC=fields.Image(string='TC')
    aadhaar_no=fields.Char(string="Aadhaar no")
    status=fields.Selection([("draft","Draft"),("registration","Registration")], default='draft', string="Status"   )


    def  create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['sequence']=self.env['ir.sequence'].next_by_code('sequence') or 'New'
        return super(SchoolStudents, self).create(vals)







