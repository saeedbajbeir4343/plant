# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
'name': 'Plant Nursery',
'version': '1.0',
'category': 'Tools',
'summary': 'Plants and customers management',
'depends': ['base','web','mail','event'],
# 'depends': ['base'],
'data': [
    
'security/security.xml', 
'security/ir.model.access.csv',
'views/nursery_views.xml',



],
'demo': [
# 'data/demo.xml',
],
'css': [],
'installable': True,
'auto_install': False,
'application': True,
}