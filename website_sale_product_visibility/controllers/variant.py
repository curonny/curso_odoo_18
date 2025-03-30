from odoo import http
from odoo.addons.website_sale.controllers.variant import WebsiteSaleVariantController
from odoo.http import request


class WebsiteSaleVariantController(WebsiteSaleVariantController):

    def get_combination_info_website(self, product_template_id, product_id, combination, add_qty,
                                     parent_combination=None, **kwargs):
        res = super(WebsiteSaleVariantController, self).get_combination_info_website(product_template_id, product_id,
                                                                                     combination, add_qty,
                                                                                     parent_combination, **kwargs)

        if res['product_id'] in request.env.user.partner_id.not_allowed_products_ids.ids:
            res['is_combination_possible'] = False

        return res
