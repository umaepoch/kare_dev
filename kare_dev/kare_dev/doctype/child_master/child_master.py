# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils.file_manager import save_file
from frappe.contacts.address_and_contact import load_address_and_contact, delete_contact_and_address
import base64
import json

class ChildMaster(Document):
	def onload(self):
		"""Load address and contacts in `__onload`"""
		load_address_and_contact(self)

	def on_trash(self):
		delete_contact_and_address('Child Master', self.name)

@frappe.whitelist()
def create_image_url(doc):
	try:
		img = json.loads(doc)
		b64 = base64.b64decode(img['data'])
		first_name = img['first_name']
		image_name = img['image_name']
		doctype = img['doctype']
		doc_name = img['doc_name']

		if img:
			sf = save_file(first_name+"_"+image_name+".png", b64, doctype, doc_name)
			return {"SC": True, "file_url":sf.file_url}

		return {"SC": False}
	except Exception as ex:
		return {"EX": ex}

@frappe.whitelist()
def get_caregiver_Add(name_of_child):
	get_caregiver_address=frappe.db.sql("""select `tabAddress`.`address_title`,`tabAddress`.`address_line1`,`tabAddress`.`address_line2`,`tabAddress`.`city`,`tabAddress`.`state`,`tabAddress`.`country`, `tabAddress`.`pincode`, `tabAddress`.`phone` from `tabAddress` where `tabAddress`.`address_title`='"""+name_of_child+"""' """, as_dict=1)
	print("get_caregiver_address",get_caregiver_address)
	return get_caregiver_address

#@frappe.whitelist()
#def set_caregiver_name(name,child_name,child_record):
#	print("name",name)
#	print("name",child_name)
#	print("child_record",child_record)
#	frappe.clear_cache()
#	frappe.client.set_value("Child Master",child_record,"motherguardiancaregivers_name",name)
#	frappe.db.commit()
	
@frappe.whitelist()
def get_care_number(name):
	#get_care_num=frappe.db.sql("""select ca.name,ca.child_name from `tabCaregiver Master` as ca inner join `tabChild Master` as ch where ch.name=ca.child_name and ch.name='"""+name+"""' """, as_dict=1)
	get_care_num=frappe.db.sql("""select ca.name,ca.child_name,ca.first_name,ca.middle_name,ca.last_name from `tabCaregiver Master` as ca inner join `tabChild Master` as ch where ch.name=ca.child_name and ch.name='"""+name+"""' """, as_dict=1)
	print("get_care_num",get_care_num)
	return get_care_num

#@frappe.whitelist()
#def get_filter_bankac(child):
#	#get_child_holder_record=frappe.db.sql("""select account_holder_record from `tabBankAC`""", as_dict=1)
#	get_child_holder_record=frappe.db.sql("""select ch.name,ba.name,ba.account_holder_record from `tabChild Master` as ch inner join `tabBankAC` as ba where ch.name=ba.account_holder_record and ch.name ='"""+child+"""' """, as_dict=1)
#	print("get_child_holder_record",get_child_holder_record)
#	return get_child_holder_record