import requests
import inspect


def get_file(filename="QUESTION8.py"):
    URL=None
    down = requests.get(URL)
    with open(filename, "wb") as file:
        file.write(down.content
                   )
sourcecode=inspect.getsource(get_file)
print(sourcecode)