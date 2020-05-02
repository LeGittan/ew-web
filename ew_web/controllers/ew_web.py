from odoo import http
import json
import re

class EwOdooApps(http.Controller):
    @http.route('/api/apps/', auth='public',cors="*", csrf=False)
    def index(self):
        odoo_apps = http.request.env['ew.app'].sudo().search([])
        name = []
        description = []
        price_per_month = []
        icon_data = []
        for a in odoo_apps:
            name.append(a.name)
            description.append(a.description)
            price_per_month.append(a.price_per_month)
            icon_data.append(str(a.icon))
        pre_output = [{"name": n, "description": d, "price_per_month": p, "icon": i, "active": False} for n, d, p,
        i in zip(name, description, price_per_month, icon_data)]
        output = json.dumps(pre_output)
        return output