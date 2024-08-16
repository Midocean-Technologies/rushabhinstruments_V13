
from distutils.command import sdist
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
					"label": "Batch",
					"fieldtype": "Link",
					"fieldname": "batch",
					"options": "Batch",
					"width": 170
				}
			]
	return column



def get_data(filters):
	so_data = get_sales_order_data(filters)
	pp_data = get_production_plan_data(so_data)
	mr_data = get_material_request_data(filters, pp_data)
	po_data = get_purchase_order_data(filters, mr_data)
	pr_data = get_purchase_receipt_data(filters, po_data)
	wo_data = get_work_order_data(filters, pp_data)
	pick_list_for_mt_data = get_pick_list_for_mt(filters, wo_data)
	stock_entry_for_mt_data = get_stock_entry_for_mt(filters, pick_list_for_mt_data)
	pick_list_for_manu_data = get_pick_list_for_manu(filters, wo_data)
	stock_entry_for_manu_data = get_stock_entry_for_manu(filters, pick_list_for_mt_data)
	delivery_note_data = get_delivery_note_data(filters, so_data)

	data = []

	for so_rec in so_data:
		data.append(
					{
						'document_type': 'Sales Order',
						'document_name': so_rec.get("so_name"),
						'indent': 0,
						'document_date': so_rec.get("so_date"),
						'party_name': so_rec.get("customer_name"),
						'item_code': so_rec.get("so_item_code"),
						'item_name': so_rec.get("so_item_name"),
						'qty': so_rec.get("so_item_qty"),
						'batch': ''
					}
				)
		data.append(
					{
						'document_type': 'Backword Tracebility',
						'document_name': '',
						'indent': 1,
						'document_date': '',
						'party_name': '',
						'item_code': '',
						'item_name': "",
						'qty': '',
						'batch': ''
					}
				)
		pp_list = []
		data.append(
					{
						'document_type': 'Production Plan With Lead Time',
						'document_name': '',
						'indent': 2,
						'document_date': '',
						'party_name': '',
						'item_code': '',
						'item_name': "",
						'qty': '',
						'batch': ''
					}
				)
		for pp_rec in pp_data:
			if so_rec.get("so_name") == pp_rec.get("pp_so_name"):
				data.append(
						{
							'document_type': 'Production Plan With Lead Time',
							'document_name': pp_rec.get("production_plan_name"),
							'indent': 3,
							'document_date': pp_rec.get("production_plan_date"),
							'party_name': "",
							'item_code': "",
							'item_name': "",
							'qty': "",
							'batch': ''
						}
					)
				pp_list.append(pp_rec.get("production_plan_name"))
				
		mr_list = []
		data.append(
					{
						'document_type': 'Material Request',
						'document_name': '',
						'indent': 2,
						'document_date': '',
						'party_name': '',
						'item_code': '',
						'item_name': "",
						'qty': '',
						'batch': ''
					}
				)
		for mr_rec in mr_data:
			if mr_rec.get("pp_name") in pp_list:
				data.append(
				{
					'document_type': 'Material Request',
					'document_name': mr_rec.get("mr_name"),
					'indent': 3,
					'document_date': mr_rec.get("mr_date"),
					'party_name': "",
					'item_code': "",
					'item_name': "",
					'qty': "",
					'batch': ''
					}
				)
				mr_list.append(mr_rec.get("mr_name"))

		po_list = []
		data.append(
					{
						'document_type': 'Purchase Order',
						'document_name': '',
						'indent': 2,
						'document_date': '',
						'party_name': '',
						'item_code': '',
						'item_name': "",
						'qty': '',
						'batch': ''
					}
				)
		for po_rec in po_data:
			if po_rec.get("po_mr_name") in mr_list:
				data.append(
				{
					'document_type': 'Purchase Order',
					'document_name': po_rec.get("po_name"),
					'indent': 3,
					'document_date': po_rec.get("po_date"),
					'party_name': po_rec.get("po_supplier"),
					'item_code': "",
					'item_name': "",
					'qty': "",
					'batch': ''
					}
				)
				po_list.append(po_rec.get("po_name"))
		
		pr_list = []
		data.append(
					{
						'document_type': 'Purchase Receipt',
						'document_name': '',
						'indent': 2,
						'document_date': '',
						'party_name': '',
						'item_code': '',
						'item_name': "",
						'qty': '',
						'batch': ''
					}
				)
		for pr_rec in pr_data:
			if pr_rec.get("pr_po_name") in po_list:
				data.append(
				{
					'document_type': 'Purchase Receipt',
					'document_name': pr_rec.get("pr_name"),
					'indent': 3,
					'document_date': pr_rec.get("pr_date"),
					'party_name': pr_rec.get("pr_supplier"),
					'item_code': pr_rec.get("pr_item_code"),
					'item_name': pr_rec.get("pr_item_name"),
					'qty': pr_rec.get("pr_qty"),
					'batch': pr_rec.get("pr_batch_bundle")
					}
				)
				pr_list.append(pr_rec.get("pr_name"))

		
		data.append(
					{
						'document_type': 'Forward Tracebility',
						'document_name': '',
						'indent': 1,
						'document_date': '',
						'party_name': '',
						'item_code': '',
						'qty': '',
						'batch': ''
					}
				)

		wo_list = []
		data.append(
					{
						'document_type': 'Work Order',
						'document_name': '',
						'indent': 2,
						'document_date': '',
						'party_name': '',
						'item_code': '',
						'item_name': "",
						'qty': '',
						'batch': ''
					}
				)
		for wo_rec in wo_data:
			if wo_rec.get("wo_pp") in pp_list:
				data.append(
				{
					'document_type': 'Work Order',
					'document_name': wo_rec.get("wo_name"),
					'indent': 3,
					'document_date': wo_rec.get("wo_date"),
					'party_name': "",
					'item_code': wo_rec.get("wo_item_code"),
					'item_name': wo_rec.get("wo_item_name"),
					'qty': wo_rec.get("wo_qty"),
					'batch': ''
					}
				)
				wo_list.append(wo_rec.get("wo_name"))

		
		pl_mt_list = []
		data.append(
					{
						'document_type': 'Consolidated Pick List (Material Trasfer)',
						'document_name': '',
						'indent': 2,
						'document_date': '',
						'party_name': '',
						'item_code': '',
						'item_name': "",
						'qty': '',
						'batch': ''
					}
				)
		for pl_mt_rec in pick_list_for_mt_data:
			if pl_mt_rec.get("pl_mt_wo") in wo_list:
				data.append(
				{
					'document_type': 'Consolidated Pick List (Material Trasfer)',
					'document_name': pl_mt_rec.get("mt_pick_list_name"),
					'indent': 3,
					'document_date': pl_mt_rec.get("mt_pick_list_date"),
					'party_name': "",
					'item_code': "",
					'item_name': "",
					'qty': "",
					'batch': ''
					}
				)
				pl_mt_list.append(pl_mt_rec.get("mt_pick_list_name"))


		se_mt_list = []
		data.append(
					{
						'document_type': 'Stock Entry (Material Trasfer)',
						'document_name': '',
						'indent': 2,
						'document_date': '',
						'party_name': '',
						'item_code': '',
						'item_name': "",
						'qty': '',
						'batch': ''
					}
				)
		for se_mt_rec in stock_entry_for_mt_data:
			if se_mt_rec.get("se_mt_pl") in pl_mt_list:
				data.append(
				{
					'document_type': 'Stock Entry (Material Trasfer)',
					'document_name': se_mt_rec.get("se_mt_name"),
					'indent': 3,
					'document_date': se_mt_rec.get("se_mt_date"),
					'party_name': "",
					'item_code': se_mt_rec.get("se_mt_item"),
					'item_name': se_mt_rec.get("se_mt_item_name"),
					'qty': se_mt_rec.get("se_mt_qty"),
					'batch': se_mt_rec.get("se_mt_batch_bundle")
					}
				)
				se_mt_list.append(se_mt_rec.get("se_mt_name"))
		
		pl_manu_list = []
		data.append(
					{
						'document_type': 'Consolidated Pick List (Manufacture)',
						'document_name': '',
						'indent': 2,
						'document_date': '',
						'party_name': '',
						'item_code': '',
						'item_name': "",
						'qty': '',
						'batch': ''
					}
				)
		for pl_manu_rec in pick_list_for_manu_data:
			if pl_manu_rec.get("manu_wo") in wo_list:
				data.append(
				{
					'document_type': 'Consolidated Pick List (Manufacture)',
					'document_name': pl_manu_rec.get("manu_pick_list_name"),
					'indent': 3,
					'document_date': pl_manu_rec.get("manu_pick_list_date"),
					'party_name': "",
					'item_code': "",
					'item_name': "",
					'qty': "",
					'batch': ''
					}
				)
				pl_manu_list.append(pl_manu_rec.get("manu_pick_list_name"))


		se_manu_list = []
		data.append(
					{
						'document_type': 'Stock Entry (Manufacture)',
						'document_name': '',
						'indent': 2,
						'document_date': '',
						'party_name': '',
						'item_code': '',
						'item_name': "",
						'qty': '',
						'batch': ''
					}
				)
		for se_manu_rec in stock_entry_for_manu_data:
			if se_manu_rec.get("se_manu_pl") in pl_manu_list:
				data.append(
				{
					'document_type': 'Stock Entry (Manufacture)',
					'document_name': se_manu_rec.get("se_manu_name"),
					'indent': 3,
					'document_date': se_manu_rec.get("se_manu_date"),
					'party_name': "",
					'item_code': se_manu_rec.get("se_manu_item"),
					'item_name': se_manu_rec.get("se_manu_item_name"),
					'qty': se_manu_rec.get("se_manu_qty"),
					'batch': se_manu_rec.get("se_manu_batch_bundle")
					}
				)
				se_manu_list.append(se_manu_rec.get("se_manu_name"))

		dl_note_list = []
		data.append(
					{
						'document_type': 'Delivery Note',
						'document_name': '',
						'indent': 2,
						'document_date': '',
						'party_name': '',
						'item_code': '',
						'item_name': "",
						'qty': '',
						'batch': ''
					}
				)
		for delivery_note_rec in delivery_note_data:
			if delivery_note_rec.get("dn_so") == so_rec.get("so_name"):
				data.append(
				{
					'document_type': 'Delivery Note',
					'document_name': delivery_note_rec.get("dn_name"),
					'indent': 3,
					'document_date': delivery_note_rec.get("dn_date"),
					'party_name': "",
					'item_code': delivery_note_rec.get("dn_item"),
					'item_name': delivery_note_rec.get("dn_item_name"),
					'qty': delivery_note_rec.get("dn_qty"),
					'batch': delivery_note_rec.get("dn_batch_bundle")
					}
				)
				dl_note_list.append(delivery_note_rec.get("dn_name"))

	return data




def get_sales_order_data(filters):
	cond = ""
	if filters.get('customer'):
		cond += "AND tso.customer = '{0}'".format(filters.get('customer'))
	
	if filters.get("item_code") and frappe.db.exists("Sales Order Item", {"item_code": filters.get("item_code")}):
		cond += "AND tsoi.item_code = '{0}'".format(filters.get("item_code"))

	if filters.get("doctype") == "Sales Order" and filters.get("doctype_name"):
		cond += "AND tso.name = '{0}'".format(filters.get("doctype_name"))

	query =  """
			select 
			tso.name as so_name,
			tso.transaction_date as so_date,
			tso.customer_name,
			tsoi.item_code as so_item_code,
			tsoi.item_name as so_item_name,
			tsoi.qty as so_item_qty
			from `tabSales Order Item`tsoi 
			left join `tabSales Order` tso on tso.name = tsoi.parent
			Where 1 =1 AND tso.docstatus = 1 AND tso.status != 'Closed' {0} ORDER BY tso.name DESC""".format(cond)
	print(query)
	data = frappe.db.sql(query, as_dict=1)
	return data


def get_production_plan_data(so_data):
	so_name_list = []
	for i in so_data:
		so_name_list.append(str(i.get("so_name")))

	so_cond = ""
	if len(so_name_list) > 0:
		if len(so_name_list) == 1:
			so_cond += "AND tsot.sales_order = '{0}'".format(so_name_list[0])
		else:
			so_cond += "AND tsot.sales_order in {0}".format(tuple(so_name_list))
	query = """
		select 
		tppwlt.name as production_plan_name,
		tppwlt.from_date as production_plan_date,
		tsot.sales_order as pp_so_name
	from `tabSales Order Table` tsot
	left join `tabProduction Planning With Lead Time` tppwlt on tppwlt.name = tsot.parent 
	where 1 = 1 {0} GROUP BY tppwlt.name
	""".format(so_cond)
	print(query)
	data = frappe.db.sql(query, as_dict=1)
	return data

	
def get_material_request_data(filters, pp_data):
	pp_name_list = []
	for i in pp_data:
		pp_name_list.append(i.get("production_plan_name"))
	
	cond = ""
	if len(pp_name_list) > 0:
		if len(pp_name_list) == 1:
			cond += "AND tmr.production_planning_with_lead_time = '{0}'".format(pp_name_list[0])
		else:
			cond += " AND tmr.production_planning_with_lead_time in {0}".format(tuple(pp_name_list))

	# if filters.get("item_code") and frappe.db.exists("Material Request Item", {"item_code": filters.get("item_code")}):
	# 	cond += " AND tmri.item_code = '{0}'".format(filters.get("item_code"))

	query = """
		select 
		tmr.name as mr_name,
		tmr.transaction_date as mr_date,
		tmr.production_planning_with_lead_time as pp_name
	from `tabMaterial Request` tmr
	where 1 = 1 {0}
	""".format(cond)

	print(query)
	data = frappe.db.sql(query, as_dict=1)
	return data


def get_purchase_order_data(filters,mr_data):
	mr_name_list = []
	for i in mr_data:
		mr_name_list.append(i.get("mr_name"))
	
	cond = ""
	if len(mr_name_list) > 0:
		if len(mr_name_list) == 1:
			cond += "AND tpoi.material_request = '{0}'".format(mr_name_list[0])
		else:
			cond += "AND tpoi.material_request in {0}".format(tuple(mr_name_list))
	if filters.get("item_code") and frappe.db.exists("Purchase Order Item", {"item_code": filters.get("item_code")}):
		cond += "AND tpoi.item_code = '{0}'".format(filters.get("item_code"))
	
	if filters.get("supplier"):
		cond += " AND tpo.supplier = '{0}'".format(filters.get("supplier"))

	query = """
		select 
		tpo.name as po_name,
		tpo.transaction_date as po_date,
		tpo.supplier_name as po_supplier,
		tpoi.material_request as po_mr_name
	from `tabPurchase Order Item` tpoi
	left join `tabPurchase Order` tpo on tpo.name = tpoi.parent 
	where 1 = 1 {0} GROUP BY tpo.name
	""".format(cond)
	print(query)
	data = frappe.db.sql(query, as_dict=1)
	return data


def get_purchase_receipt_data(filters, po_data):
	po_name_list = []
	for i in po_data:
		po_name_list.append(i.get("po_name"))

	cond = ""
	if len(po_name_list) > 0:
		if len(po_name_list) == 1:
			cond += "AND tpri.purchase_order = '{0}'".format(po_name_list[0])
		else:
			cond += "AND tpri.purchase_order in {0}".format(tuple(po_name_list))
	if filters.get("item_code") and frappe.db.exists("Purchase Receipt Item", {"item_code": filters.get("item_code")}):
		cond += "AND tpri.item_code = '{0}'".format(filters.get("item_code"))
	
	if filters.get("supplier"):
		cond += " AND tpr.supplier = '{0}'".format(filters.get("supplier"))

	query = """
		select 
		tpr.name as pr_name,
		tpr.posting_date as pr_date,
		tpr.supplier_name as pr_supplier,
		tpri.item_code as pr_item_code,
		tpri.item_name as pr_item_name,
		tpri.qty as pr_qty,
		(select tsabe.batch_no from `tabSerial and Batch Entry` tsabe left join `tabSerial and Batch Bundle` tsabb on tsabb.name = tsabe.parent WHERE tsabb.voucher_type = "Purchase Receipt" and tsabb.voucher_no = tpr.name and tsabb.item_code = tpri.item_code GROUP BY tsabe.batch_no) as pr_batch_bundle,
		tpri.purchase_order as pr_po_name
	from `tabPurchase Receipt Item` tpri
	left join `tabPurchase Receipt` tpr on tpr.name = tpri.parent 
	where 1 = 1 {0}
	""".format(cond)
	print(query)
	data = frappe.db.sql(query, as_dict=1)
	return data

def get_work_order_data(filters, pp_data):
	pp_name_list = []
	for i in pp_data:
		pp_name_list.append(i.get("production_plan_name"))
	cond = ""
	if len(pp_name_list) > 0:
		if len(pp_name_list) == 1:
			cond += "AND two.production_planning_with_lead_time = '{0}'".format(pp_name_list[0])	
		else:
			cond += "AND two.production_planning_with_lead_time in {0}".format(tuple(pp_name_list))
	query = """
		select 
		two.name as wo_name,
		two.production_item as wo_item_code,
		two.item_name as wo_item_name,
		two.qty as wo_qty,
		two.production_planning_with_lead_time as wo_pp,
		two.actual_start_date as wo_date
	from `tabWork Order` two 
	where 1 = 1 {0}
	""".format(cond)
	print(query)
	data = frappe.db.sql(query, as_dict=1)
	return data


def get_pick_list_for_mt(filters, wo_data):
	wo_name_list = []
	for i in wo_data:
		wo_name_list.append(i.get("wo_name"))
	cond = ""
	if len(wo_name_list) > 0:
		if len(wo_name_list) == 1:
			cond += "AND tpo.work_order = '{0}'".format(wo_name_list[0])
		else:
			cond += "AND tpo.work_order in {0}".format(tuple(wo_name_list))
	query = """
		select 
		tcpl.name as mt_pick_list_name,
		tcpl.planned_start_date as mt_pick_list_date,
		tpo.work_order as pl_mt_wo
		from `tabPick Orders` tpo
		left join `tabConsolidated Pick List` tcpl on tcpl.name = tpo.parent
		where 1 = 1 {0} and tcpl.purpose = "Material Transfer for Manufacture" GROUP BY tcpl.name
	""".format(cond)
	print(query)
	data = frappe.db.sql(query, as_dict=1)
	return data


def get_stock_entry_for_mt(filters, pick_list_for_mt_data):
	pl_name_list = []
	for i in pick_list_for_mt_data:
		pl_name_list.append(i.get("mt_pick_list_name"))
	cond = ""
	if len(pl_name_list) > 0:
		if len(pl_name_list) == 1:
			cond += "AND tse.consolidated_pick_list = '{0}'".format(pl_name_list[0])
		else:
			cond += "AND tse.consolidated_pick_list in {0}".format(tuple(pl_name_list))
	query = """
		select 
		tse.name as se_mt_name,
		tse.posting_date as se_mt_date,
		tsed.item_code as se_mt_item,
		tsed.item_name as se_mt_item_name,
		tsed.qty as se_mt_qty,
		(select tsabe.batch_no from `tabSerial and Batch Entry` tsabe left join `tabSerial and Batch Bundle` tsabb on tsabb.name = tsabe.parent WHERE tsabb.voucher_type = "Stock Entry" and tsabb.voucher_no = tse.name and tsabb.item_code = tsed.item_code GROUP BY tsabe.batch_no) as se_mt_batch_bundle,
		tse.consolidated_pick_list as se_mt_pl
		from `tabStock Entry Detail` tsed
		left join `tabStock Entry` tse on tse.name = tsed.parent
		where 1 = 1 {0} and tse.stock_entry_type = "Material Transfer for Manufacture"
	""".format(cond)
	print(query)
	data = frappe.db.sql(query, as_dict=1)
	return data


def get_pick_list_for_manu(filters, wo_data):
	wo_name_list = []
	for i in wo_data:
		wo_name_list.append(i.get("wo_name"))
	cond = ""
	if len(wo_name_list) > 0:
		if len(wo_name_list) == 1:
			cond += "AND tpo.work_order = '{0}'".format(wo_name_list[0])
		else:
			cond += "AND tpo.work_order in {0}".format(tuple(wo_name_list))
	query = """
		select 
		tcpl.name as manu_pick_list_name,
		tcpl.planned_start_date as manu_pick_list_date,
		tpo.work_order as manu_wo
		from `tabPick Orders` tpo
		left join `tabConsolidated Pick List` tcpl on tcpl.name = tpo.parent
		where 1 = 1 {0} and tcpl.purpose = "Manufacture" GROUP BY tcpl.name
	""".format(cond)
	print(query)
	data = frappe.db.sql(query, as_dict=1)
	return data


def get_stock_entry_for_manu(filters, pick_list_for_mt_data):
	pl_name_list = []
	for i in pick_list_for_mt_data:
		pl_name_list.append(i.get("mt_pick_list_name"))
	cond = ""
	if len(pl_name_list) > 0:
		if len(pl_name_list) == 1:
			cond += "AND tse.consolidated_pick_list = '{0}'".format(pl_name_list[0])
		else:
			cond += "AND tse.consolidated_pick_list in {0}".format(tuple(pl_name_list))
	query = """
		select 
		tse.name as se_manu_name,
		tse.posting_date as se_manu_date,
		tsed.item_code as se_manu_item,
		tsed.item_name as se_manu_item_name,
		tsed.qty as se_manu_qty,
		(select tsabe.batch_no from `tabSerial and Batch Entry` tsabe left join `tabSerial and Batch Bundle` tsabb on tsabb.name = tsabe.parent WHERE tsabb.voucher_type = "Stock Entry" and tsabb.voucher_no = tse.name and tsabb.item_code = tsed.item_code GROUP BY tsabe.batch_no) as se_manu_batch_bundle,
		tse.consolidated_pick_list as se_manu_pl
		from `tabStock Entry Detail` tsed
		left join `tabStock Entry` tse on tse.name = tsed.parent
		where 1 = 1 {0} and tse.stock_entry_type = "Manufacture"
	""".format(cond)
	print(query)
	data = frappe.db.sql(query, as_dict=1)
	return data

def get_delivery_note_data(filters, so_data):
	so_name_list = []
	for i in so_data:
		so_name_list.append(i.get("so_name"))
	cond = ""
	if len(so_name_list) > 0:
		if len(so_name_list) == 1:
			cond += "AND tdni.against_sales_order = '{0}'".format(so_name_list[0])
		else:
			cond += "AND tdni.against_sales_order in {0}".format(tuple(so_name_list))
	query = """
		select 
			tdn.name as dn_name,
 			tdn.posting_date as dn_date,
 			tdni.item_code as dn_item,
 			tdni.item_name as dn_item_name,
 			tdni.qty as dn_qty,
 			(select tsabe.batch_no from `tabSerial and Batch Entry` tsabe left join `tabSerial and Batch Bundle` tsabb on tsabb.name = tsabe.parent WHERE tsabb.voucher_type = "Delivery Note" and tsabb.voucher_no = tdn.name and tsabb.item_code = tdni.item_code GROUP BY tsabe.batch_no) as dn_batch_bundle,
			tdni.against_sales_order as dn_so
		from `tabDelivery Note Item` tdni
		left join `tabDelivery Note` tdn on tdn.name = tdni.parent
		where 1 = 1 {0}
	""".format(cond)
	print(query)
	data = frappe.db.sql(query, as_dict=1)
	return data
