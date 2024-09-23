// // Copyright (c) 2024, instrument and contributors
// // For license information, please see license.txt

frappe.ui.form.on("Supplier Quotation Comparison Tool", {

});

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
 