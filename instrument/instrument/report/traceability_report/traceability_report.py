# Copyright (c) 2024, instrument and contributors
# For license information, please see license.txt

from distutils.command import sdist
import frappe



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
			"width": 140
		},
		{
			"label": "Customer Name",
			"fieldtype": "Link",
			"fieldname": "customer_name",
			"options":"Customer",
			"width": 140
		},
		{
			"label": "Sales Order Item",
			"fieldtype": "Link",
			"fieldname": "sales_order_item",
			"options":"Item",
			"width": 140
		},
		{
			"label": "Sales Order Item Qty",
			"fieldtype": "Float",
			"fieldname": "sales_order_item_qty",
			"width": 170
		},
		{
			"label": "Production Plan",
			"fieldtype": "Link",
			"fieldname": "production_plan",
			"options":"Production Planning With Lead Time",
			"width": 140
		},
		{
			"label": "Production Plan Date",
			"fieldtype": "Date",
			"fieldname": "p_date",
			"width": 170
		},
		{
			"label": "Material Request No",
			"fieldtype": "Link",
			"fieldname": "material_requesr_no",
			"options":"Material Request",
			"width": 160
		},
		{
			"label": "Material Request Date",
			"fieldtype": "Date",
			"fieldname": "material_request_date",
			"width": 170
		},


		{
			"label": "Purchase Order No",
			"fieldtype": "Link",
			"fieldname": "purchase_order_no",
			"options":"Purchase Order",
			"width": 160
		},
		{
			"label": "Purchase Order Date",
			"fieldtype": "Date",
			"fieldname": "purchase_order_date",
			"width": 170
		},
		{
			"label": "Supplier Name",
			"fieldtype": "Link",
			"fieldname": "supplier_name",
			"options":"Supplier",
			"width": 130
		},
		{
			"label": "Purchase Receipt No",
			"fieldtype": "Link",
			"fieldname": "purchase_r_no",
			"options":"Purchase Receipt",
			"width": 170
		},
		{
			"label": "Purchase Receipt Date",
			"fieldtype": "Date",
			"fieldname": "purchase_r_date",
			"width": 180
		},
		{
			"label": "Purchase Receipt Batch No",
			"fieldtype": "Data",
			"fieldname": "purchase_r_b_no",
			# "options":"",
			"width": 200
		},




		{
			"label": "Work Order No",
			"fieldtype": "Link",
			"fieldname": "work_r_no",
			"options":"Work Order",
			"width": 140
		},
		{
			"label": "Work Order Date",
			"fieldtype": "Date",
			"fieldname": "work_r_date",
			"width": 140
		},





		{
		 	"label": "Consolidated Pick List No (Material transfer for Manu)",
		 	"fieldtype": "Data",
		 	"fieldname": "consolidated_p_list_no",
		 	# "options":"",
		 	"width": 250
		 },
		{
			"label": "Consolidated Pick List Date (Material transfer for Manu)",
			"fieldtype": "Date",
			"fieldname": "consolidated_p_list_date",
			"width": 250
		},


		{
			"label": "Stock Entry No (Material transfer for Manu)",
			"fieldtype": "Link",
			"fieldname": "stock_e_no",
			"options":"Stock Entry",
			"width": 250
		},
		{
			"label": "Stock Entry Date (Material transfer for Manu)",
			"fieldtype": "Date",
			"fieldname": "stock_e_date",
			"width": 250
		},

		{
			"label": "Stock Entry Item (Material transfer for Manu)",
			"fieldtype": "Link",
			"fieldname": "stock_e_mt_item",
			"options": "Item",
			"width": 250
		},

		{
			"label": "Stock Entry qty (Material transfer for Manu)",
			"fieldtype": "Float",
			"fieldname": "stock_e_mt_qty",
			"width": 250
		},

		{
			"label": "Stock Entry Batch (Material transfer for Manu)",
			"fieldtype": "Data",
			"fieldname": "stock_e_mt_batch",
			"width": 250
		},


		{
			"label": "Consolidated Pick List No ( Manufacture)",
			"fieldtype": "Data",
			"fieldname": "consolidated_p_list_no_manufecture",
			# "options":"",
			"width": 250
		},
		{
			"label": "Consolidated Pick List Date ( Manufacture)",
			"fieldtype": "Date",
			"fieldname": "consolidated_p_list_date_manufecture",
			"width": 250
		},
		{
			"label": "Stock Entry No ( Manufacture)",
			"fieldtype": "Link",
			"fieldname": "stock_e__no",
			"options":"Stock Entry",
			"width": 200
		},
		{
			"label": "Stock Entry Date ( Manufacture)",
			"fieldtype": "Date",
			"fieldname": "stock_e_b_date",
			"width": 200
		},



		{
			"label": "Stock Entry Item ( Manufacture)",
			"fieldtype": "Link",
			"fieldname": "stock_e__item",
			"options":"Item",
			"width": 200
		},
		{
			"label": "Stock Entry Item Qty ( Manufacture)",
			"fieldtype": "Float",
			"fieldname": "stock_e__qty",
			"width": 200
		},
		{
			"label": "Stock Entry Batch ( Manufacture)",
			"fieldtype": "Data",
			"fieldname": "stock_e__batch",
			"width": 200
		},



		{
			"label": "Delivery Note No",
			"fieldtype": "Link",
			"fieldname": "delivery_n_no",
			"options":"Delivery Note",
			"width": 140
		},
		{
			"label": "Delivery Note Date",
			"fieldtype": "Date",
			"fieldname": "delivery_n_b_date",
			"width": 150
		},
		{
			"label": "Delivery Note Item",
			"fieldtype": "Link",
			"fieldname": "delivery_n_b_item",
			"options":"Item",
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
			"label": "Delivery Note Batch",
			"fieldtype": "Data",
			"fieldname": "delivery_n_b_batch",
			# "options":"",
			"width": 150
		}
		]
	return column


def get_data(filters):
	so_data = get_sales_order_data(filters)
	# print("---------------SO DATA------------------")
	# print(so_data)
	
	pp_data = get_production_plan_data(so_data)
	# print("---------------PP DATA------------------")
	# print(pp_data)

	mr_data = get_material_request_data(filters, pp_data)
	# print("---------------MR DATA------------------")
	# print(mr_data)

	po_data = get_purchase_order_data(filters, mr_data)
	# print("---------------PO DATA------------------")
	# print(po_data)

	pr_data = get_purchase_receipt_data(filters, po_data)
	# print("---------------PR DATA------------------")
	# print(pr_data)

	wo_data = get_work_order_data(filters, pp_data)
	# print("---------------WO DATA------------------")
	# print(wo_data)

	pick_list_for_mt_data = get_pick_list_for_mt(filters, wo_data)
	# print("---------------PL MT DATA------------------")
	# print(pick_list_for_mt_data)

	stock_entry_for_mt_data = get_stock_entry_for_mt(filters, pick_list_for_mt_data)
	# print("---------------SE MT DATA------------------")
	# print(stock_entry_for_mt_data)

	pick_list_for_manu_data = get_pick_list_for_manu(filters, wo_data)
	# print("---------------PL MT DATA------------------")
	# print(pick_list_for_manu_data)

	stock_entry_for_manu_data = get_stock_entry_for_manu(filters, pick_list_for_mt_data)
	# print("---------------SE MT DATA------------------")
	# print(stock_entry_for_manu_data)

	delivery_note_data = get_delivery_note_data(filters, so_data)
	# print("---------------DN DATA------------------")
	# print(delivery_note_data)

	final_list = []
	final_list_1 = []
	final_list_2 = []
	final_list_3 = []
	data = []

	for pp_rec in pp_data:
		for so_rec in so_data:
			if pp_rec.get("pp_so_name") == so_rec.get("so_name"):
				temp = {}
				temp["name"] = so_rec.get("so_name")
				temp["s_date"] = so_rec.get("so_date")
				temp["customer_name"] = so_rec.get("customer_name")
				temp["sales_order_item"] = so_rec.get("so_item_code")
				temp["sales_order_item_qty"] = so_rec.get("so_item_qty")
				temp["production_plan"] = pp_rec.get("production_plan_name")
				temp["p_date"] = pp_rec.get("production_plan_date")
				final_list.append(temp)


	for f1 in final_list:
		for mr_rec in mr_data:
			if f1.get("production_plan") == mr_rec.get("pp_name"):
				temp = {}
				temp["name"] = f1.get("name")
				temp["s_date"] = f1.get("s_date")
				temp["customer_name"] = f1.get("customer_name")
				temp["sales_order_item"] = f1.get("sales_order_item")
				temp["sales_order_item_qty"] = f1.get("sales_order_item_qty")
				temp["production_plan"] = f1.get("production_plan")
				temp["p_date"] = f1.get("p_date")
				temp["material_requesr_no"] = mr_rec.get("mr_name")
				temp["material_request_date"] = mr_rec.get("mr_date")
				final_list_1.append(temp)

	

	for f2 in final_list_1:
		for po_rec in po_data:
			if f2.get("material_requesr_no") == po_rec.get("po_mr_name"):
				temp = {}
				temp["name"] = f2.get("name")
				temp["s_date"] = f2.get("s_date")
				temp["customer_name"] = f2.get("customer_name")
				temp["sales_order_item"] = f2.get("sales_order_item")
				temp["sales_order_item_qty"] = f2.get("sales_order_item_qty")
				temp["production_plan"] = f2.get("production_plan")
				temp["p_date"] = f2.get("p_date")
				temp["material_requesr_no"] = f2.get("material_requesr_no")
				temp["material_request_date"] = f2.get("material_request_date")
				temp["purchase_order_no"] = po_rec.get("po_name")
				temp["purchase_order_date"] = po_rec.get("po_date")
				temp["supplier_name"] = po_rec.get("po_supplier")
				final_list_2.append(temp)


	for f3 in final_list_2:
		for pr_rec in pr_data:
			if f3.get("purchase_order_no") == pr_rec.get("pr_po_name"):
				f3["purchase_r_no"] = pr_rec.get("pr_name")
				f3["purchase_r_date"] = pr_rec.get("pr_date")
				f3["purchase_r_b_no"] = pr_rec.get("pr_batch_bundle")


	for f4 in final_list_2:
		for wo_rec in wo_data:
			if f4.get("production_plan") == wo_rec.get("wo_pp"):
				f4["work_r_no"] = wo_rec.get("wo_name")
				f4["work_r_date"] = wo_rec.get("wo_date")

	for f5 in final_list_2:
		for pl_mt_rec in pick_list_for_mt_data:
			if f5.get("work_r_no") == pl_mt_rec.get("pl_mt_wo"):
				f5["consolidated_p_list_no"] = pl_mt_rec.get("mt_pick_list_name")
				f5["consolidated_p_list_date"] = pl_mt_rec.get("mt_pick_list_date")

	for f6 in final_list_2:
		for se_mt_rec in stock_entry_for_mt_data:
			if f6.get("consolidated_p_list_no") == se_mt_rec.get("se_mt_pl"):
				f6["stock_e_no"] = se_mt_rec.get("se_mt_name")
				f6["stock_e_date"] = se_mt_rec.get("se_mt_date")
				f6["stock_e_mt_item"] = se_mt_rec.get("se_mt_item")
				f6["stock_e_mt_qty"] = se_mt_rec.get("se_mt_qty")
				f6["stock_e_mt_batch"] = se_mt_rec.get("se_mt_bundle")


	for f7 in final_list_2:
		for pl_manu_rec in pick_list_for_manu_data:
			if f7.get("work_r_no") == pl_manu_rec.get("manu_wo"):
				f7["consolidated_p_list_no_manufecture"] = pl_manu_rec.get("manu_pick_list_name")
				f7["consolidated_p_list_date_manufecture"] = pl_manu_rec.get("manu_pick_list_date")

	for f8 in final_list_2:
		for se_manu_rec in stock_entry_for_manu_data:
			if f8.get("consolidated_p_list_no_manufecture") == se_manu_rec.get("se_manu_pl"):
				f8["stock_e__no"] = se_manu_rec.get("se_manu_name")
				f8["stock_e_b_date"] = se_manu_rec.get("se_manu_date")
				f8["stock_e__item"] = se_manu_rec.get("se_manu_item")
				f8["stock_e__qty"] = se_manu_rec.get("se_manu_qty")
				f8["stock_e__batch"] = se_manu_rec.get("se_manu_bundle")

	for f9 in final_list_2:
		for delivery_note_rec in delivery_note_data:
			if f9.get("name") == delivery_note_rec.get("dn_so"):
				f9["delivery_n_no"] = delivery_note_rec.get("dn_name")
				f9["delivery_n_b_date"] = delivery_note_rec.get("dn_date")
				f9["delivery_n_b_item"] = delivery_note_rec.get("dn_item")
				f9["delivery_n_b_qty"] = delivery_note_rec.get("dn_qty")
				f9["delivery_n_b_batch"] = delivery_note_rec.get("dn_bundle")


	return final_list_2




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
			tsoi.qty as so_item_qty
			from `tabSales Order Item`tsoi 
			left join `tabSales Order` tso on tso.name = tsoi.parent
			Where 1 =1 AND tso.docstatus = 1 AND tso.status != 'Closed' {0} """.format(cond)
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
	where 1 = 1 {0}
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
	where 1 = 1 {0}
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
		tpri.serial_and_batch_bundle as pr_batch_bundle,
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
		where 1 = 1 {0} and tcpl.purpose = "Material Transfer for Manufacture"
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
		tsed.qty as se_mt_qty,
		tsed.serial_and_batch_bundle as se_mt_bundle,
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
		where 1 = 1 {0} and tcpl.purpose = "Manufacture"
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
			cond += "AND tse.consolidated_pick_list = '{0}'".format(pl_name_list)
		else:
			cond += "AND tse.consolidated_pick_list in {0}".format(tuple(pl_name_list))
	query = """
		select 
		tse.name as se_manu_name,
		tse.posting_date as se_manu_date,
		tsed.item_code as se_manu_item,
		tsed.qty as se_manu_qty,
		tsed.serial_and_batch_bundle as se_manu_bundle,
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
 			tdni.qty as dn_qty,
 			tdni.serial_and_batch_bundle as dn_bundle,
			tdni.against_sales_order as dn_so
		from `tabDelivery Note Item` tdni
		left join `tabDelivery Note` tdn on tdn.name = tdni.parent
		where 1 = 1 {0}
	""".format(cond)
	print(query)
	data = frappe.db.sql(query, as_dict=1)
	return data


# def get_data_1(filters):
# 	item_code = None
# 	if filters.get("item_code"):
# 		item_code = filters.get("item_code")
	
# 	if filters.get("batch"):
# 		item_code = frappe.get_value("Batch",filters.get("item_code"), "item")

# 	sales_cond = ""
# 	if item_code:
# 		sales_cond += " AND tsoi.item_code = '{0}'".format(item_code)
	
# 	if filters.get("doctype") == "Sales Order" and filters.get("doctype_name"):
# 		sales_cond += " AND tso.name = '{0}'".format(filters.get("doctype_name"))


# 	sales_data_sql = """select 
# 						tso.name,
# 						tso.transaction_date,
# 						tso.customer_name,
# 						tsoi.item_code,
# 						tsoi.qty
# 					from `tabSales Order Item`tsoi 
# 					left join `tabSales Order` tso on tso.name = tsoi.parent
# 					Where 1 =1 {0}
# 					""".format(sales_cond)
	
# 	sales_data = frappe.db.sql(sales_data_sql, as_list=1)

# 	# frappe.log_error(sales_data)

# 	production_data =[]
# 	for i in sales_data:
# 		production_data_sql = """
# 			select 
# 			tppwlt.name,
# 			tppwlt.from_date,
# 			tmr.name,
# 			tmr.transaction_date
# 		from `tabSales Order Table` tsot
# 		left join `tabProduction Planning With Lead Time` tppwlt on tppwlt.name = tsot.parent 
# 		left join `tabMaterial Request` tmr on tmr.production_planning_with_lead_time  = tppwlt.name 
# 		where tsot.sales_order = '{0}' AND tsot.item = '{1}'
# 		""".format(i[0], i[3])
		
# 		production_sql = frappe.db.sql(production_data_sql, as_list=1)
# 		if len(production_data) == 0:
# 			production_sql = [["", "", "", "", ""]]
# 		for ii in production_sql:
# 			production_data.append(i + ii)


# 	buying_data = []
# 	for pd in production_data:
# 		buying_data_sql = """
# 			select 
# 			tpo.name,
# 			tpo.transaction_date,
# 			tpo.supplier_name,
# 			tpr.name,
# 			tpr.posting_date,
# 			tpri.serial_and_batch_bundle
# 		from `tabPurchase Order` tpo
# 		left join `tabPurchase Receipt Item` tpri on tpri.purchase_order = tpo.name 
# 		left join `tabPurchase Receipt` tpr on tpr.name = tpri.parent
# 		where tpo.custom_production_planning_with_lead_time = '{0}'
# 		""".format(pd[5])
# 		buying__sql = frappe.db.sql(buying_data_sql, as_list=1)
# 		if len(buying__sql) == 0:
# 			buying__sql = [["", "", "", "", "", ""]]
# 		for bs in buying__sql:
# 			buying_data.append(pd + bs)




# 	work_order_data = []
# 	for bd in buying_data:
# 		work_order_sql = """
# 			select 
# 			two.name,
# 			two.actual_start_date,
# 			tcpl.name,
# 			tcpl.planned_start_date,
# 			tse2.name,
# 			tse2.posting_date,
# 			tsed.item_code,
# 			tsed.qty,
# 			tsed.serial_and_batch_bundle
# 		from `tabWork Order` two
# 		left join `tabPick List FG Work Orders` tplfwo on tplfwo.work_order = two.name
# 		left join `tabConsolidated Pick List` tcpl on tcpl.name = tplfwo.parent and tcpl.purpose = "Material Transfer for Manufacture"
# 		left join `tabStock Entry` tse2 on tse2.consolidated_pick_list = tcpl.name and tse2.stock_entry_type = "Material Transfer for Manufacture"
# 		left join `tabStock Entry Detail` tsed on tsed.parent = tse2.name
# 		where two.production_planning_with_lead_time = '{0}'
# 		""".format(bd[5])
# 		work_order_sql_data = frappe.db.sql(work_order_sql, as_list=1)
# 		if len(buying__sql) == 0:
# 			buying__sql = [["", "", "", "", "","", "", "", ""]]
# 		for ws in work_order_sql_data:
# 			work_order_data.append(bd + ws)


# 	stock_data = []
# 	for wd in work_order_data:
# 		stock_sql = """
# 			select 
# 			tcpl2.name,
# 			tcpl2.planned_start_date,
# 			tse.name,
# 			tse.posting_date,
# 			tsed2.item_code,
# 			tsed2.qty,
# 			tsed2.serial_and_batch_bundle,
# 			tdn.name,
# 			tdn.posting_date,
# 			tdni.item_code,
# 			tdni.qty,
# 			tdni.serial_and_batch_bundle
# 		from `tabConsolidated Pick List` tcpl2
# 		left join `tabPick List FG Work Orders` tplfwo on tplfwo.parent = tcpl2.name
# 		left join `tabStock Entry` tse on tse.consolidated_pick_list = tcpl2.name and tse.stock_entry_type = "Manufacture"
# 		left join `tabStock Entry Detail` tsed2 on tsed2.parent = tse.name
# 		left join `tabDelivery Note Item` tdni on tdni.parent = '{1}'
# 		left join `tabDelivery Note` tdn on tdn.name = tdni.parent
# 		where tplfwo.work_order = '{0}' and tcpl2.purpose = "Material Transfer for Manufacture"
# 		""".format(wd[14], wd[0])
# 		stock_sql_data = frappe.db.sql(stock_sql, as_list=1)
# 		if len(stock_sql_data) == 0:
# 			stock_sql_data = [["", "", "", "", "","","","", "","","", ""]]
# 		for sd in stock_sql_data:
# 			stock_data.append(wd + sd)

# 	return stock_data