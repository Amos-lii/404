import requests


URL="https://github.com/Amos-lii/404/blob/main/check_version.py"
res=requests.get(URL)
print(res)
sourcecode=requests.get("https://github.com/Amos-lii/404/blob/main/check_version.py")
print(sourcecode)