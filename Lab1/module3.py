import tkinter as tk


class GroupDialog:
    def __init__(self, parent):
        self.parent = parent
        self.result = None

        self.groups = ["ІМ-51", "ІМ-52", "ІМ-53", "ІМ-54", "ІМ-о51"]

        self.window = tk.Toplevel(parent)

        self.window.title("Task 2")
        self.window.geometry("350x300")
        self.window.resizable(False, False)

        self.window.transient(parent)
        self.window.grab_set()

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.window, text="Select your group:")
        self.label.pack(pady=10)

        self.listbox = tk.Listbox(self.window, height=8, width=25)
        self.listbox.pack(pady=10)

        self.fill_listbox()

        self.buttons = tk.Frame(self.window)
        self.buttons.pack(pady=10)

        self.yes_button = tk.Button(self.buttons, text="Yes", command=self.yes_clicked)
        self.yes_button.pack(side="left", padx=5)

        self.cancel_button = tk.Button(
            self.buttons, text="Cancel", command=self.cancel_clicked
        )
        self.cancel_button.pack(side="left", padx=5)

    def fill_listbox(self):
        for group in self.groups:
            self.listbox.insert(tk.END, group)

    def yes_clicked(self):
        selection = self.listbox.curselection()

        if selection:
            self.result = self.listbox.get(selection[0])
            self.window.destroy()

    def cancel_clicked(self):
        self.result = None
        self.window.destroy()

    def show(self):
        self.parent.wait_window(self.window)
        return self.result
