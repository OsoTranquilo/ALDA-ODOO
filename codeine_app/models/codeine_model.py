#-*- coding: utf-8 -*- 
from openerp import models, fields, api

class InecodeTask(models.Model):
    _name = 'codeine.task'
    place = fields.Char('Place', required=True)
    code = fields.Char('Code', required=True)
    def name_get(self):
        result = []
        for record in self:result.append((record.id,u"%s (%s)" % (record.place, record.code)))
        return result