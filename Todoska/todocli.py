#! /usr/bin/env python3
import typer
from rich.console import Console
from rich.table import Table
from rich.status import Status
from Todoska.models import Todo
from Todoska.Database import get_all_todos, delete_todo, insert_todo, complete_todo, update_todo

# from Todoska.Database import *

console = Console()

app = typer.Typer()

@app.command()
def about():
    """
    Show information about the Todoska CLI
    
    """
    console.print("""

    Todocli is a simple CLI tool for managing your todos .

    It is a simple todo list manager that allows you to add, delete, complete and edit your todos.
    License: MIT | Copyright 2022 Abhishek Kushwaha

    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the
    "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, 
    publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do 
    so, subject to the following conditions:
    

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
    FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION 
    WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


    Owner: Abhishek Kushwaha
    Email: abhishekkushwaha1479@gmail.com
    Github:https://github.com/Abbhiishek
    https://abbhishek.me
    
    """ , justify="center")
    console.print("""
    >>> Commands :
    >>> add <task> <category>
    >>> delete <position>
    >>> complete <position>
    >>> update <position> <task> <category>
    >>> show
    >>> --help         for more help 
    """)


@app.command()
def add(task: str, category: str):
    """
    Add a new task to the todo list 😀
    """
    typer.echo(f"adding {task}, {category}")
    todo = Todo(task, category)
    insert_todo(todo)
    show()

@app.command()
def delete(position: int):
    """
    Delete a task from the todo list 🎈 [Index]
    """
    typer.echo(f"deleting {position}")
    # indices in UI begin at 1, but in database at 0
    delete_todo(position-1)
    show()

@app.command()
def update(position: int, task: str = None, category: str = None):
    """
    Update a task from the todo list ↗ [Index]
    
    """
    typer.echo(f"updating {position}")
    update_todo(position-1, task, category)
    show()

@app.command()
def complete(position: int):
    """
    Mark a task as complete ♦ [Index]
    
    """
    typer.echo(f"complete {position}")
    complete_todo(position-1)
    show()




@app.command()
def show():
    """
    Show all tasks in the todo Table 😀
    
    """
    tasks = get_all_todos()
    console.print("[bold magenta]Todoska - Todo Tracker Made Simple. [/bold magenta]!", "✨" , justify="center" )
    console.print( Status(status="Fetching All the Todos 🔎" ,spinner="clock"),justify="left" )
    table = Table(show_header=True, header_style="bold dark_slate_gray2")
    table.add_column("#", style="dim", width=6 , justify="center")
    table.add_column("Todo", min_width=20 , justify="center")
    table.add_column("Category", min_width=12, justify="center")
    table.add_column("Date Added", min_width=12, justify="center")
    table.add_column("Date Of Completion", min_width=12, justify="center")
    table.add_column("Status", min_width=12, justify="center")

    def get_category_color(category):
        COLORS = {'Learn': 'cyan2', 'YouTube': 'red', 'Sports': 'cyan', 'Study': 'green' , 'Work': 'yellow' , 'Home': 'magenta', 'Other': 'blue' , 'Shopping': 'green' , 'Personal': 'magenta' }
        if category in COLORS:
            return COLORS[category]
        return 'white'

    for idx, task in enumerate(tasks, start=1):
        c = get_category_color(task.category)
        is_done_str = '✅ Done' if task.status == 2 else '❌ Not Done'
        task.date_completed = task.date_completed if task.date_completed is not None else 'Pending ⌛'
        table.add_row(str(idx), f'[bright_cyan]{task.task}[/bright_cyan]', f'[{c}]{task.category}[/{c}]', f'[orchid]{task.date_added}[/orchid]',f'[orchid]{task.date_completed}[/orchid]' ,  is_done_str)
    console.print(table)


if __name__ == "__main__":
    app()