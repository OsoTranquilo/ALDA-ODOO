# -*- coding: utf-8 -*-
from openerp import http

# class CategoryTourism(http.Controller):
#     @http.route('/category_tourism/category_tourism/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/category_tourism/category_tourism/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('category_tourism.listing', {
#             'root': '/category_tourism/category_tourism',
#             'objects': http.request.env['category_tourism.category_tourism'].search([]),
#         })

#     @http.route('/category_tourism/category_tourism/objects/<model("category_tourism.category_tourism"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('category_tourism.object', {
#             'object': obj
#         })