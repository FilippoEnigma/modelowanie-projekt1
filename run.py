import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
sys.path.append('gen')
from TodoListLexer import TodoListLexer
from TodoListParser import TodoListParser
from todo_list_interpreter import TodoListInterpreter

def main():

    if len(sys.argv) < 2:
        print("Usage: run.py <path_to_todo_list_file>")
        sys.exit(1)

    input_path = sys.argv[1]


    input_stream = FileStream(input_path)


    lexer = TodoListLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TodoListParser(stream)


    tree = parser.file_()


    interpreter = TodoListInterpreter()
    walker = ParseTreeWalker()
    walker.walk(interpreter, tree)


    print(interpreter.task_list)

if __name__ == "__main__":
    main()
