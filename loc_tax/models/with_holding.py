# -*- coding: utf-8 -*-

from openerp import models, fields, api

class with_holding(models.Model):
    _name = 'with.holding'
    _rec_name = 'concept' #indica el campo que va a apuntar el campo relacional ejemplo many2one
    concept = fields.Char('Concepto', required=True)
    base_uvt = fields.Char('A partir de UVT', required=True)
    base_pesos = fields.Char(required=True)
    rates = fields.Char('Tarifas', required=True)
    type_rates = fields.Selection(
        [
            ("Salariales", "Salariales"),
            ("Compras", "Compras"),
            ("Servicios", "Servicios"),
            ("Honorarios y Consultoria", "Honorarios y Consultoria"),
            ("Otros", "Otros")
            ], "Tipo"
                                  )
    
    @api.onchange('base_pesos')
    def _concatenate_fields(self):
        if self.base_pesos is False:
            self.base_pesos = ''
        else:
            string_tranform = str(self.base_pesos)
            concat = '$ ' + string_tranform
            self.base_pesos = concat