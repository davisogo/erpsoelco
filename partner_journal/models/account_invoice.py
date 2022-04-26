# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime, timedelta
from pytz import timezone

from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError

import logging

_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
    _inherit = "account.move"
    
    @api.model
    def create(self, vals):
        if self.env.user.partner_id.journal_id and (('move_type' in vals and vals['move_type']=='out_invoice') or 'move_type' not in vals):
            vals['journal_id']=self.env.user.partner_id.journal_id.id
        return super(AccountInvoice, self).create(vals)