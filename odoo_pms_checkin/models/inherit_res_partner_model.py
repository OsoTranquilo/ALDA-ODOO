#-*- coding: utf-8 -*- 
from openerp import models, fields, api

class Inherit_res_partner(models.Model):
    _inherit = 'res.partner'

    # Validation for under age clients (16 years old)
    @api.constrains('birthdate_date')
    def validation_under_age(self):
        from datetime import datetime, timedelta 

        years = str(datetime.now().date() - timedelta(days=365*16+4))
        limit_date = datetime.strptime(years, "%Y-%m-%d")
        birth_date = datetime.strptime(self.birthdate_date, '%Y-%m-%d')
        if limit_date < birth_date:
            raise models.ValidationError(
                'The client is under 16 years old. Data collection is not performed for those born before %s.' % (years))


    # Validation for under age clients (16 years old)
    # @api.constrains('birthdate_date')
    # Pendiente


    birthdate_date = fields.Date("Birthdate", required=True)