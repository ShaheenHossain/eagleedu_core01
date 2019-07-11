from odoo import fields, models, api, _

class EagleeduRegistration(models.Model):
    _name = 'eagleedu.registration'
    _description = 'This the Registration for student'
    _order = 'id desc'
    _inherit = ['mail.thread']


    name = fields.Char(sting = 'Student Name', required=True)
    st_name_b = fields.Char(string='Student Bangla Name')
    date_of_birth = fields.Date(string="Date Of birth")
    st_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                                string='Gender', required=False, track_visibility='onchange')
    st_blood_group = fields.Selection([('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('o+', 'O+'), ('o-', 'O-'),
                                    ('ab-', 'AB-'), ('ab+', 'AB+')], string='Blood Group', track_visibility='onchange')
    st_passport_no = fields.Char(string="Passport No.", help="Proud to say my father is", required=False)
    registration_no = fields.Char(string='Registration No', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    registration_date = fields.Datetime('Registration Date', default=lambda
        self: fields.datetime.now())  # , default=fields.Datetime.now, required=True

    st_image = fields.Binary(string='Image', help="Provide the image of the Student")
    st_father_name = fields.Char(string="Father's Name", help="Proud to say my father is", required=False)
    st_father_name_b = fields.Char(string="বাবার নাম", help="Proud to say my father is")
    st_father_occupation = fields.Char(string="Father's Occupation", help="father Occupation")
    st_father_email = fields.Char(string="Father's Email", help="father Occupation")
    father_mobile = fields.Char(string="Father's Mobile No", help="Father's Mobile No")
    st_mother_name = fields.Char(string="Mother's Name", help="Proud to say my mother is", required=False)
    st_mother_name_b = fields.Char(string="মা এর নাম", help="Proud to say my mother is")
    st_mother_occupation = fields.Char(string="Mother Occupation", help="Proud to say my mother is")
    st_mother_email = fields.Char(string="Mother Email", help="Proud to say my mother is")
    mother_mobile = fields.Char(string="Mother's Mobile No", help="mother's Mobile No")


    house_no = fields.Char(string='House No.', help="Enter the House No.")
    road_no = fields.Char(string='Area/Road No.', help="Enter the Area or Road No.")
    post_office = fields.Char(string='Post Office', help="Enter the Post Office Name")
    city = fields.Char(string='City', help="Enter the City name")
    bd_division_id = fields.Many2one('eagleedu.bddivision', string= 'Division')
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict',default=19)

    if_same_address = fields.Boolean(string="Permanent Address same as above", default=True)
    per_village = fields.Char(string='Village Name', help="Enter the Village Name")
    per_po = fields.Char(string='Post Office Name', help="Enter the Post office Name ")
    per_ps = fields.Char(string='Police Station', help="Enter the Police Station Name")
    per_dist_id = fields.Many2one('eagleedu.bddistrict', string='District', help="Enter the City of District name")
    per_country_id = fields.Many2one('res.country', string='Country', ondelete='restrict', default=19)

    guardian_name = fields.Char(string="Guardian's Name", help="Proud to say my guardian is")
    guardian_relation = fields.Many2one('eagleedu.guardian.relation', string="Guardian's Relation", help="Proud to say my guardian is")
    guardian_mobile = fields.Char(string="Guardian's Mobile")
    guardian_name = fields.Char(string="Guardian's Name")

    religious_id = fields.Many2one('eagleedu.religious', string="Religious", help="My Religion is ")
    student_id=fields.Char('Student Id')
    academic_year = fields.Many2one('eagleedu.academicyear', string='Academic Year')
    standard_class = fields.Many2one('eagleedu.standard_class')
    group_division = fields.Many2one('eagleedu.group_division')
    roll_no = fields.Integer('Roll No', help="for import only")
    section=fields.Char('Section', help="for import only")

    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id)
    email = fields.Char(string="Student Email", help="Enter E-mail id for contact purpose")
    phone = fields.Char(string="Student Phone", help="Enter Phone no. for contact purpose")
    mobile = fields.Char(string="Student Mobile", help="Enter Mobile num for contact purpose")
    nationality = fields.Many2one('res.country', string='Nationality', ondelete='restrict',default=19,
                                  help="Select the Nationality")


    state = fields.Selection([('draft', 'Draft'), ('verification', 'Verify'), ('approve', 'Approve'), ('reject', 'Reject'), ('done', 'Done')],
                             string='State', required=True, default='draft', track_visibility='onchange')

    # _sql_constraints = [
    #     ('unique_student_id', 'unique(student_id)', 'Student Id must be unique'),
    # ]



    @api.model
    def create(self, vals):
        """Overriding the create method and assigning the the sequence for the record"""
        if vals.get('registration_no', _('New')) == _('New'):
            vals['registration_no'] = self.env['ir.sequence'].next_by_code('eagleedu.registration') or _('New')
        res = super(EagleeduRegistration, self).create(vals)
        return res

    @api.multi
    def send_to_verify(self):
        """Button action for sending the application for the verification"""
        for rec in self:
            rec.write({
                'state': 'verification'
            })

    @api.multi
    def application_verify(self):
        """Button action for sending the application for the verification"""
        for rec in self:
            rec.write({
                'state': 'approve'
            })


    @api.multi
    def create_student(self):
        """Create student from the application and data and return the student"""
        for rec in self:
            values = {
                'name': rec.name,
                'registration_no': rec.registration_no,
                'standard_class': rec.standard_class.id,
                'academic_year': rec.academic_year.id,
                'group_division': rec.group_division.id,
                'st_image': rec.st_image,
                'company_id': rec.company_id.id,
                'email':rec.email,
                'phone':rec.phone,
                'mobile':rec.mobile,
                'nationality': rec.nationality.id,



            }
            student = self.env['eagleedu.student'].create(values)
            rec.write({
                'state': 'done'
            })
            return {
                'name': _('Student'),
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'eagleedu.student',
                'type': 'ir.actions.act_window',
                'res_id': student.id,
                'context': self.env.context
            }


class EagleeduBddivision(models.Model):
    _name = 'eagleedu.bddivision'
    name = fields.Char()

class EagleeduBddistrict(models.Model):
    _name = 'eagleedu.bddistrict'
    name = fields.Char()

class EagleeduReligious(models.Model):
    _name = 'eagleedu.religious'
    name = fields.Char()

class EagleeduAcademicyear(models.Model):
    _name = 'eagleedu.academicyear'
    name = fields.Char()

class EagleeduGuardianRelation(models.Model):
    _name = 'eagleedu.guardian.relation'
    name = fields.Char()

class EagleeduStandardClass(models.Model):
    _name = 'eagleedu.standard_class'
    name = fields.Char()

class EagleeduGroupDivission(models.Model):
    _name = 'eagleedu.group_division'
    name = fields.Char()
