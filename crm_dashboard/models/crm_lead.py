# -*- coding: utf-8 -*-
from odoo import models, api


class CrmLead(models.Model):
   _inherit = 'crm.lead'

   @api.model
   def get_tiles_data(self):
      company_id = self.env.company
      leads = self.search([('company_id', '=', company_id.id),
                           ('user_id', '=', self.env.user.id)])
      my_leads = leads.filtered(lambda r: r.type == 'lead')
      my_opportunity = leads.filtered(lambda r: r.type == 'opportunity')
      currency = company_id.currency_id.symbol
      expected_revenue = sum(my_opportunity.mapped('expected_revenue'))

      total_invoice = leads.user_id.total_invoiced
      print(total_invoice,"invoiced")

      lost = self.search([("won_status", "=", "lost"), ("active", "=", False), ('user_id', '=', self.env.user.id)])
      print(lost,"lost")

      won = leads.search([('stage_id.is_won', '=', True), ('user_id', '=', self.env.user.id)])
      print(won,"won")



      return {

         'total_leads': len(my_leads),
         'total_opportunity': len(my_opportunity),
         'expected_revenue': expected_revenue,
         'currency': currency,
         'total_invoice': (total_invoice),

      }

