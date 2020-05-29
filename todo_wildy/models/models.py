# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TodoTask(models.Model):
    _name = 'todo.wildy'
    _description = 'To-Do Wildy'
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active')
    user_id = fields.Many2one('res.users',
                              string='Responsible',
                              default=lambda self: self.env.user)
    team_ids = fields.Many2many('res.partner', string='Team')

    @api.multi
    def do_clear_done(self):
        for task in self:
            task.active = False

        return True

    @api.multi
    def write(self, values):
        if 'active' not in values:
            values['active'] = True

        super(TodoTask, self).write(values)