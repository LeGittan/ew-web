# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ew_odoo_apps(models.Model):
#     _name = 'ew_odoo_apps.ew_odoo_apps'
#     _description = 'ew_odoo_apps.ew_odoo_apps'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
