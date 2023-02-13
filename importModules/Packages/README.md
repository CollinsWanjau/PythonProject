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

# UUID objects

* This module provides immutable UUID objects (the UUID class) and the functions
`uuid1(), uuid3(), uuid4(), uuid5()`

* If all you want is a unique ID, you should probably call `uuid1` or `uuid4`.
Note that `uuid1()` may compromise privacy since it creates a UUID containig
the network address.

* `uuid4()` creates a random UUID.

* A safe UUID is one which is generated using synchronization methods that 
ensure no two processes can obtain the same UUID.


* The uuid module defines the following functions:

1. uuid.getnode() - get the hw address as a 48-bit positive integer.

2. uuid.uuid1(node=None, clock_seq=None)
-> Generate a UUID from a host ID, sequence number and the current time.
If node is not given, getnode() is used to obtain the hw address.
If clock_seq is given, it is used as a sequence number.

3. uuid.uuid3(namespace, name)
-> Generate a UUID based on the MD5 hash of a namespace identifier
(which is a UUID) and a name (which is a string).

4. uuid.uuid5(namespace, name)
-> Generate a UUID based on the SHA-1 hash of a namespace identifier
(which is a UUID) and a name(which is a string)

# datetime

* The datetime module supplies classes for manipiulating dates and times.

## Aware and Naive Objects

* Date and time objects may be categorized as "aware" and "naive"
depending on whether or not they include timezone info.

* With sufficient knowledge of applicalbe algorithmic and political time
adjustments, such as time zone and daylight saving information, an aware
object can locate itself relative to other aware objects.

* A naive object does not contain enough information to unambigously locate
itself relative to other date/time objects.Naive objects are easy to
understand  and to work with, at the cost of ignoring some aspects of reality.

#### Constants

* The datetime module exports the following constants:

1. <b>datetime.MINYEAR</b> - the smallest year number allowed in a date or
datetime object.

2. <b>datetime.MAXYEAR</b> - the largest number allowed in a date or datetime
object.

### Available Types

* <b>class datetime.date</b> - An idealized naive date, assuming the current
Gregorian calendar always was and always will be, in effect.

* <b>class datetime.time</b> - An idealized time, independent of any particular
day, assuming that every day has exactly 24*60*60

* <b>class datetime.datetime</b> - a combination of a date and a time

#### Common Properties

* The date, datetime, time and timezone types share these common features:
1. Objects of these types are immutable.
2. Objects of these types are hashable, meaning that they can be used as
dictionary keys.

#### Determing if an Object is Aware or Naive

* Objects of the <b>date</b> type are always naive.

* An object of type <b>time</b> or <b>datetime</b> may be aware or naive.

* A datetime object d is aware of both of the following hold:
1. `d.tzinfo` is not `None`.
2. `d.tzinfo.utcoffset(d)` does not return `None`.

* Otherwise, d is naive.

* A time object t is aware if both of the following hold:

1. `t.tzinfo` is not `None`.
2. `t.tzinfo.utcoffset(None)` does not return `None`.

* Otherwise, t is naive.

### Timedelta Objects

* A timedelta object represents a duration, the difference between two dates
or times.

* <b>class datetime.timedelata</b>(days=0, seconds=0, microseconds=0,
milliseconds=0, minutes=0, hours=0, weeks=0)

* All args are optional and default to `0`.Args may be integers or floats
and may be positive or negative.

* Only days, seconds and microseconds are stored internally.Args are converted
to those units.

* If the normalized value of days lies outside the indicated range,
`Overflowerror` is raised.
##### Supported Operations:

* str(t) - Returns a string in the form `[D days[s], ][H]H:MM:SS[.UUUUUU]`,
where D is nagative for negative `t`.

* repr(t) - Returns a string representation of the timedelta object as a constructor call with cannonical attributes.
#### Instance methods

* <b>timedelta.total_seconds()</b> -> Return the total number of seconds
contained in the duration.

Equivalent to `td / timedelta(seconds=1)`.For other interval units other
than seconds, use the division form directly(`td / timedelta(microseconds=1)`)

## date Objects

* A date object represents a date (year, month and day) in an idealized
calendar, the current Gregorian calendar indefinitely  extended in both
directions.

1. class datetime.<b>date</b>(year, month, day)

* Other constructors, all class methods:

2. classmethod date.<b>today</b>() - an equivalent to
`date.fromtimestamp(time.time())`.

3. classmethod date.<b>fromtimestamp</b>(timestamp)
-> return the local date corresponding to the POSIX timestamp, such
as is returned by `time.time()`

4. classmethod date.<b>fromordinal</b>(ordinal)
-> Return the date corresponding to the proleptic Gregorian ordinal,
where January 1 of year 1 has ordinal 1.

5. classmethod date.<b>fromisoformat</b>(date_string)
-> Return a date corresponding to a date_string in the format
`YYYY-MM-DD`.

6. classmethod date.<b>fromisocalendar</b>(year, week, day)
->Return a date corresponding to the ISO calendar date specified by year
, week and day.

* Instance methods:

1. date.<b>replace</b>(year=self.year,month=self.month,day=self.day)

2. date.<b>timetuple</b>()

3. date.<b>toordinal</b>()
-> return the proleptic Gregorian ordinal of the date, where Jan 1 of
year 1 has ordianl 1.
`date.fromordinal(d.toordinal()) == d` 

4. date.<b>weekday</b>
-> Return the day of the week as an integer, where Monday is 0 and
Sunday is 6.
`date(2002, 12, 4).weekday() == 2` a Wed

5. date.<b>isoweekday</b>
-> Monday is 1 and Sunday is 7
-> `date(2002, 12, 4).isoweekday() == 3`, a wed

6. date.<b>isocalendar</b>
-> Return a 3-tuple, (ISO year, ISO week number, ISO weekday)

7. date.<b>isoformat</b>
-> Return a string representing the date in ISO format,
`YYYY-MM-DD`

8. date.ctime()
-> Return a string representing the date:

