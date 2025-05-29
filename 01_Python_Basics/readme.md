# Bytecode

-   Bytecode = low-level + platform-independent.

# **pycache**

In Python's inner working, the **pycache** folder stores compiled bytecode files (.pyc) so that Python can run your program faster next time.

# How it works / Kaise kaam karta hai:

1. You run example.py.

2. Python compiles it to bytecode.

3. A file example.cpython-313.pyc is created inside **pycache**.

4. Next time, Python runs this .pyc file directly (faster).

-   Use: Fast execution, no need to recompile again.

-   Note: You can delete **pycache**, Python will recreate it when needed.
