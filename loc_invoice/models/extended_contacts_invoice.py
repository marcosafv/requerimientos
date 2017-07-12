# -*- coding: utf-8 -*-

from openerp import models, fields, api

class extended_account_invoice(models.Model):
    _inherit = 'account.invoice'

    # campo nit para colocar valor extraido desde el on_change es readonly para no ser editado

    nitf = fields.Char('NIT')
    first_name = fields.Char('Nombre')
    first_last_name = fields.Char('Apellido')
    with_holding_selec = fields.Boolean(string=None)
    concept = fields.Char('Concepto')
    base_uvt = fields.Char('A partir de UVT')
    base_pesos = fields.Char('Base en Pesos')
    rates = fields.Char('Tarifas')
    type_rates = fields.Char('Tipo')

    # Metodo on_change para extraer valor del nit de cada contacto

    def on_change_partner_id(self, cr, uid, ids, partner_id, context=None):
        values = {}
        if partner_id:
            partner = self.pool.get('res.partner').browse(cr, uid, partner_id, context=context)
            values = {
                'first_name': partner.x_name1,
                'first_last_name': partner.x_lastname1,
                'nitf': partner.formatedNit,
                'concept': partner.concept,
                'base_uvt': partner.base_uvt,
                'base_pesos': partner.base_pesos,
                'rates': partner.rates,
                'type_rates': partner.type_rates,
            }
        return {'value': values}
    
    """@api.onchange('with_holding_selec')
    def check_with_holding(self):
        if self.with_holding_selec is True:
            self.concept = ''
            self.base_uvt = ''
            self.base_pesos = ''
            self.rates = ''
            self.type_rates = ''
        
        else:
            self.concept = 'N/A'
            self.base_uvt = 'N/A'
            self.base_pesos = 'N/A'
            self.rates = 'N/A'
            self.type_rates = 'N/A'"""
                
    """@api.onchange('with_holding_selec')
    def onChangeWith_holding_selec(self):
    
        This function changes the person type field and the company type if
        checked / unchecked
        @return: void
        if self.with_holding_selec is True:
            self.with_holding = True
        else:
            self.with_holding_selec = str(False)"""
    
extended_account_invoice()