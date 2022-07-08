# -*- coding: utf-8 -*-
{
    'name': "stock_transfer_approval",

    'summary': """
       This Module requires a approval for internal transfer""",

    'description': """
       This Module requires a approval for internal transfer
    """,

    'author': "Dashsol",
    'website': "shhamza1@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','mail'],

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
