frappe.ui.form.on("Stock Entry", {
	refresh:function(frm){
		if(frm.doc.stock_entry_type == 'Material Transfer' || frm.doc.stock_entry_type == 'Material Receipt'){
			frm.set_value("apply_putaway_rule",1)
		}
	},
	onload:function(frm){
		if(frm.doc.__islocal && frm.doc.work_order_pick_list){
			frappe.call({
				method :"instrument.instrument.custom_instrument.stock_entry.stock_entry.get_items_from_pick_list",
				args : {
					pick_list : frm.doc.work_order_pick_list,
					work_order : frm.doc.work_order
				},
				callback:function(r){
					if(r.message){
						frm.set_value('fg_completed_qty',r.message[1])
						frm.set_value('posting_date', frappe.datetime.get_today())
						frm.set_value('posting_time',frappe.datetime.now_time())
						frm.doc.items = ''
						$.each(r.message[0], function(idx, item_row){
							if(item_row['s_warehouse']){
								var row = frappe.model.add_child(frm.doc, "Stock Entry Detail", "items");
								frappe.model.set_value(row.doctype, row.name, 'item_code', item_row['item_code']);
								frappe.model.set_value(row.doctype,row.name,'item_name',item_row['item_name']);
								frappe.model.set_value(row.doctype, row.name, 'qty', item_row['picked_qty']);
								frappe.model.set_value(row.doctype, row.name, 'uom', item_row['stock_uom']);
								frappe.model.set_value(row.doctype, row.name, 'stock_uom', item_row['stock_uom']);
								frappe.model.set_value(row.doctype, row.name, 'conversion_factor', 1);
								frappe.model.set_value(row.doctype, row.name, 's_warehouse',item_row['s_warehouse']);
								frappe.model.set_value(row.doctype, row.name, 'engineering_revision',item_row['engineering_revision']);
								frappe.model.set_value(row.doctype, row.name, 'batch_no',item_row['batch_no']);
							}else{
								var row = frappe.model.add_child(frm.doc, "Stock Entry Detail", "items");
								frappe.model.set_value(row.doctype, row.name, 'item_code', item_row['item_code']);
								frappe.model.set_value(row.doctype,row.name,'item_name',item_row['item_name']);
								frappe.model.set_value(row.doctype, row.name, 'qty', item_row['picked_qty']);
								frappe.model.set_value(row.doctype, row.name, 'uom', item_row['stock_uom']);
								frappe.model.set_value(row.doctype, row.name, 'stock_uom', item_row['stock_uom']);
								frappe.model.set_value(row.doctype, row.name, 'conversion_factor', 1);
								frappe.model.set_value(row.doctype, row.name, 't_warehouse',item_row['t_warehouse']);
								frappe.model.set_value(row.doctype, row.name, 'engineering_revision',item_row['engineering_revision']);
							}
						});
					}
				}
			})
		}
	}
})