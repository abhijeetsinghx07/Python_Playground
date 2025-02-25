## What is Variables?

- **Variables are containers that is used for storing data values. In simple terms it is used to reserved memory area to store a value.**
- Everything in Python is treated as an object so every variable is nothing but an object in Python.
- A variable can be either **mutable** or **immutable**.
    - If the variable’s value can change, the object is called **mutable**, while if the value cannot change, the object is called **immutable**.
- We don’t need to declare a variable or data type of variable before using it because python is dynamically typed. Data type declaration happens automatically when we assign a value to a variable.
- Python automatically handles **type inference** and memory allocation.

## **Definition of Dynamic Typing**

Python is a **dynamically typed** language, which means:

✔ **You don’t need to declare variable types explicitly** (e.g., `int`, `float`, `str`).

✔ **The type of a variable is determined at runtime**, based on the assigned value.

✔ **Variables can change types during execution** (type flexibility).

## **Drawbacks of Dynamic Typing**

🚨 **Runtime Errors** → Errors appear only when the program runs.

🚨 **Unexpected Type Changes** → Can lead to logic errors.

🚨 **Performance Issues** → Python must check variable types dynamically, making it slower than statically typed languages.

✔ **Solution:** Use **type hints** for better maintainability.

```python
def add_numbers(a: int, b: int) -> int:
    return a + b
```

### **Changing the value of a variable**

Many programming languages are statically typed languages where the variable is initially declared with a specific type, and during its lifetime, it must always have that type.

But in Python, variables are **dynamically typed** and not subject to the **data type** restriction. A variable may be assigned to a value of **one type**, and then later, we can also re-assigned a value of a **different type**.

### **Delete a variable**

- Use the `del` keyword to delete the variable.
- Once we delete the variable, it will not be longer accessible and eligible for the garbage collector.

```python
var1 = 100
print(var1)
```

```python
var1 = 100
del var1
```

### **Variable’s case-sensitive**

- Python is a case-sensitive language.
- If we define a variable with names `a = 100` and `A =200` then, Python differentiates between `a` and `A`.
- These variables are treated as two different variables (or objects).

### **Constant**

- **Constant** is a variable or value that does not change, which means it remains the same and cannot be modified.
- But in the case of Python, the constant concept is **not applicable**.
- We can use only uppercase characters to define the constant variable if we don’t want to change it.

**Example**

```python
MAX_VALUE = 500
```

- It is just convention, but we can change the value of `MAX_VALUE` variable
- A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

### Variable v/s Identifier

| **Variables** | **Identifier** |
| --- | --- |
| Variables are used to store data. | Identifier is used to name a variable, a function, a class, a structure, a union. |
| Variables are declared using an identifier. | Identifiers are used to declare variables, functions, classes, etc. |
| Variables have a datatype. The data type of a variable denotes the kind of data that can be stored in it. | Identifiers do not have a data type. |
| Variables have a value. The value of a variable can be modified during the execution of the program. | Identifiers do not hold a value. |
| Variables do not have naming conventions. They can be named anything. | Identifiers must follow a naming convention. Identifiers must be meaningful and descriptive. |
| All the variables names are identifiers. | All identifiers are not variables. |
| Variable is created to assign a unique name to a specific memory location. | Identifiers are created assign a name to an entity. |

---

### **Key Features of Variables in Python**

1. **Dynamic Typing**:
    - Variables in Python are dynamically typed, meaning you don’t need to declare their type explicitly. The type is determined by the value assigned to it.
    
    ```python
    x = 10  # Integer
    x = "Hello"  # Now it's a string
    
    ```
    
2. **No Declaration**:
    - You don’t need to declare variables before using them.
    
    ```python
    x = 25  # Automatically declares x as an integer
    
    ```
    
3. **No Fixed Memory Allocation**:
    - Python handles memory allocation automatically.
4. **Case-Sensitive**:
    - Variable names are case-sensitive.
    
    ```python
    name = "Alice"
    Name = "Bob"
    print(name, Name)  # Output: Alice Bob
    
    ```
    

---

### **Rules for Naming Variables**

1. Variable names must **start with a letter** (a-z, A-Z) or an underscore `_`.
    
    ```python
    _name = "John"  # Valid
    
    ```
    
2. The name can contain **letters, digits, or underscores** but cannot start with a digit.
    
    ```python
    age1 = 25  # Valid
    1age = 25  # Invalid
    
    ```
    
3. Reserved keywords cannot be used as variable names.
    
    ```python
    class = 10  # Invalid (class is a keyword)
    
    ```
    
4. Variable names are case-sensitive.
    
    ```python
    var = 10
    Var = 20
    print(var, Var)  # Output: 10 20
    
    ```
    

---

### **Variable Declaration and Assignment**

In Python, declaring and assigning variables is straightforward:

```python
variable_name = value

```

### **Examples**:

```python
x = 10          # Integer
name = "Alice"  # String
pi = 3.14       # Float
is_valid = True # Boolean

```

---

### **Variable Types in Python**

Python has **built-in data types** for variables. These can be categorized as **Primitive Types** and **Non-Primitive Types**.

---

### **A. Primitive Types**

1. **Integer (`int`)**:
    - Represents whole numbers.
    
    ```python
    age = 25
    print(type(age))  # Output: <class 'int'>
    
    ```
    
2. **Floating-Point (`float`)**:
    - Represents decimal numbers.
    
    ```python
    price = 99.99
    print(type(price))  # Output: <class 'float'>
    
    ```
    
3. **String (`str`)**:
    - Represents textual data.
    
    ```python
    name = "Alice"
    print(type(name))  # Output: <class 'str'>
    
    ```
    
4. **Boolean (`bool`)**:
    - Represents `True` or `False` values.
    
    ```python
    is_logged_in = True
    print(type(is_logged_in))  # Output: <class 'bool'>
    
    ```
    
5. **Complex Numbers (`complex`)**:
    - Represents numbers with a real and imaginary part.
    
    ```python
    z = 3 + 4j
    print(type(z))  # Output: <class 'complex'>
    
    ```
    

---

### **B. Non-Primitive Types**

1. **List**:
    - An ordered, mutable collection of items.
    
    ```python
    fruits = ["apple", "banana", "cherry"]
    print(type(fruits))  # Output: <class 'list'>
    
    ```
    
2. **Tuple**:
    - An ordered, immutable collection of items.
    
    ```python
    coordinates = (10, 20)
    print(type(coordinates))  # Output: <class 'tuple'>
    
    ```
    
3. **Set**:
    - An unordered collection of unique items.
    
    ```python
    unique_numbers = {1, 2, 3, 3}
    print(unique_numbers)  # Output: {1, 2, 3}
    
    ```
    
4. **Dictionary (`dict`)**:
    - A collection of key-value pairs.
    
    ```python
    student = {"name": "Alice", "age": 25}
    print(type(student))  # Output: <class 'dict'>
    
    ```
    

---

### **Interesting Concepts Related to Variables**

### **1. Multiple Assignment**

Assign multiple variables in a single line.

```python
x, y, z = 10, 20, 30
print(x, y, z)  # Output: 10 20 30

```

### **2. Same Value Assignment**

Assign the same value to multiple variables.

```python
a = b = c = 100
print(a, b, c)  # Output: 100 100 100

```

### **3. Variable Reassignment**

Variables can be reassigned to different types dynamically.

```python
x = 10
x = "Hello"  # Reassigned to string

```

### **4. Constants**

Python does not have built-in constants, but by convention, constants are named using all uppercase letters.

```python
PI = 3.14159  # A constant by convention

```

---

### **Scope of Variables**

1. **Global Variables**:
    - Declared outside any function.
    - Accessible throughout the program.
    
    ```python
    x = 10  # Global variable
    
    def print_global():
        print(x)
    
    print_global()  # Output: 10
    
    ```
    
2. **Local Variables**:
    - Declared inside a function.
    - Accessible only within that function.
    
    ```python
    def my_function():
        y = 20  # Local variable
        print(y)
    
    my_function()  # Output: 20
    
    ```
    
3. **Global Keyword**:
    - Used to modify a global variable inside a function.
    
    ```python
    x = 10
    
    def modify_global():
        global x
        x = 20
    
    modify_global()
    print(x)  # Output: 20
    
    ```
    

---

### **Real-Life Use Cases of Variables**

1. **E-Commerce Websites**:
    - Storing product details, user information, or cart totals.
    
    ```python
    product_name = "Laptop"
    price = 750.00
    quantity = 2
    total = price * quantity
    
    ```
    
2. **Web Applications**:
    - Maintaining user sessions, tokens, or form inputs.
    
    ```python
    user_session = {"username": "alice", "logged_in": True}
    
    ```
    
3. **Game Development**:
    - Tracking player scores, levels, and game states.
    
    ```python
    score = 0
    level = 1
    is_game_over = False
    
    ```
    
4. **Data Analysis**:
    - Storing intermediate calculations or dataset summaries.
    
    ```python
    mean = sum(data) / len(data)
    
    ```
    
5. **IoT Applications**:
    - Storing sensor readings and controlling devices.
    
    ```python
    temperature = 25.6
    humidity = 40.2
    
    ```
    

---

### **Best Practices for Variables**

1. **Use Descriptive Names**:
    
    ```python
    x = 25  # Poor
    age = 25  # Good
    
    ```
    
2. **Avoid Reserved Keywords**:
    
    ```python
    for = 10  # Invalid
    
    ```
    
3. **Follow Naming Conventions**:
    - Use snake_case for variables (`total_price`).
    - Use UPPERCASE for constants (`MAX_LIMIT`).
4. **Avoid Reassigning Important Variables**:
    
    ```python
    id = 123  # Avoid overwriting built-in functions like id()
    
    ```
    

---

### **Summary:**

| **Aspect** | **Details** |
| --- | --- |
| **Definition** | Variables are containers for storing data in memory. |
| **Dynamic Typing** | Python determines the type of a variable at runtime based on the value. |
| **Types of Variables** | Primitive (`int`, `str`, etc.), Non-Primitive (`list`, `dict`, etc.). |
| **Scope** | Global and Local variables. |
| **Best Practices** | Use descriptive names, avoid reserved keywords, follow naming conventions. |

---