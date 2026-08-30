# Copyright (c) 2026, Md sharieff and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Survey(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from pest_management.crm.doctype.survey_photo.survey_photo import SurveyPhoto

		affected_area: DF.Float
		estimated_cost: DF.Currency
		gps: DF.Geolocation | None
		lead: DF.Link
		problem_category: DF.Data | None
		property: DF.Data
		property_photos: DF.Table[SurveyPhoto]
		recommendations: DF.Text | None
		remarks: DF.Text | None
		severity: DF.Literal["Low", "Medium", "High", "Critical"]
		signature: DF.Signature | None
		suggested_chemical: DF.Data | None
		survey_date: DF.Date
		surveyor: DF.Link
		voice_note: DF.Attach | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Survey"
