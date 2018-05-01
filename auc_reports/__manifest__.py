# -*- coding: utf-8 -*-
{
    'name': 'AUC Reports',
    'category': 'All',
    'description':"""
AUC custom reports. 
""",
    'author': 'SisNe, SRL',
    'website': 'https://sisne.do/',
    'version': '1.0.1',
    'depends': ['account'],
    'data' : [
        'views/report_invoice.xml',
        'views/layout_templates.xml',
    ],
    'qweb': [],
    'auto_install': False,
    'installable': True,
    'application': True,

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: