# -*- coding: utf-8 -*-
from odoo import http

class Todo(http.Controller):

    @http.route('/todo')
    def Main(self, **kwargs):
        TodoTask = http.request.env['todo.wildy']
        domain_todo = [('is_done', '=', False)]
        tasks = TodoTask.search(domain_todo)
        return http.request.render('todo_wildy.index_template', {'tasks': tasks})