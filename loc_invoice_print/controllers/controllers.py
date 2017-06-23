# -*- coding: utf-8 -*-
from openerp import http

# class LocInvoicePrint(http.Controller):
#     @http.route('/loc_invoice_print/loc_invoice_print/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loc_invoice_print/loc_invoice_print/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('loc_invoice_print.listing', {
#             'root': '/loc_invoice_print/loc_invoice_print',
#             'objects': http.request.env['loc_invoice_print.loc_invoice_print'].search([]),
#         })

#     @http.route('/loc_invoice_print/loc_invoice_print/objects/<model("loc_invoice_print.loc_invoice_print"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loc_invoice_print.object', {
#             'object': obj
#         })