from odoo import models, fields, api


class EWApp(models.Model):
    _name = 'ew.app'
    _description = 'A App model for EW internal and external sales & marketing'

    name = fields.Char(string='Name', required=True)
    description = fields.Char(string='Description')
    price_per_month = fields.Integer(string='Price per month')
    icon = fields.Binary(string='Icon')