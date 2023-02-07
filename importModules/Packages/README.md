# Packages

* Users of the package can import individual modules from
the package:
`import sound.effects.echo`

* An alternative way of importing the submodule is:
`from sound.effects import echo`

* Another variation is to import the desired function or variable
directly.
`from sound.effects.echo import echofilter`

* The import statement first tests whether the item is defined in
the package; if not, it assumes it is a module and attempts to load
it.If it fails it finds an `Import Error Exception`.

* Contrarily, when using syntax like import item.subitem.subsubitem, 
each item except for the last must be a package; the last item can 
be a module or a package but can’t be a class or function or 
variable defined in the previous item.

* In the syntax `import item.subitem.subsubitem`, each item except
for the last one must be a package.The last item can be either a
module or a package, but it cannot be a class, function, or a
variable defined in the previous item.

* This syntax allows you to import a specific module or package from
within  a package hierachy

* The `__all__` list in the `__init__.py` file of a package is used
to define the names of modules that should be improved when the
`from package import *` statement is encountered.

* The `__all__` list should contain a list of strings, where each
string is the name of a module within the package.

* If the subpackage `effects`, and the `__init.py` file of the
`effects` package contains the following line:
```
__all__ = ['echo', 'reverb']
```

## Intra-packages

* You can also write relative imports, with the `from module import
name`.This imports use leading dots to indicate the current and
parent packages involved in the relative import.

```
from . import echo
from .. import formats
from ..filters import equalizer
```

* Since the name of the main module is always `"__main__"`,modules
intended for use as the main module of a Python application must
always use absolute imports.

# Compare with C

(file organization, not prototype vs code etc.)

In python:
```
import abs
abs.my_abs(89)
```

or

```
from abs import my_abs
my_abs(89)
```

In C: `#include "my_math/abs.h"`

In Python:
```
from my_math.abs import abs
my_abs(89)
```

or

```
import my_math.abs
my_math.abs.my_abs(89)
```

# Dotted module names == Path

`import my_math.abs` => YES but you will use your function like
that:`my_math.abs.my_abs(89)`. => not friendly.

`from my_math.abs import my_abs` => now you can use your function
like that:
`my_abs(89)`

## `import *` is dangerous

* What the difference?

* `from abs import my_abs` is using a relative path between your file who imports
and the module to import.

* `from my_math.abs import my_abs` is using an absolute path between the file
you executed and the module to import

## File storage == JSON serialization

* You can't store and restore a python instance of a class as "Bytes", the
only way is to convert it to a serializable data structure.

* Convert an instance to python built in serializable data structure(list, 
dict, number and string) - for us it will be the method `my_instance.to_json`
to retrieve a dictionary.

* Convert this data structure to a string(JSON format, but it can be YAML, XML
CSV) - for us it will be a `my_string = JSON.dumps(my_dict)`.


# cmd -- Support for line-oriented command interpreters

* The `cmd` class provides a simple framework for writing line-oriented
command interpreters.

* These are often useful for test harness, administrative tools, and
prototypes.

* `class cmd.Cmd(completekey='tab', stdin=None, stdout=None)`
-> A cmd instance or subclass instance is a line-oriented interpreter
framework.There is no good reason to instantiate cmd itself;rather, it's
useful as a superclass of an interpreter class you define yourself in order
to inherit `cmd` methods and encapsulate action methods.

# cmd -- Create line-oriented command processors

* The cmd module contains one public class, `cmd`, designed to be used as a
base class for command processors such as interactive shells and other
command interpreters.

* By default it uses `readline` for interactive prompt handling, command line
editing, and command completion

# Cmd Objects

* A cmd instance has the following methods:

1. `Cmd.cmdloop(intro=None)` - Repeatedly issue a prompt, access input, parse
an initial preifx off the received input, and dispatch to action methods
passing them the remainder of the line as arg.

* If the `readline` module is loaded, input will automatically inherit
bash-like history-list editing

* The end-of-file marker is dispacthed to `do_EOF`.If a command handler
returns a true value, the program will exit cleanly.So to give a clean way to
exit your interpreter, make sure to implement `do_EOF` and have it return
true.

2. `onecmd` - used to execute a single command passed as a string argument.
The `onecmd` is part of the `cmd.Cmd` class, which provides a basic framework
for creating line-oriented command interpreters.

* It takes a single string arg representing a command, parses it, and executes
the corresponding method that implements the command.

## Overiding Base Class Methods

* Cmd includes several methods that can be overridden as hooks for taking
or altering the base class behaviour e.g the `cmdloop` method can be overriden
to provide a custom main loop for the CLI.
