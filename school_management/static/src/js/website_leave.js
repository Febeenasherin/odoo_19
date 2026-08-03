/** @odoo-module */
import { renderToElement } from "@web/core/utils/render";
import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";
publicWidget.registry.get_latest_event = publicWidget.Widget.extend({
   selector : '.latest_event_section',

   async willStart() {
       // console.log("ijijijij")
        const res = await rpc('/get_events', {});
       if(res){
           this.$target.empty().html(renderToElement('school_management.latest_event', {result: res}))
       }
   },
});


// /** @odoo-module */
// import publicWidget from '@web/legacy/js/public/public_widget';
// import { jsonrpc } from "@web/core/network/rpc_service";
// import { renderToElement } from "@web/core/utils/render";
// let DynamicSnippets = publicWidget.Widget.extend({
//    selector: '.latest_event_section',
//    start: function(){
//        jsonrpc('/get_events', {}).then((res)=>{
//            if (res){
//                this.$el.find("#total").html(renderToElement('school_management.latest_event', {res: res}))
//            }
//        })
//    }
// });
// publicWidget.registry.DynamicSnippets = DynamicSnippets;
