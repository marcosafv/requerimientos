# -*- coding: utf-8 -*-
{
    'name': "loc_sale",

    'summary': """
        Agregando a modulo de cotizacion informacion del cliente""",

    'description': """
        Informacion del cliente en modulo de cotizacion
    """,

    'author': "Marcos Flores",
    'website': "https://softnetcorp.net/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/quotation_sale_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
