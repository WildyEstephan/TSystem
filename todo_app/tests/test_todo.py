from odoo.tests.common import TransactionCase

class TestTodo(TransactionCase):

    def test_create(self):
        "Create a simple Todo"
        Todo = self.env['todo.task']
        task = Todo.create({'name': 'Test Task'})
        self.assertEqual(task.is_done, False)

    def test_clear_done(self):
        "Clear Done sets Todo to not active"
        Todo = self.env['todo.task']
        task = Todo.create({'name': 'Test Dark'})
        task.do_clear_done()
        self.asserFalse(True)