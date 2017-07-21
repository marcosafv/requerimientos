# -*- coding: utf-8 -*-
{
    'name': "loc_invoice",

    'summary': """
        extension de campos contactos para la facturacion""",

    'description': """
        Facturacion de contactos
    """,

    'author': "Marcos Flores",
    'website': "https://softnetcorp.net/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Invoices',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','loc_contacts','loc_tax'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/extended_contacts_invoice.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}