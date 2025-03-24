from odoo import _, api, fields, models


class Estate(models.Model):
    _name = "estate.estate"
    _inherit = ["mail.thread"]
    _description = "Real estate"
    _rec_name = "name"

    name = fields.Char(required=True, tracking=True)
    company_id = fields.Many2one(
        comodel_name="res.company", default=lambda self: self.env.company
    )
    for_sale = fields.Boolean(compute="_compute_for_sale", store=True)
    currency_id = fields.Many2one("res.currency", tracking=True)
    state = fields.Selection(
        [("new", "New"), ("offer_received", "Offer Received"), ("sold", "Sold")],
        default="new",
    )
    price = fields.Float(default=0.0, tracking=True)
    country_id = fields.Many2one("res.country")
    room_quantity = fields.Integer(
        default=1,
    )
    image = fields.Binary(attachment=True)
    description = fields.Html()
    date_availability = fields.Date()
    owners_ids = fields.Many2many("res.partner")
    estate_category_id = fields.Many2one("estate.category")

    @api.depends("state")
    def _compute_for_sale(self):
        for estate in self:
            estate.for_sale = (
                True if estate.state in ["new", "offer_received"] else False
            )

    @api.constrains("price")
    def _check_price(self):
        for estate in self:
            if estate.price <= 0:
                raise models.ValidationError(
                    _("Price cannot be negative and greater than zero")
                )

    @api.constrains("estate_category_id")
    def _check_estate_category_id(self):
        for estate in self:
            if (
                estate.estate_category_id.id
                == self.env.ref("estate.category_mansion").id
            ):
                if estate.room_quantity < 3:
                    raise models.ValidationError(
                        _("Mansion must have at least 3 rooms")
                    )

    def create(self, values):
        res = super().create(values)
        return res

    def write(self, values):
        res = super().write(values)
        return res

    def unlink(self):
        for estate in self:
            if estate.state == "sold":
                raise models.ValidationError(_("Cannot delete an estate that is sold"))
        return super().unlink()
