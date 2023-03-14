from odoo import api, fields, models


class CancelAppointmentWizard(models.TransientModel):        #defining a Transient Model
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"
    
    appointment_id=fields.Many2one('hospital.appointment', string="Appointment")
