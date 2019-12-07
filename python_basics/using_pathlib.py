# One of programming’s little annoyances is that Microsoft Windows uses a 
# backslash (\) character between folder names while almost every other computer 
# uses a forward slash (/):

# Windows filenames:
# C:\some_folder\some_file.txt

# Most other operating systems:
# /some_folder/some_file.txt

# If you want your Python code to work on both Windows and Mac/Linux, you’ll
# need to deal with these kinds of platform-specific issues. Luckily, Python 
# 3 has a new module called pathlib that makes working with files nearly painless.

from pathlib import Path

path = Path(".")
# read file without having to deal with opening and closing or context manager
sample_txt = path / "sample.txt"
print(sample_txt.read_text())

# check name
print(sample_txt.name)

# check ext
print(sample_txt.suffix)

# check only name
print(sample_txt.stem)

# check if exists
if sample_txt.exists():
    print("hurray it exists")
else:
    print("doesn't exists")

# You can even use pathlib to explicitly convert a Unix path into
# a Windows-formatted path:
from pathlib import PureWindowsPath
windows_ver = PureWindowsPath(sample_txt)
print(windows_ver)

# absolute path
print(sample_txt.resolve())

#Here’s an example that will open a local file in your web browser with 
# just two lines a code:
import webbrowser

webbrowser.open(sample_txt.absolute().as_uri())

# for more info see docs for pathlib
https://docs.python.org/3/library/pathlib.html
