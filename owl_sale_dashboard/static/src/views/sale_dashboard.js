/** @odoo-module */
import {useService} from '@web/core/utils/hooks';
import {Component,onWillStart} from "@odoo/owl";

export class SaleDashBoard extends Component {
    static template = "owl_sale_dashboard.SaleDashboard";
    static props = {};

    setup() {
        this.orm = useService("orm");
        this.action = useService("action");

        onWillStart(async () => {
            this.saleData = await this.orm.call("sale.order", "retrieve_dashboard");
        });
    }
}
