# -*- coding: utf-8 -*-
from odoo import http

class TropiSchool(http.Controller):
    @http.route('/tropi_school/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    # @http.route('/tropi_school/tropi_school/objects/', auth='public')
    # def list(self, **kw):
    #     return http.request.render('tropi_school.listing', {
    #         'root': '/tropi_school/tropi_school',
    #         'objects': http.request.env['tropi_school.tropi_school'].search([]),
    #     })
    #
    # @http.route('/tropi_school/tropi_school/objects/<model("tropi_school.tropi_school"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('tropi_school.object', {
    #         'object': obj
    #     })