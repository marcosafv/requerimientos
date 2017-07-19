# -*- coding: utf-8 -*-

from openerp import models, fields, api

class quotation_sell(models.Model):
    _inherit = 'sale.order'
    
    first_name = fields.Char('Nombre')
    last_first_name = fields.Char('Apellido')
    nit = fields.Char('NIT')
     
    def on_change_quotation(self, cr, uid, ids, partner_id, context=None):
        values = {}
        if partner_id:
            partner = self.pool.get('res.partner').browse(cr, uid, partner_id, context=context)
            addr = partner.address_get(['delivery', 'invoice'])
            values = {
                'first_name': partner.x_name1,
                'last_first_name': partner.x_lastname1,
                'nit': partner.formatedNit,
                'partner_invoice_id': addr['invoice'],
                'partner_shipping_id': addr['delivery'],
                'pricelist_id': partner.property_product_pricelist,
            }
        return {'value': values}
quotation_sell()