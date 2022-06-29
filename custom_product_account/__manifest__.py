# -*- coding: utf-8 -*-
{
    "name" : "Modificaciones Cuentas en productos",
    "author" : "Coondev",
    "version":"14.0.1",

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        'views/product_template.xml',
    ],
    "application": True,
    "auto_install":False,
    "installable" : True,
    "currency": "COP"
}
