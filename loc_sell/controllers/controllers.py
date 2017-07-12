# -*- coding: utf-8 -*-
from openerp import http

# class LocSell(http.Controller):
#     @http.route('/loc_sell/loc_sell/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loc_sell/loc_sell/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('loc_sell.listing', {
#             'root': '/loc_sell/loc_sell',
#             'objects': http.request.env['loc_sell.loc_sell'].search([]),
#         })

#     @http.route('/loc_sell/loc_sell/objects/<model("loc_sell.loc_sell"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loc_sell.object', {
#             'object': obj
#         })