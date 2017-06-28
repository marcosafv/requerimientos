# -*- coding: utf-8 -*-
{
    'name': "loc_purchase_ret",

    'summary': """
        Retenciones en colombia""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Marcos Flores",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/loc_purchase_ret.xml',
        'data/loc_purchase_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}