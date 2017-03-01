#-*- coding: utf-8 -*- 
from openerp import models, fields, api

class InecodeTask(models.Model):
    _name = 'codeine.task'
    place = fields.Char('Place', required=True)
    code = fields.Char('Code', required=True)