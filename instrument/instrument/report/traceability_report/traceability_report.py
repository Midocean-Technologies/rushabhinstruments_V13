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
	item_code = None
	if filters.get("item_code"):
		item_code = filters.get("item_code")
	
	if filters.get("batch"):
		item_code = frappe.get_value("Batch",filters.get("item_code"), "item")

	sales_cond = ""
	if item_code:
		sales_cond += " AND tsoi.item_code = '{0}'".format(item_code)
	
	if filters.get("doctype") == "Sales Order" and filters.get("doctype_name"):
		sales_cond += " AND tso.name = '{0}'".format(filters.get("doctype_name"))


	sales_data_sql = """select 
						tso.name,
						tso.transaction_date,
						tso.customer_name,
						tsoi.item_code,
						tsoi.qty
					from `tabSales Order Item`tsoi 
					left join `tabSales Order` tso on tso.name = tsoi.parent
					Where 1 =1 {0}
					""".format(sales_cond)
	
	sales_data = frappe.db.sql(sales_data_sql, as_list=1)

	# frappe.log_error(sales_data)

	production_data =[]
	for i in sales_data:
		production_data_sql = """
			select 
			tppwlt.name,
			tppwlt.from_date,
			tmr.name,
			tmr.transaction_date
		from `tabSales Order Table` tsot
		left join `tabProduction Planning With Lead Time` tppwlt on tppwlt.name = tsot.parent 
		left join `tabMaterial Request` tmr on tmr.production_planning_with_lead_time  = tppwlt.name 
		where tsot.sales_order = '{0}' AND tsot.item = '{1}'
		""".format(i[0], i[3])
		
		production_sql = frappe.db.sql(production_data_sql, as_list=1)
		if len(production_data) == 0:
			production_sql = [["", "", "", "", ""]]
		for ii in production_sql:
			production_data.append(i + ii)


	buying_data = []
	for pd in production_data:
		buying_data_sql = """
			select 
			tpo.name,
			tpo.transaction_date,
			tpo.supplier_name,
			tpr.name,
			tpr.posting_date,
			tpri.serial_and_batch_bundle
		from `tabPurchase Order` tpo
		left join `tabPurchase Receipt Item` tpri on tpri.purchase_order = tpo.name 
		left join `tabPurchase Receipt` tpr on tpr.name = tpri.parent
		where tpo.custom_production_planning_with_lead_time = '{0}'
		""".format(pd[5])
		buying__sql = frappe.db.sql(buying_data_sql, as_list=1)
		if len(buying__sql) == 0:
			buying__sql = [["", "", "", "", "", ""]]
		for bs in buying__sql:
			buying_data.append(pd + bs)




	work_order_data = []
	for bd in buying_data:
		work_order_sql = """
			select 
			two.name,
			two.actual_start_date,
			tcpl.name,
			tcpl.planned_start_date,
			tse2.name,
			tse2.posting_date,
			tsed.item_code,
			tsed.qty,
			tsed.serial_and_batch_bundle
		from `tabWork Order` two
		left join `tabPick List FG Work Orders` tplfwo on tplfwo.work_order = two.name
		left join `tabConsolidated Pick List` tcpl on tcpl.name = tplfwo.parent and tcpl.purpose = "Material Transfer for Manufacture"
		left join `tabStock Entry` tse2 on tse2.consolidated_pick_list = tcpl.name and tse2.stock_entry_type = "Material Transfer for Manufacture"
		left join `tabStock Entry Detail` tsed on tsed.parent = tse2.name
		where two.production_planning_with_lead_time = '{0}'
		""".format(bd[5])
		work_order_sql_data = frappe.db.sql(work_order_sql, as_list=1)
		if len(buying__sql) == 0:
			buying__sql = [["", "", "", "", "","", "", "", ""]]
		for ws in work_order_sql_data:
			work_order_data.append(bd + ws)


	stock_data = []
	for wd in work_order_data:
		stock_sql = """
			select 
			tcpl2.name,
			tcpl2.planned_start_date,
			tse.name,
			tse.posting_date,
			tsed2.item_code,
			tsed2.qty,
			tsed2.serial_and_batch_bundle,
			tdn.name,
			tdn.posting_date,
			tdni.item_code,
			tdni.qty,
			tdni.serial_and_batch_bundle
		from `tabConsolidated Pick List` tcpl2
		left join `tabPick List FG Work Orders` tplfwo on tplfwo.parent = tcpl2.name
		left join `tabStock Entry` tse on tse.consolidated_pick_list = tcpl2.name and tse.stock_entry_type = "Manufacture"
		left join `tabStock Entry Detail` tsed2 on tsed2.parent = tse.name
		left join `tabDelivery Note Item` tdni on tdni.parent = '{1}'
		left join `tabDelivery Note` tdn on tdn.name = tdni.parent
		where tplfwo.work_order = '{0}' and tcpl2.purpose = "Material Transfer for Manufacture"
		""".format(wd[14], wd[0])
		stock_sql_data = frappe.db.sql(stock_sql, as_list=1)
		if len(stock_sql_data) == 0:
			stock_sql_data = [["", "", "", "", "","","","", "","","", ""]]
		for sd in stock_sql_data:
			stock_data.append(wd + sd)

	return stock_data