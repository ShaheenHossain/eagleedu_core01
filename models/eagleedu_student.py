from odoo import fields, models, api, _

class EagleeduStudent(models.Model):
    _name = 'eagleedu.student'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'This the application for student'
    _order = 'id desc'
    _rec_name = 'name'

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if name:
            recs = self.search([('name', operator, name)] + (args or []), limit=limit)
            if not recs:
                recs = self.search([('adm_no', operator, name)] + (args or []), limit=limit)
            if not recs:
                recs = self.search([('application_no', operator, name)] + (args or []), limit=limit)
            return recs.name_get()
        return super(EagleeduStudent, self).name_search(name, args=args, operator=operator, limit=limit)

    @api.model
    def create(self, vals):
        """Over riding the create method to assign sequence for the newly creating the record"""
        vals['adm_no'] = self.env['ir.sequence'].next_by_code('eagleedu.student')
        res = super(EagleeduStudent, self).create(vals)
        return res


    partner_id = fields.Many2one(
        'res.partner', string='Partner', required=True, ondelete="cascade")
    adm_no = fields.Char(string="Admission Number", readonly=True)
    st_image = fields.Binary(string='Image', help="Provide the image of the Student")
    application_no = fields.Char(string='Application  No', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id)
    standard_class = fields.Many2one('eagleedu.standard_class', string="Class Name", help="Enter Class Name")
    class_section = fields.Many2one('eagleedu.class_section', string="Section", help="Enter Class Section Name")
    group_division = fields.Many2one('eagleedu.group_division', string="Group Name", help="Enter Class Section Name")
    academic_year = fields.Many2one('eagleedu.academicyear', string= "Academic Year", help="Select Academic Year")
    roll_no = fields.Integer(string="Roll No.", help="Enter Roll No.")

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

    religious_id = fields.Many2one('eagleedu.religious', string="Religious", help="My Religion is ")
    student_id=fields.Char('Student Id')
    section=fields.Char('Section', help="for import only")
    email = fields.Char(string="Student Email", help="Enter E-mail id for contact purpose")
    phone = fields.Char(string="Student Phone", help="Enter Phone no. for contact purpose")
    mobile = fields.Char(string="Student Mobile", help="Enter Mobile num for contact purpose")
    nationality = fields.Many2one('res.country', string='Nationality', ondelete='restrict',default=19,
                                  help="Select the Nationality")


class EagleeduClassSection(models.Model):
    _name = 'eagleedu.class_section'
    name = fields.Char()


