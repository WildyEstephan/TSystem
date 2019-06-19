from odoo import api, fields, models

class Section(models.Model):
    _name = 'tropi.school.section'
    _description = 'Section of School'

    name = fields.Char(string="Name", required=False, readonly=True, deafult='')
    grade_id = fields.Many2one(comodel_name="tropi.school.grade",
                               string="Grade", required=True, domain="[('ground_id', '=', ground_id)]")
    section = fields.Char(string="Section", required=True, )
    student_ids = fields.One2many(comodel_name="res.partner", inverse_name="section_id",
                                  string="Students", required=False, )
    limit = fields.Integer(string="Limit of Students", required=False, default=0)
    ground_id = fields.Many2one(comodel_name="tropi.school.ground", string="Ground", required=False,)

    # @api.onchange('section')
    # def onchange_section(self):
    #     self.name_display = str(self.grade_id.name) + ' ' + str(self.section)
    #
    # @api.onchange('grade_id')
    # def onchange_grade_id(self):
    #     self.name_display = str(self.grade_id.name) + ' ' + str(self.section)

    @api.model
    def create(self, values):
        # Add code here

        grade = self.env['tropi.school.grade'].search([('id', '=', values['grade_id'])])[0]

        values['name'] = grade.name + ' ' + values['section']
        return super(Section, self).create(values)

    @api.multi
    def write(self, values):
        # Add code here
        values['name'] = values['grade_id'].name + ' ' + values['section']

        return super(Section, self).write(values)
