# commonast

A common AST description for Python

The aim of this project is to define a common ast description, that is
the same for different Python versions and implementations. All code
is in [commonast.py](https://github.com/zoofIO/flexx/blob/master/flexx/pyscript/commonast.py).
It defines a function `parse()` to act as a replacement for
`ast.parse()`.

For a definition of the nodes see 
[the nodes docs](https://github.com/almarklein/commonast/blob/master/nodes.md).

## Requirements / support

Commonast has been tested to work on:

* CPython 2.7
* CPython 3.3
* CPython 3.4
* CPython 3.5
* CPython 3.6
* pypy, pypy3, pypy4


## Installation

Copy the [commonast.py](https://github.com/zoofIO/flexx/blob/master/flexx/pyscript/commonast.py)
module to your own project or put it somewhere on your PYTHONPATH.

This module does not live on pypi and cannot be installed with pip. The
reason for this is that the ast definition may need to be changed if
new Python versions will be supported, which makes that we cannot
guarantee backward compatibility.

## Purpose

I'm using this in
[flexx.pyscript](http://flexx.readthedocs.org/en/latest/pyscript/index.html)
so that the code there can be agnostic about Python version and
implementation. Also, if me or someone else creates a pure Python AST
parser that produces commonast, then we can easily use it in PyScript
to allow it to compile itself (which would open up some awesome
possibilities).

The module is maintained from the Flexx project for now. That may change
if commonast becomes used in other projects.

Maybe this project can be useful to others as well. I'd be happy to
support making this more generally useful.

## Related projects

* https://greentreesnakes.readthedocs.org provide the missing docs on Python's ast module. I found this a crucial resource when implementing commonast 
* https://github.com/Psycojoker/baron
* https://github.com/davidhalter/jedi
* Python's buildin ast module (a C implemantation)
* Pythons buildin `lib2to3` module (probably the easiest route for a
  pure Python ast parser.
* Some people are [discussing a unified ast parser](https://github.com/davidhalter/jedi/issues/630)
