#Write a program to find out what version of Python you are using.

import sys
import platform

# print(sys.version)
# print(sys.platform) 
# print(sys.version_info) 
print(f"Python Version: {platform.python_version()}")
print(f"Version Info: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
print(f"Python Implementation: {platform.python_implementation()}")
