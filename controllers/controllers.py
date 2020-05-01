# -*- coding: utf-8 -*-
# from odoo import http


# class EwOdooApps(http.Controller):
#     @http.route('/ew_odoo_apps/ew_odoo_apps/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ew_odoo_apps/ew_odoo_apps/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ew_odoo_apps.listing', {
#             'root': '/ew_odoo_apps/ew_odoo_apps',
#             'objects': http.request.env['ew_odoo_apps.ew_odoo_apps'].search([]),
#         })

#     @http.route('/ew_odoo_apps/ew_odoo_apps/objects/<model("ew_odoo_apps.ew_odoo_apps"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ew_odoo_apps.object', {
#             'object': obj
#         })
