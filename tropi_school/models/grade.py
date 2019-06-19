from odoo import api, fields, models

class Grade(models.Model):
    _name = 'tropi.school.grade'
    _description = 'Grade of School'

    name = fields.Char(string="Name", required=True, )
    grade = fields.Selection(string="Grade",
                             selection=[('preschool', 'Preschool'),
                                        ('primary', 'Primary school'),
                                        ('secondary', 'Secondary school'),
                                        ('other', 'Other school'),
                                        ],
                             required=True, )
    ground_id = fields.Many2one(comodel_name="tropi.school.ground", string="Ground", required=True, )
    section_ids = fields.One2many(comodel_name="tropi.school.section",
                                    inverse_name="grade_id", string="Sections", required=False, )
    student_ids = fields.One2many(comodel_name="res.partner", inverse_name="grade_id",
                                  string="Students", required=False, )


