# -*- coding: utf-8 -*-
{
    'name': "ost_sales_auto_sequence",

    'summary': """
        ost_sales_auto_sequence""",

    'description': """
        Sales Order Line Auto Sequence
    """,

    'author': "Oliver Yuan",
    'website': "http://www.openstone.cn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}