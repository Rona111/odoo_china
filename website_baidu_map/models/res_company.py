# _*_ coding: utf-8 _*_
from openerp import models, fields, api


class Company(models.Model):
    _inherit = "res.company"

    longitude = fields.Char()
    latitude = fields.Char()
