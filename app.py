#!/usr/bin/env python3

from sys import argv
import json
import os
from pathlib import Path

home_dir = Path.home()
todo_dir = home_dir / ".todos"
todo_file = todo_dir / "todos.json"
todo_counter_file = todo_dir / "todos_counter.json"

os.makedirs(todo_dir, exist_ok=True)


class Task:
    def __init__(self, title) -> None:
        self.title = title
        self.next = None


class Todos:
    finshed_task = []

    def __init__(self) -> None:
        self.head = None
        self.start_up(self.read_json(todo_file))

    def start_up(self, todos):
        for todo in todos:
            self.add(todo["task"], "r")

    def add(self, task, mode):
        newTask = Task(task)
        head = self.head
        newTask.next = head
        self.head = newTask
        if mode == "w":
            self.write_to_json(todo_file, task)
            print(f"+ added {task}")

    def done(self, index):
        head = self.head
        if index == 0 or len(self.read_json(todo_file)) < index:
            print("NO TODOS TO MARK")
            return

        if index == 1 and len(self.read_json(todo_file)) >= index:
            self.delete_from_todos(index - 1)
            self.add_to_finshed(head.title)
            self.head = head.next
            return

        for _ in range(1, index - 1):
            head = head.next

        if head.next is None or index <= 0:
            print("DOX")
            return

        # write_to_json
        self.write_to_json(todo_counter_file, head.next.title)
        self.delete_from_todos(index - 1)

        self.add_to_finshed(head.next.title)
        head.next = head.next.next

    def remove(self, index):
        head = self.head

        if index == 1:
            self.head = head.next
            return

        self.delete_from_todos(index - 1)

        for _ in range(1, index - 1):
            head = head.next
        print(f"- Deleted {head.next.title}")
        head = head.next.next

    def show(self):
        head = self.head

        index = 1

        while head:
            head = head.next
            index += 1
        with open(todo_file, "r") as file:
            todos = json.load(file)

        print('"IF IT WAS EASY EVERYBODY CAN DO IT"\n')
        print("TODOS 🔐")
        if len(todos) == 0:
            print("add todos champ!! 🎯")
        for i in range(len(todos)):
            print("[{}] {}".format(i + 1, todos[i]["task"]))

    def add_to_finshed(self, task):
        print("DONE ⚡- {}".format(task))
        self.count_finshed_task()

    def read_json(self, path):
        if os.path.exists(path):
            with open(path, "r") as file:
                todos = json.load(file)
        else:
            todos = []
        return todos

    def write_to_json(self, path, task):
        todos = self.read_json(path)
        todos.append({"task": task})

        with open(path, "w") as file:
            json.dump(todos, file, indent=4)
        return todos

    def delete_from_todos(self, index):
        with open(todo_file, "r") as file:
            todos = json.load(file)
        if index <= len(todos):
            del todos[index]
        with open(todo_file, "w") as file:
            json.dump(todos, file)

    def count_finshed_task(self):
        path = "finshed_task_counter.json"
        finshed_task = dict(self.read_json(path))
        if finshed_task == {}:
            with open(path, "w") as file:
                json.dump({"count": 1}, file)
        else:
            finshed_task["count"] += 1
            with open(path, "w") as file:
                json.dump(finshed_task, file)

    def check_type(self, index):
        try:
            int(index)
        except ValueError:
            print("Invalid Index")
            return 1


def main():
    if len(argv) < 2:
        print("Usage:")
        print("  add <task>      - Add a new task to your to-do list")
        print("  done <index>    - Mark a task as completed by its index")
        print(
            "  del <index>     - Delete a task by its index (without marking it as done)"
        )
        print("  show            - Display all tasks with their status and index")
        print("  help            - Show this help message")
        return
    todos = Todos()

    command = argv[1].upper()
    task = " ".join(argv[1:])

    if command == "ADD":
        todos.add(task, "w")
    elif command == "DONE":
        if todos.check_type(argv[2]) == 1:
            return
        todos.done(int(argv[2]))
    elif command == "X" or command == "del":
        if todos.check_type(argv[2]) == 1:
            return
        todos.remove(int(argv[2]))
    elif command == "SHOW":
        todos.show()
    elif command == "HELP":
        print("\nCommands:")
        print(
            "  add <task>      - Adds a new task to your to-do list with the specified description"
        )
        print("  done <index>    - Marks the task at the given index as completed")
        print(
            "  del <index>     - Deletes the task at the given index without marking it as done"
        )
        print("  show            - Lists all tasks with their indexes and status")
        print(
            "  help            - Shows this help message with descriptions of all commands"
        )


if __name__ == "__main__":
    main()
