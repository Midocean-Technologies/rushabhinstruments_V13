// Copyright (c) 2024, instrument and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Traceability Report"] = {
    "filters": [
        {
            fieldname: "item_code",
            label: __("Item Code"),
            fieldtype: "Link",
            options: "Item",
        },
        {
            fieldname: "batch",
            label: __("Batch"),
            fieldtype: "Link",
            options: "Batch",
        },
        {
            fieldname: "doctype",
            label: __("Document Type"),
            fieldtype: "Link",
            options: "DocType",
        },
        {
            fieldname: "doctype_name",
            label: __("Document Name"),
            fieldtype: "Dynamic Link",
            options: "doctype",
        },

    ]
};
