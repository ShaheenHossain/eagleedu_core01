# -*- coding: utf-8 -*-

from odoo import fields, models, api, _

class EagleeduInstructor(models.Model):
    _name = 'eagleedu.instructor'
    _inherit = ['mail.thread']
    _description = 'All Teachers Details'

    @api.model
    def create(self, vals):
        """Over riding the create method to assign
        the sequence for newly creating records"""
        vals['instructor_id'] = self.env['ir.sequence'].next_by_code('eagleedu.instructor')
        res = super(EagleeduInstructor, self).create(vals)
        return res

    # @api.model
    # def create(self, vals):
    # #     """Overriding the create method and assigning the the sequence for the record"""
    #     if vals.get('instructor_id', _('New')) == _('New'):
    #         vals['instructor_id'] = self.env['ir.sequence'].next_by_code('eagleedu.instructor') or _('New')
    #     res = super(EagleeduInstructor, self).create(vals)
    #     return res



    ins_name = fields.Char(string="Instructor Name", required=True)
    instructor_id = fields.Char(string="Instructor ID No.", readonly=True )
    ins_father_name = fields.Char(string="Instructor Father Name")
    ins_mother_name = fields.Char(string="Instructor Mother Name")
    ins_image = fields.Binary(string="Instructor Image")
    ins_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                                string='Gender', required=False, track_visibility='onchange',
                                help="Your Gender is ")
    ins_date_of_birth = fields.Date(string="Date Of birth", help="Enter your DOB")

