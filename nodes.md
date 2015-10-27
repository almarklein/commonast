*(this document is auto-generated, do not edit)*


# Node specifications



Each node has a number of attributes as specified below. Each node also
has a `lineno` and `col_offset` property. Further it has a `tojson()`
method, and a tree can be reconstructed using `Node.fromjson()`. Running
`print(node)` will print a node's json.


## Enums

`Node.OPS` -  Operator enums: Add, And, BitAnd, BitOr, BitXor, Div, FloorDiv, Invert, LShift, Mod, Mult, Not, Or, Pow, RShift, Sub, UAdd, USub

`Node.COMP` -  Comparison enums: Eq, Gt, GtE, In, Is, IsNot, Lt, LtE, NotEq, NotIn

## General

#### class Comment

* ``value``:  the comment string.

#### class Module

Each code that an AST is created for gets wrapped in a Module node.

* ``body_nodes``:  a list of nodes.

## Literals

#### class Num

* ``value``:  the number as a native Python object (int, float, or complex).

#### class Str

* ``value``:  the native Python str object.

#### class Bytes

* ``value``:  the native Python bytes object.

#### class List

* ``element_nodes``:  the items in the list.

#### class Tuple

* ``element_nodes``:  the items in the tuple.

#### class Set

* ``element_nodes``:  the items in the set.

#### class Dict

* ``key_nodes``:  the keys of the dict.
* ``value_nodes``:  the corresponding values.

#### class Ellipsis

Represents the ``...`` syntax for the Ellipsis singleton.

#### class NameConstant

* ``value``:  the corresponding native Python object like True, False or None.

## Variables, attributes, indexing and slicing

#### class Name

* ``name``:  the string name of this variable.

#### class Starred

A starred variable name, e.g. ``*foo``. Note that this isn’t
used to define a function with ``*args`` - FunctionDef nodes have
special fields for that.

* ``value_node``:  the value that is starred, typically a Name node.

#### class Attribute

Attribute access, e.g. ``foo.bar``.

* ``value_node``:  The node to get/set an attribute of. Typically a Name node.
* ``attr``:  a string with the name of the attribute.

#### class Subscript

Subscript access, e.g. ``foo[3]``.

* ``value_node``:  The node to get/set a subscript of. Typically a Name node.
* ``slice_node``:  An Index, Slice or ExtSlice node.

#### class Index

* ``value_node``:  Single index.

#### class Slice

* ``lower_node``:  start slice.
* ``upper_node``:  end slice.
* ``step_node``:  slice step.

#### class ExtSlice

* ``dim_nodes``:  list of Index and Slice nodes (of for each dimension).

## Expressions

#### class Expr

When an expression, such as a function call, appears as a
statement by itself (an expression statement), with its return value
not used or stored, it is wrapped in this container.

* ``value_node``:  holds one of the other nodes in this section, or a
  literal, a Name, a Lambda, or a Yield or YieldFrom node.

#### class UnaryOp

A unary operation (e.g. ``-x``, ``not x``).

* ``op``:  the operator (an enum from ``Node.OPS``).
* ``right_node``:  the operand at the right of the operator.

#### class BinOp

A binary operation (e.g. ``a / b``, ``a + b``).

* ``op``:  the operator (an enum from ``Node.OPS``).
* ``left_node``:  the node to the left of the operator.
* ``right_node``:  the node to the right of the operator.

#### class BoolOp

A boolean operator (``and``, ``or``, but not ``not``).

* ``op``:  the operator (an enum from ``Node.OPS``).
* ``value_nodes``:  a list of nodes. ``a``, ``b`` and ``c`` in
  ``a or b or c``.

#### class Compare

A comparison of two or more values. 

* ``op``:  the comparison operator (an enum from ``Node.COMP``).
* ``left_node``:  the node to the left of the operator.
* ``right_node``:  the node to the right of the operator.

#### class Call

A function call.

* ``func_node``:  Name or Attribute node that represents the function.
* ``arg_nodes``:  list of nodes representing positional arguments.
* ``kwarg_nodes``:  list of Keyword nodes representing keyword arguments.

Note that an argument ``*x`` would be specified as a Starred node
in arg_nodes, and ``**y`` as a Keyword node with a name being ``None``.

#### class Keyword

Keyword argument used in a Call.

* ``name``:  the (string) name of the argument.
* ``value_node``:  the value of the arg.

#### class IfExp

An expression such as ``a if b else c``.

* ``test_node``:  the ``b`` in the above.
* ``body_node``:  the ``a`` in the above.
* ``else_node``:  the ``c`` in the above.

#### class ListComp

List comprehension.

* ``element_node``:  the part being evaluated for each item.
* ``comp_nodes``:  a list of Comprehension nodes.

#### class SetComp

Set comprehension. See ListComp.

#### class GeneratorExp

Generor expression. See ListComp.

#### class DictExp

Dict comprehension.

* ``key_node``:  the key of the item being evaluated.
* ``value_node``:  the value of the item being evaluated.
* ``comp_nodes``:  a list of Comprehension nodes.

#### class Comprehension

Represents a single for-clause in a comprehension.

* ``target_node``:  reference to use for each element, typically a
  Name or Tuple node.
* ``iter_node``:  the object to iterate over.
* ``if_nodes``:  a list of test expressions.

## Statements

#### class Assign

Assignment of a value to a variable.

* ``target_nodes``:  variables to assign to, Name or SubScript.
* ``value_node``:  the object to assign.

#### class AugAssign

Augmented assignment, such as ``a += 1``.

* ``target_node``:  variable to assign to, Name or SubScript.
* ``op``:  operator enum (e.g. ``Node.OPS.Add``)
* ``value_node``:  the object to assign.

#### class Raise

Raising an exception.

* ``exc_node``:  the exception object to be raised, normally a Call
  or Name, or None for a standalone raise.
* ``cause_node``:  the optional part for y in raise x from y.

#### class Assert

An assertion.

* ``test_node``:  the condition to test.
* ``msg_node``:  the failure message (commonly a Str node)

#### class Delete

A del statement.

* ``target_nodes``:  the variables to delete, such as Name, Attribute
  or Subscript nodes.

#### class Pass

Do nothing.

#### class Import

An import statement.

* ``root``:  the name of the module to import from. None if this is
  not a from-import.
* ``names``:  list of (name, alias) tuples, where alias can be None.
* ``level``:  an integer indicating depth of import. Zero means
  absolute import.

## Control flow

#### class If

An if-statement.

Note that elif clauses don’t have a special representation in the
AST, but rather appear as extra If nodes within the else section
of the previous one.

* ``test_node``:  the test, e.g. a Compare node.
* ``body_nodes``:  the body of the if-statement.
* ``else_nodes``:  the body of the else-clause of the if-statement.

#### class For

A for-loop.

* ``target_node``:  the variable(s) the loop assigns to.
* ``iter_node``:  the object to iterate over.
* ``body_nodes``:  the body of the for-loop.
* ``else_nodes``:  the body of the else-clause of the for-loop.

#### class While

A while-loop.

* ``test_node``:  the test to perform on each iteration.
* ``body_nodes``:  the body of the for-loop.
* ``else_nodes``:  the body of the else-clause of the for-loop.

#### class Break

Break from a loop.

#### class Continue

Continue with next iteration of a loop.

#### class Try

Try-block.

* ``body_nodes``:  the body of the try-block (i.e. the code to try).
* ``handler_nodes``:  a list of ExceptHandler instances.
* ``else_nodes``:  the body of the else-clause of the try-block.
* ``finally_nodes``:  the body of the finally-clause of the try-block.

#### class ExceptHandler

Single except-clause.

* ``type_node``:  the type of exception to catch. Often a Name node
  or None to catch all.
* ``name``:  the string name of the exception object in case of ``as err``.
* ``body_nodes``:  the body of the except-clause.

#### class With

A with-block (i.e. a context manager).

* ``item_nodes``:  a list of WithItem nodes (i.e. context managers).
* ``body_nodes``:  the body of the with-block.

#### class WithItem

A single context manager in a with block.

* ``expr_node``:  the expression for the context manager.
* ``as_node``:  a Name, Tuple or List node representing the ``as foo`` part.

## Function and class definitions

#### class FunctionDef

A function definition.

* ``name``:  the (string) name of the function.
* ``decorator_nodes``:  the list of decorators to be applied, stored
  outermost first (i.e. the first in the list will be applied
  last).
* ``annotation_node``:  the return annotation (Python 3 only).
* ``arg_nodes``:  list of Args nodes representing positional arguments.
* ``kwarg_nodes``:  list of Arg nodes representing keyword arguments.
* ``args_node``:  an Arg node representing ``*args``.
* ``kwargs_node``:  an Arg node representing ``**kwargs``.
* ``body_nodes``:  the body of the function.

#### class Lambda

Anonymous function definition.

* ``arg_nodes``:  list of Args nodes representing positional arguments.
* ``kwarg_nodes``:  list of Arg nodes representing keyword arguments.
* ``args_node``:  an Arg node representing ``*args``.
* ``kwargs_node``:  an Arg node representing ``**kwargs``.
* ``body_nodes``:  the body of the function.

#### class Arg

Function argument for a FunctionDef.

* ``name``:  the (string) name of the argument.
* ``value_node``:  the default value of this argument. Can be None.
* ``annotation_node``:  the annotation for this argument (Python3 only).

#### class Return

A return statement.

#### class Yield

Yield expression.

#### class YieldFrom

YieldFrom expression.

#### class Global

* ``names``:  a list of variable names to declare global.

#### class Nonlocal

* ``names``:  a list of variable names to declare nonlocal.

#### class ClassDef

A class definition.

* ``name``:  a string for the class name.
* ``decorator_nodes``:  the list of decorators to be applied, as in FunctionDef.
* ``arg_nodes``:  list of nodes representing base classes.
* ``kwarg_nodes``:  list of Keyword nodes representing keyword arguments.
* ``body_nodes``:  the body of the class.

Note that an argument ``*x`` would be specified as a Starred node
in arg_nodes, and ``**y`` as a Keyword node with a name being ``None``.

