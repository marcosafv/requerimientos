# -*- coding: utf-8 -*-
from openerp import http

# class LocalizacionColombia(http.Controller):
#     @http.route('/localizacion_colombia/localizacion_colombia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/localizacion_colombia/localizacion_colombia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('localizacion_colombia.listing', {
#             'root': '/localizacion_colombia/localizacion_colombia',
#             'objects': http.request.env['localizacion_colombia.localizacion_colombia'].search([]),
#         })

#     @http.route('/localizacion_colombia/localizacion_colombia/objects/<model("localizacion_colombia.localizacion_colombia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('localizacion_colombia.object', {
#             'object': obj
#         })