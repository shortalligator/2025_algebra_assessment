from tkinter import *

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
            [self.level_frame, "EASY", "#FFFB92", self.to_play, 5],
            [self.level_frame, "MEDIUM", "#95ff9c", self.to_play, 6],
            [self.level_frame, "HARD", "#ff7171", self.to_play, 7]
        ]

        # create buttons and add to list
        control_ref_list = []
        for item in levels_button_list:
            make_level_button = Button(item[0], text=item[1], bg=item[2], command=item[3],
                                       font=("Arial", 16, "bold"),
                                       width=25, fg="#000000")
            make_level_button.grid(row=item[4], padx=5, pady=5)

            control_ref_list.append(make_level_button)
    def to_play(self):
        PLay()

class PLay:
    def __init__(self):
        self.play_box = Toplevel()
        self.play_frame = Frame(self.play_box)
        self.play_frame.grid(padx=10, pady=10)
        self.title_label = Label(self.play_frame, text="Question # of #",
                                 font=("Arial", 20, "bold"))
        self.title_label.grid(row=1, pady=20)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Linear Algebra Quiz")
    Levels()
    root.mainloop()

