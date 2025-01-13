print("Welcome to my Quiz Gam!")

playing = input("You want to play? ")

if playing.lower() != 'yes':
    quit()

print("Let's play :) ")
score=0

answer = input("What does CPU stand for? ")
if answer.lower() == 'central processing unit':
    print("Correct Answer! :)\n")
    score+=1

else:
    print("Wrong Answer! ):\n")

answer = input("What does ALU stand for? ")
if answer.lower() == 'arithmatic logic unit':
    print("Correct Answer:)\n")
    score+=1

else:
    print("Wrong Answer! ):\n")


answer = input("What does RAM stand for? ")
if answer.lower() == 'random access memory':
    print("Correct Answer:)\n")
    score+=1

else:
    print("Wrong Answer! ):\n")


answer = input("What does GPU stand for? ")
if answer.lower() == 'graphics processing unit':
    print("Correct Answer:)\n")
    score+=1

else:
    print("Wrong Answer! ):\n")

print(f"You got {score} score.")
print(f"You got {round((score)/4*100)}%")

