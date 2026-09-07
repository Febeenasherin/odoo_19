 /** @odoo-module **/
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component, useState} from "@odoo/owl";
import {Dropdown} from '@web/core/dropdown/dropdown';
import {DropdownItem} from '@web/core/dropdown/dropdown_item';

class SystrayDropdown extends Component {
   setup() {
       // this.action = useService("action");
       this.orm = useService("orm");
       this.state = useState({
           temp : "",
           weather : "",
           lat : "",
           lon : "",
           location : "",
           time : "",
           icon : "",

       });
   }
    async shownotification(){
       navigator.geolocation.getCurrentPosition(
           async(position) => {
               const longitude = position.coords.longitude
               console.log("logitude",longitude)
               const latitude = position.coords.latitude



               const result = await this.orm.call("weather.notification", "get_weather", [latitude, longitude]);
               console.log("result",result)
               console.log("cdc",result.temp)
               this.state.day = result.date
                console.log("date",this.state.day)
               this.state.weather = result.weather
               console.log("weather",result.weather)
               this.state.icon = result.icon
               // this.state.png = ("http://openweathermap.org/img/wn/" + this.state.icon + "@2x.png")

               this.state.name = result.location
               this.state.temp = result.temp

           }
       )
    }

}
   SystrayDropdown.template = "systray_dropdown";
   SystrayDropdown.components = {Dropdown, DropdownItem};
   export const systrayItem = { Component: SystrayDropdown,};
   registry.category("systray").add("SystrayDropdown", systrayItem, { sequence: 1 });
