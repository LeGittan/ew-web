# -*- coding: utf-8 -*-
{
    'name': "ERPWare Odoo Apps configurator & pricing calculator",

    'summary': """
        Module for EW internal quotation creation and for EW website pricing calculator.""",

    'description': """
        Module for EW internal quotation creation and for EW website pricing calculator. The module adds the functionality
        of adding Odoo Apps with icon, description and monthly pricing. The module can then be added via the sales
        quotations to create nice quotations fast and easily. The module also creates a /api/apps endpoint 
        where the users can get the Odoo Apps as JSON.
    """,

    'author': "ERPWare Oy",
    'website': "http://www.erpware.fi",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/ew_apps_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
