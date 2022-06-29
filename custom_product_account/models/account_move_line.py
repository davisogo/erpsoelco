# -*- encoding: utf-8 -*-

from datetime import datetime, time

from odoo import api, fields, models, _
from odoo.exceptions import UserError

import logging

_logger = logging.getLogger(__name__)


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.model_create_multi
    def create(self, vals_list):
        items = super(AccountMoveLine, self).create(vals_list)
        for item in items:
            if item.move_id.move_type == 'out_refund' and item.product_id.refund_account_id:
                item.account_id = item.product_id.refund_account_id
        return items