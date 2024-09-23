// Copyright (c) 2024, instrument and contributors
// For license information, please see license.txt

frappe.query_reports["Traceability Test"] = {
	"filters": [
		{
			fieldname: "item_code",
			label: __("Item Code"),
			fieldtype: "Link",
			options: "Item",
		},
		// {
		// 	fieldname: "item_name",
		// 	label: __("Item Name"),
		// 	fieldtype: "Date"
		// },
		{
			fieldname: "batch",
			label: __("Batch"),
			fieldtype: "Link",
			options: "Batch",
		},
		{
			fieldname: "customer",
			label: __("Customer"),
			fieldtype: "Link",
			options: "Customer",
		},
		{
			fieldname: "supplier",
			label: __("Supplier"),
			fieldtype: "Link",
			options: "Supplier",
		},
		{
			fieldname: "doctype",
			label: __("Document Type"),
			fieldtype: "Link",
			options: "DocType",
			get_query: function () {
				return {
					filters: { name: ["in", ["Sales Order", "Purchase Order", "Material Request", "Stock Entry"]] },
				};
			},
		},
		{
			fieldname: "doctype_name",
			label: __("Document Name"),
			fieldtype: "Dynamic Link",
			options: "doctype",
		},

	]
};
