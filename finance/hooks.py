# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "finance"
app_title = "Finance"
app_publisher = "ridhosribumi"
app_description = "App for managing finance"
app_icon = "octicon octicon-diff"
app_color = "#8DD57F"
app_email = "develop@ridhosribumi.com"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/finance/css/finance.css"
# app_include_js = "/assets/finance/js/finance.js"

# include js, css files in header of web template
# web_include_css = "/assets/finance/css/finance.css"
# web_include_js = "/assets/finance/js/finance.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "finance.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "finance.install.before_install"
# after_install = "finance.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "finance.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"finance.tasks.all"
# 	],
# 	"daily": [
# 		"finance.tasks.daily"
# 	],
# 	"hourly": [
# 		"finance.tasks.hourly"
# 	],
# 	"weekly": [
# 		"finance.tasks.weekly"
# 	]
# 	"monthly": [
# 		"finance.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "finance.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "finance.event.get_events"
# }
