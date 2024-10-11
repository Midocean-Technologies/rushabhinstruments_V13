# Copyright (c) 2024, instrument and contributors
# For license information, please see license.txt


import frappe


def execute(filters=None):
	columns = get_column()
	data = get_data(filters)
	return columns, data


def get_column():
	column = [
				
				{
					"label": "Document Type",
					"fieldtype": "Data",
					"fieldname": "document_type",
					"width": 150
				},
				{
					"label": "Document Name",
					"fieldtype": "Data",
					"fieldname": "document_name",
					"width": 140
				},
				{
					"label": "Document Date",
					"fieldtype": "Date",
					"fieldname": "document_date",
					"width": 140
				},
				{
					"label": "Party Name",
					"fieldtype": "Data",
					"fieldname": "party_name",
					"width": 140
				},
				{
					"label": "Item Code",
					"fieldtype": "Link",
					"fieldname": "item_code",
					"options": "Item",
					"width": 170
				},
				{
					"label": "Item Name",
					"fieldtype": "Data",
					"fieldname": "item_name",
					"width": 170
				},
				{
					"label": "Qty",
					"fieldtype": "Float",
					"fieldname": "qty",
					"width": 140
				},
				{
					"label": "Warehouse",
					"fieldtype": "Link",
					"fieldname": "warehouse",
					"options": "Warehouse",
					"width": 140
				},
				{
					"label": "Batch",
					"fieldtype": "Link",
					"fieldname": "batch",
					"options": "Batch",
					"width": 170
				},
				{
					"label": "Serial and Batch Bundle",
					"fieldtype": "Link",
					"fieldname": "serial_and_batch_bundle",
					"options": "Serial and Batch Bundle",
					"width": 170
				},
				{
					"label": "Mode",
					"fieldtype": "Select",
					"fieldname": "mode",
					"options": "In Work Order\nSubassembly Item\nFinish Good",
					"width": 150
				},
			]
	return column


def get_data(filters):
	if not filters.get("batch"):
		data = []  
		return data 
	report_data = []
	batch = filters.get("batch")
	data = collect_data(batch, filters)
	for i in data:
		if i.document_type == "Stock Entry":
			serial_batches = get_stock_entry_data(i.document_name)
			for sb_rec in serial_batches:
				report_data.append(sb_rec)
			# doc = frappe.get_doc(i.document_type, i.document_name)
			# if doc.stock_entry_type == "Material Transfer for Manufacture":
			# 	i["mode"] = "In Work Order"
			# 	i["indent"] = 0
			# 	report_data.append(i)

			# 	wo_doc = frappe.get_doc("Work Order", doc.work_order)
			# 	temp = {}
			# 	temp["mode"] = "In Work Order"
			# 	temp["document_type"] = "Work Order"
			# 	temp["document_name"] = wo_doc.name
			# 	temp["item_code"] = wo_doc.production_item
			# 	temp["item_name"] = wo_doc.item_name
			# 	temp["qty"] = wo_doc.qty
			# 	temp["indent"] = 1
			# 	report_data.append(temp)

			# 	if wo_doc.so_reference:
			# 		so_doc = frappe.get_doc("Sales Order", wo_doc.so_reference)
			# 		item_code = None
			# 		item_name = None
			# 		qty = None
			# 		for item in so_doc.items:
			# 			item_code = item.item_code
			# 			item_name = item.item_name
			# 			qty = item.qty
			# 		temp = {}
			# 		temp["mode"] = "In Work Order"
			# 		temp["document_type"] = "Sales Order"
			# 		temp["document_name"] = so_doc.name
			# 		temp["document_date"] = so_doc.transaction_date
			# 		temp["party_name"] = so_doc.customer
			# 		temp["item_code"] = item_code
			# 		temp["item_name"] = item_name
			# 		temp["qty"] = qty
			# 		temp["indent"] = 2
			# 		report_data.append(temp)


			# else:
			# 	pass
		if i.document_type == "Delivery Note":
			i["mode"] = "Finish Good"
			dn_doc = frappe.get_doc("Delivery Note", i.document_name)
			i["party_name"] = dn_doc.customer
			report_data.append(i)
	
	return report_data

def collect_data(batch, filters=None):
	cond = ""
	if filters:
		if filters.get("from_date") and filters.get("to_date"):
			cond += "AND tsabb.posting_date between {0} and {1}".format(filters.get("from_date") ,filters.get("to_date"))
	query = """
		SELECT 
			tsabb.name as serial_and_batch_bundle,
			tsabb.warehouse as warehouse,
			tsabe.batch_no as batch,
			abs(sum(tsabe.qty)) as qty,
			tsabb.item_code as item_code,
			tsabb.item_name,
			tsabb.warehouse,
			tsabb.posting_date as document_date,
			tsabb.voucher_type as document_type,
			tsabb.voucher_no as document_name
		FROM `tabSerial and Batch Bundle` tsabb 
		left join `tabSerial and Batch Entry` tsabe on tsabe.parent = tsabb.name
		where tsabb.type_of_transaction = 'Outward' and tsabb.docstatus = 1 and tsabe.batch_no = '{0}' {1}
		GROUP BY tsabb.name""".format(batch, cond)
								
	data = frappe.db.sql(query, as_dict=1)
	return data


def get_stock_entry_data(document_name):
	report_data = []
	se_doc = frappe.get_doc("Stock Entry", document_name)
	sb_list = []
	for k in se_doc.items:
		if k.t_warehouse:
			temp3 = {
				"batch": "",
				"serial_and_batch_bundle": k.serial_and_batch_bundle,
				"document_type": "",
				"document_name": "",
				"item_code": k.item_code,
				"item_name": k.item_name,
				"party_name": "",
				"indent" : 1
			}
			sb_list.append(k.serial_and_batch_bundle)
			report_data.append(temp3)
	if se_doc.stock_entry_type in ["Manufacture", "Material Consumption for Manufacture"]:
		se_list = frappe.get_all("Stock Entry", filters={"stock_entry_type":["in", ["Manufacture", "Material Consumption for Manufacture"]], "work_order": se_doc.work_order})
		for k in se_list:
			se_doc1 = frappe.get_doc("Stock Entry", k.name)
			for kk in se_doc1.items:
				if kk.t_warehouse:
					mt_sub_list = get_sub_entries(kk.serial_and_batch_bundle)
					for xx in mt_sub_list:
						report_data.append(xx)

	return report_data

def get_sub_entries(sb_rec, filters=None):
	report_data = []
	sb_doc = frappe.get_doc("Serial and Batch Bundle", sb_rec)
	batch_list = []
	for sb_doc_item in sb_doc.entries:
		if sb_doc_item.batch_no not in batch_list:
			batch_list.append(sb_doc_item.batch_no)
	for bench_rec in batch_list:
		x_data = collect_data(bench_rec)
		for ii in x_data:
			if ii.document_type == "Stock Entry":
				stock_entry_type = frappe.get_value("Stock Entry", ii.document_name, "stock_entry_type")
				if stock_entry_type in ["Manufacture", "Material Consumption for Manufacture"]:
					data = get_stock_entry_data(ii.document_name)
					for y in data:
						report_data.append(y)

			temp3 = {
				"batch": bench_rec,
				"serial_and_batch_bundle": ii.serial_and_batch_bundle,
				"document_type": ii.document_type,
				"document_name":  ii.document_name,
				"item_code": ii.item_code,
				"item_name": ii.item_name,
				"party_name": "",
				"indent" : 1
			}
			report_data.append(temp3)
	return report_data