# Copyright (c) 2026, Md sharieff and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Quotation(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from pest_management.crm.doctype.quotation_item.quotation_item import QuotationItem

		amended_from: DF.Link | None
		approval_date: DF.Datetime | None
		approval_remarks: DF.SmallText | None
		approved_by: DF.Link | None
		chemical_cost: DF.Currency
		customer: DF.Data | None
		discount: DF.Percent
		discount_amount: DF.Currency
		grand_total: DF.Currency
		gst: DF.Percent
		gst_amount: DF.Currency
		labour_cost: DF.Currency
		line_items: DF.Table[QuotationItem]
		payment_terms: DF.SmallText
		quotation_date: DF.Date
		service_package: DF.Data | None
		signature: DF.Signature | None
		subtotal: DF.Currency
		survey_reference: DF.Link
		validity: DF.Date
	# end: auto-generated types

	_DOCTYPE_NAME = "Quotation"
