> # What is python?

- Python is a general-purpose, high-level, interpreted, object-oriented programming language used for various applications.
- Python was developed by **Guido Van Rossum** in 1989 while working at National Research Institute in the Netherlands. But officially, Python was made available to the public in **1991**.
- Python code syntax uses English keywords, making it easy to understand.
- In addition, it includes high-level data structures, dynamic typing, dynamic binding, and many more features that make it very attractive for rapid application development.
- It supports modules and packages, which encourages program modularity and code reuse.
- The Python interpreter and the extensive standard library are available in source or binary form for all major platforms. In addition, it has a wide range of standard and third-party libraries that helps in rapid application development.

> ## Features of python -

- **1. Free and Open Source**
    
    Python is freely available for everyone. It is freely available on its official website www.python.org. It has a large community across the world that is dedicatedly working towards make new python modules and functions. Anyone can contribute to the Python community.
    
    The open-source means, "Anyone can download its source code without paying any penny."
    
- **2. Easy to code**
    
    Python is a **high-level programming language**. Python is very easy to learn the language as compared to other languages like C, C#, Javascript, Java, etc. It is very easy to code in the Python language and anybody can learn Python basics in a few hours or days. It is also a developer-friendly language.
    
- **3. Easy to Read**
    
    As you will see, learning Python is quite simple. As was already established, Python’s syntax is really straightforward. The code block is defined by the indentations rather than by semicolons or brackets.
    
- **4. Object-Oriented Language**
    
    Python supports object-oriented language and concepts of classes and objects come into existence. It supports inheritance, polymorphism, and encapsulation, etc. The object-oriented procedure helps to programmer to write reusable code and develop applications in less code.
    
- **5. GUI Programming Support**
    
    Graphical User Interface is used for the developing Desktop application. PyQT5, Tkinter, Kivy are the libraries which are used for developing the web application.
    
- **6. High-Level Language**
    
    Python is a high-level language. When we write programs in Python, we do not need to remember the system architecture, nor do we need to manage the memory.
    
- **7. Large Community Support**
    
    Python has gained popularity over the years. Our questions are constantly answered by the enormous StackOverflow community. These websites have already provided answers to many questions about Python, so Python users can consult them as needed.
    
- **8. Easy to Debug**
    
    Excellent information for mistake tracing. You will be able to quickly identify and correct the majority of your program’s issues once you understand how to interpret Python’s error traces. Simply by glancing at the code, you can determine what it is designed to perform.
    
- **9.  Cross-platform Language**
    
    Python can run equally on different platforms such as Windows, Linux, UNIX, and Macintosh, etc. So, we can say that Python is a portable language. It enables programmers to develop the software for several competing platforms by writing a program only once.
    
- **10. Python is an Integrated language**
    
    Python is also an Integrated language because we can easily integrate Python with other languages like C, **C++**, etc.
    
- **11. Interpreted Language:**
    
    Python is an Interpreted Language because Python code is executed line by line at a time. like other languages C, C++, Java, etc. 
    
    There is no need to compile Python code this makes it easier to debug our code. The source code of Python is converted into an immediate form called **bytecode**.
    
- **12. Large Standard Library**
    
    It provides a vast range of libraries for the various fields such as machine learning, web developer, and also for the scripting. There are various machine learning libraries, such as Tensor flow, Pandas, Numpy, Keras, and Pytorch, etc. Django, flask, pyramids are the popular framework for Python web development.
    
- **13. Frontend and backend development**
    
    With a new project py script, you can run and write Python codes in HTML with the help of some simple tags <py-script>, <py-env>, etc. This will help you do frontend development work in Python like javascript. Backend is the strong forte of Python it’s extensively used for this work cause of its frameworks like Django and Flask
    
- **14. Dynamic Memory Allocation**
    
    In Python, we don't need to specify the data-type of the variable. When we assign some value to the variable, it automatically allocates the memory to the variable at run time. Suppose we are assigned integer value 15 to **x,** then we don't need to write **int x = 15.** Just write x = 15.
    

> ## Advantages of Python

- **Easy to learn and use:** Python’s simple syntax makes it beginner-friendly
- **Extensive libraries and frameworks**: Offers rich libraries for web development, data science, AI, etc.
- **Versatile:** Supports multiple programming paradigms and applications
- **Cross-platform:** Works seamlessly across Windows, macOS, and Linux
- **Great for rapid prototyping**: Quick syntax allows for fast idea implementation

> ## Applications of Python

We can use Python everywhere because Python is known for its general-purpose nature, which makes it applicable in almost every domain of software development. 

The most common application areas are:

- Desktop Applications
- Web Applications
- Database Applications
- Network Programming
- Games
- Data Analysis Applications
- Machine Learning
- Artificial Intelligence Applications
- IoT

> ## Using Blank Lines in code

A line containing only white space, possibly with a comment or within a code, is known as a blank line, and Python ignores it.

> ## End-of-Line to Terminate a Statement

In Python end of the line terminate the statement. So you don’t need to write any symbol to mark the end of the line to indicate the statement termination. 

For example, in other programming languages like Java and C, the statement must end with a semicolon (`;`).

Python statement ends with the token NEWLINE character (`\n`). But we can extend the statement over multiple lines using line continuation character (`\`). This is known as an **explicit continuation**.

```python
# addition = 10 + 20 + 30 + 40 + 50 + 60 + 70

addition = 10 + 20 + \
           30 + 40 + \
           50 + 60 + 70
print(addition)

# Output: 280
```

> ## Semi-column to Separate Multiple Statements

In Python, we can add **multiple statements on a single line** separated by semicolons, as follows:

```python
a = 2; b = 6
print('Area of rectangle:', l * b)

# Output Area of rectangle: 12
```

```python
a = 2; b = 6; print('Area of rectangle:', l * b)
```

Most Python style guides don’t recommend adding multiple statements on a single line, though occasionally, it improves readability.

> ## Indentation

Python indentation tells a Python interpreter that the group of statements belongs to a particular block of code. The indentation makes the code look neat, clean, and more readable.

A block is a combination of all multiple statements. Inside a code block, we group multiple statements for a specific purpose.

**Whitespace is used for indentation** in Python to define the indentation level. We should use **4 spaces** per indentation level. 

Indented code blocks are always preceded by a colon (`:`) on the previous line.

Take the example of the **if-else statement** in Python.

```python
num1 = 50
num2 = 100
if num1 > num2:
    print(num1, 'is greater than', num2)
elif num2 > num1:
    print(num2, 'is greater than', num1)
else:
    print('Both numbers are equal')
```

If one code block is nested in another, the child code block should separate by 4 spaces from the parent code block.

If a block has to be more deeply nested, it is simply indented further to the right. You can understand it better by looking at the following lines of code.

```python
num1 = 500
if num1 > 100:
    if num1 % 2 == 0:
        print('Even number is greater than 100')
```