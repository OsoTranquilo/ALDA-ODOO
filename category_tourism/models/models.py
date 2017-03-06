# -*- coding: utf-8 -*-

from openerp import models, fields, api

class category_tourism(models.Model):
    _name = 'category_tourism.category_tourism'
    category = fields.Char('Category', required=True)
    tipo = fields.Char('Category type', required=True)
    def name_get(self):
        result = []
        for record in self:result.append((record.id,u"%s (%s)" % (record.tipo, record.category)))
        return result