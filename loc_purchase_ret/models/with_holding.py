# -*- coding: utf-8 -*-

from openerp import models, fields, api

class with_holding(models.Model):
    _name = 'with.holding'
    
    concept = fields.Char('Concepto', required=True)
    base_uvt = fields.Char('A partir de UVT', required=True)
    base_pesos = fields.Char('Base en Pesos', required=True)
    rates = fields.Char('Tarifas', required=True)
    type_rates = fields.Char('Tipo', required=True)