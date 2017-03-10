#-*- coding: utf-8 -*- 
from openerp import models, fields, api

class Inherit_res_company(models.Model):
    _inherit = 'res.company'
    tourism = fields.Char('Tourism number', help='Registration number in the Ministry of Tourism. Used for INE statistics.')
    rooms = fields.Integer('Rooms Available',default=0, help='Used for INE statistics.')
    seats = fields.Integer('Beds available',default=0, help='Used for INE statistics.')
    permanentstaff = fields.Integer('Permanent Staff',default=0, help='Used for INE statistics.')
    eventualstaff = fields.Integer('Eventual Staff',default=0, help='Used for INE statistics.')
    police = fields.Char('Police number',size=10, help='Used to generate the name of the file that will be given to the police.')
    category_id = fields.Many2one('category',
            help='Hotel category in the Ministry of Tourism. Used for INE statistics.')
    ine_id = fields.Many2one('code_ine',
            help='Hotel category in the Ministry of Tourism. Used for INE statistics.')