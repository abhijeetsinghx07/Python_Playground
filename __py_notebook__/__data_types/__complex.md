# Complex

- A complex number is represented by a complex class.
- It is specified as *(real part) + (imaginary part)j* . For example – 2+3j
- Default value is 0j
- The **complex data type** in Python is used to represent **complex numbers**. A complex number is a number that has two parts:
    - A **real part** (e.g., 2.0)
    - An **imaginary part** (e.g., 3.0)
- Complex numbers are commonly used in mathematical computations, engineering, and scientific applications.

---

### **Key Characteristics of Complex Numbers in Python**

1. **Syntax**:
    - A complex number is written as `a + bj`, where:
        - `a` is the **real part**.
        - `b` is the **imaginary part**.
    - The imaginary part must always have a `j` (or `J`) after it (e.g., `5j`).
2. **Type**:
    - The type of a complex number is `<class 'complex'>`.
3. **Immutable**:
    - Like all numbers in Python, complex numbers are immutable.

---

### **How to Create Complex Numbers**

### **1. Using Literal Notation**

You can create a complex number directly by using the `a + bj` syntax.

```python
z = 2 + 3j
print(z)  

# Output: (2+3j)
```

### **2. Using the `complex()` Constructor**

The `complex(real, imag)` function creates a complex number from two arguments:

- `real`: The real part (default is 0).
- `imag`: The imaginary part (default is 0).

```python
z = complex(2, 3)
print(z)  

# Output: (2+3j)
```

---

### **Accessing Real and Imaginary Parts**

Python provides two attributes for complex numbers:

1. `.real` → Returns the real part.
2. `.imag` → Returns the imaginary part.

```python
z = 4 + 5j
print("Real Part:", z.real)       

# Output: 4.0

print("Imaginary Part:", z.imag) 

# Output: 5.0
```

---

### **Mathematical Operations on Complex Numbers**

Complex numbers support standard arithmetic operations:

### **Addition and Subtraction**

```python
z1 = 2 + 3j
z2 = 1 - 4j

print(z1 + z2)  
# Output: (3-1j)

print(z1 - z2)  
# Output: (1+7j)

```

### **Multiplication and Division**

```python
z1 = 2 + 3j
z2 = 1 - 4j

print(z1 * z2)  
# Output: (14-5j)

print(z1 / z2)  
# Output: (-0.5882352941176471+0.6470588235294118j)

```

### **Conjugate of a Complex Number**

The conjugate of a complex number is obtained by negating its imaginary part. Use the `.conjugate()` method.

```python
z = 3 + 4j
print(z.conjugate())  

# Output: (3-4j)
```

---

### **Using the `cmath` Module**

Python's **`cmath`** module provides functions for complex number calculations.

### **1. Magnitude and Phase**

- **Magnitude (absolute value)**:
    - The magnitude of  is .
        
        z=a+bjz = a + bj
        
        ∣z∣=a2+b2|z| = \sqrt{a^2 + b^2}
        
    - Use `abs()` or `cmath.polar()`.
- **Phase**:
    - The phase (angle) of  is the angle in radians between the positive real axis and the line connecting  to the origin.
        
        zz
        
        zz
        
    - Use `cmath.phase()`.

```python
import cmath

z = 3 + 4j

# Magnitude
print(abs(z))  

# Output: 5.0

# Phase
print(cmath.phase(z))  

# Output: 0.9272952180016122

# Polar Coordinates
magnitude, angle = cmath.polar(z)
print("Polar:", magnitude, angle)  

# Output: Polar: 5.0 0.9272952180016122

```

---

### **2. Exponential and Logarithmic Functions**

```python
z = 1 + 1j

# Exponential
print(cmath.exp(z)) 

# Output: (1.4686939399158851+2.2873552871788423j)

# Natural Logarithm
print(cmath.log(z))  

# Output: (0.34657359027997264+0.7853981633974483j)

```

---

### **3. Trigonometric Functions**

The `cmath` module provides trigonometric functions like `sin`, `cos`, and `tan`.

```python
z = 1 + 1j

print(cmath.sin(z))  

# Output: (1.2984575814159773+0.6349639147847361j)

print(cmath.cos(z))  

# Output: (0.8337300251311491-0.9888977057628651j)

```

---

### **Interesting Facts About Complex Numbers**

### **1. Real and Imaginary Parts Are Floats**

Even if you create a complex number using integers, the real and imaginary parts are stored as floats.

```python
z = 2 + 3j
print(type(z.real))  
# Output: <class 'float'>

print(type(z.imag))  
# Output: <class 'float'>

```

### **2. Complex Numbers and Euler’s Formula**

Python can easily demonstrate **Euler’s formula**:
eiπ+1=0e^{i\pi} + 1 = 0

```python
import cmath

result = cmath.exp(cmath.pi * 1j) + 1
print(result)  

# Output: 0j (approximately 0)

```

### **3. Complex Numbers in Polar Form**

You can convert complex numbers between Cartesian (rectangular) and polar forms:

- **Cartesian to Polar**: Use `cmath.polar()`.
- **Polar to Cartesian**: Use `cmath.rect(magnitude, angle)`.

```python
import cmath

# Convert to polar form
z = 1 + 1j
polar = cmath.polar(z)
print("Polar Form:", polar)  

# Output: Polar Form: (1.4142135623730951, 0.7853981633974483)

# Convert back to Cartesian form
cartesian = cmath.rect(*polar)
print("Cartesian Form:", cartesian)  

l# Output: (1+1j)

```

---

### **Examples of Use Cases**

1. **Electrical Engineering**:
    - Complex numbers are used to represent impedances and waveforms.
2. **Signal Processing**:
    - Fourier Transforms and other signal analysis rely heavily on complex numbers.
3. **Quantum Mechanics**:
    - Wave functions are often represented as complex numbers.
4. **Fractals**:
    - Complex numbers are used in generating fractals like the Mandelbrot set.

---

### **Summary Table**

| **Feature** | **Description** |
| --- | --- |
| **Definition** | Numbers with a real part and an imaginary part (e.g., `a + bj`). |
| **Type** | `<class 'complex'>`. |
| **Immutability** | Complex numbers are immutable. |
| **Real and Imaginary Parts** | Access using `.real` and `.imag`. |
| **Arithmetic Operations** | Supports addition, subtraction, multiplication, division, etc. |
| **Special Methods** | `.conjugate()` for conjugates, `cmath` for advanced functions. |
| **Polar Coordinates** | Convert to/from polar using `cmath.polar()` and `cmath.rect()`. |

---