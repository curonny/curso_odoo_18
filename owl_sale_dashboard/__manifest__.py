# -*- coding: utf-8 -*-
{
    'name': "Sale dashboard",

    'summary': "Sale dashboard",

    'description': """
Sale dashboard
    """,

    'author': "Ronny Montano",
    'category': 'Uncategorized',
    'version': '18.0.0.0.1',

    'depends': ['sale_management', "sale"],

    'data': [
        "views/sale_views.xml",
    ],
    'demo': [
    ],
    'assets': {
        'web.assets_backend': [
            'owl_sale_dashboard/static/src/views/*',
        ],
    },
}
