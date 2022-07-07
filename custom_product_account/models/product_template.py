# -*- encoding: utf-8 -*-

from datetime import datetime, time

from odoo import api, fields, models, _
from odoo.exceptions import UserError

import logging

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    refund_account_id = fields.Many2one('account.account', string='Cuenta de Devoluciones', index=True, tracking=True)