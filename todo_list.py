from typing import List, Optional, Callable
from datetime import datetime, timedelta, date
from todo import Todo, create_todo


class TodoList():
    def __init__(self) -> None:
        self._todos: List[Todo] = []

    def create_todo(self, content: str, deadline: date) -> Todo:
        todo = create_todo(content, deadline)
        self._todos.append(todo)

        return todo

    def delete_todo(self, todo_id: int) -> None:
        if 0 <= todo_id < len(self._todos):
            del self._todos[todo_id]

        else:
            raise Exception('存在しない TODO を削除しようとしました！')

    def sort_todos(self) -> None:
        self._todos.sort(key=lambda todo: todo['deadline'])

    def edit_todo(self, todo_id: int, editor: Callable[[Todo], Todo]) -> None:
        if 0 <= todo_id < len(self._todos):
            self._todos[todo_id] = editor(self._todos[todo_id])

        else:
            raise Exception('存在しない TODO を編集しようとしました！')

    def get_todo(self, todo_id: int) -> Todo:
        if 0 <= todo_id < len(self._todos):
            return self._todos[todo_id]
            
        else:
            raise Exception('存在しない TODO を取得しようとしました！')

    def get_todos(self, tag: Optional[str] = None) -> List[Todo]:
        if tag is None:
            return self._todos

        return list(filter(lambda todo: tag in todo['tags'], self._todos))
