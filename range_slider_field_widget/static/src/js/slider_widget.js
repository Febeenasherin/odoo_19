/** @odoo-module **/
import { Component } from "@odoo/owl";
import { useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
export class RangeSliderField extends Component {
    static template = 'FieldRangeSlider';

    setup() {
        const {min, max} = this.__owl__.parent.props.fieldInfo.attrs
        console.log("min value",min)
        console.log("max value",max)

        const sta = this.state
        console.log("state",sta)

        const par =  this.__owl__.parent.props
        console.log("owl",par)
        this.state = useState({
            value: this.props.record.data[this.props.name],
            min: min || 0,
            max: max || 100,
        });
    }

    getValue(e) {
        // const config = this.env.model.config
        // console.log("config",config)

        const values = Number(e.target.value)
        console.log("value",values)
        // this.state.value = e.srcElement.value

        this.state.value = values
        console.log("v1",this.state.value = values)
        const name = this.props.name
        console.log("model",name)
        const model = this.env.model.orm
        console.log("model", model)

        const value = e.srcElement.value
        console.log("value", value)

        this.props.record.update({
            [this.props.name]: values
        });


        // for (const values of config.resModel){
        //     this.env.model.orm.write(
        //     [config.resId], {
        //         [this.props.name]: this.state.value,
        //     });
        // }

    }

}


     //  }
     // update(value)   {
     //     this.props.record.update(value)
     // }


export const rangeSliderField = {
  component: RangeSliderField,
  displayName: "RangeSliderField",
  supportedTypes: ["integer"],
};
registry.category("fields").add("RangeSliderField", rangeSliderField);




