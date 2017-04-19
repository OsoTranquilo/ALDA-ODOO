# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Wizard(models.TransientModel):
    _name = 'checkin.wizard'

    def default_enter_date(self):        
        if 'reservation_id' in self.env.context:
            reservation = self.env['hotel.reservation'].search([('id','=',self.env.context['reservation_id'])])
            return reservation.checkin
        return False

    def default_exit_date(self):        
        if 'reservation_id' in self.env.context:
            reservation = self.env['hotel.reservation'].search([('id','=',self.env.context['reservation_id'])])
            return reservation.checkout
        return False

    def default_reservation_id(self):        
        if 'reservation_id' in self.env.context:
            reservation = self.env['hotel.reservation'].search([('id','=',self.env.context['reservation_id'])])
            return reservation
        return False        

    def default_partner_id(self):        
        if 'reservation_id' in self.env.context:
            reservation = self.env['hotel.reservation'].search([('id','=',self.env.context['reservation_id'])])
            return reservation.partner_id
        return False

    def default_cardex_ids(self):       
        if 'reservation_id' in self.env.context:
            reservation = self.env['hotel.reservation'].search([('id','=',self.env.context['reservation_id'])])
            return reservation.cardex_ids






    cardex_ids = fields.Many2many('cardex', 'reservation_id', default=default_cardex_ids)
    partner_id = fields.Many2one('res.partner', default=default_partner_id)
    reservation_id = fields.Many2one('hotel.reservation', default=default_reservation_id, readonly=True)
    #ine_room_id = fields.Many2one('code_ine', help='Room type in INE statistics.', required=True)
    enter_date = fields.Date( default=default_enter_date, required=True)
    exit_date = fields.Date( default=default_exit_date, required=True)
    poldocument_cardex = fields.Char('Document number', related='partner_id.poldocument')