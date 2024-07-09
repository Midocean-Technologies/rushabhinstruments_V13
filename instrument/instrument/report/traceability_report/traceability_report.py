# Copyright (c) 2024, instrument and contributors
# For license information, please see license.txt

import frappe



def execute(filters=None):
	print("....................................")
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
			"fieldtype": "Data",
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
		# {
		# 	"label": "Request For Quotation No",
		# 	"fieldtype": "Data",
		# 	"fieldname": "request_for_quotation_no",
		# 	# "options":"",
		# 	"width": 200
		# },
		# {
		# 	"label": "Request For Quotation Date",
		# 	"fieldtype": "Date",
		# 	"fieldname": "request_for_quotation_date",
		# 	"width": 210
		# },
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
		# {
		# 	"label": "Purchase Receipt Batch No",
		# 	"fieldtype": "Data",
		# 	"fieldname": "purchase_r_b_no",
		# 	# "options":"",
		# 	"width": 200
		# },
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
		# {
		# 	"label": "Stock Entry Item (Material transfer for Manu)",
		# 	"fieldtype": "Link",
		# 	"fieldname": "stock_e_item",
		# 	# "options":"Item",
		# 	"width": 250
		# },
		# {
		# 	"label": "Stock Entry Qty (Material transfer for Manu)",
		# 	"fieldtype": "Data",
		# 	"fieldname": "stock_e_qty",
		# 	"width": 250
		# },
		# {
		# 	"label": "Stock Entry Batch (Material transfer for Manu)",
		# 	"fieldtype": "Data",
		# 	"fieldname": "stock_e_batch",
		# 	# "options":"",
		# 	"width": 250
		# },
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
		# {
		# 	"label": "Stock Entry Item ( Manufacture)",
		# 	"fieldtype": "Link",
		# 	"fieldname": "stock_e_b_item",
		# 	# "options":"Item",
		# 	"width": 200
		# },
		# {
		# 	"label": "Stock Entry Qty ( Manufacture)",
		# 	"fieldtype": "Data",
		# 	"fieldname": "stock_e_b_qty",
		# 	"width": 200
		# },
		# {
		# 	"label": "Stock Entry Batch No ( Manufacture)",
		# 	"fieldtype": "Data",
		# 	"fieldname": "stock_e_b_no",
		# 	# "options":"",
		# 	"width": 200
		# },
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
		# {
		# 	"label": "Delivery Note Batch No",
		# 	"fieldtype": "Data",
		# 	"fieldname": "delivery_n_b_no",
		# 	# "options":"",
		# 	"width": 180
		# },



		]
	return column
def get_data(filters):

	cond = get_condition(filters)
	
	sql = """select 
			tso.name,
			tso.transaction_date,
			tso.customer_name,
			tsoi.item_code,
			tsoi.qty,
			tppwlt.name,
			tppwlt.from_date,
			tmr.name,
			tmr.transaction_date,
			tpo.name,
			tpo.transaction_date,
			tpo.supplier_name,
			tpr.name,
			tpr.posting_date,
			two.name,
			two.actual_start_date,
			tcpl.name,
			tcpl.planned_start_date,
			tse2.name,
			tse2.posting_date,
			tcpl2.name,
			tcpl2.planned_start_date,
			tse.name,
			tse.posting_date,
			tdn.name,
			tdn.posting_date,
			tdni.item_code,
			tdni.qty
		from `tabSales Order Item`tsoi 
		left join `tabSales Order` tso on tso.name = tsoi.parent
		left join `tabSales Order Table` tsot on tsot.sales_order = tso.name
		left join `tabProduction Planning With Lead Time` tppwlt on tppwlt.name = tsot.parent 
		left join `tabMaterial Request` tmr on tmr.production_planning_with_lead_time  = tppwlt.name 
		left join `tabPurchase Order` tpo on tpo.custom_production_planning_with_lead_time = tppwlt.name
		left join `tabPurchase Receipt Item` tpri on tpri.purchase_order = tpo.name 
		left join `tabPurchase Receipt` tpr on tpr.name = tpri.parent
		left join `tabWork Order` two on two.production_planning_with_lead_time = tppwlt.name
		left join `tabPick List FG Work Orders` tplfwo on tplfwo.work_order = two.name
		left join `tabConsolidated Pick List` tcpl on tcpl.name = tplfwo.parent and tcpl.purpose = "Material Transfer for Manufacture"
		left join `tabConsolidated Pick List` tcpl2 on tcpl2.name = tplfwo.parent and tcpl2.purpose = "Manufacture"
		left join `tabStock Entry` tse on tse.consolidated_pick_list = tcpl2.name and tse.stock_entry_type = "Manufacture"
		left join `tabStock Entry` tse2 on tse2.consolidated_pick_list = tcpl.name and tse2.stock_entry_type = "Material Transfer for Manufacture"
		left join `tabDelivery Note Item` tdni on tdni.parent = tso.name
		left join `tabDelivery Note` tdn on tdn.name = tdni.parent
		Where %s
		"""%(cond)
	data = frappe.db.sql(sql)
	return data

def get_condition(filters):
	cond = "1 = 1"
	if filters.get("item_code"):
		cond = " AND tsoi.item_code = '{0}'".format(filters.get("item_code"))

	if filters.get("doctype") == "Sales Order" and filters.get("doctype_name"):
		cond = " AND tso.name = '{0}'".format(filters.get("doctype_name"))

	if filters.get("doctype") == "Production Planning With Lead Time" and filters.get("doctype_name"):
		cond = " AND tppwlt.name = '{0}'".format(filters.get("doctype_name"))

	if filters.get("doctype") == "Material Request" and filters.get("doctype_name"):
		cond = " AND tmr.name = '{0}'".format(filters.get("doctype_name"))

	if filters.get("doctype") == "Purchase Order" and filters.get("doctype_name"):
		cond = " AND tpo.name = '{0}'".format(filters.get("doctype_name"))

	if filters.get("doctype") == "Purchase Receipt" and filters.get("doctype_name"):
		cond = " AND tpr.name = '{0}'".format(filters.get("doctype_name"))

	if filters.get("doctype") == "Work Order" and filters.get("doctype_name"):
		cond = " AND two.name = '{0}'".format(filters.get("doctype_name"))

	if filters.get("doctype") == "Consolidated Pick List" and filters.get("doctype_name"):
		cond = " AND tcpl.name = '{0}'".format(filters.get("doctype_name"))

	if filters.get("doctype") == "Stock Entry" and filters.get("doctype_name"):
		cond = " AND tse.name = '{0}'".format(filters.get("doctype_name"))
	
	if filters.get("doctype") == "Delivery Note" and filters.get("doctype_name"):
		cond = " AND tdn.name = '{0}'".format(filters.get("doctype_name"))

	return cond
