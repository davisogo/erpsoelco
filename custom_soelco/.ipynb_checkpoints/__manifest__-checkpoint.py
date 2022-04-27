# -*- coding: utf-8 -*-
# Copyright 2019 Diego Carvajal <Github@diegoivanc>
# Copyright 2019 Joan Marín <Github@joanmarin>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Modificaciones Soelco",
    "category": "Financial",
    "version": "14.0",
    "author": "Daniers D. Odooco",
    "website": "http://www.odooco.com.co",
    "license": "AGPL-3",
    "summary": "Colombian E-Invoicing",
    "depends": ['base','contacts','l10n_co_e_invoicing'],
    "data": [
        'security/group.xml',
        'security/ir.rule.csv',
        "views/account_invoice_views.xml",
        "views/sale_order.xml",
        "views/purchase_order.xml",
    ],
    "installable": True,
}
