from typing import TypedDict, Set, Final
from datetime import datetime, date

Todo = TypedDict('Todo', {
    'content': str,
    'start': date,
    'deadline': date,
    'tags': Set[str],
    'expectTimeHour': int,
})
 
def createTodo(content: str, deadline: date) -> Todo:
    if content == '':
        raise Exception('空の TODO を作成することはできません！')
    
    if deadline < datetime.now():
        raise Exception('過去の日付で TODO を作成することはできません！')
    
    return {
        'content': content,
        'start': datetime.now(),
        'deadline': deadline,
        'tags': set(),
        'expectTimeHour': 72, # 3日間を標準の期限とする
    }
    
def editDeadline(todo: Todo, deadline: date) -> Todo:
    if deadline < datetime.now():
        raise Exception('過去の日付に TODO を編集することはできません！')
    
    todo['deadline'] = deadline
    
    return todo
    
def addTag(todo: Todo, tag: str) -> Todo:
    if tag == '':
        raise Exception('空のタグを設定することはできません！')
    
    todo['tags'].add(tag)
    
    return todo

def removeTag(todo: Todo, tag: str) -> Todo:
    if tag in todo['tags']:
        todo['tags'].remove(tag)
    else:
        raise Exception('存在しないタグを削除しようとしました！')
        
    return todo