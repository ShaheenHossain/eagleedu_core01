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
    email = fields.Char(string="student Email", help="Enter E-mail id for contact purpose")
    phone = fields.Char(string="student Phone", help="Enter Phone no. for contact purpose")
    mobile = fields.Char(string="Student Mobile", help="Enter Mobile num for contact purpose")
    nationality = fields.Many2one('res.country', string='Nationality', ondelete='restrict',default=19,
                                  help="Select the Nationality")


class EagleeduClassSection(models.Model):
    _name = 'eagleedu.class_section'
    name = fields.Char()


