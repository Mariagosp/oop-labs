import tkinter as tk


class FirstDialog:
    def __init__(self, parent):
        self.parent = parent
        self.result = None

        self.window = tk.Toplevel(parent)

        self.window.title("Task 1 — Step 1")
        self.window.geometry("350x180")
        self.window.resizable(False, False)

        self.window.transient(parent)
        self.window.grab_set()

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.window, text="First dialog window")
        self.label.pack(pady=30)

        self.buttons = tk.Frame(self.window)
        self.buttons.pack()

        self.next_button = tk.Button(
            self.buttons, text="Next >", command=self.next_clicked
        )
        self.next_button.pack(side="left", padx=5)

        self.cancel_button = tk.Button(
            self.buttons, text="Cancel", command=self.cancel_clicked
        )
        self.cancel_button.pack(side="left", padx=5)

    def next_clicked(self):
        self.result = "next"
        self.window.destroy()

    def cancel_clicked(self):
        self.result = "cancel"
        self.window.destroy()

    def show(self):
        self.parent.wait_window(self.window)
        return self.result
