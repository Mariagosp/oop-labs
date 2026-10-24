import os
import tkinter as tk
from tkinter import messagebox

from shapes import Point, Line, Rectangle, Ellipse
from tooltip import ToolTip

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class GraphicEditor:
    SHAPE_OPTIONS = [
        ("Точка", "Point", "Намалювати точку", "point.png"),
        ("Лінія", "Line", "Намалювати лінію", "line.png"),
        ("Прямокутник", "Rectangle", "Намалювати прямокутник", "rectangle.png"),
        ("Еліпс", "Ellipse", "Намалювати еліпс", "ellipse.png"),
    ]

    def __init__(self, root):
        self.root = root
        self.current_shape = "Point"
        self.root.geometry("900x600")

        self.max_shapes = 107
        self.shapes = [None] * self.max_shapes
        self.shape_count = 0

        self.drawing_shape = self.current_shape
        self.drawing_allowed = True

        self.start_x = 0
        self.start_y = 0

        self.icons = {}
        self.tool_buttons = {}
        self.tool_icons = {}

        self.create_menu()
        self.create_toolbar()
        self.create_canvas()
        self.bind_mouse_events()
        self.update_shape_indicator()

    def shape_label(self, shape_name):
        for label, name, _tip, _icon in self.SHAPE_OPTIONS:
            if name == shape_name:
                return label
        return shape_name

    def update_shape_indicator(self):
        self.root.title(f"Lab3 — {self.shape_label(self.current_shape)}")
        self.update_toolbar()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Очистити", command=self.clear_canvas)
        file_menu.add_separator()
        file_menu.add_command(label="Вихід", command=self.root.destroy)
        menu_bar.add_cascade(label="Файл", menu=file_menu)

        self.objects_menu = tk.Menu(menu_bar, tearoff=0)
        self.shape_var = tk.StringVar(value=self.current_shape)

        for label, shape_name, _tip, _icon in self.SHAPE_OPTIONS:
            self.objects_menu.add_radiobutton(
                label=label,
                variable=self.shape_var,
                value=shape_name,
                command=self.select_shape,
            )

        menu_bar.add_cascade(label="Об'єкти", menu=self.objects_menu)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Про програму", command=self.show_about)
        menu_bar.add_cascade(label="Довідка", menu=help_menu)

        self.root.config(menu=menu_bar)

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED, bg="#e4e4e4")
        toolbar.pack(side=tk.TOP, fill=tk.X)

        for _label, shape_name, tip, icon_file in self.SHAPE_OPTIONS:
            image = tk.PhotoImage(file=os.path.join(BASE_DIR, "icons", icon_file))
            self.icons[shape_name] = image

            # Не Button: на macOS системна кнопка не зберігає втиснутий вигляд.
            button = tk.Frame(toolbar, bd=2, relief=tk.RAISED, bg="#f3f3f3")
            icon = tk.Label(
                button,
                image=image,
                bg="#f3f3f3",
                bd=0,
                padx=5,
                pady=5,
                cursor="hand2",
            )
            icon.pack()
            button.pack(side=tk.LEFT, padx=3, pady=3)

            for widget in (button, icon):
                widget.bind(
                    "<Button-1>",
                    lambda event, name=shape_name: self.select_shape_by_name(name),
                )
            ToolTip(icon, tip)
            self.tool_buttons[shape_name] = button
            self.tool_icons[shape_name] = icon

    def update_toolbar(self):
        for name, button in self.tool_buttons.items():
            selected = name == self.current_shape
            bg = "#c4c4c4" if selected else "#f3f3f3"
            button.config(relief=tk.SUNKEN if selected else tk.RAISED, bg=bg)
            self.tool_icons[name].config(bg=bg)

    def select_shape_by_name(self, shape_name):
        self.current_shape = shape_name
        self.shape_var.set(shape_name)
        self.update_shape_indicator()

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root, bg="white", cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def select_shape(self):
        self.current_shape = self.shape_var.get()
        self.update_shape_indicator()

    def bind_mouse_events(self):
        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

    def on_mouse_down(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.drawing_shape = self.current_shape

        self.drawing_allowed = self.shape_count < self.max_shapes

        if not self.drawing_allowed:
            messagebox.showwarning(
                "Попередження",
                f"Досягнуто межу в {self.max_shapes} об'єктів.",
            )
            return

        if self.drawing_shape == "Point":
            shape = Point(event.x, event.y)
            self.shapes[self.shape_count] = shape
            self.shape_count += 1
            shape.draw(self.canvas)

    def on_mouse_move(self, event):
        if not self.drawing_allowed:
            return

        if self.drawing_shape == "Point":
            return

        self.canvas.delete("preview")
        self.draw_preview(event.x, event.y)

    def on_mouse_up(self, event):
        self.canvas.delete("preview")

        if not self.drawing_allowed:
            return

        if self.drawing_shape == "Point":
            return

        x1 = self.start_x
        y1 = self.start_y
        x2 = event.x
        y2 = event.y

        if self.drawing_shape == "Line":
            shape = Line(x1, y1, x2, y2)

        elif self.drawing_shape == "Rectangle":
            shape = Rectangle(x1, y1, x2, y2)

        elif self.drawing_shape == "Ellipse":
            shape = Ellipse(x1, y1, x2, y2)

        else:
            return

        self.shapes[self.shape_count] = shape
        self.shape_count += 1
        shape.draw(self.canvas)

    def draw_preview(self, x, y):
        x1 = self.start_x
        y1 = self.start_y

        if self.drawing_shape == "Line":
            self.canvas.create_line(
                x1,
                y1,
                x,
                y,
                fill="black",
                width=2,
                dash=(4, 4),
                tags="preview",
            )

        elif self.drawing_shape == "Rectangle":
            left = 2 * x1 - x
            top = 2 * y1 - y

            self.canvas.create_rectangle(
                min(left, x),
                min(top, y),
                max(left, x),
                max(top, y),
                outline="black",
                fill="",
                width=2,
                dash=(4, 4),
                tags="preview",
            )

        elif self.drawing_shape == "Ellipse":
            left = min(x1, x)
            top = min(y1, y)
            right = max(x1, x)
            bottom = max(y1, y)

            self.canvas.create_oval(
                left,
                top,
                right,
                bottom,
                outline="black",
                fill="",
                width=2,
                dash=(4, 4),
                tags="preview",
            )

    def clear_canvas(self):
        self.shapes = [None] * self.max_shapes
        self.shape_count = 0
        self.canvas.delete("all")

    def show_about(self):
        messagebox.showinfo(
            "Про програму",
            "Lab3 — графічний редактор об'єктів.\n"
            "Розроблено на Python і Tkinter.",
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = GraphicEditor(root)
    root.mainloop()
