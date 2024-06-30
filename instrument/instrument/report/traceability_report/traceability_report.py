# Copyright (c) 2024, instrument and contributors
# For license information, please see license.txt

import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data

def execute(filters=None):
	columns = get_column()
	data = get_data(filters)
	return columns, data

def get_column():
	column = [
		{
			"label": "Sales Order Name",
			"fieldtype": "Link",
			"fieldname": "name",
			"options":"Sales Order",
			"width": 150
		},
		{
			"label": "Sales Order Date",
			"fieldtype": "Date",
			"fieldname": "s_date",
			# "options":"Sales Order",?
			"width": 150
		},
		{
			"label": "Customer Name",
			"fieldtype": "Link",
			"fieldname": "customer_name",
			"options":"Customer",
			"width": 150
		},
		{
			"label": "Sales Order Item",
			"fieldtype": "Link",
			"fieldname": "sales_order_item",
			"options":"Item",
			"width": 150
		},
		{
			"label": "Sales Order Item Qty",
			"fieldtype": "Link",
			"fieldname": "sales_order_item_qty",
			"options":"Item",
			"width": 150
		},
		{
			"label": "Production Plan",
			"fieldtype": "Data",
			"fieldname": "production_plan",
			# "options":"Sales Order",
			"width": 150
		},
		{
			"label": "Production Plan Date",
			"fieldtype": "Date",
			"fieldname": "p_date",
			# "options":"",
			"width": 150
		},
		{
			"label": "Material Request No",
			"fieldtype": "Data",
			"fieldname": "material_requesr_no",
			# "options":"",
			"width": 150
		},
		{
			"label": "Material Request Date",
			"fieldtype": "Date",
			"fieldname": "material_request_date",
			# "options":"",
			"width": 150
		},
		{
			"label": "Request For Quotation No",
			"fieldtype": "Data",
			"fieldname": "request_for_quotation_no",
			# "options":"",
			"width": 150
		},
		{
			"label": "Request For Quotation Date",
			"fieldtype": "Data",
			"fieldname": "request_for_quotation_date",
			# "options":"",
			"width": 150
		},
		{
			"label": "Purchase Order No",
			"fieldtype": "Data",
			"fieldname": "purchase_order_no",
			# "options":"",
			"width": 150
		},
		{
			"label": "Purchase Order Date",
			"fieldtype": "Date",
			"fieldname": "purchase_order_date",
			# "options":"",
			"width": 150
		},
		{
			"label": "Supplier Name",
			"fieldtype": "Data",
			"fieldname": "supplier_name",
			# "options":"",
			"width": 150
		},
		{
			"label": "Purchase Receipt No",
			"fieldtype": "Data",
			"fieldname": "purchase_r_no",
			# "options":"",
			"width": 150
		},
		{
			"label": "Purchase Receipt Date",
			"fieldtype": "Date",
			"fieldname": "purchase_r_date",
			# "options":"",
			"width": 150
		},
		{
			"label": "Purchase Receipt Batch No",
			"fieldtype": "Data",
			"fieldname": "purchase_r_b_no",
			# "options":"",
			"width": 150
		},
		{
			"label": "Work Order No",
			"fieldtype": "Data",
			"fieldname": "work_r_no",
			# "options":"",
			"width": 150
		},
		{
			"label": "Work Order Date",
			"fieldtype": "Data",
			"fieldname": "work_r_date",
			# "options":"",
			"width": 150
		},
		{
			"label": "Consolidated Pick List No (Material transfer for Manu)",
			"fieldtype": "Data",
			"fieldname": "consolidated_p_list_no",
			# "options":"",
			"width": 150
		},
		{
			"label": "Consolidated Pick List Date (Material transfer for Manu)",
			"fieldtype": "Data",
			"fieldname": "consolidated_p_list_date",
			# "options":"",
			"width": 150
		},
		{
			"label": "Stock Entry No (Material transfer for Manu)",
			"fieldtype": "Data",
			"fieldname": "stock_e_no",
			# "options":"",
			"width": 150
		},
		{
			"label": "Stock Entry Date (Material transfer for Manu)",
			"fieldtype": "Data",
			"fieldname": "stock_e_date",
			# "options":"",
			"width": 150
		},
		{
			"label": "Stock Entry Item (Material transfer for Manu)",
			"fieldtype": "Data",
			"fieldname": "stock_e_item",
			# "options":"",
			"width": 150
		},
		{
			"label": "Stock Entry Qty (Material transfer for Manu)",
			"fieldtype": "Data",
			"fieldname": "stock_e_qty",
			# "options":"",
			"width": 150
		},
		{
			"label": "Stock Entry Batch (Material transfer for Manu)",
			"fieldtype": "Data",
			"fieldname": "stock_e_batch",
			# "options":"",
			"width": 150
		},
		{
			"label": "Consolidated Pick List No ( Manufacture)",
			"fieldtype": "Data",
			"fieldname": "consolidated_p_list_no_manufecture",
			# "options":"",
			"width": 150
		},
		{
			"label": "Consolidated Pick List Date ( Manufacture)",
			"fieldtype": "Data",
			"fieldname": "consolidated_p_list_date_manufecture",
			# "options":"",
			"width": 150
		},
		{
			"label": "Stock Entry No ( Manufacture)",
			"fieldtype": "Data",
			"fieldname": "stock_e__no",
			# "options":"",
			"width": 150
		},
		{
			"label": "Stock Entry Date ( Manufacture)",
			"fieldtype": "Data",
			"fieldname": "stock_e_b_date",
			# "options":"",
			"width": 150
		},
		{
			"label": "Stock Entry Item ( Manufacture)",
			"fieldtype": "Data",
			"fieldname": "stock_e_b_item",
			# "options":"",
			"width": 150
		},
		{
			"label": "Stock Entry Qty ( Manufacture)",
			"fieldtype": "Data",
			"fieldname": "stock_e_b_qty",
			# "options":"",
			"width": 150
		},
		{
			"label": "Stock Entry Batch No ( Manufacture)",
			"fieldtype": "Data",
			"fieldname": "stock_e_b_no",
			# "options":"",
			"width": 150
		},
		{
			"label": "Delivery Note No",
			"fieldtype": "Data",
			"fieldname": "delivery_n_no",
			# "options":"",
			"width": 150
		},
		{
			"label": "Delivery Note Date",
			"fieldtype": "Data",
			"fieldname": "delivery_n_b_date",
			# "options":"",
			"width": 150
		},
		{
			"label": "Delivery Note Item",
			"fieldtype": "Data",
			"fieldname": "delivery_n_b_item",
			# "options":"",
			"width": 150
		},
		{
			"label": "Delivery Note Qty",
			"fieldtype": "Data",
			"fieldname": "delivery_n_b_qty",
			# "options":"",
			"width": 150
		},
		{
			"label": "Delivery Note Batch No",
			"fieldtype": "Data",
			"fieldname": "delivery_n_b_no",
			# "options":"",
			"width": 150
		},



		]
	return column
def get_data(filters):
	pending_data = []
	data = [
		"jjjjj",
		"jjjjj",
		"jjjjj",
		"jjjjj",
		"jjjjj",
		"jjjjj",
		"jjjjj",
		"1111",
		"1111",
		"1111",
		"1111",
		"1111",
		"1111",
		"1111",
		"1111",
		"1111",
		"1111",
		"2222",
		"2222",
		"2222",
		"2222",
		"2222",
		"2222",
		"2222",
		"2222",
		"2222",
		"3333",
		"3333",
		"3333",
		"3333",
		"3333",
		"3333",
		"3333",
		"3333",
		"3333",
		"3333",
		"3333",
		"3333",
	]
	pending_data.append(data)
	return pending_data