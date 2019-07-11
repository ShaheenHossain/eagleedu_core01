# -*- coding: utf-8 -*-
{
    'name': "Eagle Education Core 01",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Md. Shaheen Hossain",
    'website': "http://www.eagle-erp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/eedustudent_abedon.xml',
        'views/eedustudent_student.xml',
        'views/eagleedu_registration.xml',
        'views/eagleedu_student.xml',
        'views/eagleedu_instructor.xml',
        'views/eagleedu_division.xml',
        'views/eagleedu_standard_class.xml',
        'views/eagleedu_main_menu.xml',
        'views/templates.xml',
        'reports/print_reports.xml',
        'reports/report_edustudent.xml',
        #'data/bddivision.bddivision.csv',
        #'data/edustudent.district.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'base_demo.xml',
        'res/res_currency_demo.xml',
        'res/res_bank_demo.xml',
        'res/res_partner_demo.xml',
        'res/res_partner_demo.yml',
        # 'res/res_partner_image_demo.xml',

    ],
}