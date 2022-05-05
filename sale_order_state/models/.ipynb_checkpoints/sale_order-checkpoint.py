# -*- coding: utf-8 -*-
# Copyright 2019 Joan Marín <Github@joanmarin>
# Copyright 2019 Diego Carvajal <Github@diegoivanc>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    invoice_status = fields.Selection([
        ('upselling', 'Oportunidad de Sobreventa'),
        ('invoiced', 'Facturado'),
        ('to invoice', 'Para Facturar'),
        ('reverse', 'Factura Con Devolución'),
        ('no', 'Nada Para Facturar')
        ], string='Invoice Status', compute='_get_invoice_status', store=True, readonly=True)
    
    @api.depends('state', 'order_line.invoice_status')
    def _get_invoice_status(self):
        for item in self:
            res = super(SaleOrder, item)._get_invoice_status()
            if item.invoice_status == 'to invoice':
                invoice = item.env['account.move'].search([('invoice_origin','ilike','%'+item.name+'%'),('move_type','=','out_refund')])
                for record in invoice:
                    item.invoice_status = 'reverse'

                