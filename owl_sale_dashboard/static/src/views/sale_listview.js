/** @odoo-module **/

import {registry} from "@web/core/registry";
import {listView} from "@web/views/list/list_view";
import {SaleListRenderer} from "@sale/views/sale_onboarding_list/sale_onboarding_list_renderer";
import {SaleDashBoard} from "@owl_sale_dashboard/views/sale_dashboard";

export class ListDashBoardRenderer extends SaleListRenderer {
    static template = "owl_sale_dashboard.SaleListView";
    static components = Object.assign({}, SaleListRenderer.components, {SaleDashBoard});
}

export const SaleDashBoardListView = {
    ...listView,
    Renderer: ListDashBoardRenderer,
};

registry.category("views").add("sale_dashboard_list", SaleDashBoardListView);
