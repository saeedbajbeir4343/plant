# from odoo import ValidationError
import datetime
from odoo import fields,models,api

class Order(models.Model):
    _name = 'nursery.order'
    name = fields.Char('Reference')
    plant_id = fields.Many2one("nursery.plant", required=True)
    image  = fields.Binary('image',related='plant_id.image')
    customer_id = fields.Many2one("nursery.customer")
    state = fields.Selection([
    ('draft', 'Draft'),
    ('confirm', 'Confirmed'),
    ('cancel', 'Canceled')
    ], default='draft')
    last_modification = fields.Datetime(readonly=True)
    
    def write(self, values):
# helper to "YYYY-MM-DD"
         values['last_modification'] = fields.Datetime.now()
         return super(Order, self).write(values)
    def unlink(self):
# self is a recordset
        for order in self:
            if order.state == 'confirm':
                raise UserError("You can not delete confirmed orders")
        return super(Order, self).unlink()
    def _expand_states(self, states, domain, order):
        return [key for key, val in type(self).state.selection]