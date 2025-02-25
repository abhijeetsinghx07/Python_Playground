- In Python, a **string** is a sequence of characters enclosed in single (`'`) or double quotes (`"`).
- Strings are immutable, meaning once they are created, their content cannot be changed.
- Default Value is : ‘’ or  “”

### Example of String Creation:

```python
# Using single quotes
string1 = 'Hello, World!'

# Using double quotes
string2 = "Python is fun."

# Using triple single quotes for multi-line strings
string3 = '''This is a
multi-line string.'''

# Using triple double quotes for multi-line strings
string3 = '''This is a
multi-line string.'''

```

### String Methods

Python strings come with a variety of methods that allow you to manipulate and interact with the string data.

### 1. **`len()`** – Get the Length of the String

- This function returns the number of characters in a string.
- It will return length of string as output.

```python
my_string = "Python"
print(len(my_string))  

# Output: 6
```

### 2. **`upper()`** – Convert to Uppercase

- Converts all characters to uppercase in the string.
- It will return string in upper case as a output.
- It will not change anything in original string.

```python
my_string = "hello"
print(my_string.upper())  

# Output: HELLO
```

### 3. **`lower()`** – Convert to Lowercase

- Converts all characters in the string to lowercase.
- It will return string in lower case as a output.
- It will not change anything in original string.

```python
my_string = "HELLO"
print(my_string.lower()

# Output: hello
```

### 4. **`strip()`** – Remove Leading and Trailing Spaces

- Removes any whitespace at the beginning or the end of the string.
- It will return string after removing whitespace as a output.
- It will not change anything in original string.

```python
my_string = "   hello world   "
print(my_string.strip())  

# Output: 'hello world'

```

### 5. **`replace(old, new)`** – Replace Substring

- Replaces occurrences of a substring with a new substring.
- It will return string after replace substring as a output.
- It will not change anything in original string.

```python
my_string = "I like Python"
print(my_string.replace("like", "love"))  

# Output: I love Python

```

### 6. **`split(separator)`** – Split the String into a List

- Splits the string into a list of substrings based on the specified separator.
- If no separator is provided, it splits based on whitespace.
- It will return list as a output.
- It will not change anything in original string.

```python
*string*.split(*separator, maxsplit*)
```

- separator: Specifies the separator to use when splitting the string. By default any whitespace is a separator.
- maxsplit:  Specifies how many splits to do. Default value is -1, which is "all occurrences"
- Both are optional.

```python
>>> txt = "hello, my name is Peter, I am 26 years old"
>>> x = txt.split(", ")
>>> print(x)

['hello', 'my name is Peter', 'I am 26 years old']
```

```python
>>> txt = "apple#banana#cherry#orange"
>>> x = txt.split("#")
>>> print(x)

['apple', 'banana', 'cherry', 'orange']
```

```python
# setting the maxsplit parameter to 1, will return a list with 2 elements!
>>> txt = "apple#banana#cherry#orange"
>>> x = txt.split("#", 1)
>>> print(x)

['apple', 'banana#cherry#orange']
```

```python
>>> my_string = "apple,banana,cherry"
>>> print(my_string.split(","))

['apple', 'banana', 'cherry']

```

### 7. **`join(iterable)`** – Join List Elements into a String

- The `join()` method concatenates the elements of an iterable (e.g., list) into a single string, with a separator.

```python
string.join(iterable)
```

*iterable:*  Required. Any iterable object where all the returned values are strings

```python
>>> words
['Python', 'is', 'awesome']

>>> ' '.join(words)
'Python is awesome'

>>> ''.join(words)
'Pythonisawesome'

>>> '*'.join(words)
'Python*is*awesome'
```

```python
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)

# Output: nameTESTcountry
```

```python
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

# Output: John#Peter#Vicky
```

```python
words = ["Python", "is", "awesome"]

sentence = " ".join(words)

print(sentence)  

# Output: Python is awesome
```

### 8. **`find(substring)`** – Find the Index of a Substring

Returns the index of the first occurrence of the substring. If not found, it returns `-1`.

```python
my_string = "Hello, World!"

index = my_string.find("World")

print(index)  

# Output: 7
```

### 9. **`count(substring)`** – Count Occurrences of a Substring

Returns the number of times a substring appears in the string.

```python
my_string = "banana"
count = my_string.count("a")
print(count)  

# Output: 3

```

### 10. **`startswith(prefix)` and `endswith(suffix)`** – Check if String Starts or Ends with a Specific Substring

- `startswith()` checks if the string begins with the specified prefix.
- `endswith()` checks if the string ends with the specified suffix.

```python
my_string = "Python programming"
print(my_string.startswith("Python"))  # Output: True
print(my_string.endswith("ing"))       # Output: True

```

### Real-World Application Example

Suppose you're processing a user form where you collect and clean up email addresses:

```python
email = "   User123@Example.com   "

# Strip any leading/trailing spaces
cleaned_email = email.strip()

# Convert email to lowercase
cleaned_email = cleaned_email.lower()

# Check if it starts with "user"
if cleaned_email.startswith("user"):
    print("This email starts with 'user'")
else:
    print("This email does not start with 'user'")

print(cleaned_email)  # Output: user123@example.com

```

### Alternative Approach: List of Characters

If you want to manipulate individual characters of a string, you can treat a string as a sequence of characters:

```python
my_string = "hello"
char_list = list(my_string)  # Converts the string into a list of characters
print(char_list)  # Output: ['h', 'e', 'l', 'l', 'o']

```

### Summary

- Strings in Python are immutable and can be manipulated using a variety of built-in methods.
- Common string methods include `upper()`, `lower()`, `replace()`, `split()`, `join()`, and `find()`, among others.
- String manipulation is widely used in applications such as form processing, data cleaning, file handling, etc.


## Raw Strings in Python

A **raw string** in Python is a string where **backslashes (`\\`) are treated as literal characters** and not as escape characters. This is useful when dealing with strings that contain backslashes, such as file paths or regular expressions, where you don’t want Python to interpret backslashes as escape sequences (e.g., `\\n` for a newline, `\\t` for a tab).

You define a raw string by prefixing it with an **`r`** or **`R`** before the opening quote.

### Regular String vs. Raw String

### Example of Regular String:

```python
regular_string = "Hello\\nWorld"
print(regular_string)  # Output with newline

```

Output:

```
Hello
World

```

Here, `\\n` is interpreted as a newline character.

### Example of Raw String:

```python
raw_string = r"Hello\\nWorld"
print(raw_string)  # Output with literal "\\n"

```

Output:

```
Hello\\nWorld

```

In this case, the backslash `\\` is treated as a literal character, and `\\n` is printed as `\\n`, not as a newline.

### Why Use Raw Strings?

1. **File Paths**: When working with file paths on Windows, backslashes are used to separate directories, which would normally be treated as escape characters in a regular string. Using a raw string avoids that problem.

### Example: File Path with Regular String

```python
file_path = "C:\\\\Users\\\\Samantha\\\\Documents"
print(file_path)

```

Output:

```
C:\\Users\\Samantha\\Documents

```

### Example: File Path with Raw String

```python
file_path = r"C:\\Users\\Samantha\\Documents"
print(file_path)

```

Output:

```
C:\\Users\\Samantha\\Documents

```

Here, you don’t need to escape each backslash (`\\\\`), which makes it cleaner and easier to read.

1. **Regular Expressions**: Raw strings are commonly used with regular expressions because many special characters (like `\\d`, `\\w`, etc.) are prefixed with backslashes, and raw strings make it easier to write them without having to escape the backslashes.

### Example: Regular Expression with Raw String

```python
import re

pattern = r"\\d+"  # Matches one or more digits
text = "There are 123 apples"

match = re.findall(pattern, text)
print(match)  # Output: ['123']

```

### Without Raw Strings:

If you don't use raw strings in regular expressions, you'd have to escape the backslashes manually:

```python
pattern = "\\\\d+"

```

### When **Not** to Use Raw Strings

While raw strings are useful for avoiding escape sequences, **you cannot end a raw string with a single backslash** because the backslash would escape the closing quote. For example:

```python
raw_string = r"Some text with a backslash at the end\\"
# This will raise a SyntaxError

```

### Summary of Raw Strings:

- A raw string treats backslashes (`\\`) as literal characters.
- It’s defined by prefixing a string with an `r` or `R`.
- Useful for:
    - File paths with backslashes (e.g., on Windows).
    - Writing regular expressions without needing to escape backslashes.

## Real-World Use Cases

The **string** data type is one of the most fundamental and widely used types in Python. Strings are sequences of characters that can represent text-based data, making them essential in various real-world applications. Below are some common real-world use cases for strings and examples of how they are utilized in Python.

---

### **1. Handling User Input**

In most applications, user input is captured as a string. Usernames, passwords, search queries, and form inputs are all typically strings. String methods like `strip()`, `lower()`, and `replace()` can be used to clean and process the input before using it.

### **Example**: Capturing and Processing User Input

```python
# Getting user input
username = input("Enter your username: ")

# Processing the input
cleaned_username = username.strip().lower()

# Displaying the cleaned username
print(f"Cleaned Username: {cleaned_username}")

```

### **Use Case**:

- **Web Forms**: Collecting data such as names, addresses, and email inputs.
- **Command-line Tools**: Capturing inputs for command-based applications.

---

### **2. File and Data Handling (Reading and Writing Files)**

Strings are used extensively when working with files, whether you're reading from or writing to a file. You read the contents of a file as a string and often process or transform it before saving the modified data back to a file.

### **Example**: Reading and Writing a File

```python
# Reading from a file
with open('sample.txt', 'r') as file:
    content = file.read()

# Processing the content
word_count = len(content.split())

# Writing processed data back to the file
with open('output.txt', 'w') as file:
    file.write(f"Word Count: {word_count}")

```

### **Use Case**:

- **Log Management**: Reading logs, processing them, and saving analysis results.
- **Text Files**: Storing and retrieving user documents or application settings.

---

### **3. Generating and Parsing URLs**

URLs are strings, and working with URLs often involves parsing, encoding, or generating strings. This is common in web scraping, REST API requests, and dynamic link generation.

### **Example**: URL Generation for API Requests

```python
# Base URL for API
base_url = "<https://api.example.com/data>"

# Query parameters
params = {
    'city': 'New York',
    'category': 'weather',
    'units': 'metric'
}

# Building the URL
query_string = "&".join([f"{key}={value}" for key, value in params.items()])
api_url = f"{base_url}?{query_string}"

# Resulting URL
print(api_url)
# Output: <https://api.example.com/data?city=New> York&category=weather&units=metric

```

### **Use Case**:

- **Web Scraping**: Building query parameters and sending requests to websites or APIs.
- **Dynamic Link Generation**: Generating URLs dynamically in web applications.

---

### **4. Data Serialization and Deserialization (JSON)**

When working with APIs or databases, JSON (JavaScript Object Notation) is a common format for exchanging data. JSON data is represented as strings in Python, and libraries like `json` allow us to convert between strings and Python objects.

### **Example**: JSON Parsing

```python
import json

# JSON string (received from an API)
json_data = '{"name": "Alice", "age": 25, "city": "New York"}'

# Converting JSON string to Python dictionary
data = json.loads(json_data)

# Accessing data from the dictionary
print(data['name'])  # Output: Alice

# Converting Python dictionary to JSON string
json_string = json.dumps(data)
print(json_string)  # Output: {"name": "Alice", "age": 25, "city": "New York"}

```

### **Use Case**:

- **API Communication**: Sending and receiving JSON-formatted data in web APIs.
- **Data Storage**: Storing structured data in JSON files.

---

### **5. Data Cleaning and Transformation**

In data science and machine learning, cleaning and transforming text data (e.g., user reviews, tweets, product descriptions) is essential. This often involves string operations like tokenization, lowercasing, and removing special characters.

### **Example**: Text Data Cleaning for Analysis

```python
text = "The movie was Great!!!  I really loved it. Great acting!!"

# Lowercase the text
clean_text = text.lower()

# Remove special characters
clean_text = clean_text.replace("!", "")

# Tokenizing the text
words = clean_text.split()

# Count occurrences of a word
great_count = words.count('great')

print(f"Cleaned Text: {clean_text}")
print(f"Occurrences of 'great': {great_count}")

```

### **Use Case**:

- **Natural Language Processing (NLP)**: Preprocessing text data for sentiment analysis, keyword extraction, or chatbot training.
- **Data Cleaning**: Preparing raw text data for analysis.

---

### **6. Formatted Output (User Reports and Logs)**

When generating reports, logs, or formatted output in applications, strings are used to create readable and structured text. Using **f-strings** or the **format()** method, you can dynamically insert values into strings.

### **Example**: Generating a Report with String Formatting

```python
# Sample data
name = "Alice"
sales = 1500.75
bonus = 200.50

# Generating the report using f-string
report = f"Employee: {name}\\nTotal Sales: ${sales:.2f}\\nBonus: ${bonus:.2f}"
print(report)

# Output:
# Employee: Alice
# Total Sales: $1500.75
# Bonus: $200.50

```

### **Use Case**:

- **Logging**: Writing structured logs with dynamic data.
- **Reports**: Generating human-readable reports with statistics, financial data, etc.

---

### **7. String Search and Pattern Matching (Regular Expressions)**

Strings are often used in conjunction with **regular expressions** (regex) to perform pattern matching, searching, and validating text data. This is commonly used for tasks like validating emails, extracting phone numbers, or searching for specific patterns in text.

### **Example**: Validating Email Addresses with Regular Expressions

```python
import re

# Sample email
email = "test.email@example.com"

# Regex pattern for validating email
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"

# Check if the email matches the pattern
if re.match(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")

```

### **Use Case**:

- **Data Validation**: Validating user input (emails, phone numbers, IDs).
- **Text Search**: Finding specific patterns in logs, documents, or web pages.

---

### **8. Internationalization and Localization (Unicode Strings)**

With Python's support for **Unicode** strings, you can work with characters and text in any language, making your application accessible to a global audience. This is particularly important for multilingual applications.

### **Example**: Working with Unicode Strings

```python
# Example with Unicode characters (Japanese)
greeting = "こんにちは"  # Hello in Japanese

# Checking if a string contains Unicode characters
print(f"Length of greeting: {len(greeting)}")

```

### **Use Case**:

- **Multilingual Applications**: Supporting multiple languages, including complex scripts.
- **Internationalization**: Handling user input and output in different character encodings.

---

### **9. Password Encryption and Masking**

In security-focused applications, strings are used to handle sensitive data such as passwords. You can hash and encrypt passwords or mask them when displaying in the user interface.

### **Example**: Masking a Password Input

```python
import getpass

# Masking user password input
password = getpass.getpass("Enter your password: ")

# Output masked password
print("Password entered (masked):", '*' * len(password))

```

### **Use Case**:

- **Login Systems**: Accepting, hashing, and verifying passwords.
- **Security**: Ensuring sensitive data is hidden or encrypted.

---

### **10. Tokenization and String Operations in Natural Language Processing**

String manipulation is crucial in Natural Language Processing (NLP) for tasks like tokenization, stop-word removal, stemming, and lemmatization. This is especially important for chatbots, language models, and search engines.

### **Example**: Tokenizing and Cleaning Text for NLP

```python
# Sample sentence
sentence = "Natural Language Processing with Python is powerful!"

# Tokenizing the sentence
tokens = sentence.lower().split()

# Removing stop words (e.g., 'is', 'with')
stop_words = ['is', 'with']
filtered_tokens = [word for word in tokens if word not in stop_words]

print(f"Filtered Tokens: {filtered_tokens}")
# Output: ['natural', 'language', 'processing', 'python', 'powerful']

```

### **Use Case**:

- **Chatbots**: Preprocessing user input for understanding.
- **Text Analysis**: Extracting useful information from raw text data.

---

### **Conclusion**

The **string** data type in Python is extremely versatile and serves many important purposes across different industries and applications. From user input and file handling to web scraping and NLP, strings are central to many programming tasks. Understanding how to manipulate and work with strings efficiently is essential for writing effective Python programs.
