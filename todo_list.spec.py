import unittest
from datetime import datetime, timedelta
from todo_list import TodoList


class TestTodoList(unittest.TestCase):
    def test_createTodo(self):
        todo_list = TodoList()
        todo_list.create_todo('テスト', datetime.now() + timedelta(days=1))
        
        self.assertEqual(len(todo_list.get_todos()), 1)
        
    def test_deleteTodo(self):
        todo_list = TodoList()
        todo_list.create_todo('テスト', datetime.now() + timedelta(days=1))
        todo_list.delete_todo(0)
        
        self.assertEqual(len(todo_list.get_todos()), 0)
        
    def test_deleteTodoRaisesInvalidIdError(self):
        with self.assertRaises(Exception):
            todo_list = TodoList()
            todo_list.delete_todo(0)
        
    def test_sortTodos(self):
        todo_list = TodoList()
        todo_list.create_todo('Day 2', datetime.now() + timedelta(days=2))
        todo_list.create_todo('Day 1', datetime.now() + timedelta(days=1))
        todo_list.sort_todos()
        
        self.assertEqual(
            list(map(lambda todo: todo['content'], todo_list.get_todos())),
            [ 'Day 1', 'Day 2' ],
        )
        
    def test_editTodo(self):
        todo_list = TodoList()
        todo_list.create_todo('テスト', datetime.now() + timedelta(days=1))
        
        def editor(todo):
            return {
                **todo,
                'content': 'テスト (編集済み)',
            }
        
        todo_list.edit_todo(0, editor)
        
        self.assertEqual(
            todo_list.get_todos()[0]['content'], # *1
            'テスト (編集済み)',
        )
        
    def test_editTodoRaisesInvalidIdError(self):
        with self.assertRaises(Exception):
            todo_list = TodoList()
            todo_list.edit_todo(0, lambda todo: todo)
        
    def test_getTodos(self):
        todo_list = TodoList()
        todo_list.create_todo('テスト 1', datetime.now() + timedelta(days=1))
        todo_list.create_todo('テスト 2', datetime.now() + timedelta(days=2))
        
        self.assertEqual(len(todo_list.get_todos()), 2)
        
    def test_getTodosWithTag(self):
        todo_list = TodoList()
        todo_list.create_todo('テスト 1', datetime.now() + timedelta(days=1))
        todo_list.create_todo('テスト 2', datetime.now() + timedelta(days=2))
        
        def editor(todo):
            return {
                **todo,
                'tags': set([ 'プライベート' ]),
            }
        
        todo_list.edit_todo(0, editor)
        
        self.assertEqual(len(todo_list.get_todos('プライベート')), 1)


if __name__ == '__main__':
    unittest.main()
    