from odoo import http

class TropiSchool(http.Controller):
    @http.route('/todo/',)
    def index(self, **kw):
        return "Hello, world"