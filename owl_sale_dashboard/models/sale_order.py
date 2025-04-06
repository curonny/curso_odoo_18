from datetime import datetime, time

from odoo import fields, models, api
from odoo.fields import Datetime


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def retrieve_dashboard(self):
        result = {
            'total_customer': 0,
            "last_7_days": 0,
            "order_today": 0,
            "qty_sale_orders": 0
        }

        today = datetime.today().date()
        start_of_day = Datetime.to_string(datetime.combine(today, time.min))
        end_of_day = Datetime.to_string(datetime.combine(today, time.max))

        so = self.env['sale.order']
        result['order_today'] = so.search_count(
            [('create_date', '>=', start_of_day), ('create_date', '<=', end_of_day)])
        result['total_customer'] = len(so.search([]).mapped('partner_id').ids)

        return result
