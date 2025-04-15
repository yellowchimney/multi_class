from lib.todo_list import TodoList
from lib.todo import Todo
def test_adds_task_instance_to_todo_list():
    todo_list = TodoList()

    assert todo_list.all_tasks == []

    task = Todo("do something")
    todo_list.add(task)

    assert len(todo_list.all_tasks) == 1
    assert todo_list.all_tasks[0].task == "do something"

def test_incomplete_returns_all_tasks_marked_false():
    todo_list = TodoList()

    task = Todo("do something")
    todo_list.add(task)
    task.mark_complete()

    assert todo_list.incomplete() == []