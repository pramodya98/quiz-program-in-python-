from tkinter import *
from tkinter import messagebox
import json
import random
from tkinter import font as tkfont


class ProgramGUI:


    def __init__(self):
        self.root = Tk()
        self.root.title('Fast-Food Quiz')
        self.root.geometry('400x150')
        self.root.resizable(False, False)

        self.question_frame = Frame(self.root, width=300, height=100, pady=10)
        self.button_frame = Frame(self.root, width=300, height=50, pady=10)

        self.question_frame.grid(columnspan=3)
        self.button_frame.grid(columnspan=1)

        self.question_frame.grid(row=0, sticky="nsew")
        self.button_frame.grid(row=1, sticky="nsew")

        try:
            with open('data.txt') as data_file:
                self.data = json.load(data_file)
            if len(self.data) < 2:
                self.file_error()
                return
        except :
            self.file_error()
            return

        self.components = ['energy', 'fat', 'protein', 'carbohydrates', 'sugar', 'sodium']

        self.left_button = Button(self.button_frame, command=lambda: self.check_answer('left'), 
            font=tkfont.Font(size=13))
        self.middle_button = Button(self.button_frame, text="Roughly Equal", command=lambda: self.check_answer('middle'), 
            font=tkfont.Font(size=13))
        self.right_button = Button(self.button_frame, command=lambda: self.check_answer('right'), 
            font=tkfont.Font(size=13))

        self.question_label = Label(self.question_frame, font=tkfont.Font(size=20))

        self.show_question()
        self.root.mainloop()


    def file_error(self):
        self.root.withdraw()
        messagebox.showinfo("Error", "Missing/Invalid file!")
        self.root.destroy()
        return


    def show_question(self):
        # This method is responsible for for randomly selecting two fast-food items and a nutritional component and showing them in the GUI.
        self.nutri_comp = random.choice(self.components)
        self.question_label.config(text=f"Which one has more...\n{self.nutri_comp.upper()}")

        self.left_item, self.right_item = random.sample(self.data, 2)
        self.left_button.config(text=self.left_item['name'])
        self.right_button.config(text=self.right_item['name'])

        self.question_label.grid(row=0, columnspan=3)
        self.left_button.grid(row=1, column=0, sticky='nsew', padx=5)
        self.middle_button.grid(row=1, column=1, sticky='nsew', padx=5)
        self.right_button.grid(row=1, column=2, sticky='nsew', padx=5)
        
        return


    def check_answer(self, choice):   
        # This method is responsible for determining whether the user clicked the correct button and showing a Correct/Incorrect messagebox.
        if (choice == 'left' and self.left_item[self.nutri_comp] > self.right_item[self.nutri_comp]):
            self.correct()
        elif (choice == 'right' and self.left_item[self.nutri_comp] < self.right_item[self.nutri_comp]):
            self.correct()
        elif (choice == 'middle'):
            max_val, min_val = max(self.left_item[self.nutri_comp], self.right_item[self.nutri_comp]), min(self.left_item[self.nutri_comp], self.right_item[self.nutri_comp])
            if (min_val >= max_val - max_val * 0.1):
                self.correct()
            else:
                self.incorrect()
        else:
            self.incorrect()
            
        return


    def correct(self):
        messagebox.showinfo("Correct!", "You got it right!")
        self.show_question()


    def incorrect(self):
        messagebox.showerror("Incorrect!", "You got it wrong!")
        self.show_question()

        
# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()


# If you have been paid to write this program, please delete this comment.
