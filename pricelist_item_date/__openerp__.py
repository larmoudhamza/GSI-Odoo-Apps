# coding: utf-8
# © 2017 David BEAL @ Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Pricelist Item Date - GRS',
    'summary': 'Keep product pricelist item used on sale order line',
    'version': '8.0.1.0.0',
    'author': 'GRS',
    'maintainer': 'GRS',
    'category': 'Sale',
    'depends': [
        'sale',
    ],
    'website': 'http://www.grscasablanca.com/',
    'data': [
        'views/sale_view.xml',
        'views/pricelist_item_view.xml',
    ],
    'installable': True,
    'license': 'AGPL-3',
}
