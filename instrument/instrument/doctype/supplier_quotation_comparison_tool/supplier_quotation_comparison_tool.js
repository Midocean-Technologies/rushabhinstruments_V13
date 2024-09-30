// // Copyright (c) 2024, instrument and contributors
// // For license information, please see license.txt

frappe.ui.form.on("Supplier Quotation Comparison Tool", "create_purchase_order", function(frm, cdt, cdn) {
  var child_data=[]
  let selected = frm.get_selected()
  selected.supplier_quotation_comparison_table.forEach(function(item, index, array) {
    let row = locals["Supplier Quotation Comparison Table"][item]
      if(row.purchase_order_created == 1){
        frappe.throw("Purchase Order Already Created for Selected Row")
      }
        child_data.push({
        "supplier_quotation":row.supplier_quotation,
        "supplier":row.supplier,
        "item_code":row.item_code,
        "quotation_qty":row.rate,
        "rate":row.rate,
        "material_request":row.material_request
    });
  });
  // console.log(selected)
                const fields = [{
                    label: 'Items',
                    fieldtype: 'Table',
                    fieldname: 'items',
                    description: __(''),
                    fields: [
                      {
                        fieldtype: 'Link',
                        options:'Supplier Quotation',
                        label: __('Supplier Quotation'),
                        fieldname: 'supplier_quotation',
                        in_list_view: 1
                      },
                      {
                        fieldtype: 'Link',
                        fieldname: 'supplier',
                        options:'Supplier',
                        label: __('Supplier'),
                        in_list_view: 1
                      },
                      {
                        fieldtype: 'Link',
                        fieldname: 'item_code',
                        options:'Item',
                        label: __('Item Code'),
                        in_list_view: 1
                      },
                     
                      {
                        fieldtype: 'Float',
                        fieldname: 'purchase_qty',
                        label: __('PUrchase Qty'),
                        in_list_view: 1
                      },
                      {
                        fieldtype: 'Date',
                        fieldname: 'required_by',
                        label: __('Required By'),
                        in_list_view: 1
                    },
                    {
                      fieldtype: 'Currency',
                      fieldname: 'rate',
                      label: __('Rate'),
                      in_list_view: 1
                  },
                  {
                    fieldtype: 'Float',
                    fieldname: 'quotation_qty',
                    label: __('Quotation Qty'),
                    in_list_view: 1
                  },
                 
                    {
                      fieldtype: 'Link',
                      fieldname: 'material_request',
                      options:'Material Request',
                      label: __('Material Request'),
                      in_list_view: 1
                  },
                    ],
                    data: child_data,
                    get_data: () => {
                        return child_data
                    },
                }]
                var d = new frappe.ui.Dialog({
                    title: __('Create Purchase Order'),
                    fields: fields,
                    primary_action: function() {
                        var data = {items: d.fields_dict.items.grid.data};
                        frm.call({
                            doc: frm.doc,
                            method: 'make_bulk_item_purchase_order',
                            args: {
                                items: data,
                            },
                            freeze: true,
                            callback: function(r) {
                                console.log(r)
                                if(r.message[0] == 1){
                                  selected.supplier_quotation_comparison_table.forEach(function(item, index, array) {
                                    let row = locals["Supplier Quotation Comparison Table"][item]
                                    frappe.model.set_value("Supplier Quotation Comparison Table", "item", "purchase_order_created", 1);
                                    frappe.model.set_value("Supplier Quotation Comparison Table", "item", "purchase_order", r.message[1]);
                                  });
                                  frm.save();
                                  frappe.msgprint("Purchase Order Created Successfully");
                                }
                                d.hide();
                                frm.reload_doc();
                            }
                        });
                    },
                     primary_action_label: __('Submit')
                     });
                d.show();
                d.$wrapper.find('.modal-dialog').css("width", "90%");
                d.$wrapper.find('.modal-dialog').css("max-width", "90%");
            }
       );

frappe.ui.form.on("Supplier Quotation Comparison Tool", "sort_data", function (frm, cdt, cdn) {

    let notes = frm.doc.supplier_quotation_comparison_table || [];
    if(frm.doc.sort_by == "Rate"){
      notes.sort(function (a, b) {
        return a.rate < b.rate ? 1 : -1;
      });
    }

    if(frm.doc.sort_by == "Lead Time Days"){
      notes.sort(function (a, b) {
        return a.lead_time_days < b.lead_time_days ? 1 : -1;
      });
    }

    if(frm.doc.sort_by == "Last Purchase Rate"){
      notes.sort(function (a, b) {
        return a.last_purchase_rate < b.last_purchase_rate ? 1 : -1;
      });
    }

    if(frm.doc.sort_by == "Lead Time Date"){
      notes.sort(function (a, b) {
        return new Date(a.lead_time_date) - new Date(b.lead_time_date);
      });
    }

    if(frm.doc.sort_by == "Supplier"){
      notes.sort(function (a, b) {
        return a.supplier.localeCompare(b.supplier);
      });
    }


    frm.doc.supplier_quotation_comparison_table = []
    frm.doc.supplier_quotation_comparison_table = notes
    frm.refresh_field("supplier_quotation_comparison_table")
});
 

frappe.ui.form.on("Supplier Quotation Comparison Table", "make_purchase_order", function (frm, cdt, cdn) {

  var row = locals[cdt][cdn];
  if(row.purchase_order_created == 1){
    frappe.msgprint("Purchase Order Already Created")
  }else{
  let d = new frappe.ui.Dialog({
    title: 'Enter details',
    fields: [
        {
            label: 'Qty',
            fieldname: 'qty',
            fieldtype: 'Float',
  
        },

        {
            label: 'Required Date',
            fieldname: 'required_date',
            fieldtype: 'Date',
  
        },
        
    ],
    primary_action_label: 'Submit',
    primary_action: function () {
      var qty = d.get_values().qty
      var required_date = d.get_values().required_date
      frm.call({
      doc: frm.doc,
      method: 'make_single_item_purchase_order',
      args: {
          item_code: row.item_code,
          item_name: row.item_name,
          uom: row.uom,
          rate: row.rate,
          supplier: row.supplier,
          material_request: row.material_request,
          min_required_qty: row.min_required_qty,
          required_date: required_date,
          qty: qty,

      },
      callback: function (r) {
        if(r.message[0] == 1){
          // row.set_value("purchase_order_created", true);
          frappe.model.set_value(cdt, cdn, "purchase_order_created", 1);
          frappe.model.set_value("Supplier Quotation Comparison Table", "item", "purchase_order", r.message[1]);
          frm.save()
          frappe.msgprint("Purchase Order Created Successfully");
          frm.refresh()
        }else{
          frappe.msgprint("Something went wrong");
        }
      }
    });
      d.hide();
    },
});

d.show();
}
})


