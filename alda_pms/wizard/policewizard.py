# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging
_logger=logging.getLogger(__name__)


class Wizard(models.TransientModel):
    _name = 'police.wizard'

    @api.one
    def generate_file(self):
        recordset = self.env['cardex'].search([('enter_date','=',self.env.context['enter_date'])
        content = ""
        for line in recordset :
            content += line.enter_date

        content += self.partner_id.poldocument
        content += """
"""
        content += self.partner_id.firstname
        content += """
"""
        content += self.partner_id.lastname
        content += """
"""
        content += self.reservation_id.reservation_no
        content += """
"""
        content += self.enter_date
        content += """
"""
        content += self.exit_date

        return self.write({
            'txt_filename': 'file.txt',
            'txt_binary': base64.encodestring(content)
        })



    partner_id_police = fields.Many2one('res.partner', default=default_partner_id)
    reservation_id_police = fields.Many2one('hotel.reservation', default=default_reservation_id, readonly=True)
    enter_date_police = fields.Date( default=default_enter_date, required=True)
    exit_date_police = fields.Date( default=default_exit_date, required=True)

    txt_filename = fields.Char()
    txt_binary = fields.Binary()