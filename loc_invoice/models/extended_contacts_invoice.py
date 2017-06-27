# -*- coding: utf-8 -*-

from openerp import models, fields, api

class extended_account_invoice(models.Model):
    _inherit = 'account.invoice'

    # campo nit para colocar valor extraido desde el on_change es readonly para no ser editado

    nitf = fields.Char('NIT')
    first_name = fields.Char('Nombre')
    first_last_name = fields.Char('Apellido')

    # Metodo on_change para extraer valor del nit de cada contacto

    def on_change_partner_id(self, cr, uid, ids, partner_id, context=None):
        values = {}
        if partner_id:
            partner = self.pool.get('res.partner').browse(cr, uid, partner_id, context=context)
            values = {
                'first_name': partner.x_name1,
                'first_last_name': partner.x_lastname1,
                'nitf': partner.formatedNit,
            }
        return {'value': values}

extended_account_invoice()