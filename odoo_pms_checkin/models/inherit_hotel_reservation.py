#-*- coding: utf-8 -*- 

from openerp import models, fields, api

class Inherit_hotel_reservation(models.Model):
    _inherit = 'hotel.reservation'

    cardex_ids = fields.One2many('cardex', 'reservation_id')