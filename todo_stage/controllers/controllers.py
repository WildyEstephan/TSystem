# -*- coding: utf-8 -*-
from odoo import http

# class HelpdeskRequest(http.Controller):
#     @http.route('/helpdesk_request/helpdesk_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/helpdesk_request/helpdesk_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('helpdesk_request.listing', {
#             'root': '/helpdesk_request/helpdesk_request',
#             'objects': http.request.env['helpdesk_request.helpdesk_request'].search([]),
#         })

#     @http.route('/helpdesk_request/helpdesk_request/objects/<model("helpdesk_request.helpdesk_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('helpdesk_request.object', {
#             'object': obj
#         })