from cx_Freeze import Executable, setup
import sys
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\u300310\\AppData\\Local\\Programs\\Python\\\Python38-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\u300310\\AppData\\Local\\\Programs\\Python\\\Python38-32\\tcl\\tk8.6"

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

executable = [Executable("start.py", base=base)]

packages = [
    "process",
]

options = {
    'build_exe': {
    'packages': packages,
    'include_files': [
        os.path.join("C:\\Users\\u300310\\AppData\\Local\\Programs\\Python\\\Python38-32\\DLLs\\tcl86t.dll"),
        os.path.join("C:\\Users\\u300310\\AppData\\Local\\Programs\\Python\\\Python38-32\\DLLs\\tk86t.dll"),
        ]
    },
}

setup(name="Processadora",
      options=options,
      version="1.0",
      desrition="Primeiro teste do processador de q2",
      executable=executable,)
