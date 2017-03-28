#-*- coding: utf-8 -*- 

from openerp import models, fields, api

class Cardex(models.Model):
    _name = 'cardex'


    @api.constrains('exit_date')
    def validation_dates(self):
        if self.exit_date < self.enter_date:
             raise models.ValidationError('Departure date (%s) is prior to arrival on %s' % (self.exit_date, self.enter_date))

    def validation_under_age(self):
        diferencia = self.birthdate_date - datetime.datetime.now().time()
        if self.birthdate_date <> Null:
            raise models.ValidationError('He is under 16 years old, he is only %s years old.' % (diferencia))

    
    def default_reservation_id(self):        
        if 'reservation_id' in self.env.context:
            reservation = self.env['hotel.reservation'].search([('id','=',self.env.context['reservation_id'])])
            return reservation
        return False

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

    def default_partner_id(self):        
        if 'reservation_id' in self.env.context:
            reservation = self.env['hotel.reservation'].search([('id','=',self.env.context['reservation_id'])])
            return reservation.partner_id
        return False

    partner_id = fields.Many2one('res.partner', default=default_partner_id)
    reservation_id = fields.Many2one('hotel.reservation', default=default_reservation_id, readonly=True)
    ine_room_id = fields.Many2one('code_ine', help='Room type in INE statistics.', required=True)
    enter_date = fields.Date( default=default_enter_date, required=True)
    exit_date = fields.Date( default=default_exit_date, required=True)