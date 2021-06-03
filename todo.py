from typing import TypedDict, Set, Optional, Tuple, cast
from datetime import datetime, timedelta, date


Todo = TypedDict('Todo', {
    'content': str,
    'start': date,
    'finish': Optional[date],
    'deadline': date,
    'tags': Set[str],
})

def create_todo(content: str, deadline: date) -> Todo:
    if content == '':
        raise Exception('空の TODO を作成することはできません！')

    if deadline <= datetime.now():
        raise Exception('過去の日付で TODO を作成することはできません！')

    return {
        'content': content,
        'start': datetime.now(),
        'finish': None,
        'deadline': deadline,
        'tags': set(),
    }

def finish_todo(todo: Todo) -> Tuple[Todo, int]:
    finished_todo = cast(Todo, {
        **todo,
        'finish': datetime.now(),
    })

    expect_delta = (finished_todo['deadline'] - finished_todo['start']) / timedelta(hours=1)
    actual_delta = (finished_todo['finish'] - finished_todo['start'])  / timedelta(hours=1) # type: ignore[operator]

    ratio = int(actual_delta / expect_delta * 100)

    return (finished_todo, ratio)

def edit_deadline(todo: Todo, deadline: date) -> Todo:
    if deadline <= datetime.now():
        raise Exception('過去の日付に TODO を編集することはできません！')

    edited_todo = cast(Todo, {
        **todo,
        'deadline': deadline,
    })

    return edited_todo

def add_tag(todo: Todo, tag: str) -> Todo:
    if tag == '':
        raise Exception('空のタグを設定することはできません！')

    tags = set(todo['tags'])
    tags.add(tag)

    edited_todo = cast(Todo, {
        **todo,
        'tags': tags,
    })

    return edited_todo

def remove_tag(todo: Todo, tag: str) -> Todo:
    if tag not in todo['tags']:
        raise Exception('存在しないタグを削除しようとしました！')

    tags = set(todo['tags'])
    tags.remove(tag)

    edited_todo = cast(Todo, {
        **todo,
        'tags': tags,
    })

    return edited_todo
