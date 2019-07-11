# -*- coding: utf-8 -*-

from odoo.exceptions import ValidationError
from odoo import fields, models, api, _

class EagleeduClassDivision(models.Model):
    _name = 'eagleedu.class_division'
    _description = "Class room"

    class_division_name = fields.Char(string='Class Division Name')
    instructor_id = fields.Many2one('eagleedu.instructor', string='Instructor Name', help="Class teacher/Faculty")
    instructor_name = fields.Many2one('eagleedu.instructor', 'ins_name', help="Class teacher/Faculty")
    academicyear = fields.Many2one('eagleedu.academicyear', string='Academic Year',
                                       help="Select the Academic Year", required=True)
    standard_class = fields.Many2one('eagleedu.standard_class', string='Class', required=True,
                               help="Select the Class")
    group_division = fields.Many2one('eagleedu.group_division', string='Division', help="Select the Division")
    class_section = fields.Many2one('eagleedu.class_section', string='Section', help="Select the Section")
    # student_id = fields.One2many('eagleedu.student', 'standard_class', string='Students')

    @api.model
    def create(self, vals):
        """Return the name as a str of class + division"""
        # res = super(EducationClassDivision, self).create(vals)
        standard_class = self.env['eagleedu.standard_class'].browse(vals['standard_class'])
        group_division = self.env['eagleedu.group_division'].browse(vals['group_division'])
        class_section = self.env['eagleedu.class_section'].browse(vals['class_section'])
        batch = self.env['eagleedu.academicyear'].browse(vals['academic_year_id'])
        className=''
        divisionName=''
        sectionName=''
        batchName=batch.academic_year
        if standard_class.id>0:
            className=standard_class.name
        if group_division.id>0:
            divisionName=group_division.name
        if class_section.id>0:
            sectionName=class_section.name
        name = str(className + '-' + divisionName+ '-' + sectionName+ '-' + batchName)
        vals['name'] = name
        return super(EagleeduClassDivision, self).create(vals)