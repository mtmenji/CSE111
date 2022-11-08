def main():
    family = get_family()
    save_my_family(family)

'''
Purpose: In class exercise on Nov 8, 2022 where we receive names and ages of the user's family. The program then inputs the input to a dictionary, and each dictionary is entered into a list. The list is printed to a text file.
'''
def get_family():
    continue_bool = 'Y'
    family = []
    while continue_bool == 'Y':
        name = input("\nWhat is your family member's name? ")
        age = input((f"What is {name}'s age? "))
        person = {'name': name, 'age': age}
        family.append(person)
        user_input = input('Continue? (Y/n)')
        continue_bool = 'n' if user_input == 'n' else 'Y'
    return family

def save_my_family(family):
    file = open('family.txt', 'w')
    file.write('Here is a list of your family members. \n\n')
    for person in family:
        file.write(person['name'] + ' is ' + person['age'] + ' years old.\n')

main()