from tkinter import *

class Levels:
    """
    Gets the user to select a level for the algebra quiz
    """
    def __init__(self):
        # set up the frame
        self.level_frame = Frame(padx=10, pady=10, bg="#cce5ff")
        self.level_frame.grid()

        levels_labels_list = [
            ["Linear Algebra Quiz", ("Arial", "18", "bold")],
            ["Select a Level", ("Arial", "16", "bold")]
        ]

        levels_labels_ref = []
        for count, item in enumerate(levels_labels_list):
            make_label = Label(self.level_frame, text=item[0], font=item[1],
                               fg="#000000",bg="#cce5ff", justify="left", padx=10, pady=10)
            make_label.grid(row=count)

            levels_labels_ref.append(make_label)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Linear Algebra Quiz")
    Levels()
    root.mainloop()

