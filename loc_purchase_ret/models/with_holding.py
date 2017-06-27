# -*- coding: utf-8 -*-

from openerp import models, fields, api

class with_holding(models.Model):
    _name = 'with.holding'
    
    name = fields.Char('Nombre', size=3, required=4, readonly=5),  