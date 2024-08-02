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
			fieldname: "item_name",
			label: __("Item Name"),
			fieldtype: "Date"
		},
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
		},
		{
			fieldname: "doctype_name",
			label: __("Document Name"),
			fieldtype: "Dynamic Link",
			options: "doctype",
		},

	]

};
