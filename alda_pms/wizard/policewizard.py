# -*- coding: utf-8 -*-

from openerp import models, fields, api
import base64  
#import logging
#_logger=logging.getLogger(__name__)


class Wizard(models.TransientModel):
    _name = 'police.wizard'

    #partner_id_police = fields.Many2one('res.partner')
    #reservation_id_police = fields.Many2one('hotel.reservation')
    #enter_date_police = fields.Date()
    #exit_date_police = fields.Date()

    download_date = fields.Date('Date to generate the file',required=True)
    download_num = fields.Char('Correlative number',required=True,size=3)
    txt_filename = fields.Char()
    txt_binary = fields.Binary()

    @api.one
    def generate_file(self):
        recordset = self.env['cardex'].search([('enter_date','=',self.download_date)])



        content = "xxx " + self.download_date
        for line in recordset :
            content += self.download_date + "/"
            content += line.enter_date + "/"
            content += line.exit_date + "/"
            content += line.reservation_id + "/"
            content += line.partner_id.poldocument + "/"

#         content += self.partner_id.poldocument
#         content += """
# """
#         content += self.partner_id.firstname
#         content += """
# """
#         content += self.partner_id.lastname
#         content += """
# """
#         content += self.reservation_id.reservation_no
#         content += """
# """
#         content += self.enter_date
#         content += """
# """
#         content += self.exit_date
        content += """
"""
        company_obj = self.env['res.company']
        company_ids = company_obj.search([])

        return self.write({
            'txt_filename': 'pol_'+ company_ids[0].police +'.'+ self.download_num,
            'txt_binary': base64.encodestring(content)
            })
