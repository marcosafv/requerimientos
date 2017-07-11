# -*- coding: utf-8 -*-
{
    'name': "loc_invoice_print",

    'summary': """
        Modulo para la creacion de facturas de venta""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Marcos Flores",
    'website': "https://softnetcorp.net/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report','loc_invoice'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/invoice_print.xml',
        'views/template_invoice_print.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}