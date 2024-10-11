# Copyright (c) 2024, instrument and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class SupplierQuotationComparisonTool(Document):

	@frappe.whitelist()
	def demo(self, items):
		print(items)

	@frappe.whitelist()
	def get_data(self):
		cond = "1 = 1"
		if self.supplier:
			cond += " and tsq.supplier = '{0}'".format(self.supplier)

		if self.item_code:
			cond += " and tsqi.item_code = '{0}'".format(self.item_code)

		if self.request_for_quotation:
			cond += " and tsqi.request_for_quotation = '{0}'".format(self.request_for_quotation)

		if self.supplier_quotation:
			cond += " and tsq.name = '{0}'".format(self.supplier_quotation)

		print(cond)
		query = """
				select 
					tsq.name as supplier_quotations,
					tsq.supplier,
					tsqi.item_code,
					tsqi.item_name,
					tsqi.uom,
					tsqi.rate,
					tsqi.amount,
					tsqi.lead_time_days,
					tsqi.expected_delivery_date 
				from `tabSupplier Quotation` tsq 
				left join `tabSupplier Quotation Item` tsqi on tsqi.parent = tsq.name
				WHERE {0}
		""".format(cond)
		
		data = frappe.db.sql(query, as_dict=True)
		if len(data) == 0:
			frappe.throw("No data found")
		
		for i in data:
			last_purchase_date = None
			last_purchase_rate = None
			po_query = """SELECT 
							tpo.transaction_date,
							tpoi.rate 
						FROM `tabPurchase Order Item` tpoi 
						left join `tabPurchase Order` tpo on tpoi.parent = tpo.name
						WHERE tpoi.item_code = '{0}' 
						ORDER BY tpo.creation DESC 
						LIMIT 1""".format(i.item_code)
			po_data = frappe.db.sql(po_query, as_dict=True)
			if po_data:
				last_purchase_date = po_data[0].transaction_date
				last_purchase_rate = po_data[0].rate
			self.append("supplier_quotation_comparison_table",{
				"item_code" : i.item_code,
				"item_name" : i.item_name,
				"uom" : i.uom,
                "rate" : i.rate,
                "amount" : i.amount,
                "supplier_quotation" : i.supplier_quotations,
                "supplier" : i.supplier,
				"lead_time_date" : i.expected_delivery_date,
				"lead_time_days" : i.lead_time_days,
				"last_purchase_date" : last_purchase_date,
                "last_purchase_rate" : last_purchase_rate
			})

	@frappe.whitelist()
	def make_single_item_purchase_order(self, item_code, item_name, uom, rate, supplier, required_date, qty, material_request=None, min_required_qty=None ):
		if not required_date:
			frappe.throw("Please Provide a required date")

		if not qty:
			frappe.throw("Please Provide a Quantity")

		doc = frappe.new_doc("Purchase Order")
		doc.supplier = supplier
		doc.schedule_date = required_date
		doc.append("items",{
			"item_code": item_code,
            "item_name": item_name,
            "uom": uom,
            "rate": rate,
            "qty": qty,
            "material_request": material_request,
		})
		doc.save()
		return 1, doc.name
	
	
	@frappe.whitelist()
	def make_bulk_item_purchase_order(self, items):
		supplier = []
		for row in items.get('items'):
			if row.get('supplier') not in supplier:
				supplier.append(row.get('supplier')) 
		
		if len(supplier) > 1:
			frappe.throw("Please Make a Purchase Order for each Supplier separately")


		doc = frappe.new_doc("Purchase Order")
		doc.supplier = supplier[0]
		# doc.schedule_date = required_date
		for row in items.get('items'):
			doc.append("items",{
				"item_code": row.get('item_code'),
				"rate": row.get("rate"),
				"qty": row.get("purchase_qty"),
				"material_request": row.get('material_request'),
				"schedule_date" : row.get('required_by')
			})
		doc.save()
		return 1, doc.name