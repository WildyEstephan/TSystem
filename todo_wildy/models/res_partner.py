from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    todo_ids = fields.Many2many('todo.wildy', string="To-do Teams")