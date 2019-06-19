from odoo import api, fields, models

class Scholarship(models.Model):
    _name = 'tropi.school.scholarship'
    _description = 'Scholarship of School'

    name = fields.Char(string="Name", required=True, )
    student_ids = fields.One2many(comodel_name="res.partner",
                                    inverse_name="scholarship_id",
                                    string="Students", required=False, )
    type_scholarship = fields.Selection(string="",
                                        selection=[('complete', 'Complete'),
                                                   ('partial', 'Partial'),
                                                   ], required=False, )
    percentage = fields.Float(string="Percentage",  required=False, default=50.0)
    count = fields.Integer(string="Scholarship Students", required=False, compute='')

    @api.multi
    @api.depends('student_ids')
    def _compute_count(self):
        """
        @api.depends() should contain all fields that will be used in the calculations.
        """
        c = 0
        for s in self.student_ids:
            c = c + 1

        self.write(
            {
                'count': c
            }
        )
