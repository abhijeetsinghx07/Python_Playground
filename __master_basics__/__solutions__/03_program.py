#Write a program to display the current date and time.

from datetime import datetime

current_time = datetime.now()

print(current_time)
print(current_time.strftime("%Y-%m-%d %H:%M:%S"))
