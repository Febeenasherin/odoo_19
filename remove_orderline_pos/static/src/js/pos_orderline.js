/** @odoo-module */


import { Numpad } from "@point_of_sale/app/components/numpad/numpad";
import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { Orderline } from "@point_of_sale/app/components/orderline/orderline";


// patch(Numpad.prototype, {
//
//
// })
//

console.log("ooodooo")
patch(ProductScreen.prototype, {

    setup() {
        super.setup(...arguments);
         console.log("setup")
   },

   async onButtonClick(){
      console.log("hii")
      const currentOrder = this.pos.getOrder();
      console.log("orders", currentOrder)
      const orderline  = currentOrder.getOrderlines
      console.log("lines",orderline)
       for (const orderline of currentOrder.getOrderlines()) {
           const product = orderline.getProduct();
           console.log("products", product)
           currentOrder.removeOrderline(orderline)


       }
   },
});



patch(Orderline.prototype, {

    setup() {
        super.setup(...arguments);
        console.log("setup")
    },
    async onremove() {
        console.log("click")
        const currentOrder = this.pos.getOrder();
      console.log("orders", currentOrder)


    }
})












