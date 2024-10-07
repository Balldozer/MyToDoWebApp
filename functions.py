FILEPATH_1 = "todos.txt"


def get_todos():
    """Read a text file and return the to-do items."""
    with open(FILEPATH_1, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local


def store_todos(todos_arg):
    """Take a to-do list and store them in a text file."""
    with open(FILEPATH_1, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")