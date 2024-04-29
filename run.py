import sys
import json
from datetime import datetime, timedelta
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from verbose_error_listener import VerboseErrorListener

sys.path.append('gen')
from TodoListLexer import TodoListLexer
from TodoListParser import TodoListParser
from todo_list_interpreter import TodoListInterpreter
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from task import Task

def read_tasks_from_file(filename):
    with open(filename, 'r') as file:
        tasks_data = json.load(file)
        tasks = []
        for data in tasks_data:
            data['deadline'] = Task.parse_date(data['deadline'])
            data['start_date'] = Task.parse_date(data['start_date'])
            tasks.append(Task(**data))
        return tasks

def plot_gantt(tasks):
    fig, ax = plt.subplots()
    y_positions = range(len(tasks))
    start_dates = [datetime.strptime(task['start_date'], "%Y-%m-%d") for task in tasks]
    end_dates = [datetime.strptime(task['start_date'], "%Y-%m-%d") + timedelta(days=task['duration']) for task in tasks]
    colors = ['red', 'green', 'blue', 'cyan', 'magenta']

    for pos, start, end, task in zip(y_positions, start_dates, end_dates, tasks):
        ax.barh(pos, (end - start).days, left=start, height=0.4, color=colors[pos % len(colors)], label=task['name'])

    ax.set_yticks(y_positions)
    ax.set_yticklabels([task['name'] for task in tasks])
    ax.set_xlabel('Dates')
    ax.set_title('Gantt Chart')
    plt.tight_layout()
    plt.show()


def main():
    if len(sys.argv) < 2:
        print("Usage: run.py <path_to_todo_list_file>")
        sys.exit(1)

    input_path = sys.argv[1]
    input_stream = FileStream(input_path)
    lexer = TodoListLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TodoListParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(VerboseErrorListener())
    tree = parser.file_()
    interpreter = TodoListInterpreter()
    walker = ParseTreeWalker()
    walker.walk(interpreter, tree)
    tasks = [task.to_dict() for task in interpreter.task_list.tasks.values()]

    with open('output_tasks.txt', 'w') as file:
        json.dump(tasks, file, indent=4)

    plot_gantt(tasks)


if __name__ == "__main__":
    main()
