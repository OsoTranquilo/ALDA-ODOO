#-*- coding: utf-8 -*- 
from openerp import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    #@api.model
    #def name_search(self, name, args=None, operator='ilike', limit=100):
        # args = args or []
        # if name:
        #     # Be sure name_search is symetric to name_get
        #     name = name.split(' / ')[-1]
        #     args = [('name', operator, name)] + args
        # categories = self.search(args, limit=limit)
        # return categories.name_get()



    poldocument = fields.Char('Document number', required=True)
    polexpedition = fields.Date('Document expedition date', required=True)
    documenttype = fields.Selection([
        ('D', 'DNI'),
        ('P', 'Pasaporte'),
        ('C', 'Permiso de Conducir'),
        ('I', 'Carta o Doc. de Identidad'),
        ('N', 'Permiso Residencia Español'),
        ('X', 'Permiso Residencia Europeo')],
        help='blabla',
        required=True,
        string='Document type')

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


    # Validation for expedicion anterior al nacimiento
    # @api.constrains('x')
    # Pendiente

    # Validation for Tipo de documento no valido para Extranjero
    # @api.constrains('x')
    # Pendiente


    # Validation for Nacionalidad erronea
    # @api.constrains('x')
    # Pendiente


    # Validation for DNI/Permiso conducir erroneo
    # @api.constrains('x')
    # Pendiente


    # Validation for Fecha anterior a 1900
    # @api.constrains('x')
    # Pendiente


    # Validation for Fecha posterior a hoy
    # @api.constrains('x')
    # Pendiente


    # Validation for unicos caracteres permitos numeros y letras
    # @api.constrains('x')
    # Pendiente


    birthdate_date = fields.Date("Birthdate", required=True)
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female')],
                                required=True)
    #documenttype = fields.Selection([('D', 'DNI'),
                                      # ('P', 'Pasaporte'),
                                      # ('C', 'Permiso de Conducir'),
                                      # ('I', 'Carta o Doc. de Identidad'),
                                      # ('N', 'Permiso Residencia Español'),
                                      # ('X', 'PermisoResidenciaEuropeo')],                                ],
                                      # required=True)