#Program 2:
# Create another program that ask user for fullname. 
# Find the full name in the txt file (output of program1). 
# Display the informations found in the txt file.

searched_name = input('input the name your searching for\n')

with open("./users.txt", "r") as opened_file:
    user_data = opened_file.read()
    changed_data_to_list = user_data.split('\n')
    
output = []

for listed_data in changed_data_to_list:
    if searched_name in listed_data:
        output.append(listed_data)

print('Data is ordered as Name, Age, Height(cm), Country, Crush respectively')
print(output)