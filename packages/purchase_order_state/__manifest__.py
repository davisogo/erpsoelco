# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Estado revertido / Compra',
    'version': '14.0.0.1',
    'summary': 'Estado revertido / Compra',
    'sequence': 10,
    'description': "Estado revertido / Compra",
    'author': "Daniel Caldas",
    'website': "https://www.soelco.co",
    'license': 'AGPL-3',
    'category': 'Technical/Technical,',
    'images': ['pruchase_order_state/static/description/icon.png'],
    'support': 'daniel.caldas@soelco.com.co',
    'contributors': ['Daniel Esteban Caldas'],
    
    'depends': [
        'base',
        'purchase',
        'sale',
        'sales_team',
    ],
   'data': [
        #'security/ir.model.access.csv'
    ],
    'qweb': [
    ],
    'demo': [
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}

