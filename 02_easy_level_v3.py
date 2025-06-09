from tkinter import *
import random
from functools import partial  # to prevent unwanted windows


def easy_questions():
    list_of_operators = ["+", "-", "*", "/"]

    operator = random.choice(list_of_operators)
    if operator == "*":
        a = random.choice([i for i in range(-10, 11) if i != 0])
        b = random.choice([i for i in range(-10, 11) if i != 0])
    else:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)

    # x+a = b
    if operator == "+":
        x = b - a
        equation = f"x + {a} = {b}"

    # x-a = b
    elif operator == "-":
        x = b + a
        equation = f"x - {a} = {b}"

    # xa = b
    elif operator == "*":
        x = b / a
        equation = f"x * {a} = {b}"

    # x/a = b
    else:
        x = b * a
        equation = f"x / {a} = {b}"

    return equation, x


class Levels:
    """
    Gets the user to select a level for the algebra quiz
    """

    def __init__(self):
        # set up the frame
        self.level_frame = Frame(padx=10, pady=10, bg="#cce5ff")
        self.level_frame.grid()

        intro_string = (
            "Welcome to the Linear Algebra Quiz\n\n"
            "Test your knowledge of basic algebra by solving\nequations to find the value of x. "
            "Choose how many\nquestions you'd like to answer, then select a difficulty\nlevel. "
            "If the answer has decimals, round it to 2\ndecimal places"
        )

        # list for the heading labels (text | font)
        headings_labels_list = [
            ["Linear Algebra Quiz", ("Arial", "18", "bold")],
            [intro_string, ("Arial", "10", "bold")],
            ["How many questions?", ("Arial", "16", "bold")]
        ]

        # create the labels
        levels_labels_ref = []
        for count, item in enumerate(headings_labels_list):
            make_label = Label(self.level_frame, text=item[0], font=item[1],
                               fg="#000000", bg="#cce5ff", justify="left", padx=10, pady=10)
            make_label.grid(row=count)

            levels_labels_ref.append(make_label)

        # extract choice label so that it can be changed into an error message
        self.choose_label = levels_labels_ref[2]

        self.levels_label = Label(self.level_frame, text="Select a level",
                                  font=("Arial", 16, "bold"),
                                  bg="#cce5ff")
        self.levels_label.grid(row=4)

        self.num_rounds_entry = Entry(self.level_frame,
                                      font=("Arial", 20, "bold"),
                                      width=10, bg="#ffffff")
        self.num_rounds_entry.grid(row=3, padx=10, pady=10)

        # list for buttons (frame | text | bg | command | width | row)
        levels_button_list = [
            [self.level_frame, "EASY", "#FFFB92", self.check_rounds_to_easy_level, 5],
            [self.level_frame, "MEDIUM", "#95ff9c", "", 6],
            [self.level_frame, "HARD", "#ff7171", "", 7]
        ]

        # create buttons and add to list
        control_ref_list = []
        for item in levels_button_list:
            make_level_button = Button(item[0], text=item[1], bg=item[2], command=item[3],
                                       font=("Arial", 16, "bold"),
                                       width=25, fg="#000000")
            make_level_button.grid(row=item[4], padx=5, pady=5)

            control_ref_list.append(make_level_button)


    def check_rounds_to_easy_level(self):
        rounds_wanted = self.num_rounds_entry.get()

        # reset label and entry box (for when users come back to home screen)
        self.choose_label.config(fg="#000000", font=("Arial", "16", "bold"))
        self.num_rounds_entry.config(bg="#FFFFFF")

        error = "please choose a whole number more than zero."
        has_errors = "no"

        # checks that the amount wanted is a number above zero
        try:
            rounds_wanted = int(rounds_wanted)
            if rounds_wanted > 0:
                self.num_rounds_entry.delete(0, END)
                self.choose_label.config(text="How many questions?")
                EasyLevel(rounds_wanted)
                # root.withdraw()
            else:
                has_errors = "yes"
        except ValueError:
            has_errors = "yes"

        # display the error if necessary
        if has_errors == "yes":
            self.choose_label.config(text=error, fg="#990000",
                                     font=("Arial", "12", "bold"))
            self.num_rounds_entry.config(bg="#F4CCCC")
            self.num_rounds_entry.delete(0, END)


class EasyLevel:
    """
    single step linear algebra, solving for x
    
    e.g. 5x = 10, x/2 = 8, x - 1 = 6, x + 3 = 9
    """

    def __init__(self, how_many):
        self.easy_box = Toplevel(padx=10, pady=10, bg="#fff2cc")

        self.questions_answered = IntVar()
        self.questions_answered.set(0)

        self.num_of_questions_wanted = IntVar()
        self.num_of_questions_wanted.set(how_many)

        self.correct_questions = IntVar()

        self.easy_frame = Frame(self.easy_box, bg="#fff2cc")
        self.easy_frame.grid()

        self.game_heading_label = Label(self.easy_frame, text="Question # of #",
                                        font=("Arial", 15, "bold"), bg="#fff2cc")
        self.game_heading_label.grid(row=0)

        self.question_label = Label(self.easy_frame, text="",
                                    font=("Arial", 20), bg="#fff2cc")
        self.question_label.grid(row=1, pady=10)

        self.correct_answer = None

        self.answer_frame = Frame(self.easy_frame, bg="#fff2cc")
        self.answer_frame.grid(row=2, padx=10)

        self.answer_entry = Entry(self.answer_frame, font=("Arial", 20, "bold"),
                                  width=10, bg="#ffffff")
        self.answer_entry.grid(row=3, column=1, padx=10, pady=10)

        self.submit_button = Button(self.answer_frame, text="Submit",
                                    font=("Arial", 12, "bold"), bg="#4CAF50",
                                    fg="white", command=self.check_answer)
        self.submit_button.grid(row=4, column=1, pady=5)

        self.feedback_label = Label(self.answer_frame, text="",
                                    font=("Arial", 14, "bold"), bg="#fff2cc")
        self.feedback_label.grid(row=2, column=0, columnspan=2, pady=(0, 10))

        self.generate_question()

        self.x_label = Label(self.answer_frame, text="X  =",
                             font=("Arial", 25, "bold"), bg="#fff2cc")
        self.x_label.grid(column=0, row=3)

        self.buttons_frame = Frame(self.easy_frame, bg="#fff2cc")
        self.buttons_frame.grid(row=3)

        self.hints_stats_frame = Frame(self.buttons_frame, bg="#fff2cc")
        self.hints_stats_frame.grid(row=2)

        # list for buttons ( text | bg | command | width | row | column )
        buttons_list = [
            [self.buttons_frame, "NEXT QUESTION", "#1ba1e2", self.generate_question, 22, 1, None],
            [self.hints_stats_frame, "Hints", "#FF8000", "", 10, 2, 0],
            [self.hints_stats_frame, "Stats", "#333333", "", 10, 2, 1],
            [self.buttons_frame, "END GAME", "#008a00", "", 22, 3, None]
        ]

        # create buttons and add to list
        control_ref_list = []
        for item in buttons_list:
            make_control_button = Button(item[0], text=item[1], bg=item[2], command=item[3],
                                         font=("Arial", 16, "bold"),
                                         width=item[4], fg="#FFFFFF")
            make_control_button.grid(row=item[5], column=item[6], padx=5, pady=5)

            control_ref_list.append(make_control_button)

        self.next_question_button = control_ref_list[0]
        self.stats_button = control_ref_list[1]
        self.end_game_button = control_ref_list[3]

    def generate_question(self):
        question, answer = easy_questions()
        self.correct_answer = round(answer, 2)
        self.question_label.config(text=question)
        self.answer_entry.delete(0, END)
        self.feedback_label.config(text="")
        self.submit_button.config(state=NORMAL)

        # Update heading label
        current = self.questions_answered.get() + 1
        total = self.num_of_questions_wanted.get()
        self.game_heading_label.config(text=f"Question {current} of {total}")


    def check_answer(self):
        user_input = self.answer_entry.get()

        try:
            user_answer = float(user_input)
            if round(user_answer, 2) == round(self.correct_answer, 2):
                feedback = "Correct!"
                self.correct_questions.set(self.correct_questions.get() + 1)
            else:
                feedback = f"Incorrect! The correct answer was {self.correct_answer}"

            self.questions_answered.set(self.questions_answered.get() + 1)
            self.feedback_label.config(text=feedback, fg="#008000" if "Correct" in feedback else "#ff0000")
            self.submit_button.config(state=DISABLED)

        except ValueError:
            self.feedback_label.config(text="Please enter a valid number", fg="#990000")



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Linear Algebra Quiz")
    Levels()
    root.mainloop()
