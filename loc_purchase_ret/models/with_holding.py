# -*- coding: utf-8 -*-

from openerp import models, fields, api

class with_holding(models.Model):
    _name = 'with.holding'
    _rec_name = 'concept' #indica el campo que va a apuntar el campo relacional ejemplo many2one
    concept = fields.Char('Concepto', required=True)
    base_uvt = fields.Char('A partir de UVT', required=True)
    base_pesos = fields.Char('Base en Pesos', required=True)
    rates = fields.Char('Tarifas', required=True)
    type_rates = fields.Char('Tipo', required=True)
    
    """@api.depends('base_pesos')
        def _concatenate_fields(self):
        concat = '$ '+ str(self.base_pesos)
        self.base_pesos = concat"""