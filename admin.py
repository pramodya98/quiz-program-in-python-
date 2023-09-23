# This function repeatedly prompts for input until an integer is entered.
def input_int(prompt):
    value = -1
    while not (isinstance(value, int) and value >= 0):
        try:
            value = int(input(prompt))
        except:
            print("The entered value is not valid. Please enter an integer ")
    return value


# This function repeatedly prompts for input until something other than whitespace is entered.
def input_something(prompt):
    value = ''
    while value.strip() == '':
        value = str(input(prompt))
    return value


# This function opens "data.txt" in write mode and writes data_list to it in JSON format.
def save_data(data_list):
    with open('data.txt', 'w', encoding='utf-8') as f:
        json.dump(data_list, f, indent=4)

# Open the data.txt file and read the data
try:
    with open('data.txt') as data_file:
        data = json.load(data_file)
except:
    data = []

print('Welcome to the Fast-Food Quiz Admin Program.')


while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower().strip()
        
    if choice == 'a':
        # Add a new fast-food item.
        name = input_something('Enter the name of the fast food item: ')

        for index,item in enumerate(data):
            if item.get('name') == name:
                print('Item already exists')
                item = f'{index+1}) ' + item.get('name')
                print(item)
                break
            


        energy = input_int('Enter the energy in kilojoules: ')
        fat = input_int('Enter the fat in grams: ')
        protein = input_int('Enter the protein in grams: ')
        carbohydrates = input_int('Enter the carbohydrates in grams: ')
        sugar = input_int('Enter the sugars in grams: ')
        sodium = input_int('Enter the sodium in milligrams: ')

        food_item = {
            'name' : name,
            'energy' : energy,
            'fat' : fat,
            'protein' : protein,
            'carbohydrates' : carbohydrates,
            'sugar' : sugar,
            'sodium' : sodium
        }

        data.append(food_item)
        save_data(data)
        print('Fast-food item added')


    
    elif choice == 'l':
        # List the current fast-food items.
        if len(data) == 0:
            print("There are no items saved.")
        else:
            print("list of items:")

            for index,item in enumerate(data):
                item = f'   {index+1}) ' + item.get('name')
                print(item)



    elif choice == 's':
        # Search the current fast-food items.
        if len(data) == 0:
            print("There are no items saved.")
        else:
            search_term = input_something('Enter search term ')
            print("Search results: ")

            results = 0

            for index,item in enumerate(data):
                if search_term.lower() in item.get('name').lower():
                    item = f'   {index+1}) ' + item.get('name')
                    print(item)
                    results += 1 
            
            if(results == 0):
                print('No results found ')



    elif choice == 'v':
        # View a fast food item
        if len(data) == 0:
            print("There are no items saved.")
        else:
            index = input_int("Enter item number to view: ")
            try:
                item = data[index-1]
                print(item.get('name'))
                print('Energy: ', item.get('energy'), 'kilojoules')
                print('Fat: ', item.get('fat', 'grams'))
                print('Protein: ', item.get('protein', 'grams'))
                print('Carbohydrates: ', item.get('carbohydrates'), 'grams')
                print('Sugar: ', item.get('sugar'), 'grams')
                print('Sodium: ', item.get('sodium'), 'milligrams')

            except:
                print('Invalid index number')

        

    elif choice == 'd':
        # Delete a fast food item
        if len(data) == 0:
            print("There are no items saved.")
        else:
            try:
                index = input_int("Enter item number to delete: ")
                item = data[index-1]
                data.remove(item)
                print(item.get('name'), 'deleted')
                save_data(data)

            except:
                print('Invalid index number')


        

    elif choice == 'q':
        # Exit the program
        print('Goodbye!')
        break



    else:
        # Wrong selection
        print("Invalid choice")
        pass



# If you have been paid to write this program, please delete this comment.
