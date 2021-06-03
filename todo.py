from typing import TypedDict, Set, Optional, Tuple, cast
from datetime import datetime, date

Todo = TypedDict('Todo', {
    'content': str,
    'start': date,
    'finish': Optional[date],
    'deadline': date,
    'tags': Set[str],
})

def createTodo(content: str, deadline: date) -> Todo:
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

def finishTodo(todo: Todo) -> Tuple[Todo, int]:
    finised_todo = cast(Todo, {
        **todo,
        'finish': datetime.now(),
    })
    
    expect_delta = getattr(finised_todo['deadline'] - finised_todo['start'], 'hours', 1)
    actual_delta = getattr(finised_todo['finish'] - finised_todo['start'], 'hours', 1) # type: ignore[operator]
    
    ratio = int(actual_delta / expect_delta * 100)
    
    return (finised_todo, ratio)
     
def editDeadline(todo: Todo, deadline: date) -> Todo:
    if deadline <= datetime.now():
        raise Exception('過去の日付に TODO を編集することはできません！')

    edited_todo = cast(Todo, {
        **todo,
        'deadline': deadline,
    })

    return edited_todo

def addTag(todo: Todo, tag: str) -> Todo:
    if tag == '':
        raise Exception('空のタグを設定することはできません！')

    tags = set(todo['tags'])
    tags.add(tag)

    edited_todo = cast(Todo, {
        **todo,
        'tags': tags,
    })
 
    return edited_todo

def removeTag(todo: Todo, tag: str) -> Todo:
    if tag in todo['tags']:
        tags = set(todo['tags'])
        tags.remove(tag)
    
        edited_todo = cast(Todo, {
            **todo,
            'tags': tags,
        })
    else:
        raise Exception('存在しないタグを削除しようとしました！')

    return edited_todo
