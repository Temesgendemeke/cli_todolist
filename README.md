---

# CLI To-Do List (cli_todolist)

`cli_todolist` is a simple, terminal-based to-do list manager that lets you manage tasks directly from the command line. You can add tasks, mark them as finished, delete them, and view your to-do list. All commands are case-insensitive for convenience.

## Features

- **Add tasks** to your to-do list
- **Delete tasks** with optional marking
- **Mark tasks as finished**
- **View** the current to-do list
- **Help** command for manual and guidance

## Installation

Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/Temesgendemeke/cli_todolist.git
cd cli_todolist
```

## Usage

| Command                      | Description                                        | Example               |
| ---------------------------- | -------------------------------------------------- | --------------------- |
| `add <task name>`            | Adds a new task to the to-do list.                 | `add Finish homework` |
| `x <index>` or `del <index>` | Deletes a task by its index, marking it if needed. | `x 2` or `del 2`      |
| `done <index>`               | Marks a task as finished.                          | `done 3`              |
| `show`                       | Displays all current tasks.                        | `show`                |
| `help`                       | Lists all available commands with descriptions.    | `help`                |

### Examples

- Add a task:

  ```bash
  add Buy groceries
  ```

- Mark a task as finished:

  ```bash
  done 1
  ```

- Delete a task:

  ```bash
  del 2
  ```

- View all tasks:

  ```bash
  show
  ```

- Get help:
  ```bash
  help
  ```

### Notes

- **Case-Insensitive Commands**: You can use commands in any case (e.g., `ADD`, `add`, `Add` are all valid).

---

Feel free to adjust the example commands or features as you expand the project.
