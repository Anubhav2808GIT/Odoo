{
    'name': 'Hospital Management Test',
    'version': '1.0.1',
    'category': 'Hospital',
    'author': 'Anubhav',
    'summary': 'System for Hospital Management',
    'description': 'This is a system for Hospital Management',
    'depends': ['mail', 'product'],  # The list of modules that must install before installing the module
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/appointment_view.xml',
    ],  # contains all other data files with the module's initial data
    'demo': [],  # contains data files with demonstration data
    'installable': True,  # works in odoo 14
    'auto_install': False,
    'application': True,  # to include our module in the app list
    'sequence': -100,  # to bring our module on top of app list
    'icon': '/om_hospital/static/description/icon.png',
    'license': 'LGPL-3',
}
