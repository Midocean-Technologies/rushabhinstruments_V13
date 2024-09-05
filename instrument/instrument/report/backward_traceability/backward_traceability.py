# Copyright (c) 2024, instrument and contributors
# For license information, please see license.txt

# import frappe


def execute(filters=None):
	columns = get_column()
	data = get_data(filters)
	return columns, data


def get_column():
	column = [
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
					"label": "Party Name",
					"fieldtype": "Data",
					"fieldname": "party_name",
					"width": 140
				}
			]
	return column


def get_data(filters):
	data = []
	return data