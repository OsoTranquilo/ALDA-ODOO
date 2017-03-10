#-*- coding: utf-8 -*- 

from openerp import models, fields, api

class IneCode(models.Model):
    _name = 'cardex'


    partner_id = fields.Many2one('res.partner')
    reserva_id = fields.Many2one('hotel.reservation')
    ine_room_id = fields.Many2one('code_ine', help='Room type in INE statistics.')
