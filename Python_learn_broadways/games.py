
# day 10 
# 16 3 2026

# random
import random

# print(random.random())

# print(random.random()*100)
# a = ["hari", "shyam", "suman","sudan"]
# print(random.choice(a))

# crypto secret instead of random
''''

random_num = random.randint(1,10)
print("random number is: ", random_num)
count = 0
play_count = 0 

while True:
    count = count + 1
    user_num = int(input("Enter a number: "))

    if user_num == random_num:
        print("Number Matched in", count, "times")
        play_count = play_count + 1

        user_input = input("Do you want to play again (y/n) ?").lower()

        if user_input == "y":
            print("lets play again")
            random_num = random.randint(1,20)
            print("inside while loop", random_num)
            count = 0
        else:
            print("Thank you for playing")
            print("Total games played: ", play_count)
            break
    else:
        print("try again")
        print('\t')


leaderboard
random number from 1 to 10 only
total attempts = 3
remaining attempts = 
if remaining attempt 0 then play again input should run
user points = 0 
computer points = 0
if user or computer points reached 100, game should be over.


# CODE

random_num = random.randint(1,10)
print("random number is", random_num)
count = 0
play_count = 0 
computer_points = 0
user_points= 0
max_attempt = 0

while True: 
    if user_points >= 100 or computer_points >= 100:
        print("\n Game Over")
        print("User points: ", user_points)
        print("Computer Points:", computer_points)
        break

    count = count + 1
    remaining_attempt = max_attempt - count

    user_num = int(input("Enter a number: "))

    if user_num == random_num:
        print("Number Matched in", count, "times")
        play_count = play_count + 1
        user_points +=5

        print("Leaderboard")
        print("User",user_points)
        print("Computer:", computer_points)

        user_input = input("Do you want to play again (y/n) ?").lower()

        if user_input == "y":
            print("lets play again")
            random_num = random.randint(1,20)
            print("inside while loop", random_num)
            count = 0
        else:
            print("Thank you for playing")
            print("Total games played: ", play_count)
            break
    else:
        if remaining_attempt >= 0:

        print("try again")
        print('\t')

'''

# CORRCT CODE

import random
 
random_num = random.randint(1, 10)
print("random number is", random_num)
 
count = 0
games = 0
user_points = 0
computer_points = 0
max_attempt = 3
 
while True:
    if user_points >= 100 or computer_points >= 100:
        print("\nGame Over!")
        print("User Points:", user_points)
        print("Computer Points:", computer_points)
        break
 
    count = count+1
    remaining_attempt = max_attempt - count
 
    user_num = int(input("Enter a number: "))
 
    if user_num == random_num:
        print("Number match in", count, "times")
        games = games+1
        user_points = user_points+5
        print("User gets 5 points")
 
        print("Leaderboard")
        print("User:", user_points)
        print("Computer:", computer_points)
 
        user_input = input("Do you want to play again (y/n): ").lower()
 
        if user_input == "y":
            print("Lets play again")
            random_num = random.randint(1, 10)
            print("inside while loop", random_num)
            count = 0
        else:
            print("Thank you for playing")
            print("You played", games, "game(s)")
            break
 
    else:
        if remaining_attempt >= 0:
            print("Try Again")
            print("Remaining attempt:", remaining_attempt)
 
        if count == max_attempt:
            print("No more attempts")
            print("Computer wins this round")
            print("Correct number was:", random_num)
 
            computer_points = computer_points+5
            games = games+1
 
            print("Leaderboard")
            print("User:", user_points)
            print("Computer:", computer_points)
 
            user_input = input("Do you want to play again (y/n): ").lower()
 
            if user_input == "y":
                random_num = random.randint(1, 10)
                count = 0
            else:
                print("Thank you for playing")
                print("You played", games, "games")
                break
 