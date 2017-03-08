# -*- coding: utf-8 -*-

from openerp import models, fields, api

class category_tourism(models.Model):
    _name = 'category_tourism.category_tourism'
    _rec_name = 'category'


    @api.depends('name','tipo')
    def category_comp(self):
        for record in self:
            record.category = record.tipo + "(" + record.name + ")"


    name = fields.Char('Category', required=True)
    tipo = fields.Char('Category type', required=True)
    category = fields.Char(compute='category_comp')