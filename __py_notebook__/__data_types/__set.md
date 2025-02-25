# Set

- A **set** is a built-in data type in Python that represents an **unordered collection of unique items**.
- Sets are similar to mathematical sets and are primarily used for operations like **union, intersection, difference, and membership testing**.
- Default value of set is set()

---

### **Key Features of Sets**

1. **Unordered**:
    - Sets do not maintain the order of elements.
    - The items in a set are stored in a **hashed** structure for quick access.
2. **Unique Elements**:
    - Sets do not allow duplicate elements.
    - If duplicates are added, they are automatically removed.
    
    Example:
    
    ```python
    my_set = {1, 2, 2, 3}
    print(my_set)  # Output: {1, 2, 3}
    
    ```
    
3. **Mutable**:
    - Sets are mutable, meaning you can add or remove items after creation. However, the individual elements in a set must be immutable (e.g., integers, strings, tuples).
4. **No Indexing or Slicing**:
    - Sets do not support indexing or slicing because they are unordered.
5. **Supports Set Operations**:
    - Sets support mathematical operations like **union**, **intersection**, **difference**, and **symmetric difference**.
6. **Heterogeneous**: Elements in a set can be of different data types.

---

### **How to Create a Set**

1. **Using Curly Braces `{}`**:
    
    ```python
    my_set = {1, 2, 3}
    print(my_set)  # Output: {1, 2, 3}
    
    ```
    
2. **Using the `set()` Constructor**:
    
    ```python
    my_set = set([1, 2, 3])
    print(my_set)  # Output: {1, 2, 3}
    
    ```
    
3. **Empty Set**:
    - You cannot create an empty set using `{}` because it creates an empty dictionary.
    - Use `set()` instead:
    
    ```python
    empty_set = set()
    print(type(empty_set))  # Output: <class 'set'>
    
    ```
    
4. **Frozen Set**:
    - A **frozen set** is an immutable version of a set, created using the `frozenset()` function.
    
    ```python
    frozen = frozenset([1, 2, 3])
    print(frozen)  # Output: frozenset({1, 2, 3})
    
    ```
    

---

### **Accessing Elements in a Set**

Since sets are unordered, you cannot access elements by index. Instead, you can:

1. **Use a Loop**:
    
    ```python
    my_set = {1, 2, 3}
    for item in my_set:
        print(item)
    
    ```
    
2. **Check Membership**:
    - Use the `in` keyword to test if an element is in the set.
    
    ```python
    print(2 in {1, 2, 3})  
    
    # Output: True
    
    ```
    

---

### **Set Methods (Detailed Explanation with Examples)**

Below are all the important methods available for Python sets, categorized for better understanding:

---

### **1. Adding and Removing Elements**

1. **`add()`**:
    - Adds a single element to the set.
    
    ```python
    my_set = {1, 2}
    my_set.add(3)
    print(my_set)  # Output: {1, 2, 3}
    
    ```
    
2. **`update()`**:
    - Adds multiple elements to the set from an iterable (e.g., list, tuple).
    
    ```python
    my_set = {1, 2}
    my_set.update([3, 4])
    print(my_set)  # Output: {1, 2, 3, 4}
    
    ```
    
3. **`remove()`**:
    - Removes a specific element from the set. Raises a `KeyError` if the element does not exist.
    
    ```python
    my_set = {1, 2, 3}
    my_set.remove(2)
    print(my_set)  # Output: {1, 3}
    
    ```
    
4. **`discard()`**:
    - Removes a specific element from the set but does not raise an error if the element is not found.
    
    ```python
    my_set = {1, 2, 3}
    my_set.discard(4)  # No error
    print(my_set)  # Output: {1, 2, 3}
    
    ```
    
5. **`pop()`**:
    - Removes and returns a random element from the set. Raises a `KeyError` if the set is empty.
    
    ```python
    my_set = {1, 2, 3}
    print(my_set.pop())  # Random element (e.g., 1)
    print(my_set)  # Output: Remaining elements
    
    ```
    
6. **`clear()`**:
    - Removes all elements from the set.
    
    ```python
    my_set = {1, 2, 3}
    my_set.clear()
    print(my_set)  # Output: set()
    
    ```
    

---

### **2. Mathematical Set Operations**

1. **`union()` / `|`**:
    - Returns a set that contains all elements from both sets.
    
    ```python
    set1 = {1, 2}
    set2 = {2, 3}
    print(set1.union(set2))  # Output: {1, 2, 3}
    print(set1 | set2)  # Output: {1, 2, 3}
    
    ```
    
2. **`intersection()` / `&`**:
    - Returns a set with elements common to both sets.
    
    ```python
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    print(set1.intersection(set2))  # Output: {2, 3}
    print(set1 & set2)  # Output: {2, 3}
    
    ```
    
3. **`difference()` / ``**:
    - Returns a set with elements in the first set but not in the second.
    
    ```python
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    print(set1.difference(set2))  # Output: {1}
    print(set1 - set2)  # Output: {1}
    
    ```
    
4. **`symmetric_difference()` / `^`**:
    - Returns a set with elements in either set, but not both.
    
    ```python
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    print(set1.symmetric_difference(set2))  # Output: {1, 4}
    print(set1 ^ set2)  # Output: {1, 4}
    
    ```
    

---

### **3. Subset and Superset Operations**

1. **`issubset()`**:
    - Checks if all elements of one set are in another set.
    
    ```python
    set1 = {1, 2}
    set2 = {1, 2, 3}
    print(set1.issubset(set2))  # Output: True
    
    ```
    
2. **`issuperset()`**:
    - Checks if one set contains all elements of another set.
    
    ```python
    print(set2.issuperset(set1))  # Output: True
    
    ```
    
3. **`isdisjoint()`**:
    - Checks if two sets have no elements in common.
    
    ```python
    set1 = {1, 2}
    set2 = {3, 4}
    print(set1.isdisjoint(set2))  # Output: True
    
    ```
    

---

### **4. Copying Sets**

1. **`copy()`**:
    - Returns a shallow copy of the set.
    
    ```python
    my_set = {1, 2, 3}
    new_set = my_set.copy()
    print(new_set)  # Output: {1, 2, 3}
    
    ```
    

---

### **Real-Life Use Cases of Sets**

1. **Removing Duplicates**:
    - Quickly remove duplicates from a list using sets.
    
    ```python
    items = [1, 2, 2, 3, 3]
    unique_items = set(items)
    print(unique_items)  # Output: {1, 2, 3}
    
    ```
    
2. **Membership Testing**:
    - Sets are optimized for fast membership testing, useful for searching.
    
    ```python
    large_set = {i for i in range(100000)}
    print(99999 in large_set)  # Output: True
    
    ```
    
3. **Recommendation Systems**:
    - Use sets to find common or unique items between user preferences.
    
    ```python
    user1_movies = {"Inception", "Matrix", "Titanic"}
    user2_movies = {"Matrix", "Avatar"}
    common_movies = user1_movies & user2_movies
    print(common_movies)  # Output: {'Matrix'}
    
    ```
    
4. **Tagging Systems**:
    - Sets can represent tags where uniqueness is required.
    
    ```python
    tags = {"python", "coding", "python", "tutorial"}
    print(tags)  # Output: {'python', 'coding', 'tutorial'}
    
    ```
    
5. **Network Analysis**:
    - Sets are used to analyze common friends or connections in social networks.

---

### **Comparison: Sets vs Lists**

| **Feature** | **Set** | **List** |
| --- | --- | --- |
| **Order** | Unordered | Ordered |
| **Duplicates** | Not allowed | Allowed |
| **Mutability** | Mutable | Mutable |
| **Indexing** | Not supported | Supported |
| **Performance** | Faster for membership tests | Slower for membership tests |

---

### **Built-in Functions with Sets**

### **1. `len()`**

Returns the number of elements in the set.

### Example:

```python
my_set = {1, 2, 3, 4}
print(len(my_set))  # Output: 4

```

---

### **2. `min()` and `max()`**

Return the smallest and largest elements in the set, respectively.

### Example:

```python
my_set = {1, 2, 3, 4}

print(min(my_set))  # Output: 1
print(max(my_set))  # Output: 4

```

---

### **3. `sum()`**

Returns the sum of all elements in the set.

### Example:

```python
my_set = {1, 2, 3, 4}
print(sum(my_set))  # Output: 10

```

---

### **4. `sorted()`**

Returns a sorted list from the elements of the set.

### Example:

```python
my_set = {3, 1, 4, 2}
print(sorted(my_set))  # Output: [1, 2, 3, 4]

```

---

### **Use Cases for Sets**:

- **Removing Duplicates**: Since sets automatically discard duplicates, they are a great way to remove duplicates from a list or other collections.
- **Mathematical Set Operations**: Sets support operations like union, intersection, and difference, making them ideal for tasks involving groups of items.
- **Membership Testing**: Sets allow for fast membership testing (`in` operator) because they are implemented using hash tables, which makes checking if an element exists efficient.

---

### **Example: Removing Duplicates from a List**

```python
my_list = [1, 2, 2, 3, 4, 4, 5]

# Convert list to set to remove duplicates
unique_items = set(my_list)
print(unique_items)  # Output: {1, 2, 3, 4, 5}

# Convert back to list if needed
my_list = list(unique_items)
print(my_list)  # Output: [1, 2, 3, 4, 5]

```

---

### **Summary of Set Methods and Functions**

| **Method/Function** | **Description** |
| --- | --- |
| **`add()`** | **Adds an element to the set** |
| **`remove()`** | **Removes an element from the set (raises error if not found)** |
| **`discard()`** | **Removes an element from the set (no error if not found)** |
| **`pop()`** | **Removes and returns an arbitrary element from the set** |
| **`clear()`** | **Removes all elements from the set** |
| **`copy()`** | **Returns a shallow copy of the set** |
| **`union()`** | **Returns a new set containing all elements from both sets** |
| **`intersection()`** | **Returns a new set with elements common to both sets** |
| **`difference()`** | **Returns a new set with elements in the first set but not in the second** |
| **`symmetric_difference()`** | **Returns a new set with elements in either set but not in both** |
| **`update()`** | **Updates the set with elements from another set or iterable** |
| **`intersection_update()`** | **Updates the set to contain only the common elements** |
| **`difference_update()`** | **Updates the set to remove elements found in another set** |
| **`symmetric_difference_update()`** | **Updates the set to contain elements in either set but not in both** |
| **`issubset()`** | **Checks if the set is a subset of another set** |
| **`issuperset()`** | **Checks if the set is a superset of another set** |
| **`isdisjoint()`** | **Checks if the sets have no elements in common** |
| **`len()`** | **Returns the number of elements in the set** |
| **`min()`** | **Returns the smallest element in the set** |
| **`max()`** | **Returns the largest element in the set** |
| **`sum()`** | **Returns the sum of all elements in the set** |
| **`sorted()`** | **Returns a sorted list from the elements of the set** |