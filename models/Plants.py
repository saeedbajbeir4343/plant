from odoo import fields,models,api
    
class Plants(models.Model):
    _name = 'nursery.plant'
    # _inherit = ('mail.thread')
    name = fields.Char("Plant Name")
    price = fields.Float()
    image = fields.Binary("Plant Image", attachment=True,store=True)
    number_in_stock = fields.Integer()
    order_count = fields.Integer(compute='_compute_order_count',store=True,string="Total sold")
    
    
    @api.constrains('order_count', 'number_in_stock')
    def _check_available_in_stock(self):
        for plant in self:
            if plant.number_in_stock and plant.order_count > plant.number_in_stock:
             raise UserError("There is only %s %s in stock but %s were sold"
                    % (plant.number_in_stock, plant.name, plant.order_count))
    
    