# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = "res.partner"
    
    journal_id = fields.Many2one(comodel_name="account.journal", string="Billing Journal", domain="[('type', '=', 'sale')]", check_company=True)
            
                