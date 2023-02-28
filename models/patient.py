from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]     # both are part of mail module in manifest file-->depends, inherit is used for chatter.
    _description = "Hospital Patient"

    name = fields.Char(string='Name' , tracking = True)   #Track visibility is used to track the changes made to the fields, as our system is a multi-user system and the different people can access the same record. 
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age', tracking = True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking = True)
    active = fields.Boolean(string='Active' default=True)           # gives the Visibility of the records in the view.
