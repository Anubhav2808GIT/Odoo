from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.Appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]     # both are part of mail module in manifest file-->depends, inherit is used for chatter.
    _description = "Hospital Appointment"
    _rec_name = "ref"             #  for each record, there will have a display name that likes to look like that record name
    
    patient_id = fields.Many2one('hospital.patient', string = 'Patient')
    gender = fields.Selection(related="patient_id.gender")     # we can add another attribute, "read_only=True/False" to make it editable. By default it is True.
    appointment_time = fields.Datetime(string = 'Appointment Time' , default = fields.Datetime.now)
    booking_date = fields.Date(string = 'Booking Date' , default = fields.Date.context_today)
    ref = fields.Char(string='Reference', help="Reference of the patient form thepatient records")   # help will show a message when hover over the reference in the form
    prescription = fields.Html(string = 'Prescription')          # defining HTML field
    priority = fields.Selection([                   # adding Priority Widget
        ('0' , 'Normal'),
        ('1' , 'Low'),
        ('2' , 'High'),
        ('3' , 'Very High')], string="Priority")
    state = fields.Selection([                   # adding statusbar
        ('draft' , 'Draft'),
        ('in_consultation' , 'In Consultation'),
        ('done' , 'Done'),
        ('cancel' , 'Cancelled')], default="draft", string="Status", required=True)
    doctor_id = field.Many2one( 'res.users', string = "Doctor", tracking=True)
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string="Pharmacy Lines")
    
    @api.onchange("patient_id")
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
        
    def action_test(self):
        print("Button Clicked!!!!!!!")
        return{               # adding rainbow effect on clicking
            'effect':{
                'fadeout':'slow',         # helps to fade away the effect automatically
                'message':'Click Successfull',
                'type':'rainbow_man',
            }
        }
    
    def action_in_consultation(self):
        for rec in self:
            rec.state="in_consultation"
            
    def action_done(self):
        for rec in self:
            rec.state="done"
            
    def action_cancel(self):
        for rec in self:
            rec.state="cancel"
            
    def action_draft(self):
        for rec in self:
            rec.state="draft"
            
    
class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "Appointment Pharmacy Lines"
    
    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(related='product_id.list_price') 
    qty = fields.Integer(string="Quantity", default=1)
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
    
    
    
    
