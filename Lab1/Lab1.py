import tkinter as tk

import module1
import module2

root = tk.Tk()
root.title("Лабораторна робота №1")
root.geometry("500x300")

def run_work1():
    current_window = "first"

    while True:
        if current_window == "first":
            result = module1.show_first_dialog(root)

            if result == "next":
                current_window = "second"
            else:
                break

        elif current_window == "second":
            result = module2.show_second_dialog(root)

            if result == "back":
                current_window = "first"
            else:
                break

work1_button = tk.Button(
    root,
    text="Робота 1",
    command=run_work1
)
work1_button.pack(pady=50)

root.mainloop()
