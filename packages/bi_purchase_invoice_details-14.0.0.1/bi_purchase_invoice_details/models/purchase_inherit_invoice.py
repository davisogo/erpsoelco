# -*- coding : utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class PurchaseOrderUpdate(models.Model):
	_inherit = 'purchase.order'

	invoiced_amount = fields.Float(string = 'Invoiced Amount',compute ='_compute_invoiced_amount')
	amount_due = fields.Float(string ='Amount Due', compute ='_computedue')
	paid_amount = fields.Float(string ='Paid Amount', compute ='_computepaid')
	amount_paid_percent = fields.Float(compute = 'action_amount_paid')
	currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.user.company_id.currency_id)

	@api.depends('paid_amount','invoiced_amount', 'amount_due')
	def _compute_invoiced_amount(self):
		for record in self:
			invoice_ids = self.env['account.move'].search(['&',('invoice_origin','=', record.name),'|',('state','=','draft'),('state','=','posted'),('payment_state', 'not in', ['reversed', 'invoicing_legacy'])])
			total = 0
			if invoice_ids:
				for bill in invoice_ids:
					total = bill.amount_total
					record.invoiced_amount = total
			else:
				record.invoiced_amount = total


	
	@api.depends('paid_amount','invoiced_amount', 'amount_due')
	def _computedue(self):
		for record in self:
			invoice_ids = self.env['account.move'].search(['&',('invoice_origin','=', record.name),'|',('state','=','draft'),('state','=','posted'),('payment_state', 'not in', ['reversed', 'invoicing_legacy'])])
			amount = 0
			if invoice_ids:
				for inv in invoice_ids:
					amount  += inv.amount_residual   
					record.amount_due = amount
			else:
				record.amount_due = amount
			

	@api.onchange('invoiced_amount','amount_due')
	def _computepaid(self):
		self.paid_amount = float(self.invoiced_amount) - float(self.amount_due)		


	@api.depends('paid_amount','invoiced_amount')
	def action_amount_paid(self):
		if self.invoiced_amount :
			self.amount_paid_percent = round(100 * self.paid_amount / self.invoiced_amount, 3)
		return self.amount_paid_percent
