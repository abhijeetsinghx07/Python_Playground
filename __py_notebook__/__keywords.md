# **What is keyword in Python?**

- Python keywords are **reserved words that have a special meaning** associated with them and we can’t use it for other things.
- Each keyword is designed to achieve specific functionality.

Python keywords are **case-sensitive**.

1. All keywords contain only letters (no special symbols)
2. Except for three keywords (`True`, `False`, `None`), all keywords have lower case letters

# **Get the List of Keywords**

As of Python 3.12.8, there are **35 keywords** available. This number can vary slightly over time.

We can use the following two ways to get the list of keywords in Python

- **keyword module**: The keyword is the built-in module to get the list of keywords. Also, this module allows a Python program to determine if a string is a keyword.
- **`help()` function**: Apart from a keyword module, we can use the **`help()`** function to get the list of keywords

```python
import keyword
print(keyword.kwlist)
```

```python
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
'return', 'try', 'while', 'with', 'yield']
```

All the keywords except, `True`, `False`, and `None`, must be written in a lowercase alphabet symbol.

```python
help("keywords")
```

```python
Here is a list of the Python keywords.  Enter any keyword to get more help.

False               break               for                 not
None                class               from                or
True                continue            global              pass
__peg_parser__      def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
```

**Note**:

- We cannot use any of the keywords as identifiers in our programs. If we try to do so, we will get an error.
- An identifier is a name given to an entity, For example, variables name, functions name, or class name.

# **Understand Any keyword**

The python **`help()` function** is used to display the documentation of modules, functions, classes, keywords.

Pass the keyword name to the `help()` function to get to know how to use it. The `help()` function returns the description of a keyword along with an example.

Let’s understand how to use the `if` keyword.

```python
print(help('if'))
```

```python
The "if" statement
******************

The "if" statement is used for conditional execution:

   if_stmt ::= "if" assignment_expression ":" suite
               ("elif" assignment_expression ":" suite)*
               ["else" ":" suite]

It selects exactly one of the suites by evaluating the expressions one
by one until one is found to be true (see section Boolean operations
for the definition of true and false); then that suite is executed
(and no other part of the "if" statement is executed or evaluated).
If all expressions are false, the suite of the "else" clause, if
present, is executed.
```

# **Keyword Module**

Python keyword module allows a Python program to determine if a string is a keyword.

**`iskeyword(s)`: Returns `True` if `s` is a keyword**

```python
import keyword

print(keyword.iskeyword('if'))
# Output = True 

print(keyword.iskeyword('range'))
# Output = False
```

**Output**:

As you can see in the output, it returned True because ‘if’ is the keyword, and it returned False because the range is not a keyword (it is a built-in function).

Also, keyword module provides following functions to identify keywords.

- **`keyword.kwlist:`** It return a sequence containing all the keywords defined for the interpreter.
- **`keyword.issoftkeyword(s)`**: Return **`True`** if *s* is a Python soft keyword.
- **`keyword.softkwlist`**: Sequence containing all the soft keywords defined for the interpreter.

```python
>>> import keyword as key
>>> key.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

>>> key.iskeyword('True')
True

>>> key.iskeyword('range')
False

>>> key.softkwlist
['_', 'case', 'match', 'type']

>>> key.issoftkeyword('_')
True

>>> key.issoftkeyword('or')
False
```

### **Can We Use Soft Keywords as Identifiers in Python?**

✅ **Yes, we can use soft keywords as identifiers in Python!** Unlike **reserved keywords**, soft keywords have special meaning only in specific contexts but can still be used as variable names outside those contexts.

---

## **🔹 What are Soft Keywords in Python?**

Soft keywords are **not fully reserved keywords**, meaning they only have special meaning in specific situations. Outside of those contexts, they can be used as variable names, function names, or class names.

---

### **📌 Example: Using Soft Keywords as Identifiers**

Let's take the soft keyword `match` (introduced in Python 3.10 for `match-case` statements).

```python
match = "This is a soft keyword!"
print(match)  # ✅ No error, it works as a normal variable.

```

✅ **Output:**

```
This is a soft keyword!

```

Even though `match` is used in `match-case` statements, it **does not act as a reserved keyword outside that context**.

---

## **🔹 List of Soft Keywords in Python 3.11+**

Soft keywords introduced in different Python versions:

| Soft Keyword | Introduced In | Meaning (Context) |
| --- | --- | --- |
| `_` | Python 3.10 | Wildcard in pattern matching (`case _:`) |
| `match` | Python 3.10 | Pattern matching (`match-case`) |
| `case` | Python 3.10 | Used in `match-case` |
| `type` | Python 3.10 | Used in Structural Pattern Matching |
| `as` | Earlier versions | Used in `import ... as` but also works as a variable |
| `yield` | Earlier versions | Used in generators but not always reserved |

---

### **📌 `_` as a Soft Keyword in Python 3.10+**

In **Python 3.10+**, `_` is a **soft keyword** inside `match-case` statements, where it acts as a **wildcard** that matches anything.

### **Example: `_` in Pattern Matching (Wildcard Use)**

```python
value = 10

match value:
    case 1:
        print("Matched 1")
    case _:
        print("Wildcard match")  # `_` matches anything

```

✅ **Output:**

```
Wildcard match

```

Here, `_` acts as a **wildcard** and has special meaning **only inside `match-case` blocks**.

---

### **📌 When Soft Keywords Cannot Be Used as Identifiers**

Soft keywords can be used as identifiers **except when they are in their special context**.

### ❌ **Example where `_` is used in pattern matching (error if misused)**:

```python
match = 5

match match:  # ❌ SyntaxError in Python 3.10+
    case _:
        print("Invalid usage")

```

Since `match` is used in its special **pattern matching** context, it cannot be treated as an identifier here.

---

### **💡 Conclusion**

✅ **Soft keywords can be used as identifiers unless they are in their special context.**

✅ Unlike **reserved keywords**, they do not always have fixed meanings.

✅ **Starting from Python 3.10, `_` is a soft keyword in pattern matching** but can still be used as a variable outside that context.
