// Copyright (c) 2023, ideen and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vendor  details', {
	refresh: function(frm) {
		frm.events.approve_reject(frm)

	},
	approve_reject:function(frm){
		if(frm.doc.status=="New"){
			console.log("new");
			frm.page.add_action_item("Approve", () => {
			
				frm.doc.status = "Approved";
			
				frm.dirty();
				frm.save();
			
				
			  });
	
			  frm.page.add_action_item("Reject", () => {
				
				frm.doc.status = "Rejected";
			
				frm.dirty();
				frm.save();
			  });
			

		}
		else{
			frm.disable_form()
		}
		
		
	}
});
