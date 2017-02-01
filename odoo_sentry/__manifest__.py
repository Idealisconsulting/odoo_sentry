# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.
{
    'name': 'Sentry',
    'version': '2.0.0',
    'author': [
        'Mohammed Barsi',
        'Versada',
    ],
    'category': 'Extra Tools',
    'summary': 'Sentry integration with Odoo',
    'depends': [
        'base',
    ],
    'external_dependencies': {
        'python': [
            'raven',
        ]
    },
    'auto_install': False,
    'application': False,
}
