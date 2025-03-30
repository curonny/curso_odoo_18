from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    not_allowed_products_ids = fields.Many2many(
        "product.product", string="Not Allowed Products"
    )
