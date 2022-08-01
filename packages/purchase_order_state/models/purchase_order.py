# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    
    invoice_status = fields.Selection([
        ('no', 'Nada Para Facturar'),        
        ('to invoice', 'Para Facturar'),
        ('invoiced', 'Facturado'),
        ('refund', 'Factura Con Devolución'),
        ], string='Invoice Status', compute='_get_invoice_status', store=True, readonly=True)
    