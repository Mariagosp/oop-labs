import tkinter as tk

def show_second_dialog(parent):
    result = {"value": None}

    window = tk.Toplevel(parent)
    window.title("Task 1 — step 2")
    window.geometry("350x180")
    window.resizable(False, False)

    window.transient(parent)
    window.grab_set()

    label = tk.Label(
        window,
        text="Second dialog window"
    )
    label.pack(pady=30)

    buttons = tk.Frame(window)
    buttons.pack()

    def back_clicked():
        result["value"] = "back"
        window.destroy()

    def yes_clicked():
        result["value"] = "yes"
        window.destroy()

    def cancel_clicked():
        result["value"] = "cancel"
        window.destroy()

    back_button = tk.Button(
        buttons,
        text="< Back",
        command=back_clicked
    )
    back_button.pack(side="left", padx=5)

    yes_button = tk.Button(
        buttons,
        text="Yes",
        command=yes_clicked
    )
    yes_button.pack(side="left", padx=5)

    cancel_button = tk.Button(
        buttons,
        text="Cancel",
        command=cancel_clicked
    )
    cancel_button.pack(side="left", padx=5)

    parent.wait_window(window)

    return result["value"]
  