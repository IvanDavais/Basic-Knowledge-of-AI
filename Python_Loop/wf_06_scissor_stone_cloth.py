import random

print("This is the bet game!")
your_choice = int(input("Please choice stone (1), scissor (2), and cloth (3)! "))
print("your choice is : %d" %your_choice)

computer= random.randint(1,3)
print("The computer select %d" %computer)

if ((your_choice == 1 and computer == 2)
        or (your_choice == 2 and computer == 3)
        or(your_choice ==3 and computer ==1)):
    print("you win this game!")

elif(your_choice == computer):
    print("Equal, do it again!")

else:
    print("Sorry, you lose this game!")


