# -*- coding: utf-8 -*-
from odoo import http

# class Manteni(http.Controller):
#     @http.route('/manteni/manteni/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manteni/manteni/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('manteni.listing', {
#             'root': '/manteni/manteni',
#             'objects': http.request.env['manteni.manteni'].search([]),
#         })

#     @http.route('/manteni/manteni/objects/<model("manteni.manteni"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manteni.object', {
#             'object': obj
#         })