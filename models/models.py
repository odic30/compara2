# -*- coding: utf-8 -*-

from odoo import models, fields, api


class walmartProducto(models.Model):
     _name = 'walmart.producto'

class amazonProducto(models.Model):
     _name = 'amazon.producto'
     
    
class productComparador(models.Model):
     _name = 'products.comparador'
     
     productoWmt = fields.Many2one('walmart.product',string='Producto Walmart')
     productoAmz = fields.Many2one('amazon.product',string='Producto Amazon')
