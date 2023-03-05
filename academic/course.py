from odoo import api, fields, models

class Course(models.Model):
    _name = "academic.course"

    name = fields.Char("Name", required = True, size=100)
    desc = fields.Text("Description")
    responsible_id = fields.Many2one(
        comodel_name="res.users", #ini data bawaan odoo
        string="Responsible",
        required = True,
    )

    session_ids = fields.One2many(
        comodel_name="academic.session",
        string="Sessions",
        inverse_name="course_id" #foreign key
    )