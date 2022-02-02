# -*- coding: utf-8 -*-
import odoo.addons.decimal_precision as dp

from odoo import api, fields, models

class PurchaseOrderTax(models.Model):
    _name = 'purchase.order.tax'

    purchase_order = fields.Many2one('purchase.order', string='Purchase Order', ondelete='cascade')
    name = fields.Char(string='Tax Description', required=True)
    amount = fields.Float(string='Amount', digits=dp.get_precision('Account'))
    account_id = fields.Many2one('account.account', string='Tax Account')
    tax_id = fields.Many2one('account.tax', string="Tax")


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    taxes = fields.One2many('purchase.order.tax', 'purchase_order', string='Taxes',
                            compute='_compute_purchase_order_taxes')

    @api.depends('order_line.taxes_id')
    def _compute_purchase_order_taxes(self):
        for rec in self:
            rec.taxes = [(5, 0, 0)]
            for line in rec.order_line:
                previous_taxes_ids = rec.taxes.mapped('tax_id').ids
                if line.taxes_id:
                    price = line.price_unit
                    taxes = line.taxes_id.compute_all(
                        price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id,
                        partner=line.partner_id)['taxes']
                    val_list = []
                    for tax in taxes:
                        if tax['id'] in previous_taxes_ids:
                            purchase_tax = rec.taxes.filtered(lambda taxes: taxes.tax_id.id == tax['id'])
                            purchase_tax.amount += tax['amount']
                        else:
                            val = {
                                'purchase_order': rec.id,
                                'name': tax['name'],
                                'tax_id': tax['id'],
                                'amount': tax['amount'],
                                'account_id': tax['account_id'],
                            }
                            val_list.append(val)
                    rec.taxes.create(val_list)
