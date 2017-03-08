#-*- coding: utf-8 -*- 
from openerp import models, fields, api

class IneCode(models.Model):
    _name = 'code_ine'
    _rec_name = 'inecode'

    @api.depends('place','code')
    def inecode_comp(self):
        for record in self:
            subcode = record.code
            if len(record.code)>3:
                subcode = 'ESP'
            record.inecode = record.place + " (" + subcode + ")"


    place = fields.Char('Place', required=True)
    code = fields.Char('Code', required=True)
    inecode = fields.Char('INE Code',compute='inecode_comp')