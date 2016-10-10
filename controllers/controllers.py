# -*- coding: utf-8 -*-
from openerp import http

# class KbcsSales(http.Controller):
#     @http.route('/kbcs_sales/kbcs_sales/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kbcs_sales/kbcs_sales/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kbcs_sales.listing', {
#             'root': '/kbcs_sales/kbcs_sales',
#             'objects': http.request.env['kbcs_sales.kbcs_sales'].search([]),
#         })

#     @http.route('/kbcs_sales/kbcs_sales/objects/<model("kbcs_sales.kbcs_sales"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kbcs_sales.object', {
#             'object': obj
#         })