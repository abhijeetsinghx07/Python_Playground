# Float

- This value is represented by the float class. It is a real number with a floating-point representation. It is specified by a decimal point.
- Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation.
- It supports both positive and negative numbers, as well as very small and very large numbers due to its floating-point representation.
- If we perform any operation with float, output of that operation will be float only.
- Default Value of float is 0.0
- **Float (float)** :
    - Represents floating-point numbers (decimal values).
    - Example: y = 10.5

### **Key Characteristics of Floats**

1. **Decimal Numbers**:
    - Floats are numbers with a decimal point.
    - Example: `3.14`, `0.1`, `42.5`.
2. **Scientific Notation**:
    - Floats can be written using **scientific notation** to represent very large or very small numbers.
    - Example: `1.5e3` (which means 1.5×103=1500.0).
        
        1.5×103=1500.01.5 \times 10^3 = 1500.0
        
3. **Immutability**:
    - Like all numbers in Python, floats are **immutable**, meaning their value cannot be changed after creation.
4. **Precision**:
    - Floats are **approximations** of real numbers because they are stored in binary, which may lead to slight inaccuracies for some values (e.g., `0.1`).

```python
x = 3.14
y = -2.5
print(x, y)  # Output: 3.14 -2.5

```

```python
x = 1.5e3  # 1.5 × 10^3 = 1500.0
y = 2.5e-4  # 2.5 × 10^-4 = 0.00025
print(x, y)  # Output: 1500.0 0.00025

```

```python
x = 3.14
print(type(x))  # Output: <class 'float'>
```

```python
a = 5.0
b = 2.0

print(a + b)  # Addition: 7.0
print(a - b)  # Subtraction: 3.0
print(a * b)  # Multiplication: 10.0
print(a / b)  # Division: 2.5
print(a // b)  # Floor division: 2.0
print(a % b)  # Modulus: 1.0
```

```python
x = 3.14
y = 2.71

print(x > y)  # True
print(x < y)  # False
print(x == y)  # False

```

### **Conversion to Float**

Python provides the **`float()`** function to convert other data types into floats:

### **From Integers**:

```python
x = float(5)  # Convert integer 5 to float
print(x)  

# Output: 5.0
```

### **From Strings**:

```python
x = float("3.14")  # Convert string to float
print(x)  

# Output: 3.14
```

### **From Scientific Notation Strings**:

```python
x = float("1e3")  # Convert scientific notation string
print(x)  

# Output: 1000.0
```

### **Interesting Properties of Floats**

### **1. Precision Limitations**

Floats are stored in a binary format, which cannot represent all decimal fractions precisely. For example:

```python
x = 0.1 + 0.2
print(x)  

# Output: 0.30000000000000004
```

- This is due to how numbers are represented in binary.
- Python provides the **`decimal`** module for high-precision calculations (discussed later).

### **2. Special Float Values**

Python floats support **special values**:

- **`inf` (Infinity)**: Represents values larger than any finite number.
- **`inf` (Negative Infinity)**: Represents values smaller than any finite number.
- **`nan` (Not a Number)**: Represents undefined or un-representable values (e.g., 0/0).

```python
x = float('inf')  # Positive infinity
y = float('-inf')  # Negative infinity
z = float('nan')  # Not a number

print(x, y, z)  # Output: inf -inf nan

```

### **Interesting Applications of Floats**

### **1. Rounding Floats**:

Use the **`round()`** function to round floats to a specified number of decimal places.

```python
x = 3.14159
print(round(x, 2)) 

# Output: 3.14
```

---

### **2. High-Precision Calculations**:

Python’s **`decimal`** module provides more precise arithmetic for applications requiring high precision.

```python
from decimal import Decimal

x = Decimal("0.1") + Decimal("0.2")
print(x)  

# Output: 0.3 (exactly)
```

---

### **3. Truncating Floats**:

Use **`int()`** to truncate a float (remove its fractional part).

```python
x = 3.99
print(int(x))  

# Output: 3
```

---

### **4. Handling Infinity and NaN**:

Check for **`inf`** or **`nan`** using **`math.isinf()`** or **`math.isnan()`**.

```python
import math

x = float('inf')
y = float('nan')

print(math.isinf(x))  # True
print(math.isnan(y))  # True
```

---

### **Precision Limitations Example**

### Why does `0.1 + 0.2` not equal `0.3`?

Floats in Python use the **IEEE 754** standard, which stores numbers in binary. Some decimal numbers cannot be exactly represented in binary, leading to small errors.

```python
x = 0.1 + 0.2
print(x)  

# Output: 0.30000000000000004
```

---

### **Summary**

| **Feature** | **Description** |
| --- | --- |
| **Definition** | Represents real numbers with a fractional part using decimal points. |
| **Precision** | Limited due to binary representation. |
| **Special Values** | Supports `inf`, `-inf`, and `nan`. |
| **Scientific Notation** | Allows compact representation of very large or very small numbers (e.g., `1e-3`). |
| **Conversions** | Can be converted from integers, strings, or other formats using `float()`. |
| **High Precision** | Use `decimal` for applications requiring exact decimal precision. |

```python
# Demonstrating various float properties
x = 0.1 + 0.2
print("0.1 + 0.2 =", x)  # Approximation due to float precision

print("Scientific Notation: 1e3 =", 1e3)  # 1000.0

from decimal import Decimal
y = Decimal("0.1") + Decimal("0.2")
print("High Precision (Decimal):", y)  # Exact 0.3

print("Infinity:", float('inf'), float('-inf'))
print("NaN:", float('nan'))

```