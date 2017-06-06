#-*- coding: utf-8 -*- 

from openerp import models, fields, api

class Inherit_hotel_reservation(models.Model):
    _inherit = 'hotel.reservation'

    cardex_ids = fields.One2many('cardex', 'reservation_id')
    cardex_count = fields.Integer('Cardex counter', compute='_compute_cardex_count')
    cardex_pending = fields.Boolean('Cardex Pending', compute='_compute_cardex_pending')
    cardex_pending_num = fields.Integer('Cardex Pending', compute='_compute_cardex_pending')

    def _compute_cardex_count(self):
        self.cardex_count = len(self.cardex_ids)

    def _compute_cardex_pending(self):
        self.cardex_pending_num = self.adults + self.children - len(self.cardex_ids)
        if (self.adults + self.children - len(self.cardex_ids))<=0:
            self.cardex_pending = False
        else:
            self.cardex_pending = True


