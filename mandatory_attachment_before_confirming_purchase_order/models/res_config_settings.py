# -*- coding: utf-8 -*-
from odoo import fields, models, api



class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    attachment = fields.Boolean(string="Attachment",
        config_parameter='mandatory_attachment_before_confirming_purchase_order.attachment'
    )