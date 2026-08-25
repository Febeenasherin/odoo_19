/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { Orderline } from "@point_of_sale/app/components/orderline/orderline";


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
    async onClear() {
        console.log("click")

        // const order = this.pos.getOrder();
        // console.log(order)

        const line = this.props.line
        console.log("line",line)

        const order = line.order_id
        console.log("l",order)

        order.removeOrderline(line)
    }
})












