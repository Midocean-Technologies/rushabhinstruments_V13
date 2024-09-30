# Copyright (c) 2024, instrument and contributors
# For license information, please see license.txt

from erpnext.crm import report
from erpnext.manufacturing.doctype import bom_update_batch
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
					"label": "Serial and Batch Bundle",
					"fieldtype": "Link",
					"fieldname": "serial_and_batch_bundle",
					"options": "Serial and Batch Bundle",
					"width": 170
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
					"label": "Batch",
					"fieldtype": "Link",
					"fieldname": "batch",
					"options": "Batch",
					"width": 170
				},
				
				{
					"label": "Party Name",
					"fieldtype": "Data",
					"fieldname": "party_name",
					"width": 140
				}
			]
	return column


def get_data(filters):
	# return []
	report_data = []
	print(filters)
	batch = filters.get("batch")
	data = collect_data(batch, filters)
	print(data)
	temp = {
				"batch": batch,
				"serial_and_batch_bundle": "",
				"document_type": "Batch",
				"document_name": batch,
				"item_code": frappe.get_value("Batch", batch, "item"),
				"item_name": frappe.get_value("Batch", batch, "item_name"),
				"party_name": "",
				"indent" : 1
			}
	report_data.append(temp)
	
	for i in data:
		

		temp1 = {
				"batch": i.batch,
				"serial_and_batch_bundle": i.serial_and_batch_bundle,
				"document_type": "Serial and Batch Bundle",
				"document_name": i.serial_and_batch_bundle,
				"item_code": frappe.get_value("Batch", i.batch, "item"),
				"item_name": frappe.get_value("Batch", i.batch, "item_name"),
				"party_name": "",
				"indent" : 2
			}
		report_data.append(temp1)

		if i.document_type == "Stock Entry":
			se_doc = frappe.get_doc("Stock Entry", i.document_name)
			if se_doc.work_order:
				wo_doc = frappe.get_doc("Work Order", se_doc.work_order)
				temp2 = {
					"batch": "",
					"serial_and_batch_bundle": "",
					"document_type": "Work Order",
					"document_name": wo_doc.name,
					"item_code": wo_doc.production_item,
					"item_name": wo_doc.item_name,
					"party_name": "",
					"indent" : 3
				}
				report_data.append(temp2)

				se_list = frappe.get_all("Stock Entry", filters={"stock_entry_type":"Material Transfer for Manufacture", "work_order": wo_doc.name})
				for k in se_list:
					se_doc1 = frappe.get_doc("Stock Entry", k.name)
					for kk in se_doc1.items:
						pr_data = collect_pr_data(kk.batch_no)
						for l in pr_data:
							pr_doc = frappe.get_doc("Purchase Receipt", l.document_name)
							temp2 = {
								"batch": l.batch,
								"serial_and_batch_bundle": l.serial_and_batch_bundle,
								"document_type": "Purchase Receipt",
								"document_name": pr_doc.name,
								"item_code": l.item_code,
								"item_name": l.item_name,
								"party_name": pr_doc.supplier,
								"indent" : 4
							}
							report_data.append(temp2)
		if i.document_type == "Purchase Receipt":
			pr_doc = frappe.get_doc("Purchase Receipt", i.document_name)
			temp2 = {
				"batch": "",
				"serial_and_batch_bundle": "",
				"document_type": "Purchase Receipt",
				"document_name": pr_doc.name,
				"item_code": i.item_code,
				"item_name": i.item_name,
				"party_name": pr_doc.supplier,
				"indent" : 3
			}
			report_data.append(temp2)
	return report_data

def collect_data(batch, filters=None):
	cond = ""
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
		where tsabb.type_of_transaction = 'Inward' and tsabb.docstatus = 1 and tsabe.batch_no = '{0}' {1}
		GROUP BY tsabb.name""".format(batch, cond)
	print(query)					
	data = frappe.db.sql(query, as_dict=1)
	print(data)
	return data

def collect_pr_data(batch):
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
		where tsabb.type_of_transaction = 'Inward' and tsabb.docstatus = 1 and tsabe.batch_no = '{0}' and tsabb.voucher_type = 'Purchase Receipt'
		GROUP BY tsabb.name""".format(batch)
								
	data = frappe.db.sql(query, as_dict=1)

	print(data)
	return data