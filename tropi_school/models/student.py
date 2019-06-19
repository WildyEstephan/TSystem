from odoo import api, fields, models

class Student(models.Model):
    _inherit = 'res.partner'

    student = fields.Boolean(string="Is Student",  )
    parent = fields.Boolean(string="Is Parent",  )
    id_student = fields.Char(string="ID Student", required=False, )
    ground_id = fields.Many2one(comodel_name="tropi.school.ground", string="Ground", required=False, )
    grade_id = fields.Many2one(comodel_name="tropi.school.grade",
                               string="Grade", required=False, domain="[('ground_id', '=', ground_id)]")
    section_id = fields.Many2one(comodel_name="tropi.school.section",
                                 string="Section", required=False, domain="[('grade_id', '=', grade_id)]")
    scholarship_id = fields.Many2one(comodel_name="tropi.school.scholarship",
                                     string="Scholarship", required=False, )


    @api.model
    def create(self, values):
        # Add code here

        if values['student'] and values['ground_id']:

            ground = self.env['tropi.school.ground'].search([('id', '=', values['ground_id'])])[0]

            values['id_student'] = ground.code + self.env['ir.sequence'].next_by_code('seq.id.student')



        return super(Student, self).create(values)