#-*- coding: utf-8 -*- 
from openerp import models, fields, api

class Inherit_res_company(models.Model):
    _inherit = 'res.company'
    tourism = fields.Char('Tourism number')
    category = fields.Char('Hotel Category')
    rooms = fields.Char('Rooms Available')
    seats = fields.Char('Beds available')
    permanentstaff = fields.Char('Permanent Staff')
    eventualstaff = fields.Char('Eventual Staff')
    police = fields.Char('Police number')
    