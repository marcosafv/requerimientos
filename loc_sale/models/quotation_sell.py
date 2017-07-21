# -*- coding: utf-8 -*-

from openerp import models, fields, api

class quotation_sell(models.Model):
    _inherit = 'sale.order'
    
    nit = fields.Char(compute="_save", store=True)
    nit_aux = fields.Char()
    first_name = fields.Char(compute="_save", store=True)
    first_name_aux = fields.Char()
    last_first_name = fields.Char(compute="_save", store=True)
    last_first_name_aux = fields.Char()
     
    def on_change_quotation(self, cr, uid, ids, partner_id, context=None):
        values = {}
        if partner_id:
            partner = self.pool.get('res.partner').browse(cr, uid, partner_id, context=context)
            addr = partner.address_get(['delivery', 'invoice'])
            values = {
                'first_name_aux': partner.x_name1,
                'last_first_name_aux': partner.x_lastname1,
                'nit_aux': partner.formatedNit,
                'partner_invoice_id': addr['invoice'],
                'partner_shipping_id': addr['delivery'],
                'pricelist_id': partner.property_product_pricelist,
            }
        return {'value': values}
    
    @api.depends('nit', 'nit_aux')
    def _save(self):
        self.nit = self.nit_aux
        self.first_name = self.first_name_aux
        self.last_first_name = self.last_first_name_aux
quotation_sell()