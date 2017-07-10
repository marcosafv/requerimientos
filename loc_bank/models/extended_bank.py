# -*- coding: utf-8 -*-

from openerp import models, fields, api

class bank_add(models.Model):
    _inherit = 'res.partner.bank'
    bank_ids = fields.Many2one()
bank_add()