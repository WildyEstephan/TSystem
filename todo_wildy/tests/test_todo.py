from odoo.tests.common import TransactionCase

class TestTodo(TransactionCase):

    def test_create(self):
        "Create a simple Todo"
        Todo = self.env['todo.wildy']
        task = Todo.create({'name': 'Test Task'})
        self.assertEqual(task.is_done, False)

    def test_clear_done(self):
        "Clear Done sets Todo to not active"
        Todo = self.env['todo.wildy']
        task = Todo.create({'name': 'Test Tark'})
        task.do_clear_done()
        self.asserFalse(task.active)

        print('Your test was succesfull!')

    def setUp(self, *args, **kwargs):
        result= super(TestTodo, self).setUp(*args, **kwargs)

        user_demo = self.env.ref('base.user_demo')
        self.env =self.env(user=user_demo)
        return result
