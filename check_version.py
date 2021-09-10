import requests


def get_file(filename="QUESTION8.py"):
    URL="https://raw.githubusercontent.com/Amos-lii/404/main/check_version.py"
    down = requests.get(URL)
    with open(filename, "wb") as file:
        file.write(down.content
                   )
sourcecode=requests.get("https://raw.githubusercontent.com/Amos-lii/404/main/check_version.py")
print(sourcecode)