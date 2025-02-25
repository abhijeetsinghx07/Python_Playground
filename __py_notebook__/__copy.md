# **Types of Copy in Python**

Copying in Python refers to creating duplicates of objects. Python offers **two types of copies**:

1. **Shallow Copy**
2. **Deep Copy**

Both types serve different purposes, and understanding their differences is critical when working with mutable objects like lists, dictionaries, or other collections.

---

### **Why Copying is Important?**

When you assign one variable to another, Python does not create a new object. Instead, both variables reference the same object in memory. Modifying one will affect the other.

Example:

```python
original = [1, 2, 3]
copy = original
copy[0] = 100
print(original)  # Output: [100, 2, 3]

```

To avoid this, we use **copying**.

---

### **1. Shallow Copy**

### **What is a Shallow Copy?**

A **shallow copy** creates a new object and copies the **references** of the original object's elements. If the original object contains mutable elements (like lists), changes made to those mutable elements will be reflected in the copied object.

### **How to Create a Shallow Copy?**

- Using the `copy()` method.
- Using the `copy` module’s `copy()` function.
- Using slicing (`[:]`) for lists.

### **Example of Shallow Copy**:

```python
import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow = copy.copy(original)

# Modify the mutable object inside the original
original[0][0] = 100
print(original)  # Output: [[100, 2, 3], [4, 5, 6]]
print(shallow)   # Output: [[100, 2, 3], [4, 5, 6]] (Both reflect the change)

```

### **Important Note**:

- Only the outer object is duplicated.
- Inner mutable objects (e.g., nested lists) share references.

---

### **2. Deep Copy**

### **What is a Deep Copy?**

A **deep copy** creates a completely independent copy of the original object, including all nested objects. Changes to the original object or its elements will not affect the copied object.

### **How to Create a Deep Copy?**

- Using the `copy.deepcopy()` function.

### **Example of Deep Copy**:

```python
import copy

original = [[1, 2, 3], [4, 5, 6]]
deep = copy.deepcopy(original)

# Modify the mutable object inside the original
original[0][0] = 100
print(original)  # Output: [[100, 2, 3], [4, 5, 6]]
print(deep)      # Output: [[1, 2, 3], [4, 5, 6]] (Deep copy is unaffected)

```

### **Key Differences Between Shallow and Deep Copy**:

| **Aspect** | **Shallow Copy** | **Deep Copy** |
| --- | --- | --- |
| **Copy Type** | Only duplicates the outer object. | Duplicates the outer and all inner objects. |
| **Nested Objects** | References are shared. | Creates independent copies of nested objects. |
| **Performance** | Faster (less memory and time). | Slower (more memory and time). |
| **Usage** | Suitable for flat structures or read-only scenarios. | Ideal for nested structures that need isolation. |

---

### **Methods for Copying Objects**

### **1. Assignment (`=`)**

- Creates a new reference to the same object (no actual copy is made).
- Changes to one variable affect the other.

Example:

```python
original = [1, 2, 3]
assigned = original
assigned[0] = 100
print(original)  # Output: [100, 2, 3]

```

---

### **2. Shallow Copy Methods**

1. **Using `copy()` for Lists and Dictionaries**:
    
    ```python
    original = [1, 2, 3]
    shallow = original.copy()
    shallow[0] = 100
    print(original)  # Output: [1, 2, 3]
    print(shallow)   # Output: [100, 2, 3]
    
    ```
    
2. **Using `[:]` Slicing**:
    
    ```python
    original = [1, 2, 3]
    shallow = original[:]
    shallow[0] = 100
    print(original)  # Output: [1, 2, 3]
    
    ```
    
3. **Using `copy.copy()`**:
    
    ```python
    import copy
    original = [1, 2, 3]
    shallow = copy.copy(original)
    
    ```
    

---

### **3. Deep Copy Method**

1. **Using `copy.deepcopy()`**:
    
    ```python
    import copy
    
    original = [[1, 2], [3, 4]]
    deep = copy.deepcopy(original)
    
    original[0][0] = 100
    print(original)  # Output: [[100, 2], [3, 4]]
    print(deep)      # Output: [[1, 2], [3, 4]]
    
    ```
    

---

### **Important Notes About Copying**

1. **Immutable Objects**:
    - Immutable objects (like integers, strings, and tuples) are not affected by shallow or deep copies. Both methods create a new reference but point to the same value since immutability ensures no changes can occur.
    
    Example:
    
    ```python
    original = (1, 2, 3)
    shallow = original[:]
    print(original is shallow)  # Output: True (Same reference)
    
    ```
    
2. **Custom Objects**:
    - Copying custom objects requires implementing the `__copy__()` and `__deepcopy__()` methods in your class.
    
    Example:
    
    ```python
    import copy
    
    class MyClass:
        def __init__(self, value):
            self.value = value
    
    obj = MyClass(42)
    shallow = copy.copy(obj)
    deep = copy.deepcopy(obj)
    
    ```
    

---

### **Real-Life Use Cases of Copying**

1. **Creating Backups**:
    - Deep copies are used to create backups of data structures that can be independently modified without affecting the original.
    - Example: In a chess game, save the current state of the board before trying a move.
2. **Working with Nested Data**:
    - When dealing with JSON-like data structures (nested dictionaries and lists), deep copies are crucial to prevent unintentional changes to the original data.
    
    Example:
    
    ```python
    import copy
    
    config = {
        "settings": {"theme": "dark", "notifications": True},
        "user": {"name": "Alice"}
    }
    backup_config = copy.deepcopy(config)
    
    ```
    
3. **Handling Undo/Redo in Applications**:
    - In text editors, graphics editors, or games, keeping deep copies of the state allows implementing undo/redo functionality.
4. **Simulations**:
    - In scientific computations or simulations, deep copies ensure that experiments can run on independent data sets.
5. **Machine Learning**:
    - Copying data structures (e.g., training data) to preprocess or augment them without modifying the original dataset.

---

### **Summary**

| **Aspect** | **Shallow Copy** | **Deep Copy** |
| --- | --- | --- |
| **Definition** | Copies the outer object only. | Creates a full independent copy. |
| **Nested Objects** | Shares references to inner objects. | Copies all nested objects. |
| **Performance** | Faster and uses less memory. | Slower and uses more memory. |
| **When to Use** | Flat structures or read-only data. | Complex, nested, or modifiable data. |

---

### **Key Takeaways**

- **Shallow Copy**: Faster but shares references for nested objects.
- **Deep Copy**: Completely independent copy but slower and consumes more memory.
- **Assignment**: No actual copy is made; both variables share the same reference.
- **Real-World Importance**: Copying ensures data safety in projects like data processing, backups, simulations, or undo/redo implementations.