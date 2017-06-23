# -*- coding: utf-8 -*-
from openerp import http

# class LocInvoice(http.Controller):
#     @http.route('/loc_invoice/loc_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loc_invoice/loc_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('loc_invoice.listing', {
#             'root': '/loc_invoice/loc_invoice',
#             'objects': http.request.env['loc_invoice.loc_invoice'].search([]),
#         })

#     @http.route('/loc_invoice/loc_invoice/objects/<model("loc_invoice.loc_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loc_invoice.object', {
#             'object': obj
#         })