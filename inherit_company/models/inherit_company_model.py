#-*- coding: utf-8 -*- 
from openerp import models, fields, api

class Inherit_res_company(models.Model):
    _inherit = 'res.company'
    tourism = fields.Char('Tourism number')
    category = fields.Char('Hotel Category')
    rooms = fields.Integer('Rooms Available',default=0)
    seats = fields.Integer('Beds available',default=0)
    permanentstaff = fields.Integer('Permanent Staff',default=0)
    eventualstaff = fields.Integer('Eventual Staff',default=0)
    police = fields.Char('Police number',size=10)
    