# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Ground(models.Model):
    _name = 'tropi.school.ground'
    _description = 'Ground of School'

    name = fields.Char(string="Name", required=True, )
    code = fields.Char(string="Short Code", required=True, )
    street = fields.Char(string="Street", required=False, )
    street2 = fields.Char(string="Street 2", required=False, )
    country_id = fields.Many2one(comodel_name="res.country", string="Country",
                                 required=False, default=lambda self: self.env.user.company_id.country_id.id)
    zip = fields.Char(string="Zip", required=False, )
    telephone = fields.Char(string="Telephone", required=False, )
    email = fields.Char(string="Email", required=False, )

    grade_ids = fields.One2many(comodel_name="tropi.school.grade",
                                inverse_name="ground_id", string="Grades", required=False, )




