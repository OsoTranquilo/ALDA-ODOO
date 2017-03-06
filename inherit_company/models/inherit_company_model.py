#-*- coding: utf-8 -*- 
from openerp import models, fields, api

class Inherit_res_company(models.Model):
    _inherit = 'res.company'
    tourism = fields.Char('Tourism number')
    category = fields.Char('Hotel Category')
    rooms = fields.Integer('Rooms Available')
    seats = fields.Integer('Beds available')
    permanentstaff = fields.Integer('Permanent Staff')
    eventualstaff = fields.Integer('Eventual Staff')
    police = fields.Char('Police number',
        size=10)
    