# -*- coding: utf-8 -*-

from openerp import models, fields, api

class extended_contacts(models.Model):
    _inherit = 'res.partner'
    
    concept = fields.Many2one('with.holding','Concepto')
    base_uvt = fields.Char('A partir de UVT')
    base_pesos = fields.Char('Base en Pesos')
    rates = fields.Char('Tarifas')
    type_rates = fields.Char('Tipo')
    
    def on_change_with_holding(self, cr, uid, ids, concept, context=None):
        values = {}
        if concept:
            concepto = self.pool.get('with.holding').browse(cr, uid, concept, context=context)
            values = {
                'base_uvt': concepto.base_uvt,
                'base_pesos': concepto.base_pesos,
                'rates': concepto.rates,
                'type_rates': concepto.type_rates,
            }
        return {'value': values}
    
extended_contacts()