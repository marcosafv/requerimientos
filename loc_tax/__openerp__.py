# -*- coding: utf-8 -*-
{
    'name': "loc_tax",

    'summary': """
        Agrega Retenciones, ICA""",

    'description': """
        Impuestos en colombia
    """,

    'author': "Marcos Flores",
    'website': "https://softnetcorp.net/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tax',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','loc_contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/with_holding.xml',
        'views/tax_ica.xml',
        'views/tax_iva_client.xml',
        'views/tax_iva_provider.xml',
        'data/with_holding_data.xml',
        'data/tax_ica_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}