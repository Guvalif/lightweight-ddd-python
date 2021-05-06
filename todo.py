from typing import TypedDict, Set
from datetime import datetime, date

Todo = TypedDict('Todo', {
    'content': str,
    'deadline': date,
    'tag': Set[str],
    'actualTime': int,
    'expectTime': int,
})

def createTodo(content: str, deadline: date) -> Todo:
    pass
