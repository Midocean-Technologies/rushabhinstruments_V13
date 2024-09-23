// Copyright (c) 2024, instrument and contributors
// For license information, please see license.txt

frappe.query_reports["Backward Traceability"] = {
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
			get_query: function () {
				var item_code = frappe.query_report.get_filter_value("item_code");
				return {
					filters: {
						item: item_code,
					},
				};
			},
		}
	]
};
