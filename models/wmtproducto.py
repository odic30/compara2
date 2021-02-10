# -*- coding: utf-8 -*-

from odoo import models, fields, api


class walmartProducto(models.Model):
     _name = 'walmart.producto'
     
    nombre = fields.Char('Nombre', required=True)
    sku1 = fields.Char('SKU')
    asin = fields.Char('ASIN')
    upc = fields.Char('UPC')
    marca = fields.Char('Marca')
    categoria = fields.Char('Categoria')
    cantidad = fields.Float()
    UoM = fields.Char('Unidad de Medida')
    precio = fields.Float()

