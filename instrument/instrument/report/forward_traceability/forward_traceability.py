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
					"label": "Mode",
					"fieldtype": "Select",
					"fieldname": "mode",
					"options": "In Work Order\nSubassembly Item\nFinish Good",
					"width": 150
				},
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
				}
			]
	return column


def get_data(filters):
	if not filters.get("batch"):
		data = []  
		return data 
	report_data = []
	batch = filters.get("batch")
	data = collect_data(batch)
	for i in data:
		if i.document_type == "Stock Entry":
			doc = frappe.get_doc(i.document_type, i.document_name)
			if doc.stock_entry_type == "Material Transfer for Manufacture":
				i["mode"] = "In Work Order"
				i["indent"] = 0
				report_data.append(i)

				wo_doc = frappe.get_doc("Work Order", doc.work_order)
				temp = {}
				temp["mode"] = "In Work Order"
				temp["document_type"] = "Work Order"
				temp["document_name"] = wo_doc.name
				temp["item_code"] = wo_doc.production_item
				temp["item_name"] = wo_doc.item_name
				temp["qty"] = wo_doc.qty
				temp["indent"] = 1
				report_data.append(temp)

				if wo_doc.so_reference:
					so_doc = frappe.get_doc("Sales Order", wo_doc.so_reference)
					item_code = None
					item_name = None
					qty = None
					for item in so_doc.items:
						item_code = item.item_code
						item_name = item.item_name
						qty = item.qty
					temp = {}
					temp["mode"] = "In Work Order"
					temp["document_type"] = "Sales Order"
					temp["document_name"] = so_doc.name
					temp["document_date"] = so_doc.transaction_date
					temp["party_name"] = so_doc.customer
					temp["item_code"] = item_code
					temp["item_name"] = item_name
					temp["qty"] = qty
					temp["indent"] = 2
					report_data.append(temp)


			else:
				pass
		if i.document_type == "Delivery Note":
			i["mode"] = "Finish Good"
			dn_doc = frappe.get_doc("Delivery Note", i.document_name)
			i["party_name"] = dn_doc.customer
			report_data.append(i)
	
	return report_data

def collect_data(batch):
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
		where tsabb.type_of_transaction = 'Outward' and tsabb.docstatus = 1 and tsabe.batch_no = '{0}'
		GROUP BY tsabb.name""".format(batch)
								
	data = frappe.db.sql(query, as_dict=1)
	return data