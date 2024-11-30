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
# put the 5 list into a txt file

names = []
ages = []
heights = []
countrys = []
crushes = []

while True:
    while True:
        try:
            name_temp = input('Input your username\n')
            age_temp = input('Input your age\n')
            height_temp = input('Input your height in cm\n')
            country_temp = input('Input your country\n')
            crush_temp = input('Input your crush\n')
            break
            
        except:
            print('Error. Input again.')
            
    names.append(name_temp)
    ages.append(age_temp)
    heights.append(height_temp)
    countrys.append(country_temp)
    crushes.append(crush_temp)
        
    retry = input('Input another one? Y/N\n')

    if retry not in ('Y', 'y', 'yes', 'Yes', 'si'):
        break

user_database = list(zip(names, ages, heights, countrys, crushes))

print('Your Input has been saved to users.txt')

with open("./users.txt", "w") as user_iterate:
    for inside_list in user_database:
        user_iterate.write('{}\n'.format(inside_list))