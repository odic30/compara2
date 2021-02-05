# -*- coding: utf-8 -*-
from odoo import http

# class Compara2(http.Controller):
#     @http.route('/compara2/compara2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/compara2/compara2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('compara2.listing', {
#             'root': '/compara2/compara2',
#             'objects': http.request.env['compara2.compara2'].search([]),
#         })

#     @http.route('/compara2/compara2/objects/<model("compara2.compara2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('compara2.object', {
#             'object': obj
#         })