{
    'name': 'To-Do Application',
    'description': 'Manage personal to-do  tasks',
    'author': 'Wildy Estephan',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_menu.xml',
        'views/todo_view.xml',
        'views/res_partner_view.xml',
             ],
    'application': True,
}