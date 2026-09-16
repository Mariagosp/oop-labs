import tkinter as tk

def show_first_dialog(parent):
    result = {"value": None}

    window = tk.Toplevel(parent)
    window.title("Робота 1 — крок 1")
    window.geometry("350x180")
    window.resizable(False, False)

    window.transient(parent)
    window.grab_set()

    label = tk.Label(
        window,
        text="Перше діалогове вікно"
    )
    label.pack(pady=30)

    buttons = tk.Frame(window)
    buttons.pack()

    def next_clicked():
        result["value"] = "next"
        window.destroy()

    def cancel_clicked():
        result["value"] = "cancel"
        window.destroy()

    next_button = tk.Button(
        buttons,
        text="Далі >",
        command=next_clicked
    )
    next_button.pack(side="left", padx=5)

    cancel_button = tk.Button(
        buttons,
        text="Відміна",
        command=cancel_clicked
    )
    cancel_button.pack(side="left", padx=5)

    parent.wait_window(window)

    return result["value"]