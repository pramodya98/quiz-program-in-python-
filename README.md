This Python program, titled "Fast-Food Quiz Admin Program," is designed to manage a database of fast-food items and their nutritional information through a text-based interface. Below is a description of the program's functionality and structure:

Admin Program:

The program begins by attempting to load data from a file named "data.txt" and storing it in a list called data. If the file is missing or invalid, the program displays an error message and terminates.

It provides a menu-driven interface for the user, allowing them to choose from the following options:

[a]dd: Add a new fast-food item to the database, including details such as name, energy, fat, protein, carbohydrates, sugar, and sodium content.
[l]ist: List all the fast-food items currently in the database.
[s]earch: Search for fast-food items by a keyword and display matching results.
[v]iew: View detailed information about a specific fast-food item, including its nutritional content.
[d]elete: Delete a fast-food item from the database.
[q]uit: Exit the program.
Data Handling:

The program uses a list called data to store fast-food items, where each item is represented as a dictionary with attributes like name, energy, fat, protein, carbohydrates, sugar, and sodium content.

The program repeatedly prompts for user input based on the selected menu option.

Functions:

input_int(prompt): A function that repeatedly prompts for input until an integer is entered. It is used to ensure valid integer input.

input_something(prompt): A function that repeatedly prompts for input until non-whitespace text is entered.

save_data(data_list): A function that writes the data_list to the "data.txt" file in JSON format to save the database.

Main Class: ProgramGUI

This class sets up the graphical user interface (GUI) for the Fast-Food Quiz game. It uses the Tkinter library to create a simple window with buttons and labels.

The GUI presents the user with questions about fast-food items and their nutritional components, comparing two randomly selected items and asking the user to choose which one has more of a specified component (e.g., more fat).

Depending on the user's choice, the program displays Correct or Incorrect messages and proceeds to the next question.

The program reads data from a "data.txt" file to generate questions and checks user responses against correct answers.

The file_error, show_question, check_answer, correct, and incorrect methods control the game's logic and interface.

Usage:

To use the admin program, the user can select menu options by entering the corresponding letter.

When adding a fast-food item, the program requests information such as name, energy, fat, protein, carbohydrates, sugar, and sodium content.

The program allows searching for items, viewing details, and deleting items based on user input.

The user can exit the program by selecting the "q" option.

Note:

The code includes error handling to ensure that invalid input and missing data files are handled gracefully.

The admin program also includes comments and documentation for clarity and maintainability.
