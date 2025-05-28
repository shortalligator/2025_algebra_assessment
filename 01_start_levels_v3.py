from tkinter import *

class Levels:
    """
    Gets the user to select a level for the algebra quiz
    """
    def __init__(self):
        # set up the frame
        self.level_frame = Frame(padx=10, pady=10, bg="#cce5ff")
        self.level_frame.grid()

        intro_string = "introduction will go here"

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
                               fg="#000000",bg="#cce5ff", justify="left", padx=10, pady=10)
            make_label.grid(row=count)

            levels_labels_ref.append(make_label)

        self.levels_label = Label(self.level_frame, text="Select a level",
                                  font=("Arial", 16, "bold"),
                                  bg="#cce5ff")
        self.levels_label.grid(row=4)

        # list for buttons (frame | text | bg | command | width | row)
        levels_button_list = [
            [self.level_frame, "EASY", "#FFFB92", "", 20, 5],
            [self.level_frame,"MEDIUM", "#95ff9c", "", 20, 6],
            [self.level_frame, "HARD", "#ff7171", "", 20, 7]
        ]

        # create buttons and add to list
        control_ref_list = []
        for item in levels_button_list:
            make_level_button = Button(item[0], text=item[1], bg=item[2], command=item[3],
                                         font=("Arial", 16, "bold"),
                                         width=item[4], fg="#000000")
            make_level_button.grid(row=item[5], padx= 5, pady=5)

            control_ref_list.append(make_level_button)

        self.num_rounds_entry = Entry(self.level_frame,
                                      font=("Arial", 20, "bold",),
                                      width=10)
        self.num_rounds_entry.grid(row=3, column=0, padx=10, pady=10)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Linear Algebra Quiz")
    Levels()
    root.mainloop()

