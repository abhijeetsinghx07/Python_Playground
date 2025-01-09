# 41. Write a program to check whether a file exists.

file_name = input("Enter the file name: ")
files=["hey.py","elif.py","loop.py","conditional.py","comprehension.py"]

if file_name in files:
    print(f"Yes, your file '{file_name}' exist in that directory.")

else:
    print(f"No, with that name: '{file_name}' don't exist in that directory. ")
    print("Try with another name.")
