###############################################################################################
#
# Luis Felipe Paternina  - Julian Bocanegra                                
# Odoo Dev                 Odoo Consulting
# 
# Bogotá,Colombia
#
#
###############################################################################################

{
    'name': 'co customer reports',

    'version': '14.0.0.0',

    'author': "Coondev S.A.S",

    'contributors': ['Luis Felipe Paternina'],

    'website': "www.coodev.com",

    'category': 'reports',

    'depends': [

        'account_accountant',
        'base',
        'l10n_co_dian_data',
        'l10n_co_e_invoicing',
        'od_journal_sequence',
    ],

    'data': [
        'reports/invoice_report.xml',      
    ],
    'installable': True
}
