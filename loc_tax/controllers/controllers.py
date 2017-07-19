# -*- coding: utf-8 -*-
from openerp import http

# class LocPurchaseRet(http.Controller):
#     @http.route('/loc_purchase_ret/loc_purchase_ret/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loc_purchase_ret/loc_purchase_ret/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('loc_purchase_ret.listing', {
#             'root': '/loc_purchase_ret/loc_purchase_ret',
#             'objects': http.request.env['loc_purchase_ret.loc_purchase_ret'].search([]),
#         })

#     @http.route('/loc_purchase_ret/loc_purchase_ret/objects/<model("loc_purchase_ret.loc_purchase_ret"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loc_purchase_ret.object', {
#             'object': obj
#         })