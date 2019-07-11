# -*- coding: utf-8 -*-
from odoo import http

# class EagleeduCore(http.Controller):
#     @http.route('/eagleedu_core/eagleedu_core/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eagleedu_core/eagleedu_core/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('eagleedu_core.listing', {
#             'root': '/eagleedu_core/eagleedu_core',
#             'objects': http.request.env['eagleedu_core.eagleedu_core'].search([]),
#         })

#     @http.route('/eagleedu_core/eagleedu_core/objects/<model("eagleedu_core.eagleedu_core"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eagleedu_core.object', {
#             'object': obj
#         })