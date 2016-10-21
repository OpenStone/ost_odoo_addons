# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError


class sale_order_line(models.Model):
    _inherit = "sale.order.line"

    @api.model
    def default_get(self, fields):
        res = super(sale_order_line, self).default_get(fields)
        if self._context:
            context_keys = self._context.keys()
            next_sequence = 1
            if 'order_line' in context_keys:
                if len(self._context.get('order_line')) > 0:
                    next_sequence = len(self._context.get('order_line')) + 1
        res.update({'sequence': next_sequence})
        return res
