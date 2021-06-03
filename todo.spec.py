import unittest
from datetime import datetime, timedelta
import todo as todo_module


class TestTodo(unittest.TestCase):
    def test_createTodo(self):
        content = 'テスト'
        deadline = datetime.now() + timedelta(days=1)

        todo = todo_module.create_todo(content, deadline)

        self.assertEqual(todo['content'], content)
        self.assertEqual(todo['deadline'], deadline)

    def test_createTodoRaisesNoContentError(self):
        with self.assertRaises(Exception):
            todo = todo_module.create_todo('', datetime.now() + timedelta(days=1))

    def test_createTodoRaisesBeforeDeadlineError(self):
        with self.assertRaises(Exception):
            todo = todo_module.create_todo('テスト', datetime.now() - timedelta(days=1))

    def test_finishTodo(self):
        todo = todo_module.create_todo('テスト', datetime.now() + timedelta(days=1))
        finished_todo, ratio = todo_module.finish_todo(todo)

        self.assertEqual(ratio, 0)
        self.assertNotEqual(todo['finish'], finished_todo['finish'])

    def test_editDeadline(self):
        todo = todo_module.create_todo('テスト', datetime.now() + timedelta(days=1))
        edited_todo = todo_module.edit_deadline(todo, datetime.now() + timedelta(days=2))

        self.assertNotEqual(todo['deadline'], edited_todo['deadline'])

    def test_editDeadlineRaisesBeforeDeadlineError(self):
        with self.assertRaises(Exception):
            todo = todo_module.create_todo('テスト', datetime.now() + timedelta(days=1))
            edited_todo = todo_module.edit_deadline(todo, datetime.now())

    def test_addTag(self):
        todo = todo_module.create_todo('テスト', datetime.now() + timedelta(days=1))
        temp_todo = todo_module.add_tag(todo, 'プライベート')
        edited_todo = todo_module.add_tag(temp_todo, '仕事用')
        
        self.assertIn('プライベート', edited_todo['tags'])
        self.assertIn('仕事用', edited_todo['tags'])
        self.assertNotEqual(todo['tags'], edited_todo['tags'])

    def test_addTagRaisesEmptyTagError(self):
        with self.assertRaises(Exception):
            todo = todo_module.create_todo('テスト', datetime.now() + timedelta(days=1))
            edited_todo = todo_module.add_tag(todo, '')

    def test_removeTag(self):
        todo = todo_module.create_todo('テスト', datetime.now() + timedelta(days=1))
        temp_todo_0 = todo_module.add_tag(todo, 'プライベート')
        temp_todo_1 = todo_module.add_tag(temp_todo_0, '仕事用')
        edited_todo = todo_module.remove_tag(temp_todo_1, 'プライベート')

        self.assertNotIn('プライベート', edited_todo['tags'])
        self.assertIn('仕事用', edited_todo['tags'])

    def test_removeTagRaisesTagNotFoundError(self):
        with self.assertRaises(Exception):
            todo = todo_module.create_todo('テスト', datetime.now() + timedelta(days=1))
            added_todo = todo_module.add_tag(todo, 'プライベート')
            edited_todo = todo_module.remove_tag(added_todo, '仕事')


if __name__ == '__main__':
    unittest.main()
