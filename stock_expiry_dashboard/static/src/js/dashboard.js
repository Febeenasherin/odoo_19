/** @odoo-module **/
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component } from  "@odoo/owl";
const actionRegistry = registry.category("actions");
class CrmDashboard extends Component {
  setup() {
        super.setup();
        this.orm = useService('orm');
        this._fetch_data();
  }
  async _fetch_data(){
     let result = await this.orm.call("stock.expiry", "stock_expiration", [], {});
     document.getElementById('count_expiry').innerHTML = `<span>${result.total_count}</span>`;

  }
}
CrmDashboard.template = "my_module.CrmDashboard";
actionRegistry.add("crm_dashboard_tag", CrmDashboard);