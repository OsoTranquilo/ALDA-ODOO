# -*- coding: utf-8 -*-
{
    'name': "Category in Tourism",
    'summary': """
        Hotel category in the Ministry of Tourism. Used for INE statistics.
        Alda PMS""",
    'description': """
        Hotel category in the Ministry of Tourism. Used for INE statistics.
    """,
    'author': "Jose Luis Algara",
    'website': "http://www.aldahotels.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'AldaPMS',
    'version': '9.0.1.0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/category_tourism.category_tourism.csv'
    ],
}