from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Report"),
			"items": [
			    {
					"type": "report",
					"name": "Accounts Receivable",
					"doctype": "Sales Invoice",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Accounts Payable",
					"doctype": "Purchase Invoice",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "List Accounts",
					"doctype": "Jejak Finance",
					"is_query_report": True
				},
			]

		}

	]
