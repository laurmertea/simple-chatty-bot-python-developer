# Description
# Now you will teach your bot to count. It's going to become an expert in numbers!

# Objective
# At this stage, you will program the bot to count from 0 to any positive number users enter.

# Example
# The greater-than symbol followed by space (> ) represents the user input. Notice that it's not the part of the input.

# Example 1: a dialogue with the new version of the bot

# `Hello! My name is Aid.`
# `I was created in 2020.`
# `Please, remind me your name.`
# > Max​​​​​​​
# `What a great name you have, Max!`
# `Let me guess your age.`
# `Tell me remainders of dividing your age by 3, 5 and 7.`
# > 1
# > 2
# > 1
# `Your age is 22; that's a good time to start programming!`
# `Now I will prove to you that I can count to any number you want.`
# > 5
# `0 !`
# `1 !`
# `2 !`
# `3 !`
# `4 !`
# `5 !`
# `Completed, have a nice day!`

# Note: each number starts with a new line, and after a number, 
# the bot should print the exclamation mark.
# Use the provided template to simplify your work. 
# You can change the text if you want, but be especially careful when counting numbers.

print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

rem3 = int(input())
rem5 = int(input())
rem7 = int(input())
age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

print("Your age is " + str(age) + "; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')

number = int(input())

x = range(number)

for n in x:
  print(str(n) + ' !')
print(str(number) + ' !')

print('Completed, have a nice day!')
