# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2021-today Ascetic Business Solution <www.asceticbs.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################

{
    'name': "Top Sold Products",
    'author': 'Ascetic Business Solution',
    'category': 'sale_management',
    'summary': """Reports of Top Sold Products""",
    'license': 'AGPL-3',
    'website': 'http://www.asceticbs.com',
    'description': """""",
    'version': '14.0.1.0',
    'depends': ['base','product','sale_management'],
    'data': [
             'security/ir.model.access.csv',
             'wizard/top_sales_view.xml',
             'views/top_sold_view.xml',
             'report/selected_product_report.xml',
             'report/selected_product_template.xml',
             'report/selected_product_amount_report.xml',
             'report/selected_product_amount_template.xml'],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',    
    'installable': True,
    'application': True,
    'auto_install': False,
}
