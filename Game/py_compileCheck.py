import py_compile
try:
    py_compile.compile("game.py", doraise=True)
except py_compile.PyCompileError:
    print("Compilation failed!")
