# List

- A **list** is a built-in data type in Python that represents an **ordered, mutable collection of items**. Lists can hold items of any data type (integers, strings, floats, other lists, etc.), and a single list can mix different data types.
- A **list** in Python is a versatile and powerful **data structure** that is used to store an ordered collection of items.
- Lists are **mutable**, which means that the elements inside a list can be changed after the list is created.
- Lists can hold items of **mixed data types**, including numbers, strings, and even other lists.
- Default value of list is : [ ]

---

### Key Features of Python Lists:

- **Ordered**: Elements have a defined order, and this order will not change unless explicitly modified.
- **Mutable**:  ****The elements of the list can be modified. Elements can be added, removed, or changed.
- **Heterogeneous**: Can store different data types (e.g., integers, strings, floats).
- **Indexed**: Access to list elements is via indexing, starting from 0 for the first element.
- **Contain Duplicates**: List can contain duplicates.

---

**Why use a list?**

- The list data structure is very flexible It has many unique inbuilt functionalities like `pop()`, `append()`, etc which makes it easier, where the data keeps changing.
- Also, the list can contain duplicate elements i.e two or more items can have the same values.
- Lists are Heterogeneous i.e, different kinds of objects/elements can be added
- As Lists are mutable it is used in applications where the values of the items change frequently.

---

### Creating a List

You can create a list by placing all the elements inside square brackets `[]`, separated by commas.

### Example:

```python
my_list = [] # Empty list
print(my_list)

#Output: []

my_list = [1, "Hello", 3.14, [5, 6]] # List with heterogeneous elements
print(my_list)  

# Output: [1, "Hello", 3.14, [5, 6]]

```

---

### Accessing List Elements

Lists are **indexed**, meaning you can access individual elements using an index number. Indexing in Python starts at **0**.

### Example:

```python
my_list = [10, 20, 30, 40, 50]

# Access the first element
print(my_list[0])  # Output: 10

# Access the last element
print(my_list[-1])  # Output: 50

```

You can modify items in a list **without using any method** by accessing the elements directly through **indexing**. Since lists are **mutable**, you can change the value of an element at a specific index by directly assigning a new value to that index.

### Example of Modifying a List Item by Index

### 1. Modify a Single Item:

You can replace an existing item by assigning a new value to a particular index.

```python
my_list = [10, 20, 30, 40, 50]

# Modify the element at index 2
my_list[2] = 99  # Changing 30 to 99

print(my_list)  # Output: [10, 20, 99, 40, 50]

```

### 2. Modify Multiple Items Using Slicing:

You can also modify multiple elements at once using **slicing**. This allows you to replace a range of elements with new values.

```python
my_list = [1, 2, 3, 4, 5]

# Modify elements from index 1 to 3 (exclusive)
my_list[1:4] = [10, 20, 30]

print(my_list)  # Output: [1, 10, 20, 30, 5]

```

```python
>>> coffee
['Espresso', 'Cold Coffee', 'Cold Coffee', 'Black']

>>> coffee[1:3]=["Cappucino","Americano"]

>>> coffee
['Espresso', 'Cappucino', 'Americano', 'Black']

>>> coffee[1:1]
[]

>>> coffee[1:1]=["Cafe","Cafe"]

>>> coffee
['Espresso', 'Cafe', 'Cafe', 'Cappucino', 'Americano', 'Black']

>>> coffee[1:2]
['Cafe']

>>> coffee[1:3]
['Cafe', 'Cafe']

>>> coffee[1:3]=[]

>>> coffee
['Espresso', 'Cappucino', 'Americano', 'Black']
```

---

### Additional Examples:

### Modifying the First and Last Elements:

```python
my_list = ['apple', 'banana', 'cherry']

# Modify the first element
my_list[0] = 'orange'

# Modify the last element
my_list[-1] = 'grape'

print(my_list)  # Output: ['orange', 'banana', 'grape']

```

### Replacing Part of a List with Another List:

```python
my_list = [1, 2, 3, 4, 5]

# Replace elements from index 1 to 3 with new values
my_list[1:4] = [100, 200]

print(my_list)  # Output: [1, 100, 200, 5]

```

---

You don't need to use a specific method (like `append()`, `insert()`, or `remove()`) to modify items in a list. You can simply use indexing or slicing to directly assign new values to elements in a list. This is one of the key advantages of lists being **mutable** in Python.

---

---

---

### **Key Features of a List**

1. **Ordered**:
    - Items in a list are stored in a specific order and can be accessed using an **index**.
    - Example:
        
        ```python
        my_list = [10, 20, 30]
        print(my_list[0])  # Output: 10
        
        ```
        
2. **Mutable**:
    - Lists can be modified after creation (items can be added, removed, or changed).
    - Example:
        
        ```python
        my_list = [10, 20, 30]
        my_list[1] = 25
        print(my_list)  # Output: [10, 25, 30]
        
        ```
        
3. **Heterogeneous**:
    - A single list can store items of **different data types**.
    - Example:
        
        ```python
        mixed_list = [1, "hello", 3.14, True]
        print(mixed_list)  # Output: [1, 'hello', 3.14, True]
        
        ```
        
4. **Dynamic**:
    - Lists can grow or shrink dynamically as items are added or removed.

---

### **How to Create a List**

### **1. Using Square Brackets `[]`**

```python
my_list = [1, 2, 3]

```

### **2. Using the `list()` Constructor**

```python
my_list = list((1, 2, 3))

```

### **3. Empty List**

```python
empty_list = []

```

### **4. Nested List**

```python
nested_list = [1, [2, 3], [4, [5, 6]]]

```

---

### **List Indexing and Slicing**

1. **Accessing Elements by Index**:
    - Indexing starts at `0`.
    - Negative indexing allows access from the end.
    
    ```python
    my_list = [10, 20, 30, 40]
    print(my_list[0])  # Output: 10
    print(my_list[-1])  # Output: 40
    
    ```
    
2. **Slicing**:
    - Extract sublists using `start:end:step`.
    
    ```python
    my_list = [10, 20, 30, 40, 50]
    print(my_list[1:4])  # Output: [20, 30, 40]
    print(my_list[::2])  # Output: [10, 30, 50]
    
    ```
    

---

### **Common List Operations**

### **1. Length of a List**

```python
my_list = [1, 2, 3]
print(len(my_list))  # Output: 3

```

### **2. Membership Test**

```python
my_list = [10, 20, 30]
print(20 in my_list)  # Output: True
print(50 not in my_list)  # Output: True

```

### **3. Concatenation**

```python
list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2)  # Output: [1, 2, 3, 4]

```

### **4. Repetition**

```python
my_list = [1, 2]
print(my_list * 3)  # Output: [1, 2, 1, 2, 1, 2]

```

---

### **List Methods (Detailed Explanation with Examples)**

Here’s a complete list of methods available for Python lists:

---

### **1. `append()`**

- Adds an element to the **end** of the list.

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

```

---

### **2. `extend()`**

- Adds all elements of another iterable (e.g., list, tuple) to the **end** of the list.

```python
my_list = [1, 2]
my_list.extend([3, 4])
print(my_list)  # Output: [1, 2, 3, 4]

```

---

### **3. `insert()`**

- Inserts an element at a **specific index**.

```python
my_list = [1, 3, 4]
my_list.insert(1, 2)  # Insert 2 at index 1
print(my_list)  # Output: [1, 2, 3, 4]

```

---

### **4. `remove()`**

- Removes the **first occurrence** of a specified element.

```python
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]

```

---

### **5. `pop()`**

- Removes and **returns** the element at the specified index (default is the last element).

```python
my_list = [1, 2, 3]
print(my_list.pop())  # Output: 3
print(my_list)  # Output: [1, 2]

```

---

### **6. `clear()`**

- Removes all elements from the list.

```python
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []

```

---

### **7. `index()`**

- Returns the **index** of the first occurrence of a specified value.

```python
my_list = [1, 2, 3, 2]
print(my_list.index(2))  # Output: 1

```

---

### **8. `count()`**

- Returns the **number of times** a value appears in the list.

```python
my_list = [1, 2, 3, 2]
print(my_list.count(2))  # Output: 2

```

---

### **9. `reverse()`**

- Reverses the elements of the list **in place**.

```python
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  

# Output: [3, 2, 1]
```

---

### **10. `sort()`**

- Sorts the list in **ascending order** by default.

```python
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3]

# Sort in descending order
my_list.sort(reverse=True)
print(my_list)  # Output: [3, 2, 1]

```

---

### **11. `copy()`**

- Returns a **shallow copy** of the list.

```python
my_list = [1, 2, 3]
new_list = my_list.copy()
print(new_list)  # Output: [1, 2, 3]

```

---

### **12. `del` (Not a Method, but Important)**

- Deletes an element or slice from the list.

```python
my_list = [1, 2, 3]
del my_list[1]  # Delete element at index 1
print(my_list)  # Output: [1, 3]

del my_list[:]  # Delete all elements
print(my_list)  # Output: []

```

---

### **Interesting Notes and Advanced Topics**

### **1. Lists vs Tuples**

- Lists are **mutable**, while tuples are **immutable**.
- Lists have more methods because they can be modified.

### **2. Nested Lists**

- Lists can store other lists, allowing for the creation of 2D or multi-dimensional arrays.

```python
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])  # Output: 3

```

### **3. List Comprehensions**

- A concise way to create lists.

```python
# Generate a list of squares
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

```

### **4. Slicing with Steps**

- You can use slicing to access elements with specific steps.

```python
my_list = [1, 2, 3, 4, 5]
print(my_list[::2])  # Output: [1, 3, 5]

```

---

### Summary of List Methods:

| **Method** | **Description** | **Syntax** |
| --- | --- | --- |
| **`append()`** | **Adds an element to the end of the list** | **`mylist.append(element)` ,`mylist.append([elements])`** |
| **`extend()`** | **Adds all elements from another iterable** | **`mylist.extend([elements])`** |
| **`insert()`** | **Inserts an element at a specified index** | **`mylist.insert(index, element)`** |
| **`remove()`** | **Removes the first occurrence of an element** | **`mylist.remove(element)`** |
| **`pop()`** | **Removes and returns the element at a specified index** | **`mylist.pop(index)`** |
| **`clear()`** | **Removes all elements from the list** | **`mylist.clear()`** |
| **`index()`** | **Returns the index of the first occurrence of an element** | **`mylist.index(element, start, end)`** |
| **`count()`** | **Returns the number of occurrences of an element** | **`mylist.count(element)`** |
| **`sort()`** | **Sorts the list in ascending or descending order** | **`mylist.sort(reverse=False)`** |
| **`reverse()`** | **Reverses the order of elements in the list** | **`mylist.reverse()`** |
| **`copy()`** | **Returns a shallow copy of the list** | **`mylist.copy()`** |

```python
fruits = ['apple', 'banana', 'apple', 'orange', 'apple', 'banana']

# 1. Using len() to find the number of elements
print("Length of the list:", len(fruits)) 
 # Output: 6

# 2. Using count() to find how many times 'apple' appears
print("Count of 'apple':", fruits.count('apple'))  
# Output: 3

# 3. Using append() to add a new element
fruits.append('grape')
print("List after append:", fruits)  
# Output: ['apple', 'banana', 'apple', 'orange', 'apple', 'banana', 'grape']

# 4. Using remove() to remove the first occurrence of 'banana'
fruits.remove('banana')
print("List after remove:", fruits)  
# Output: ['apple', 'apple', 'orange', 'apple', 'banana', 'grape']

# 5. Using index() to find the position of 'orange'
print("Index of 'orange':", fruits.index('orange'))  
# Output: 2

# 6. Using reverse() to reverse the order of elements
fruits.reverse()
print("List after reverse:", fruits)  
# Output: ['grape', 'banana', 'apple', 'orange', 'apple', 'apple']

```