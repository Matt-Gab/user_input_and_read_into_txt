#Program 1:
# Create a program that ask user for personal information.
# Minimum of 5 information per person, more info the better. 
# eg. Fullname, Address, etc. Write the collected information in a txt file. 
# It's up to you on how you'd like to format the information in the file. 
# The program should ask user if want to input another person or exit.

# user asked for input
# ask user to input if they want again
# if yes then save the last input into 5 list as dictionaries and go to step 1
# if no then save input into 4 list as dict and add the each index in the list into a list
# put the 4 list into a txt file

user_database = []

names = []
ages = []
heights = []

while True:
    try:
        names.append(input('input yo name\n'))
        ages.append(int(input('input age\n')))
        heights.append(int(input('input height in cm\n')))
        
    except:
        print('error lol')
        
    user_database = list(zip(names, ages, heights))
    
    with open("./users.txt", "a") as user_iterate:
        user_iterate.write(f'{user_database[-1]}\n')
    
    retry = input('Input another one? Y/N\n')

    if retry not in ('Y', 'y', 'yes', 'Yes', 'si'):
        break
    

print(user_database)