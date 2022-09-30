print("Welcome to my Computer Quiz")
playing =input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okey ,Lets play :)")
score=0

answer=input("What does CPU stand for?")
if answer.lower()== "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect,Try again!")

answer=input("What does Dekut stand for?")
if answer.lower()== "Dedan Kimathi University of Technology":
    print("Correct!")
    score+=1

else:
    print("Incorrect,Try again!")

    answer=input("What does RAM stand for?")
if answer.lower()== "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect,Try again!")

    answer=input("What does GPU stand for?")
if answer.lower()== "graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect,Try again!")
    print("You got " +  str(score) +" questions correct!")
    print("You got " +  str((score/4) * 100 )+" %")

