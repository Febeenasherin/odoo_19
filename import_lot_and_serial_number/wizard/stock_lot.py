from odoo import models, fields,_
import openpyxl
import base64
from io import BytesIO
from odoo.exceptions import UserError


class ImportCustomerWizard(models.TransientModel):
   _name = "import.customer.wizard"

   file = fields.Binary(string="File", required=True)


   def import_excel(self):
      print("valid")


      wb = openpyxl.load_workbook(
      filename=BytesIO(base64.b64decode(self.file)), read_only=True
      )

      ws = wb.active

      for record in ws.iter_rows(min_row=2, max_row=None, min_col=None,
                              max_col=None, values_only=True):
         print(record,"record")
         number = record[0]
         print("number",number)
         product = record[1]
         print("product:",product)


         search = self.env['stock.lot'].search([
            ('name', '=', record[0])])
         print(search,"search")

         products = self.env['product.product'].search([('name', 'like', product), ('is_storable', '=', True)],limit=1)
         print("product",products)

         if not products:
            raise UserError(_('product not found'))

         if not search:
            print("hii")
            serl = self.env['stock.lot'].create({
            'name': record[0],
            'product_id': products.id,
            'company_id': self.env.company.id,

            })
            print(serl,"ee")




            return  {
               'type': 'ir.actions.client',
               'tag': 'display_notification',
               'params': {
                  'title': 'Message!',
                  'message': f'Lot/Serial Number Created successfully .',
                  'type': 'success',
                  'sticky': False,
               }
         }





      # except:
      #    print("hii")
      #    raise UserError(
      #       _('Please insert a valid file'))