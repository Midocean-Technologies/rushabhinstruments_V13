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

	]
};
