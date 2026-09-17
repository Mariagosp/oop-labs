import tkinter as tk


class SecondDialog:
    def __init__(self, parent):
        self.parent = parent
        self.result = None

        self.window = tk.Toplevel(parent)

        self.window.title("Task 1 — Step 2")
        self.window.geometry("350x180")
        self.window.resizable(False, False)

        self.window.transient(parent)
        self.window.grab_set()

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.window, text="Second dialog window")
        self.label.pack(pady=30)

        self.buttons = tk.Frame(self.window)
        self.buttons.pack()

        self.back_button = tk.Button(
            self.buttons, text="< Back", command=self.back_clicked
        )
        self.back_button.pack(side="left", padx=5)

        self.yes_button = tk.Button(self.buttons, text="Yes", command=self.yes_clicked)
        self.yes_button.pack(side="left", padx=5)

        self.cancel_button = tk.Button(
            self.buttons, text="Cancel", command=self.cancel_clicked
        )
        self.cancel_button.pack(side="left", padx=5)

    def back_clicked(self):
        self.result = "back"
        self.window.destroy()

    def yes_clicked(self):
        self.result = "yes"
        self.window.destroy()

    def cancel_clicked(self):
        self.result = "cancel"
        self.window.destroy()

    def show(self):
        self.parent.wait_window(self.window)
        return self.result
