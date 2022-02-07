# -*- coding: utf-8 -*-
# Copyright (c) 2021, Pavithra M R and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CaseMaster(Document):
	pass

@frappe.whitelist()
def get_case_details(case_proposal):
	print("child",case_proposal)	
	get_case_data=frappe.db.sql("""select `tabChild Master`.`name`,`tabChild Master`.`first_name`,`tabChild Master`.`middle_name`,`tabChild Master`.`last_name`,`tabChild Master`.`date_of_birth`,`tabChild Master`.`gender`,`tabCase Proposal`.`display_address`,`tabCase Proposal`.`caregiver`,`tabCase Proposal`.`name_of_caregiver`,`tabCase Proposal`.`saathiproposed_saathi`,`tabCase Proposal`.`name_of_saathi`,`tabCase Proposal`.`proposed_coordinator`,`tabCase Proposal`.`name_of_coordinator`,`tabCase Proposal`.`case_type` from `tabChild Master` join `tabCase Proposal` on `tabCase Proposal`.`child` = `tabChild Master`.`name` and `tabCase Proposal`.`name`='"""+case_proposal+"""' """, as_dict=1)
	print("pppppp",get_case_data)
	return get_case_data

