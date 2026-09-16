import tkinter as tk

def show_group_dialog(parent):
    result = {"value": None}

    window = tk.Toplevel(parent)
    window.title("Task 2")
    window.geometry("350x300")
    window.resizable(False, False)

    window.transient(parent)
    window.grab_set()

    label = tk.Label(
        window,
        text="Select your group:"
    )
    label.pack(pady=10)

    groups = [
        "ІМ-51",
        "ІМ-52",
        "ІМ-53",
        "ІМ-54",
        "ІМ-о51"
    ]

    listbox = tk.Listbox(
        window,
        height=8,
        width=25
    )
    listbox.pack(pady=10)

    for group in groups:
        listbox.insert(tk.END, group)

    buttons = tk.Frame(window)
    buttons.pack(pady=10)

    def yes_clicked():
        selection = listbox.curselection()

        if selection:
            result["value"] = listbox.get(selection[0])
            window.destroy()

    def cancel_clicked():
        result["value"] = None
        window.destroy()

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
