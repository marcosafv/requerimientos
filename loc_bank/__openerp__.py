# -*- coding: utf-8 -*-
{
    'name': "loc_bank",

    'summary': """
        Agrega Entidades Bancarias de Colombia""",

    'description': """
        Entidades Bancarias de Colombia
    """,

    'author': "Marcos Flores",
    'website': "https://softnetcorp.net/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Bank',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/banks_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}