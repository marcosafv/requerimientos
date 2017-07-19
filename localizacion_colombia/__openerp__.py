# -*- coding: utf-8 -*-
{
    'name': "localizacion_colombia",

    'summary': """
        Instala todos los modulos de la localizacion de colombia de manera completa""",

    'description': """
        Localizacion Colombia
    """,

    'author': "Marcos Flores",
    'website': "https://softnetcorp.net/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'loc_co',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','loc_bank','loc_contacts','loc_invoice','loc_invoice_print','loc_tax','loc_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}