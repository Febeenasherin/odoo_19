/** @odoo-module **/
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component, onWillStart } from  "@odoo/owl";



// const actionRegistry = registry.category("actions");
class Expirydashboard extends Component {
    setup() {
        super.setup();
        this.orm = useService('orm');
        this.action = useService("action");
        this.data = {};


        onWillStart(async () => {
            this.data = await this.orm.call("stock.expiry", "stock_expiration", [], {});


        })
    }

    openexpired() {
        this.action.doAction({
            name: 'lot expiry',
            type: "ir.actions.act_window",
            res_model: 'stock.lot',
            views: [
                [false, "list"],
                [false, "form"],
            ],
            // domain: [["id", "in", ids]],
            // context: context,
        });
    }
}
// }
Expirydashboard.template = "stock_expiry.Dashboard";
registry.category('actions').add('stock_expiry',Expirydashboard);
// registry.category("views").add("stock_dashboard_kanban", Expirydashboard);