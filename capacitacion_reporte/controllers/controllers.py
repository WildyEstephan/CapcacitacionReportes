# -*- coding: utf-8 -*-
from odoo import http

# class CapacitacionReporte(http.Controller):
#     @http.route('/capacitacion_reporte/capacitacion_reporte/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/capacitacion_reporte/capacitacion_reporte/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('capacitacion_reporte.listing', {
#             'root': '/capacitacion_reporte/capacitacion_reporte',
#             'objects': http.request.env['capacitacion_reporte.capacitacion_reporte'].search([]),
#         })

#     @http.route('/capacitacion_reporte/capacitacion_reporte/objects/<model("capacitacion_reporte.capacitacion_reporte"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('capacitacion_reporte.object', {
#             'object': obj
#         })