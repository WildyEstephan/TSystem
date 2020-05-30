from odoo import api, fields, models
class Tag(models.Model):
    _name = 'todo.wildy.tag'
    _description = 'To-do Tag'

    name = fields.Char(string="Name", traslate=True)


