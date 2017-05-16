#-*- coding: utf-8 -*- 

from openerp import models, fields, api

class Inherit_hotel_reservation(models.Model):
    _inherit = 'hotel.reservation'

    cardex_ids = fields.One2many('cardex', 'reservation_id')
    cardex_count = fields.Integer('Cardex counter', compute='_compute_cardex_count')
    cardex_pending = fields.Boolean('Cardex Pending', compute='_compute_cardex_pending')
    cardex_pending_num = fields.Integer('Cardex Pending', compute='_compute_cardex_pending')
    state = fields.Selection(selection_add=[('checkin', 'Checkin')])
    folio_count = fields.Integer('Folio counter', compute='_compute_folio_count')

    @api.multi
    def action_reservation_checkout(self):
	for r in self:        
		self.state = 'done'

    def _compute_cardex_count(self):
        self.cardex_count = len(self.cardex_ids)

    def _compute_folio_count(self):
        self.folio_count = len(self.folio_id)

    def _compute_cardex_pending(self):
        self.cardex_pending_num = self.adults + self.children - len(self.cardex_ids)
        if (self.adults + self.children - len(self.cardex_ids))<=0:
            self.cardex_pending = False
        else:
            self.cardex_pending = True

    def _create_folio(self):
	reservations_confirm = self.search([('state','=','confirm')])
	reservations_checkin = self.search([('state','=','checkin')])
	folio = super(Inherit_hotel_reservation, self)._create_folio()
	reservations_confirm.write({'state': 'confirm'})
	reservations_checkin.write({'state': 'checkin'})
