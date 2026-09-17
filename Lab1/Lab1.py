import tkinter as tk

from module1 import FirstDialog
from module2 import SecondDialog
from module3 import GroupDialog


class Lab1App:
    def __init__(self, root):
        self.root = root

        self.root.title("Laboratory Work №1")
        self.root.geometry("500x300")

        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        self.result_label = tk.Label(
            self.root,
            text="Select a menu item",
            font=("Arial", 14),
            fg="white"
        )
        self.result_label.pack(pady=100)

    def create_menu(self):
        self.menu_bar = tk.Menu(self.root)

        self.work_menu = tk.Menu(
            self.menu_bar,
            tearoff=0
        )

        self.work_menu.add_command(
            label="Task 1",
            command=self.run_work1
        )

        self.work_menu.add_command(
            label="Task 2",
            command=self.run_work2
        )

        self.menu_bar.add_cascade(
            label="Laboratory Work",
            menu=self.work_menu
        )

        self.root.config(menu=self.menu_bar)

    def run_work1(self):
        first_dialog = FirstDialog(self.root)
        result = first_dialog.show()

        if result != "next":
            return

        second_dialog = SecondDialog(self.root)
        result = second_dialog.show()

        if result == "back":
            self.run_work1()
        elif result == "yes":
            self.result_label.config(
                text="Task 1 completed"
            )

    def run_work2(self):
        group_dialog = GroupDialog(self.root)
        result = group_dialog.show()

        if result is not None:
            self.result_label.config(
                text=f"Selected group: {result}"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = Lab1App(root)
    root.mainloop()
