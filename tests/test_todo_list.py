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

    task = Todo("do something else")
    todo_list.add(task)

    assert len(todo_list.incomplete()) == 1



def test_complete_returns_all_tasks_marked_true():
    todo_list = TodoList()

    task = Todo("do something")
    todo_list.add(task)

    assert len(todo_list.complete()) == 0

    task.mark_complete()

    assert len(todo_list.complete()) == 1

    task1 = Todo("do something else")
    todo_list.add(task1)
    task1.mark_complete()

    assert len(todo_list.complete()) == 2

def test_give_up_marks_all_tasks_complete():
    todo_list = TodoList()
    task = Todo("do something")
    todo_list.add(task)

    task1 = Todo("do something else")
    todo_list.add(task1)

    result = todo_list.give_up()

    for entry in todo_list.all_tasks:
        assert entry.complete == True