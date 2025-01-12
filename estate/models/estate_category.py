from odoo import fields, models


class EstateCategory(models.Model):
    _name = "estate.category"
    _description = "Real estate category"
    _rec_name = "name"

    name = fields.Char(required=True)
