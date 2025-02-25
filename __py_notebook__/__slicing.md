# Slicing

- Slicing in Python is a technique used to extract a **subset of elements** from **collection** like **strings, lists, tuples**.
- It allows you to access parts of a sequence without modifying the original data.

---

## **2. Syntax of Slicing**

```python
sequence[start index : stop index : step]
```

- **`start`** → The index where the slice begins (inclusive).
- **`stop`** → The index where the slice ends (exclusive).
- **`step`** → The interval between elements (defaults to **`1`**).

### **Example:**

```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[2:7])  

# Output: [2, 3, 4, 5, 6]
```

```python
>>> i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> i[0:8:2]
[0, 2, 4, 6]

>>> i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> i[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

>>> i[9::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

>>> i[9:0:-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1]

>>> i[2:8:-1]
[]
```

---

## **3. Positive and Negative Indexing in Slicing**

Python supports both **positive** and **negative** indexing.

### **A. Positive Indexing**

- Starts from `0` (first element) and increments by `1`.
- Example:

```python
my_string = "PYTHON"
print(my_string[1:4])  

# Output: 'YTH'
```

| P | Y | T | H | O | N |
| --- | --- | --- | --- | --- | --- |
| 0 | 1 | 2 | 3 | 4 | 5 |

### **B. Negative Indexing**

- Starts from `1` (last element) and decrements by `1`.
- Example:

```python
my_string = "PYTHON"
print(my_string[-5:-2])  

# Output: 'YTH'
```

| P | Y | T | H | O | N |
| --- | --- | --- | --- | --- | --- |
| -6 | -5 | -4 | -3 | -2 | -1 |

---

## **4. How `step` Works in Slicing**

The `step` value determines how many elements to **skip** between each selection.

### **A. Forward Slicing (Positive Step)**

- Extracts elements **left to right**.
- Default step value is `1`.
- Example:

```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[1:8:2])  

# Output: [1, 3, 5, 7]
```

**Explanation:**

- Start from index `1` (`1`).
- Take every `2nd` element (`3, 5, 7`).
- Stop before index `8`.

---

### **B. Reverse Slicing (Negative Step)**

- Extracts elements **right to left**.
- The `step` must be **negative**.
- Example:

```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[8:1:-2])  

# Output: [8, 6, 4, 2]
```

**Explanation:**

- Start from index `8` (`8`).
- Move **backward** by `2` steps (`6, 4, 2`).
- Stop **before** index `1`.

---

## **5. Omitting `start`, `stop`, and `step`**

You can omit parts of the slicing syntax to extract different portions of a sequence.

### **A. Omitting `start` (Defaults to 0)**

```python
my_string = "PYTHON"
print(my_string[:4])  # Output: 'PYTH' (from index `0` to `4`)

```

### **B. Omitting `stop` (Defaults to End)**

```python
my_string = "PYTHON"
print(my_string[2:])  # Output: 'THON' (from index `2` to end)

```

### **C. Omitting `step` (Defaults to 1)**

```python
my_string = "PYTHON"
print(my_string[::2])  # Output: 'PTO' (every 2nd element)

```

### **D. Omitting Everything (`[:]` - Copy Entire Sequence)**

```python
my_list = [1, 2, 3, 4, 5]
copy_list = my_list[:]
print(copy_list)  

# Output: [1, 2, 3, 4, 5]
```

> This is often used to create a **shallow copy** of a list.
> 

```python

```

---

## **6. Reversing a Sequence Using Slicing**

You can reverse any sequence by setting `step` to `-1`.

```python
my_string = "PYTHON"
print(my_string[::-1])  

# Output: 'NOHTYP'
```

| P | Y | T | H | O | N |
| --- | --- | --- | --- | --- | --- |
| -6 | -5 | -4 | -3 | -2 | -1 |

---

## **7. Interesting and Important Notes**

1. **Slicing Never Raises an Error**:
    - If `start` or `stop` exceed the valid index range, Python **does not raise an error**.
    
    ```python
    my_list = [1, 2, 3, 4]
    print(my_list[1:10])  # Output: [2, 3, 4]
    
    ```
    
2. **Using `None` Instead of Empty Indices**:
    - `None` can replace `start` and `stop`.
    
    ```python
    my_string = "PYTHON"
    print(my_string[slice(None, None, -1)])  
    
     # Output: 'NOHTYP'
    
    >>> print(my_string[None: None: -1])
    
    	# Output: NOHTYP
    ```
    
3. **Using `slice()` Instead of `[:]`**
    - **`slice(start, stop, step)`** can be used explicitly.
    
    ```python
    my_list = [1, 2, 3, 4, 5]
    s = slice(1, 4)
    print(my_list[s])  
    
     # Output: [2, 3, 4]
    ```
    

---

## **8. Real-Life Use Cases of Slicing**

### **1. Extracting User Data**

```python
email = "user123@gmail.com"
username = email[:email.index("@")]
print(username)  

 # Output: 'user123'
```

### **2. Pagination in Web Apps**

```python
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
page_size = 3
page1 = data[:page_size]  # First 3 items

page2 = data[page_size:page_size*2]  # Next 3 items

print(page1, page2)  

 # Output: [1, 2, 3] [4, 5, 6]
```

### **3. Data Analysis (Extracting Columns)**

```python
csv_row = ["John", "Doe", 30, "Engineer", "USA"]
name, surname, *rest = csv_row

print(name, surname)  

# Output: 'John Doe'
```

### **4. Image Processing (Extracting ROI)**

```python
import numpy as np

image = np.zeros((100, 100))   # 100x100 pixel image
roi = image[30:70, 30:70]   # Extract center 40x40 region

```

### **5. Reversing Strings for Palindrome Checking**

```python
def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("racecar"))  # Output: True

```

---

## **9. Summary Table**

| **Operation** | **Example** | **Explanation** |
| --- | --- | --- |
| **Extracting a range** | **`my_list[1:4]`** | **Get items from index `1` to `3`** |
| **Omitting `start`** | **`my_list[:4]`** | **Start from `0` and go up to index `3`** |
| **Omitting `stop`** | **`my_list[2:]`** | **Start from index `2` till the end** |
| **Omitting `step`** | **`my_list[::2]`** | **Take every 2nd element** |
| **Negative step** | **`my_list[::-1]`** | **Reverse the sequence** |
| **Using `slice()`** | **`slice(1, 4)`** | **Equivalent to `[1:4]`** |

---

## **10. Key Takeaways**

1. **Slicing works on all sequences** (`str`, `list`, `tuple`, etc.).
2. **Positive indices move forward; negative indices move backward**.
3. **Omitting `start`, `stop`, or `step` allows flexibility**.
4. **Slicing never raises an error**.
5. **Useful in text processing, data analysis, and computer vision**.

---