# -*- coding: utf-8 -*-
{
    'name': 'Purchase Order Tax Summary',
    'summary': 'Purchase Order Tax Summary',
    'description': """Show the summary of the taxes selected in the purchase order lines.""",
    'author': "Odoo Being",
    'website': "https://www.odoobeing.com",
    'license': 'AGPL-3',
    'category': 'Purchase',
    'images': ['static/description/purchase_tax_summary.png'],
    'version': '14.0.1.0.0',
    'support': 'odoobeing@gmail.com',
    'depends': ['purchase'],
    'data': [
        "security/ir.model.access.csv",
        'views/purchase_order.xml',

    ],
    'installable': True,
    'auto_install': False,
}
