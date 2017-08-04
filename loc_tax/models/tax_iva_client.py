# -*- coding: utf-8 -*-

from openerp import models, fields, api

class tax_iva_client(models.Model):
    _name = 'tax.iva.client'
    diary_iva = fields.Many2one('account.journal', required=True)
    client = fields.Many2one('res.partner', required=True)
    accounting_date = fields.Date()
    force_period = fields.Selection(
        [
            ("Periodo de apertura 2017", "Periodo de apertura 2017"),
            ("01/2017", "01/2017"),
            ("02/2017", "02/2017"),
            ("03/2017", "03/2017"),
            ("04/2017", "04/2017"),
            ("05/2017", "05/2017"),
            ("06/2017", "06/2017"),
            ("07/2017", "07/2017"),
            ("08/2017", "08/2017"),
            ("09/2017", "09/2017"),
            ("10/2017", "10/2017"),
            ("11/2017", "11/2017"),
            ("12/2017", "12/2017"),
            ], 
                                     )
    type = fields.Char(change_default="Factura de Cliente")
    third_person = fields.Many2one('res.partner')
    internal_code = fields.Char()
    accounts_receivable = fields.Char(related="diary_iva.default_debit_account_id.name", required=True)
    accounts_payable = fields.Char(related="diary_iva.default_credit_account_id.name", required=True)
    description = fields.Char(required=True)
    voucher_date = fields.Date()
tax_iva_client() 