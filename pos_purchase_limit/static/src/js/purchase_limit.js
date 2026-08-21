/** @odoo-module */

import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/services/pos_store";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { useService } from "@web/core/utils/hooks";
import { _t } from "@web/core/l10n/translation";



patch(PosStore.prototype, {
    async pay() {
        const currentOrder = this.getOrder();
        console.log("orders", currentOrder)
        const customer = currentOrder.getPartner()
        console.log("partner", customer)


        if (!customer) {
            this.env.services.dialog.add(AlertDialog, {
                title: _t("Alert"),
                body: _t("Select a Customer"),
            });
        } else {
            await super.pay();
        }
    },


})

patch(PaymentScreen.prototype, {
    async validateOrder() {
        const orders = this.pos.getOrder()
        console.log("customer",orders)
        const cust = orders.partner_id;
        console.log("order", cust.name)

        const active = cust.is_purchase_limit
        console.log("active",active)

        const limit = cust.purchase_limit
        console.log("value:",limit)


        const price = orders.currencyDisplayPrice
        console.log("price",price)

        const total = orders.displayPrice
        console.log("total",total)



        if (active === true) {
            console.log("yyyy")
            if (limit < total) {
                console.log("price not")
                this.env.services.dialog.add(AlertDialog, {
                title: _t("Alert"),
                body: _t("Customer Only can purchase $%s ", limit ,),
            });
        }
            else {
            await super.validateOrder();
        }
            }


        }


})





