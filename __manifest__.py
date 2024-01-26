# -*- coding: utf-8 -*-
{
    'name': "manteni",

    'summary': """
        Example module made to teach Odoo""",

    'description': """
        Example module made to teach Odoo
        Industrial maintenance
    """,

    'author': "Mikel López Villarroya",
    'website': "http://www.github.com/mlvillarroya",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Industrial',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/partner.xml',
        'views/views.xml',
        'views/templates.xml',
        'report/manteni_report.xml',
        'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}