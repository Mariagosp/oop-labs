import tkinter as tk

import module1
import module2
import module3

root = tk.Tk()
root.title("Laboratory Work №1")
root.geometry("500x300")

result_label = tk.Label(
    root,
    text="Select a menu item",
    font=("Arial", 14),
    fg="white"
)
result_label.pack(pady=100)

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
            elif result == "yes":
                result_label.config(
                    text="Task 1 completed"
                )
                break
            else:
                break

def run_work2():
    result = module3.show_group_dialog(root)

    if result is not None:
        result_label.config(
            text=f"Selected group: {result}"
        )

menu_bar = tk.Menu(root)

work_menu = tk.Menu(
    menu_bar,
    tearoff=0
)

work_menu.add_command(
    label="Task 1",
    command=run_work1
)

work_menu.add_command(
    label="Task 2",
    command=run_work2
)

menu_bar.add_cascade(
    label="Laboratory Work",
    menu=work_menu
)

root.config(menu=menu_bar)

root.mainloop()
