# Boolean

- In Python, the **Boolean** data type (`bool`) represents one of two values:
    - **`True`**
    - **`False`**
- The Boolean data type is commonly used in decision-making, comparisons, and logical operations.
- Default Value of bool is False
- It is case-sensitive. First letter have to be uppercase True & False

---

### **Key Characteristics of Booleans**

1. **Two Possible Values**:
    - `True` and `False` are the only values of the `bool` data type.
    - They are case-sensitive and must be written with an uppercase first letter.
2. **Built-In Type**:
    - Booleans are a subclass of integers in Python.
    - Internally:
        - `True` is equivalent to `1`.
        - `False` is equivalent to `0`.
3. **Default Boolean Evaluation**:
    - Objects in Python can evaluate to `True` or `False` when used in a Boolean context.
    - Certain values are considered **False**, such as `0`, `None`, `""` (empty string), and empty collections (`[]`, `{}`, etc.).

---

### **Boolean Type Examples**

### **Basic Boolean Values**

```python
x = True
y = False

print(type(x))  

# Output: <class 'bool'>
```

### **Booleans as Integers**

```python
print(int(True))   
# Output: 1

print(int(False))  
# Output: 0

print(True + True)  
# Output: 2 (1 + 1)

print(False + 5)    
# Output: 5 (0 + 5)

```

---

### **Boolean Expressions**

### **Comparison Operators**

Boolean values are often the result of comparison operations.

```python
a = 10
b = 5

print(a > b)   
# True

print(a == b)  
# False

print(a <= b)  
# False

```

### **Logical Operators**

Booleans can be combined using logical operators:

1. **`and`**: Returns `True` if both conditions are `True`.
2. **`or`**: Returns `True` if at least one condition is `True`.
3. **`not`**: Negates the Boolean value.

```python
x = True
y = False

print(x and y)  
# Output: False

print(x or y)   
# Output: True

print(not x)    
# Output: False

```

---

### **Interesting Properties of Booleans**

### **1. Booleans are Subclasses of Integers**

Booleans are derived from the `int` type in Python.

```python
print(isinstance(True, int))   
# Output: True

print(isinstance(False, int))  
# Output: True

```

This means you can use Booleans in arithmetic operations.

```python
result = True + False + True
print(result)  

# Output: 2
```

---

### **2. Boolean Evaluation of Objects**

In Python, the following objects evaluate to **`False`**:

- **Constants**: `None`, `False`
- **Zero Values**: `0`, `0.0`, `0j` (complex zero)
- **Empty Containers**: `""` (empty string), `[]` (empty list), `{}` (empty dictionary), `set()`, `()`, etc.

Everything else evaluates to **`True`**.

```python
print(bool(0))        # Output: False
print(bool(""))       # Output: False
print(bool([]))       # Output: False
print(bool("Python")) # Output: True
print(bool(100))      # Output: True

```

---

### **3. Boolean Short-Circuiting**

Logical operators (`and`, `or`) employ **short-circuit evaluation**:

- **`and`** stops and returns the first `False` value.
- **`or`** stops and returns the first `True` value.

```python
# and short-circuiting
print(False and (5 / 0))  
# Output: False (doesn't evaluate 5 / 0)

# or short-circuiting
print(True or (5 / 0))    
# Output: True (doesn't evaluate 5 / 0)

```

---

### **Examples of Boolean Use Cases**

### **1. Decision-Making**

```python
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

```

### **2. Filtering Data**

```python
numbers = [1, 2, 3, 0, -1, -2]

# Keep only positive numbers
positive_numbers = [n for n in numbers if n > 0]
print(positive_numbers)  # Output: [1, 2, 3]

```

### **3. Default Values with `or`**

Use `or` to provide a default value when a variable is `Falsy`.

```python
username = ""  # Empty string evaluates to False
print(username or "Guest")  # Output: Guest

```

### **4. Boolean as Flags**

Booleans are often used as flags to control program flow.

```python
is_logged_in = False

if is_logged_in:
    print("Welcome back!")
else:
    print("Please log in.")

```

---

### **Summary**

| **Aspect** | **Description** |
| --- | --- |
| **Values** | `True` and `False` |
| **Type** | Subclass of `int` |
| **Default Boolean Values** | Objects like `0`, `None`, `""`, and empty collections evaluate to `False`. |
| **Operators** | Logical (`and`, `or`, `not`), Comparison (`>`, `<`, `==`, `!=`, etc.). |
| **Short-Circuiting** | Logical operators stop evaluation when result is determined. |
| **Use Cases** | Decision-making, flags, filtering, and validating inputs. |

---