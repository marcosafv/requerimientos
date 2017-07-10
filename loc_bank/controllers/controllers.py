# -*- coding: utf-8 -*-
from openerp import http

# class LocBank(http.Controller):
#     @http.route('/loc_bank/loc_bank/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loc_bank/loc_bank/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('loc_bank.listing', {
#             'root': '/loc_bank/loc_bank',
#             'objects': http.request.env['loc_bank.loc_bank'].search([]),
#         })

#     @http.route('/loc_bank/loc_bank/objects/<model("loc_bank.loc_bank"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loc_bank.object', {
#             'object': obj
#         })