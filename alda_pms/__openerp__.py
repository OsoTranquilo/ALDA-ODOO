# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2017 Solucións Aloxa S.L. <info@aloxa.eu>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

# TODO: Meter el capitulo de 

{
    'name': 'Alda PMS',
    'version': '9.0.0.2',
    'author': "Jose Luis Algara",
    'website': "http://www.aldahotels.com",
    'category': 'AldaPMS',
    'summary': "",
    'description': "",
    'depends': [
        'stock',
        'hotel_reservation',
        'partner_contact_gender',
        'partner_contact_birthdate',
        'partner_firstname',
    ],
    'data': [
        'wizard/checkinwizard.xml',
        'views/cardex.xml',
        'views/cardex_partner.xml',
        'views/category.xml',
        'views/code_ine.xml',
        'views/inherit_hotel_reservation.xml',
        'views/inherit_res_company.xml',
        #'views/inherit_res_partner_id_number_view.xml',

        'data/code_ine.csv',
        'data/category.csv',
        #'data/res.partner.id_category.csv',
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}