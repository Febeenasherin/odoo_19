/** @odoo-module */
import { renderToElement } from "@web/core/utils/render";
import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";
publicWidget.registry.get_events = publicWidget.Widget.extend({
   selector : '.latest_event_section',
   async willStart() {
       console.log("events")
       const result = await rpc('/get_events', {});
       if(result){
           this.$().html(renderToElement('school_management.latest_event', {result: result}))
       }
   },
});

// /** @odoo-module */
// import PublicWidget from "@web/legacy/js/public/public_widget";
// import { jsonrpc } from "@web/core/network/rpc_service";
// var TestController = PublicWidget.Widget.extend({
//    willStart: async function () {
//            const data = await jsonrpc('/get_events', {})
//        },
// });

























// /** @odoo-module */
// import { renderToElement } from "@web/core/utils/render";
// import publicWidget from "@web/legacy/js/public/public_widget";
// import { rpc } from "@web/core/network/rpc";
//
// publicWidget.registry.get_latest_event = publicWidget.Widget.extend({
//     selector : '.latest_event_section',
//
//     async willStart() {
//     console.log("ijijijij")
//
//     const events = await rpc('/get_events', {});
//             },
//
//
//
//        if(res){
//            this.$target.$('.latest_event_container').html(renderToElement('school_management.latest_event', {result: events}))
//        }
//    },
// });

//     start()
//        {this.$('.latest_event_container').html(renderToElement('school_management.latest_event',
//                    {
//                        events: this.events
//                    }
//                )
//            );
//            return this._super(...arguments)
//        }
//    });



// /** @odoo-module */
// import PublicWidget from "@web/legacy/js/public/public_widget";
// import { jsonrpc } from "@web/core/network/rpc_service";
// var TestController = PublicWidget.Widget.extend({
//      selector : '.latest_event_section',
//    willStart: async function () {
//            const data = await jsonrpc('/get_events', {})
//        },
//     if(data){
//         this.$target.$('.latest_event_container').html('school_management.latest_event', {result: data})
//     }
// });




//        if(res){
//            this.$target.$('.latest_event_container').html(renderToElement('school_management.latest_event', {result: res}))
//        }
//    },
// });


    // start(){
    //     this.$('.latest_event_container').html(renderToElement('school_management.latest_event' , {events:this.events,}))
    // }


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
