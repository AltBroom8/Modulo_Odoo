# -*- coding: utf-8 -*-
{
    'name': "com_int",

    'summary': """
        In this module you will be able to manage the shipping
        of the packages of your company.""",

    'description': """
        In this module, you will gain comprehensive capabilities 
        to effectively oversee and streamline the shipping processes
        within your company. This module is designed to empower you with 
        the tools and knowledge necessary to manage the entire lifecycle of package shipping seamlessly.

        You will delve into various aspects of shipping management, including but not limited to, 
        order processing, packaging, labeling, and carrier selection. 
        Understanding these key elements will enable you to make 
        informed decisions that optimize the shipping workflow, 
        ensuring timely and cost-effective delivery of packages.
    """,

    'author': "Carlos(Admin)",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
}
