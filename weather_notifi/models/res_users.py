from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    recently_viewed_ids = fields.One2many(
        "ir.recent.record",
        "user_id",
        string="Recently Viewed History",
        readonly=True,
    )
