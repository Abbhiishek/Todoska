# Todoska
<div align= "center">
<h2> Todoska is a simple 😇, fast ⏩, and powerful todo list manager 🛠.</h2>
</div>

<br>
<br>

<img src="./src/todoska.gif">


## Installation

```python
pip install todoska
```


## Usage

```python
todoska --help

>>> Usage: todoska [OPTIONS] COMMAND [ARGS]...
Try 'todoska --help' for help.

Error: Missing command.
```


```python

todoska --help

>>>> python
Usage: todoska [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.     
  --help                          Show this message and exit.

Commands:
  add       Add a new task to the todo list 😀
  complete  Mark a task as complete ♦ [Index]
  delete    Delete a task from the todo list 🎈 [Index]
  show      Show all tasks in the todo Table 😀
  update    Update a task from the todo list ↗ [Index]

```


## Usage :

- `Add new task :`

```python

todoska add --help

>>> Usage: todoska add [OPTIONS] TASK CATEGORY

Arguments:
  TASK      [required]
  CATEGORY  [required]

Options:
  --help  Show this message and exit.

```

- `Update a task :`
```python
todoska update <task-id> <task-name>
>>> Usage: todoska update [OPTIONS] POSITION

Arguments:
  POSITION  [required]

Options:
  --task TEXT
  --category TEXT
  --help           Show this message and exit.

```
- `Delete a task :`

```python
todoska delete <task-id>
>>> Usage: todoska delete [OPTIONS] POSITION

Arguments:
  POSITION  [required]

Options:
  --help  Show this message and exit

```
- `View All task :`
```python
todoska show --help
>>> $ todoska show  --help
Usage: todoska show [OPTIONS]

Options:
  --help  Show this message and exit.

```



## Demo :

todoska add "Buy milk" "Home"

```python

        adding Buy milk, Home
        Todos! 💻
        ┌────────┬──────────────────────┬──────────────┬──────────────┐     
        │ #      │ Todo                 │     Category │         Done │     
        ├────────┼──────────────────────┼──────────────┼──────────────┤     
        │ 1      │ Buy milk             │         Home │          ❌  │      
        └────────┴──────────────────────┴──────────────┴──────────────┘

```
