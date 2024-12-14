```markdown

1. Write a program to create an Instagram login page.
    - Input Required:
        - Username (`input()`): Ask the user to enter their Instagram username.
        - Password (`input()`): Ask the user to enter their password.
    - Check if the entered username exists in the database (simulate with predefined values).
        - If the username is valid, check the password.
        - If the password matches:
            - Print a success message: "Login successful! Welcome to Instagram."
        - Else: Print: "Incorrect password. Please try again."
    - If the username is invalid, print: "Username not found. Please sign up."
    - Extra Features:
        - Add a "Forgot Password?" option to simulate a password recovery process.
        - Allow three attempts for login before locking the account.

2. Write a program to take a student's marks as input and assign a grade based on the following criteria:
    - If the marks are greater than or equal to 90, assign grade `A`.
    - If the marks are between 70 and 89, assign grade `B`.
        - Within this range, if the marks are above 85, add a comment: "Good performance!"
    - If the marks are between 50 and 69, assign grade `C`.
        - Within this range, if the marks are below 60, add a comment: "Needs Improvement."
    - If the marks are below 50, assign grade `F`.

3. Write a program to calculate the electricity bill based on the following criteria:
    - If the number of units consumed is less than or equal to 100, the rate is `₹5` per unit.
    - If the number of units is between 101 and 300:
        - For the first 100 units, the rate is `₹5` per unit.
        - For the remaining units, the rate is `₹7` per unit.
    - If the number of units is greater than 300:
        - For the first 100 units, the rate is `₹5` per unit.
        - For the next 200 units, the rate is `₹7` per unit.
        - For the remaining units, the rate is `₹10` per unit.

4. Write a program to check whether three sides entered by the user can form a triangle:
    - First, check if the sum of any two sides is greater than the third side.
    - If it's valid, classify the triangle:
        - If all sides are equal, it's an Equilateral triangle.
        - If only two sides are equal, it's an Isosceles triangle.
        - If no sides are equal, it's a Scalene triangle.
    - If the sides cannot form a triangle, print an error message.

5. Write a program to find the number of days in a given month and year:
    - Take the month and year as input.
    - If the month is February:
        - Check if the year is a leap year. If it is, February has 29 days; otherwise, it has 28 days.
    - For months with 30 days: April, June, September, November.
    - For months with 31 days: January, March, May, July, August, October, December.
    - Print the number of days in the month.

6. Write a program to take three numbers as input and find the largest among them:
    - First, check if the first number is greater than or equal to the second and third numbers.
        - If true, print that the first number is the largest.
    - Else, check if the second number is greater than or equal to the first and third numbers.
        - If true, print that the second number is the largest.
    - Otherwise, print that the third number is the largest.

7. Create a program to simulate an ATM withdrawal system:
    
    Prompt the user to enter their PIN.
    
    - If the PIN is correct:
        - Ask the user for the amount to withdraw.
        - Check if the amount is a multiple of `100`.
        - Check if the account balance is sufficient.
            - If yes, deduct the amount and display the new balance.
            - If no, show "Insufficient balance."
    - If the PIN is incorrect, display an error message.
    
8. Write a program to calculate the ticket price based on the following conditions:
    
    Ask the user for their age:
    
    - If age is below 18, the ticket price is $5.
    - If age is between 18 and 60:
        - Ask if the user is a student. If yes, the ticket price is $8. Otherwise, it's $12.
    - If age is above 60, the ticket price is $7.
    - Display the final ticket price.
9. Create a program to check if someone is eligible for car insurance:
    
    Ask the user for their age :
    
    - If the age is below 18, print "Not eligible for insurance."
    - If the age is between 18 and 70:
        - Ask if they have a valid driving license.
            - If yes, print "Eligible for insurance."
            - If no, print "You need a valid license to apply for insurance."
    - If the age is above 70, print "Too old to apply for insurance."
10. Write a program to calculate the discount for a customer:
    
    Ask the user for their total purchase amount:
    
    - If the amount is less than $100, no discount.
    - If the amount is between $100 and $500:
        - Ask if the customer has a membership card.
            - If yes, apply a 10% discount.
            - If no, apply a 5% discount.
    - If the amount is above $500:
        - Ask if it's a holiday season.
            - If yes, apply a 20% discount.
            - If no, apply a 15% discount.
    - Display the final price after the discount.
11. Create a program to check if a student is eligible for admission:
    
    Ask the student for their high school percentage :
    
    - If the percentage is below 50%, print "Not eligible for admission."
    - If the percentage is between 50% and 75%:
        - Check if they have any sports quota.
            - If yes, print "Eligible under sports quota."
            - If no, print "Eligible for admission."
    - If the percentage is above 75%, print "Direct admission granted."

12. Program to print middle value of the given heterogeneous tuple collection only if the middle value is string and having the length greater than 3.

13. Write a program to check the greater among four numbers using nested if.

14. Write a program to find the second greatest among four numbers.

15. Write a program to check greatest among three numbers using nested if.

16. Write a program to check second greatest among three numbers using nested if.

17. Write a program to find the smallest among three numbers. 

18. Write a program to consider an integer number. 
    1. Print happy if the number is divisible by two. 
    2. Print SAD if the number is divisible by 5.
    3. Print square of the numbers only if it is divisible by seven else print the number as it is.

19. Program to consider an input string. 
    1. Print the string as it is if it is palindrome.
    2. Print the reverse string if it has an even number of characters. 
    3. Print all the characters present at an odd index if the string is having an odd number of characters.

20. Write a program to print middle Character of given string only if it is upper case character.

21. Write a program that determines the movie ticket price based on the age and day of the week
    - The user inputs their age and the day of the week.
    - The day is converted to lowercase using `.strip().lower()` to ensure the input is case-insensitive (e.g., `Tuesday`, `tuesday`, and `TUESDAY` are treated the same).
    - For children under 1 year:
        - `$6` on Tuesdays, `$8` on other days.
    - For seniors (65 and older):
        - Always `$5`, regardless of the day.
    - For adults (18+ years):
        - `$10` on Tuesdays, `$12` on other days.
    - The ticket price is displayed based on the conditions.

22. Leap Year Checker: Write a program that determines if a given year is a leap year. A leap year is a year divisible by 4, but not by 100 unless it's also divisible by 400.

23. Design a program that takes two inputs (length1, length2) and identifies the geometric shape based on the values:

      - If lengths are equal: Square
      - If one length is twice the other: Rectangle
      - Otherwise: Not a square or rectangle

24. Write a program to simulate a vending machine that dispenses items based on the amount inserted and item choice.

1. The vending machine offers:
    - Soda: $1.50
    - Chips: $2.00
    - Candy: $1.00
2. The user:
    - Inputs the amount of money inserted.
    - Selects an item by entering the corresponding name.
3. The vending machine:
    - Checks if the user has enough money.
    - Dispenses the item and returns the change.
    - If the amount is insufficient, displays an error message.

25. Write a program to calculate the total bill after applying discounts based on the restaurant's rules.

1. Discounts offered:
    - If the bill amount is less than $100, no discount.
    - If the bill is between $100 and $300:
        - If it's a weekday, give a 10% discount.
        - If it's a weekend, give a 15% discount.
    - If the bill is over $300:
        - If the customer is a VIP, give a 25% discount.
        - If not, give a 20% discount.
2. The user:
    - Inputs the bill amount.
    - Indicates whether it's a weekday or weekend.
    - Indicates if they are a VIP (for bills over $300).

```
