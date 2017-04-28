#-*- coding: utf-8 -*- 

from openerp import models, fields, api

class Inherit_hotel_reservation(models.Model):
    _inherit = 'hotel.reservation'

    cardex_ids = fields.One2many('cardex', 'reservation_id')
    cardex_count = fields.Integer('Cardex counter', compute='_compute_cardex_count')

    def _compute_cardex_count(self):
        self.cardex_count = len(self.cardex_ids)