#-*- coding: utf-8 -*- 
from openerp import models, fields, api

class Inherit_res_company(models.Model):
    _inherit = 'res.company'
    tourism = fields.Char('Tourism', required=True)
    category = fields.Char('Category', required=True)
    rooms = fields.Char('Rooms', required=True)
    seats = fields.Char('Seats', required=True)
    permanentstaff = fields.Char('Permanent Staff', required=True)
    eventualstaff = fields.Char('Eventual Staff', required=True)
    policia = fields.Char('Police', required=True)