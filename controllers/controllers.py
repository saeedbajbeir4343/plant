# -*- coding: utf-8 -*-
# from odoo import http


# class Plant(http.Controller):
#     @http.route('/plant/plant/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/plant/plant/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('plant.listing', {
#             'root': '/plant/plant',
#             'objects': http.request.env['plant.plant'].search([]),
#         })

#     @http.route('/plant/plant/objects/<model("plant.plant"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('plant.object', {
#             'object': obj
#         })
