# Integer

- This value is represented by int class. It contains positive or negative whole numbers (without fractions or decimals).
- In Python, there is no limit to how long an integer value can be.
- Default value of int is 0
- **Integer (int)** :
    - Represents whole numbers.
    - Example: x = 10

### **Key Characteristics of `int` in Python**:

1. **Whole Numbers**:
    - Integers are whole numbers, meaning they don't have decimal points.
2. **Unlimited Precision**:
    - Python integers can grow as large as the available memory allows. There's no fixed range (like 32-bit or 64-bit in other languages).
3. **Automatic Type Conversion**:
    - Python seamlessly converts integers to larger representations when needed.
    - Python integers automatically grow to accommodate larger values, as long as memory is available.
4. **Base Support**:
    - Integers can be represented in different bases, such as binary, octal, decimal, or hexadecimal.

```python
# Float to int
print(int(4.8))  # Output: 4

# String to int
print(int("42"))  # Output: 42

# Binary string to int
print(int("101010", 2))  # Output: 42

# Hexadecimal string to int
print(int("2A", 16))  # Output: 42

```

### **Interesting Properties of Python Integers**

### **1. Arbitrary Precision**

Python integers automatically grow to accommodate larger values, as long as memory is available.

```python
x = 10**100  # 10 raised to the power of 100
print(x)

```

**Output**:

```
10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

```

In most programming languages, integers have a fixed range (e.g., 32-bit or 64-bit), and exceeding that range causes overflow. Python avoids this limitation.

---

### **2. Type Flexibility**

Python automatically converts between integers and other numeric types when needed.

```python
x = 42
y = 42.0

print(type(x))  # Output: <class 'int'>
print(type(x + y))  # Output: <class 'float'> (int + float = float)

```

---

### **3. Negative Numbers**

Integers in Python can also be negative.

```python
x = -42
print(x)  # Output: -42

```

### **Operations with Integers**

Python provides several operations for integers, including arithmetic, relational, and bitwise operations.

### **Arithmetic Operations**

```python
x = 10
y = 3

print(x + y)  # Addition: 13
print(x - y)  # Subtraction: 7
print(x * y)  # Multiplication: 30
print(x // y)  # Integer Division: 3
print(x % y)  # Modulus: 1
print(x ** y)  # Exponentiation: 1000

```

### **Bitwise Operations**

Integers support bitwise operations, which work at the binary level:

- **AND (`&`)**
- **OR (`|`)**
- **XOR (`^`)**
- **Left Shift (`<<`)**
- **Right Shift (`>>`)**

```python
python
CopyEdit
a = 5  # Binary: 101
b = 3  # Binary: 011

print(a & b)  # AND: 1 (Binary: 001)
print(a | b)  # OR: 7 (Binary: 111)
print(a ^ b)  # XOR: 6 (Binary: 110)
print(a << 1)  # Left shift: 10 (Binary: 1010)
print(a >> 1)  # Right shift: 2 (Binary: 10)

```

### **Interesting Applications of Integers**

1. **Checking Palindromic Numbers**:
Check if an integer reads the same backward and forward.
    
    ```python
    num = 121
    is_palindrome = str(num) == str(num)[::-1]
    print(is_palindrome)  # Output: True
    
    ```
    
2. **Factorial Calculation**:
Python integers make it easy to compute large factorials.
    
    ```python
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    print(factorial(100))
    
    ```
    
3. **Efficient Number Theory**:
Use modular arithmetic or bitwise operations for fast algorithms in cryptography or competitive programming.

### **Summary Table**

| **Feature** | **Description** |
| --- | --- |
| **Immutability** | Integers are immutable in Python. |
| **Arbitrary Precision** | Can represent integers as large as memory allows. |
| **Base Support** | Supports decimal, binary, octal, and hexadecimal bases. |
| **Arithmetic** | Supports standard operations like addition, subtraction, multiplication, etc. |
| **Bitwise Operations** | Supports bit-level operations like AND, OR, XOR, shifts. |
| **Conversion** | Convert other types to integers using `int()`. |