from tkinter import *

class Levels:
    """
    Gets the user to select a level for the algebra quiz
    """
    def __init__(self):
        # set up the frame
        self.level_frame = Frame(padx=10, pady=10, bg="#cce5ff")
        self.level_frame.grid()

        # list for the heading labels (text | font)
        headings_labels_list = [
            ["Linear Algebra Quiz", ("Arial", "18", "bold")],
            ["Select a Level", ("Arial", "16", "bold")]
        ]

        # create the labels
        levels_labels_ref = []
        for count, item in enumerate(headings_labels_list):
            make_label = Label(self.level_frame, text=item[0], font=item[1],
                               fg="#000000",bg="#cce5ff", justify="left", padx=10, pady=10)
            make_label.grid(row=count)

            levels_labels_ref.append(make_label)

        # list for buttons (frame | text | bg | command | width | row)
        levels_button_list = [
            [self.level_frame, "EASY", "#FFFB92", self.to_question_amount, 20, 3],
            [self.level_frame,"MEDIUM", "#95ff9c", self.to_question_amount, 20, 4],
            [self.level_frame, "HARD", "#ff7171", self.to_question_amount, 20, 5]
        ]

        # create buttons and add to list
        control_ref_list = []
        for item in levels_button_list:
            make_level_button = Button(item[0], text=item[1], bg=item[2], command=item[3],
                                         font=("Arial", 16, "bold"),
                                         width=item[4], fg="#000000")
            make_level_button.grid(row=item[5], padx= 5, pady=5)

            control_ref_list.append(make_level_button)

    def to_question_amount(self):
        QuestionAmount()
        # root.withdraw()


class QuestionAmount:
    """
    asks the user how many questions the user wants to answer
    """

    def __init__(self):
        self.num_of_questions_box = Toplevel()

        self.num_of_questions_frame = Frame(self.num_of_questions_box)
        self.num_of_questions_frame.grid(padx=10, pady=10)

        self.num_of_questions_label = Label(self.num_of_questions_frame, text="How many questions?",
                                            font=("Arial", 16, "bold"))
        self.num_of_questions_label.grid(row=1)

        # # frame so that entry box and bottom can be in the same row
        # self.entry_area_frame = Frame(self.num_of_questions_frame)
        # self.entry_area_frame.grid(row=3)

        self.num_rounds_entry = Entry(self.num_of_questions_frame,
                                      font=("Arial", 20, "bold",),
                                      width=10)
        self.num_rounds_entry.grid(row=2, column=0, padx=10, pady=10)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Linear Algebra Quiz")
    Levels()
    root.mainloop()

