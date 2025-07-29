from tkinter import *
import random
from functools import partial  # to prevent unwanted windows


def easy_questions():
    list_of_operators = ["+", "-", "*", "/"]

    operator = random.choice(list_of_operators)

    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    x = random.randint(-10, 10)

    # x+a = b
    if operator == "+":
        b = x + a
        equation = f"x + {a} = {b}"

    # x-a = b
    elif operator == "-":
        b = x - a
        equation = f"x - {a} = {b}"

    # xa = b
    elif operator == "*":
        b = x * a
        equation = f"x * {a} = {b}"

    # x/a = b
    else:
        x = a * b
        equation = f"x / {a} = {b}"

    return equation, x


def medium_questions():

    operator1 = random.choice(["*", "/"])
    operator2 = random.choice(["+", "-"])

    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    x = random.randint(-10, 10)

    # ax + b = c
    if operator1 == "*" and operator2 == "+":
        c = a * x + b
        equation = f"{a}x + {b} = {c}"
    # ax - b = c
    elif operator1 == "*" and operator2 == "-":
        c = a * x - b
        equation = f"{a}x - {b} = {c}"
    # x / a + b = c
    elif operator1 == "/" and operator2 == "+":
        x = (c - b) * a
        equation = f"x/{a} + {b} = {c}"
    # x / a - b = c
    else:
        x = (c + b) * a
        equation = f"x/{a} - {b} = {c}"

    return equation, x


def hard_questions():
    operator1 = "*"
    operator2 = random.choice(["+", "-"])

    a = random.randint(-10, 10)
    b = random.randint(-20, 20)
    c = random.randint(-20, 20)
    x = random.randint(-20, 20)

    # a(bx + c) = d
    if operator1 == "*" and operator2 == "+":
        d = a * (b * x + c)
        equation = f"{a}({b}x + {c}) = {d}"

    # a(bx - c) = d
    else:
        d = a * (b * x - c)
        equation = f"{a}({b}x - {c}) = {d}"

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
            "\n\nYOU DON'T NEED A CALCULATOR"
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
            [self.level_frame, "EASY", "#FFFB92", self.to_easy, 5],
            [self.level_frame, "MEDIUM", "#95ff9c", self.to_medium, 6],
            [self.level_frame, "HARD", "#ff7171", self.to_hard, 7]
        ]

        # create buttons and add to list
        control_ref_list = []
        for item in levels_button_list:
            make_level_button = Button(item[0], text=item[1], bg=item[2], command=item[3],
                                       font=("Arial", 16, "bold"),
                                       width=25, fg="#000000")
            make_level_button.grid(row=item[4], padx=5, pady=5)

            control_ref_list.append(make_level_button)

    def check_rounds_to_algebra_level(self, difficulty, question_func):
        rounds_wanted = self.num_rounds_entry.get()

        self.choose_label.config(fg="#000000", font=("Arial", "16", "bold"))
        self.num_rounds_entry.config(bg="#FFFFFF")

        error = "Please choose a whole number more than zero."
        has_errors = "no"

        try:
            rounds_wanted = int(rounds_wanted)
            if rounds_wanted > 0:
                self.num_rounds_entry.delete(0, END)
                self.choose_label.config(text="How many questions?")
                Start(rounds_wanted, difficulty, question_func)
                root.withdraw()
            else:
                has_errors = "yes"
        except ValueError:
            has_errors = "yes"

        if has_errors == "yes":
            self.choose_label.config(text=error, fg="#990000", font=("Arial", "12", "bold"))
            self.num_rounds_entry.config(bg="#F4CCCC")
            self.num_rounds_entry.delete(0, END)

    def to_easy(self):
        self.check_rounds_to_algebra_level("easy", easy_questions)

    def to_medium(self):
        self.check_rounds_to_algebra_level("medium", medium_questions)

    def to_hard(self):
        self.check_rounds_to_algebra_level("hard", hard_questions)


class Start:
    """
    General algebra quiz class for all difficulty levels.
    Accepts a difficulty string and corresponding question generator function.
    """

    def __init__(self, how_many, difficulty, question_func):
        self.difficulty = difficulty
        self.generate_question_func = question_func  # Function to generate questions

        # Background colors and titles for each difficulty
        settings = {
            "easy": {"bg": "#fff2cc", "title": "Easy Linear Algebra"},
            "medium": {"bg": "#d9fdd3", "title": "Medium Linear Algebra"},
            "hard": {"bg": "#ffd9ec", "title": "Hard Linear Algebra"}
        }

        self.bg_color = settings[difficulty]["bg"]

        # Create a new top-level window for the quiz
        self.window = Toplevel(padx=10, pady=10, bg=self.bg_color)
        self.window.title(settings[difficulty]["title"])

        # Bind the window close button to close_game method
        self.window.protocol("WM_DELETE_WINDOW", self.close_game)

        # Track number of answered and correct questions
        self.questions_answered = IntVar(value=0)
        self.num_of_questions_wanted = IntVar(value=how_many)
        self.correct_questions = IntVar(value=0)

        # Main container frame
        self.main_frame = Frame(self.window, bg=self.bg_color)
        self.main_frame.grid()

        # Question header label
        self.game_heading_label = Label(self.main_frame, text="Question # of #",
                                        font=("Arial", 20, "bold"), bg=self.bg_color)
        self.game_heading_label.grid(row=0)

        # Label to display the question
        self.question_label = Label(self.main_frame, text="", font=("Arial", 20), bg=self.bg_color)
        self.question_label.grid(row=1, pady=10)

        self.correct_answer = None  # Holds the correct answer for comparison

        # Answer input area
        self.answer_frame = Frame(self.main_frame, bg=self.bg_color)
        self.answer_frame.grid(row=2, padx=10)

        self.feedback_label = Label(self.answer_frame, text="", font=("Arial", 14, "bold"), bg=self.bg_color)
        self.feedback_label.grid(row=2, column=0, columnspan=2, pady=(0, 10))

        self.answer_entry = Entry(self.answer_frame, font=("Arial", 20, "bold"), width=10, bg="#ffffff")
        self.answer_entry.grid(row=3, column=1, padx=10, pady=10)

        self.submit_button = Button(self.answer_frame, text="Submit", font=("Arial", 12, "bold"),
                                    bg="#4CAF50", fg="#ffffff", command=self.check_answer)
        self.submit_button.grid(row=4, column=1, pady=5)

        self.x_label = Label(self.answer_frame, text="X  =", font=("Arial", 23, "bold"), bg=self.bg_color)
        self.x_label.grid(column=0, row=3)

        # Navigation buttons (Next, Hints, Stats, End Game)
        self.buttons_frame = Frame(self.main_frame, bg=self.bg_color)
        self.buttons_frame.grid(row=3)

        self.hints_stats_frame = Frame(self.buttons_frame, bg=self.bg_color)
        self.hints_stats_frame.grid(row=2)

        buttons_list = [
            [self.buttons_frame, "NEXT QUESTION", "#1ba1e2", self.generate_question, 22, 1, None],
            [self.hints_stats_frame, "Hints", "#FF8000", self.to_hints, 10, 2, 0],
            [self.hints_stats_frame, "Stats", "#333333", self.to_stats, 10, 2, 1],
            [self.buttons_frame, "END GAME", "#e31010", self.close_game, 22, 3, None]
        ]

        control_ref_list = []
        for item in buttons_list:
            make_control_button = Button(item[0], text=item[1], bg=item[2], command=item[3],
                                         font=("Arial", 16, "bold"), width=item[4], fg="#FFFFFF")
            make_control_button.grid(row=item[5], column=item[6], padx=5, pady=5)
            control_ref_list.append(make_control_button)

        self.next_question_button = control_ref_list[0]
        self.hints_button = control_ref_list[1]
        self.stats_button = control_ref_list[2]
        self.end_game_button = control_ref_list[3]
        self.next_question_button.config(state=DISABLED)

        self.generate_question()  # Start with the first question

    def generate_question(self):
        # Use the provided question function to get a new question and answer
        question, answer = self.generate_question_func()
        self.correct_answer = round(answer, 2)
        self.question_label.config(text=question)
        self.answer_entry.delete(0, END)
        self.feedback_label.config(text="")
        self.submit_button.config(state=NORMAL)
        self.next_question_button.config(state=DISABLED)

        # Update heading with current progress
        current = self.questions_answered.get() + 1
        total = self.num_of_questions_wanted.get()
        self.game_heading_label.config(text=f"Question {current} of {total}")

    def check_answer(self):
        # Validate and check user's answer
        user_input = self.answer_entry.get()
        try:
            user_answer = float(user_input)
            if round(user_answer, 2) == round(self.correct_answer, 2):
                feedback = "Correct!"
                self.correct_questions.set(self.correct_questions.get() + 1)
            else:
                feedback = f"Incorrect! The correct answer was {self.correct_answer}"

            self.questions_answered.set(self.questions_answered.get() + 1)
            self.feedback_label.config(text=feedback, fg="#008000" if "Correct" in feedback else "#990000")
            self.submit_button.config(state=DISABLED)
            self.next_question_button.config(state=NORMAL)

        except ValueError:
            self.feedback_label.config(text="Please enter a valid number", fg="#990000")

    def close_game(self):
        # Close the quiz window and show main menu again
        root.deiconify()
        self.window.destroy()

    def to_hints(self):
        # Show hints window (stub)
        DisplayHints(self)

    def to_stats(self):
        # Show statistics window (stub)
        DisplayStats(self)


class DisplayHints:

    def __init__(self, partner):
        self.hints_box = Toplevel()
        self.hints_box.title("Hints")
        background = "#fad7ac"

        # disable hints button
        partner.hints_button.config(state=DISABLED)

        # If users press the cross at the top, closes and 'releases' the hints button
        self.hints_box.protocol('WM_DELETE_WINDOW', partial(self.close_hints, partner))

        self.hints_frame = Frame(self.hints_box, width=200, height=150,
                                 bg=background)
        self.hints_frame.grid()

        self.hints_heading_label = Label(self.hints_frame, text="Hints",
                                         font=("Arial", 16, "bold"), bg=background)
        self.hints_heading_label.grid(row=0)

        hints_text = "hints will go here"

        self.hints_text_label = Label(self.hints_frame, text=hints_text,
                                      wraplength=250, justify="left",
                                      font=("Arial", 12), bg=background)
        self.hints_text_label.grid(row=1, padx=10, pady=10)

        self.dismiss_button = Button(self.hints_frame, font=("Arial", 12, "bold"),
                                     text="DISMISS", bg="#CC6600", fg="#ffffff",
                                     command=partial(self.close_hints, partner))
        self.dismiss_button.grid(row=2, pady=10, padx=10)

    def close_hints(self, partner):
        """
        Closes hints dialogue box and enables hints button
        """
        # Put hints button back to normal
        partner.hints_button.config(state=NORMAL)
        self.hints_box.destroy()


class DisplayStats:
    def __init__(self, partner):
        self.stats_box = Toplevel()
        self.stats_box.title("Game Stats")
        background = "#f9f7ed"

        partner.stats_button.config(state=DISABLED)

        self.stats_box.protocol("WM_DELETE_WINDOW", partial(self.close_stats, partner))

        self.stats_frame = Frame(self.stats_box, bg=background, padx=20, pady=20)
        self.stats_frame.grid()

        # Heading
        self.heading = Label(self.stats_frame, text="Game Statistics",
                             font=("Arial", 18, "bold"), bg=background)
        self.heading.grid(row=0, pady=(0, 10))

        # Calculate stats
        answered = partner.questions_answered.get()
        correct = partner.correct_questions.get()
        percent_correct = round((correct / answered) * 100, 1) if answered else 0

        stats_text = (f"Questions Answered: {answered}\n"
                      f"Correct Answers: {correct}\n"
                      f"Percentage Correct: {percent_correct}%")

        self.stats_label = Label(self.stats_frame, text=stats_text,
                                 font=("Arial", 14), bg=background, justify="left")
        self.stats_label.grid(row=1)

        # Dismiss button
        self.dismiss_button = Button(self.stats_frame, text="Close",
                                     font=("Arial", 12, "bold"),
                                     bg="#007acc", fg="white",
                                     command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=2, pady=10)

    def close_stats(self, partner):
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Linear Algebra Quiz")
    Levels()
    root.mainloop()
