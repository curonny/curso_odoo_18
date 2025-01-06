from odoo import fields, models


class Estate(models.Model):
    _name = "estate.estate"
    _description = "Real estate"
    _rec_name = "name"

    name = fields.Char(required=True)
    company_id = fields.Many2one(
        comodel_name="res.company", default=lambda self: self.env.company
    )
    for_sale = fields.Boolean()
    currency_id = fields.Many2one("res.currency")
    state = fields.Selection(
        [("new", "New"), ("offer_received", "Offer Received"), ("sold", "Sold")],
        default="new",
    )
    price = fields.Float(default=0.0)
    country_id = fields.Many2one("res.country")
    room_quantity = fields.Integer(
        default=1,
    )
    image = fields.Binary(attachment=True)
    description = fields.Html()
    date_availability = fields.Date()
    owners_ids = fields.Many2many("res.partner")
