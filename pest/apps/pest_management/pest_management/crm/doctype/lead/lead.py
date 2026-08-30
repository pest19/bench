# Copyright (c) 2026, Md sharieff and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Lead(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		attachments: DF.Attach | None
		company: DF.Data | None
		customer_name: DF.Link
		email: DF.Data | None
		interested_services: DF.Data | None
		lead_source: DF.Literal["Website", "Phone", "Email", "Referral", "Social", "Media", "Advertisement", "Walk-in", "Other"]
		lead_status: DF.Literal["Open", "Contacted", "Survey Scheduled", "Qualified", "Quotation Sent", "Won", "Lost"]
		notes: DF.Text | None
		phone: DF.Phone | None
		property: DF.Data
		sales_executive: DF.Link | None
		timeline: DF.SmallText | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Lead"
