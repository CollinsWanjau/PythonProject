# 26.2. doctest — Test interactive Python examples

* There are sveral ways to use doctest:

1. To check that a module’s docstrings are up-to-date by verifying that all 
interactive examples still work as documented.

2. To perform regression testing by verifying that interactive examples 
from a test file or a test object work as expected.

3. To write tutorial documentation for a package, liberally illustrated with 
input-output examples. Depending on whether the examples or the expository 
text are emphasized, this has the flavor of “literate testing” or 
“executable documentation”.

# 26.2.1. Simple Usage: Checking Examples in Docstrings

* The simplest way to start using doctest is to end each module
M with:
```
if __name == "__main__":
    import doctest
    doctest.testmod()
```
* There is also a command line shortcut for running `testmod()`.You
can instruct the python interpreter to run the doctest module directly
from the standard library and pass the module name(s) on the
command line.
```
python -m doctest -v example.py
```

* This will import `example.py` as a standalone module and run `testmod()` on it.

* For `testfile()`, it is used in files that don't end with `.py`

