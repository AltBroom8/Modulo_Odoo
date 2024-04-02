# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class d:\users\solos\desktop\modulos\com_int(models.Model):
#     _name = 'd:\users\solos\desktop\modulos\com_int.d:\users\solos\desktop\modulos\com_int'
#     _description = 'd:\users\solos\desktop\modulos\com_int.d:\users\solos\desktop\modulos\com_int'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
class Shipping(models.Model):
    _name = 'com_int.shipping'
    _description = 'It allows you to describe the features of your shipping'

    name = fields.Char('Shipping', required=True, help='Name of the shipping entry')
    idShipping = fields.Integer('ID', required=True, help='Unique identifier for the shipping entry')
    shippingPoint = fields.Char('Shipping Point', required=True, help='Location where the shipping originates')
    pickUpPoint = fields.Char('Pick-Up Point', required=True, help='Location where the package will be picked up')
    shippingDate = fields.Date('Shipping Date', required=True, help='Date when the shipping will take place')
    cost = fields.Float('Cost', required=True, help='Cost associated with the shipping')
    
    # Relación One2many
    product_ids = fields.One2many('com_int.product', 'shipping_id', string='Product List')
    
    # Campo calculado para el costo total
    total_cost = fields.Float('Total Cost', compute='_calculate_total_cost', store=True)

    @api.depends('cost', 'product_ids.cost')
    def _calculate_total_cost(self):
        for record in self:
            record.total_cost = record.cost + sum(record.product_ids.mapped('cost'))

class Product(models.Model):
    _name = 'com_int.product'
    _description = 'It allows you to describe an actual product'

    name = fields.Char('Product', required=True, help='Name of the product entry')
    idproduct = fields.Integer('ID', required=True, help='Unique identifier for the product entry')
    description = fields.Text('Description', required=True, help='Description of the product')
    productName = fields.Char('Product Name', required=True, help='Actual name of the product')
    
    # Relación Many2one
    shipping_id = fields.Many2one('com_int.shipping', string='Shipping', help='Foreign key linking the product to a shipping entry')
    
    cost = fields.Float('Cost', required=True, help='Cost associated with the product')