 #Peanut Butter Jelly Time!

# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich

# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make

# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )

# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches

# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.

#variables are amounts of ingredients. One full sandwich is 2 slices of bread, and one spoonful each of peanut butter and jelly.

#Status: Just finished Lesson 1, Goal 1 completed

bread="4"
pb="2"
jelly="2"

#Greeting

print("Hi \nWe're here to answer one questions and answer it well. \nCan YOU make a PB&J sandwich?")

if bread>=2 and pb>=1 and jelly>=1:
	print("Peanut butter jelly time!")
else:
	print("It is 'NOT' peanut butter jelly time :(")