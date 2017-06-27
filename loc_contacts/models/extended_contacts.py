# -*- coding: utf-8 -*-

from openerp import models, fields, api

class extended_contacts(models.Model):
    _inherit = 'res.partner'

    first_name = fields.Char('Primer Nombre',)
    first_last_name = fields.Char('Primer Apellido',)
    second_name = fields.Char('Segundo Nombre',)
    second_last_name = fields.Char('Segundo Apellido',)
    doc_type = fields.Selection(
        [
            (1, "Nro identification"),
            (11, "11 - Registro civil"),
            (12, "12 - Tarjeta de identidad"),
            (13, "13 - Cédula de ciudadanía"),
            (21, "21 - Tarjeta de extranjería"),
            (22, "22 - Cédula de extranjería"),
            (31, "31 - NIT (Número de identificación tributaria)"),
            (41, "41 - Pasaporte"),
            (42, "42 - Tipo de documento extranjero"),
            (43, "43 - Para uso definido por la DIAN")

        ], "Tipo de Identificacion"
    )
    numb_id = fields.Integer('Nro de identificacion')
    verif_digit = fields.Integer('DV', size=2)

extended_contacts()