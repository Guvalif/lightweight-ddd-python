from datetime import datetime, timedelta
from flask import Flask, request, render_template
from todo import Todo, edit_deadline, finish_todo, add_tag, remove_tag
from todo_list import TodoList

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

todolist = TodoList()

@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/todolist', methods=['GET'])
def get_todolist():
    return str(todolist.get_todos())

@app.route('/todolist', methods=['POST'])
def post_todolist():
    content = request.form['content']

    deadline = request.form['deadline']
    deadline = datetime.strptime(deadline, '%Y/%m/%d %H:%M')

    todo = todolist.create_todo(content, deadline)

    return str(todo)

@app.route('/todo/<int:todo_id>', methods=['GET'])
def get_todo(todo_id: int):
    return str(todolist.get_todo(todo_id))

@app.route('/todo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id: int):
    todolist.delete_todo(todo_id)

    return str(todo_id)

@app.route('/todo/<int:todo_id>/content', methods=['GET'])
def get_todo_content(todo_id: int):
    return str(todolist.get_todo(todo_id)['content'])

@app.route('/todo/<int:todo_id>/deadline', methods=['GET'])
def get_todo_deadline(todo_id: int):
    return str(todolist.get_todo(todo_id)['deadline'])

@app.route('/todo/<int:todo_id>/deadline', methods=['PUT'])
def put_todo_deadline(todo_id: int):
    deadline = request.form['deadline']
    deadline = datetime.strptime(deadline, '%Y/%m/%d %H:%M')

    def editor(todo: Todo) -> Todo:
        return edit_deadline(todo, deadline)

    todolist.edit_todo(todo_id, editor)

    return str(deadline)

@app.route('/todo/<int:todo_id>/start', methods=['GET'])
def get_todo_start(todo_id: int):
    return str(todolist.get_todo(todo_id)['start'])

@app.route('/todo/<int:todo_id>/finish', methods=['GET'])
def get_todo_finish(todo_id: int):
    return str(todolist.get_todo(todo_id)['finish'])

@app.route('/todo/<int:todo_id>/finish', methods=['POST'])
def post_todo_finish(todo_id: int):
    ratio = 0

    def editor(todo: Todo) -> Todo:
        global ratio
        finished_todo, ratio = finish_todo(todo) # type: ignore[name-defined]

        return finished_todo

    todolist.edit_todo(todo_id, editor)

    return str(ratio)

@app.route('/todo/<int:todo_id>/tags', methods=['GET'])
def get_todo_tags(todo_id: int):
    return str(todolist.get_todo(todo_id)['tags'])

@app.route('/todo/<int:todo_id>/tags', methods=['POST'])
def post_todo_tags(todo_id: int):
    tag = request.form['tag']

    def editor(todo: Todo) -> Todo:
        return add_tag(todo, tag)

    todolist.edit_todo(todo_id, editor)

    return str(tag)

@app.route('/todo/<int:todo_id>/tags', methods=['DELETE'])
def delete_todo_tags(todo_id: int):
    tag = request.form['tag']

    def editor(todo: Todo) -> Todo:
        return remove_tag(todo, tag)

    todolist.edit_todo(todo_id, editor)

    return str(tag)

app.run(host='0.0.0.0', port=80)
