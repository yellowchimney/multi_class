# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self.all_tasks = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.all_tasks.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        list_of_incompletes = []
        for task in self.all_tasks:
            if task.complete == False:
                list_of_incompletes.append(task)
        return list_of_incompletes


    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass


