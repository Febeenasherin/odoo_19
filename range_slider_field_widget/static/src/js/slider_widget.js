/** @odoo-module **/
import { Component } from "@odoo/owl";
import { useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
export class RangeSliderField extends Component {
    static template = 'FieldRangeSlider';

    setup() {
        const {min, max} = this.__owl__.parent.props.fieldInfo.attrs
        this.state = useState({
            value: this.props.record.data[this.props.name],
            min: min,
            max: max,
        });
    }

    getValue(e) {
        const config = this.env.model.config
        console.log("config",config)
        this.state.value = e.srcElement.value

        const model = this.env.model.orm
        console.log("model", model)

        const value = e.srcElement.value
        console.log("value", value)

        this.env.model.orm.write(config.resModel,
                              [config.isRoot], {
                              [this.props.name]: this.state.value,
      });

        // for (const values of config.resModel){
        //     this.env.model.orm.write(
        //     [config.resId], {
        //         [this.props.name]: this.state.value,
        //     });
        // }

    }

}
     // return this.props.record.data[value];
      // this.env.model.orm.write(config.resModel


     //  }
     // update(value)   {
     //     this.props.record.update(value)
     // }

//
// async createRecord(value) {
//     console.log("djd",value)}
// }
export const rangeSliderField = {
  component: RangeSliderField,
  displayName: "RangeSliderField",
  supportedTypes: ["integer"],
};
registry.category("fields").add("RangeSliderField", rangeSliderField);

// /** @odoo-module **/
// import { Component } from "@odoo/owl";
// import { useState } from "@odoo/owl";
// import { registry } from "@web/core/registry";
// export class RangeSliderField extends Component {
//   static template = 'FieldRangeSlider';
//   setup(){
//        const {min,max} = this.__owl__.parent.props.fieldInfo.attrs
//       console.log("min",min)
//       console.log("max",max)
//        this.state = useState({
//            value : this.props.record.data[this.props.name],
//            min : min,
//            max : max,
//        });
//   }
//   getValue(e) {
//       const config = this.env.model.config
//       console.log("config", config)
//       this.state.value = e.srcElement.value
//       console.log(this.state.value, "value")
//       // this.env.model.orm.write(
//
//       const model =this.env.model.orm
//       console.log("model",model)
//
//       const value = e.srcElement.value
//       console.log("value",value)
//
//
//       this.env.model.orm.write(config.resModel,
//                               [config.resId], {
//                               [this.props.name]: this.state.value,
//       });
//
//
//
//
//   }
//   async createRecord() {
//       const store = this.store
//       console.log("store",store)
//       return this.store
//       const name = this.props.name
//       console.log("name",name)
//
//     }
//
//
// }
//
// export const rangeSliderField = {
//    component: RangeSliderField,
//    displayName: "RangeSliderField",
//    supportedTypes: ["int"],
// };
// registry.category("fields").add("RangeSliderField", rangeSliderField);



