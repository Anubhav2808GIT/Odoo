from datetime import date
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]     # both are part of mail module in manifest file-->depends, inherit is used for chatter.
    _description = "Hospital Patient"

    name = fields.Char(string='Name' , tracking = True)   #Track visibility is used to track the changes made to the fields, as our system is a multi-user system and the different people can access the same record. 
    date_of_birth = field.Date(string='Date Of Birth')
    ref = fields.Char(string='Reference', default = 'Odoo Mates')
    age = fields.Integer(string='Age', compute='_compute_age' , tracking = True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking = True, default = 'Female')
    active = fields.Boolean(string='Active' default=True)           # gives the Visibility of the records in the view.
    appointment_id = fields.Many2one('hospital.appointment', string = 'Appointment')    # for many2one fields, it is shown that rec_name._rec_name is intended to define the record value used to display it in search for many2one and other cases
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('patient.tag', string='Tags')
    
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age=1
