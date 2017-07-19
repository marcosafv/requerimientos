# -*- coding: utf-8 -*-

from openerp import models, fields, api

class tax_ica(models.Model):
    _name = 'tax.ica'
    
    list_activities = fields.Char('Lista de Actividades')
    current_rates = fields.Char('Tarifas Vigentes')
    type_activity = fields.Selection(
        [
            ("Actividades Industriales", "Actividades Industriales"),
            ("Actividades Comerciales", "Actividades Comerciales"),
            ("Actividades de servicios", "Actividades de servicios"),
            ("Actividades financieras", "Actividades financieras"),
            ], "Tipo de Actividad"
                                     )
    
tax_ica() 