# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Cancel Multiple Sale Orders',
    'version': '14.0',
    'category': 'Sales',
    'summary': 'This app used to cancel multiple sale orders using one button click',
    'description': """
        cancel sale orders
        cancel sales orders
        multiple cancel sale orders
        multiple cancel sales orders
        cancel multiple sale orders
        cancel multiple sales orders
        cancel orders
        odoo teqstars apps
        teqstars odoo apps
        sales order cancel
        sale order cancel
        sale cancel
        sales cancel
    """,
    'depends': ['sale_stock'],
    'data': [
            'wizard/cancel_multi_order_wizard_view.xml',
            'security/ir.model.access.csv',
    ],
    'images': ['static/description/multiple_cancel_sale_orders_banner.png'],
    'author': 'Teqstars',
    'website': 'https://teqstars.com',
    'support': 'support@teqstars.com',
    'maintainer': 'Teqstars',
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
    'price': '0.0',
    'currency': 'EUR',
}
