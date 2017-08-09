# -*- coding: utf-8 -*-

from openerp import models, fields, api

class extended_account_invoice(models.Model):
    _inherit = 'account.invoice'

    # campo nit para colocar valor extraido desde el on_change es readonly para no ser editado

    nit = fields.Char(compute="_save", store=True)
    nit_aux = fields.Char()
    first_name = fields.Char(compute="_save", store=True)
    first_name_aux = fields.Char()
    first_last_name = fields.Char(compute="_save", store=True)
    first_last_name_aux = fields.Char()
    with_holding_selec = fields.Boolean(string=None)
    concept = fields.Many2one('with.holding','Concepto')
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
                'first_name_aux': partner.x_name1,
                'first_last_name_aux': partner.x_lastname1,
                'nit_aux': partner.formatedNit,
                }
        return {'value': values}
    
    @api.depends('nit', 'nit_aux')
    def _save(self):
        self.nit = self.nit_aux
        self.first_name = self.first_name_aux
        self.first_last_name = self.first_last_name_aux
    

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

class extended_account_invoice_line(models.Model):
    _inherit = 'account.invoice.line'
    
    concept = fields.Many2one('with.holding','Concepto')