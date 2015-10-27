# Node specifications

### Module

 Each code that an AST is created for gets wrapped in a Module node.
    
    Attributes:
        body_nodes: a list of nodes.

## Literals

### Num


    Attributes:
        value: the number as a native Python object (int, float, or complex).

### Str


    Attributes:
        value: the native Python str object.

### Bytes


    Attributes:
        value: the native Python bytes object.

### List


    Attributes:
        element_nodes: the items in the list.

### Tuple


    Attributes:
        element_nodes: the items in the tuple.

### Set


    Attributes:
        element_nodes: the items in the set.

### Dict


    Attributes:
        key_nodes: the keys of the dict.
        value_nodes: the corresponding values.

### Ellipsis

 Represents the ``...`` syntax for the Ellipsis singleton.

### NameConstant


    Attributes:
        value: the corresponding native Python object like True, False or None.

## Variables, attributes, indexing and slicing

### Name


    Attributes:
        name: the string name of this variable.

### Starred

 A starred variable name, e.g. ``*foo``. Note that this isn’t
    used to define a function with ``*args`` - FunctionDef nodes have
    special fields for that.
    
    Attributes:
        value_node: the value that is starred, typically a Name node.

### Attribute

 Attribute access, e.g. ``foo.bar``.
    
    Attributes:
        value_node: The node to get/set an attribute of. Typically a Name node.
        attr: a string with the name of the attribute.

### Subscript

 Subscript access, e.g. ``foo[3]``.
    
    Attributes:
        value_node: The node to get/set a subscript of. Typically a Name node.
        slice_node: An Index, Slice or ExtSlice node.

### Index


    Attributes:
        value_node: Single index.

### Slice


    Attributes:
        lower_node: start slice.
        upper_node: end slice.
        step_node: slice step.

### ExtSlice


    Attributes:
        dim_nodes: list of Index and Slice nodes (of for each dimension).

## Expressions

### Expr

 When an expression, such as a function call, appears as a
    statement by itself (an expression statement), with its return value
    not used or stored, it is wrapped in this container.
    
    Attributes:
        value_node: holds one of the other nodes in this section, or a
            literal, a Name, a Lambda, or a Yield or YieldFrom node.

### UnaryOp

 A unary operation (e.g. ``-x``, ``not x``).
    
    Attributes:
        op: the operator (an enum from ``Node.OPS``).
        value_nodes: a list with one node (i.e. the operand).

### BinOp

 A binary operation (e.g. ``a / b``, ``a + b``).
    
    Attributes:
        op: the operator (an enum from ``Node.OPS``).
        value_nodes: a list with two nodes (the one to the left and the
            one to the right of the operator).

### BoolOp

 A boolean operator (``and``, ``or``, but not ``not``).
    
    Attributes:
        op: the operator (an enum from ``Node.OPS``).
        value_nodes: a list of nodes. ``a``, ``b`` and ``c`` in 
            ``a or b or c``.

### Compare

 A comparison of two or more values. 
    
    Attributes:
        op: the comparison operator (an enum from ``Node.COMP``).
        value_nodes: a list with two nodes (the one to the left and the
            one to the right of the operator).

### Call

 A function call.
    
    Attributes:
        func_node: Name or Attribute node that represents the function.
        arg_nodes: list of nodes representing positional arguments.
        kwarg_nodes: list of Keyword nodes representing keyword arguments.
    
    Note that an argument ``*x`` would be specified as a Starred node
    in arg_nodes, and ``**y`` as a Keyword node with a name being ``None``.

### Keyword

 Keyword argument used in a Call.
    
    Attributes:
        name: the (string) name of the argument.
        value_node: the value of the arg.

### IfExp

 An expression such as ``a if b else c``.
    
    Attributes:
        test_node: the ``b`` in the above.
        body_node: the ``a`` in the above.
        else_node: the ``c`` in the above.

### ListComp

 List comprehension.
    
    Attributes:
        element_node: the part being evaluated for each item.
        comp_nodes: a list of Comprehension nodes.

### SetComp

 Set comprehension. See ListComp.

### GeneratorExp

 Generor expression. See ListComp.

### DictExp

 Dict comprehension.
    
    Attributes:
        key_node: the key of the item being evaluated.
        value_node: the value of the item being evaluated.
        comp_nodes: a list of Comprehension nodes.

### Comprehension

 Represents a single for-clause in a comprehension.
    
    Attributes:
        target_node: reference to use for each element, typically a
            Name or Tuple node.
        iter_node: the object to iterate over.
        if_nodes: a list of test expressions.

## Statements

### Assign

 Assignment of a value to a variable.
    
    Attributes:
        target_nodes: variables to assign to, Name or SubScript.
        value_node: the object to assign.

### AugAssign

 Augmented assignment, such as ``a += 1``.
    
    Attributes:
        target_node: variable to assign to, Name or SubScript.
        op: operator enum (e.g. ``Node.OPS.Add``)
        value_node: the object to assign.

### Raise

 Raising an exception.
    
    Attributes:
        exc_node: the exception object to be raised, normally a Call
            or Name, or None for a standalone raise.
        cause_node: the optional part for y in raise x from y.

### Assert

 An assertion.
    
    Attributes:
        test_node: the condition to test.
        msg_node: the failure message (commonly a Str node)

### Delete

 A del statement.
    
    Attributes:
        target_nodes: the variables to delete, such as Name, Attribute
            or Subscript nodes.

### Pass

 Do nothing.

### Import

 An import statement.
    
    Attributes:
        root: the name of the module to import from. None if this is
            not a from-import.
        names: list of (name, alias) tuples, where alias can be None.
        level: an integer indicating depth of import. Zero means
            absolute import.

## Control flow

### If

 An if-statement.
    
    Note that elif clauses don’t have a special representation in the
    AST, but rather appear as extra If nodes within the else section
    of the previous one.
    
    Attributes:
        test_node: the test, e.g. a Compare node.
        body_nodes: the body of the if-statement.
        else_nodes: the body of the else-clause of the if-statement.

### For

 A for-loop.
    
    Attributes:
        target_node: the variable(s) the loop assigns to.
        iter_node: the object to iterate over.
        body_nodes: the body of the for-loop.
        else_nodes: the body of the else-clause of the for-loop.

### While

 A while-loop.
    
    Attributes:
        test_node: the test to perform on each iteration.
        body_nodes: the body of the for-loop.
        else_nodes: the body of the else-clause of the for-loop.

### Break

 Break from a loop.

### Continue

 Continue with next iteration of a loop.

### Try

 Try-block.
    
    Attributes:
        body_nodes: the body of the try-block (i.e. the code to try).
        handler_nodes: a list of ExceptHandler instances.
        else_nodes: the body of the else-clause of the try-block.
        finally_nodes: the body of the finally-clause of the try-block.

### ExceptHandler

 Single except-clause.
    
    Attributes:
        type_node: the type of exception to catch. Often a Name node
            or None to catch all.
        name: the string name of the exception object in case of ``as err``.
        body_nodes: the body of the except-clause.

### With

 A with-block (i.e. a context manager).
    
    Attributes:
        item_nodes: a list of WithItem nodes (i.e. context managers).
        body_nodes: the body of the with-block.

### WithItem

 A single context manager in a with block.
    
    Attributes:
        expr_node: the expression for the context manager.
        as_node: a Name, Tuple or List node representing the ``as foo`` part.

## Function and class definitions

### FunctionDef

 A function definition.
    
    Attributes:
        name: the (string) name of the function.
        decorator_nodes: the list of decorators to be applied, stored
            outermost first (i.e. the first in the list will be applied
            last).
        annotation_node: the return annotation (Python 3 only).
        arg_nodes: list of Args nodes representing positional arguments.
        kwarg_nodes: list of Arg nodes representing keyword arguments.
        args_node: an Arg node representing ``*args``.
        kwargs_node: an Arg node representing ``**kwargs``.
        body_nodes: the body of the function.

### Lambda

 Anonymous function definition.
    
    Attributes:
        arg_nodes: list of Args nodes representing positional arguments.
        kwarg_nodes: list of Arg nodes representing keyword arguments.
        args_node: an Arg node representing ``*args``.
        kwargs_node: an Arg node representing ``**kwargs``.
        body_nodes: the body of the function.

### Arg

 Function argument for a FunctionDef.
    
    Attributes:
        name: the (string) name of the argument.
        value_node: the default value of this argument. Can be None.
        annotation_node: the annotation for this argument (Python3 only).

### Return

 A return statement.

### Yield

 Yield expression.

### YieldFrom

 YieldFrom expression.

### Global


    Attributes:
        names: a list of variable names to declare global.

### Nonlocal


    Attributes:
        names: a list of variable names to declare nonlocal.

### ClassDef

 A class definition.
    
    Attributes:
        name: a string for the class name.
        decorator_nodes: the list of decorators to be applied, as in FunctionDef.
        arg_nodes: list of nodes representing base classes.
        kwarg_nodes: list of Keyword nodes representing keyword arguments.
        body_nodes: the body of the class.
    
    Note that an argument ``*x`` would be specified as a Starred node
    in arg_nodes, and ``**y`` as a Keyword node with a name being ``None``.

