# Copyright (c) 2023, ideen and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.share import add as add_share

class Vendordetails(Document):
	def on_update(self):
		vendor_data=frappe.db.sql("""select name,din,mobile_number,pan_number from `tabVendor  details` where name !=%(name)s and ( din=%(din)s or pan_number=%(pan_number)s 
		or mobile_number=%(mobile_number)s)""",values={'din':self.din,'pan_number':self.pan_number,'mobile_number':self.mobile_number,'name':self.name},as_dict=1)
		print("vendor data",vendor_data)
		if vendor_data:
			self.reference=[]
			for d in vendor_data:
				description=[]
				if d.din==self.din:
					description.append("Din Number")
				if d.pan_number==self.pan_number:
					description.append("Pan Number")
				if d.mobile_number==self.mobile_number:
					description.append("Mobile Number")
				description_str = ', '.join(description)+" Duplicated"
				
				self.append('reference',{
					'reference':d['name'],
					'description':description_str 
				})
			
	
	def before_insert(self):
		vendor_data=frappe.db.sql("""select name,din,mobile_number,pan_number from `tabVendor  details` where  din=%(din)s or pan_number=%(pan_number)s 
		or mobile_number=%(mobile_number)s""",values={'din':self.din,'pan_number':self.pan_number,'mobile_number':self.mobile_number,'name':self.name},as_dict=1)
		print("vendor data",vendor_data)
		if vendor_data:
			self.reference=[]
			for d in vendor_data:
				description=[]
				if d.din==self.din:
					description.append("Din Number")
				if d.pan_number==self.pan_number:
					description.append("Pan Number")
				if d.mobile_number==self.mobile_number:
					description.append("Mobile Number")
				description_str = ', '.join(description)+" Duplicated"
				
				self.append('reference',{
					'reference':d['name'],
					'description':description_str 
				})
			


	
			