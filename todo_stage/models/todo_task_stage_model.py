from odoo import api, fields, models

class Stage(models.Model):
    _name = 'todo.wildy.stage'
    _description = 'Stage'

    name = fields.Char('Name', translate-True)
    sequence = fields.Integer('Sequence')

