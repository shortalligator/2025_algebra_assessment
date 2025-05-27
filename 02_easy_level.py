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

        self.choose_label = levels_labels_ref[2]

        self.levels_label = Label(self.level_frame, text="Select a level",
                                  font=("Arial", 16, "bold"),
                                  bg="#cce5ff")
        self.levels_label.grid(row=4)


        self.num_rounds_entry = Entry(self.level_frame,
                                      font=("Arial", 20, "bold"),
                                      width=10)
        self.num_rounds_entry.grid(row=3, column=0, padx=10, pady=10)

        # list for buttons (frame | text | bg | command | width | row)
        levels_button_list = [
            [self.level_frame, "EASY", "#FFFB92", self.check_rounds_to_easy_level(), 20, 5],
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

    def check_rounds_to_easy_level(self):
        rounds_wanted = self.num_rounds_entry.get()

        # reset label and entry box (for when users come back to home screen)
        self.choose_label.config(fg="#17b317", font=("Arial", "12", "bold"))
        self.num_rounds_entry.config(bg="#FFFFFF")

        error = "please choose a whole number more than zero."
        has_errors = "no"

        # checks that the amount wanted is a number above absolute zero
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
                                     font=("Arial", "10", "bold"))
            self.num_rounds_entry.config(bg="#F4CCCC")
            self.num_rounds_entry.delete(0, END)



class EasyLevel:
    """
    asks the user how many questions the user wants to answer
    """

    def __init__(self):
        self.easy_box = Toplevel()

        self.easy_frame = Frame(self.easy_box)
        self.easy_frame.grid(padx=10, pady=10)

        self.idk_label = Label(self.easy_frame, text="hello",
                               font=("Arial", 15, "bold"))


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Linear Algebra Quiz")
    Levels()
    root.mainloop()

