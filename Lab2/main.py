import tkinter as tk
from tkinter import messagebox

from shapes import Point, Line, Rectangle, Ellipse


class GraphicEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Lab2 — Graphic Object Editor")
        self.root.geometry("900x600")

        self.shapes = []
        self.max_shapes = 106

        self.current_shape = "Point"
        self.drawing_shape = self.current_shape

        self.start_x = 0
        self.start_y = 0

        self.preview_id = None

        self.create_menu()
        self.create_canvas()
        self.bind_mouse_events()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Clear", command=self.clear_canvas)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)

        self.objects_menu = tk.Menu(menu_bar, tearoff=0)

        self.shape_types = ["Point", "Line", "Rectangle", "Ellipse"]

        self.shape_var = tk.StringVar(value=self.current_shape)

        for shape_name in self.shape_types:
            self.objects_menu.add_radiobutton(
                label=shape_name,
                variable=self.shape_var,
                value=shape_name,
                command=self.select_shape,
            )

        menu_bar.add_cascade(label="Objects", menu=self.objects_menu)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu_bar)

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root, bg="white", cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def select_shape(self):
        self.current_shape = self.shape_var.get()

    def bind_mouse_events(self):
        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

    def on_mouse_down(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.drawing_shape = self.current_shape

        if self.drawing_shape == "Point":
            if len(self.shapes) >= self.max_shapes:
                messagebox.showwarning(
                    "Warning",
                    f"The limit of {self.max_shapes} objects has been reached.",
                )
                return

            shape = Point(event.x, event.y)
            self.shapes.append(shape)
            shape.draw(self.canvas)

    def on_mouse_move(self, event):
        if self.drawing_shape == "Point":
            return

        self.canvas.delete("preview")

        self.draw_preview(event.x, event.y)

    def on_mouse_up(self, event):
        self.canvas.delete("preview")

        if self.drawing_shape == "Point":
            return

        if len(self.shapes) >= self.max_shapes:
            messagebox.showwarning(
                "Warning", f"The limit of {self.max_shapes} objects has been reached."
            )
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

        self.shapes.append(shape)
        shape.draw(self.canvas)

    def draw_preview(self, x, y):
        x1 = self.start_x
        y1 = self.start_y

        if self.drawing_shape == "Line":
            self.canvas.create_line(x1, y1, x, y, fill="blue", width=2, tags="preview")

        elif self.drawing_shape == "Rectangle":
            self.canvas.create_rectangle(
                x1, y1, x, y, outline="blue", fill="", width=2, tags="preview"
            )

        elif self.drawing_shape == "Ellipse":
            left = min(x1, 2 * x1 - x)
            top = min(y1, 2 * y1 - y)
            right = max(x1, 2 * x1 - x)
            bottom = max(y1, 2 * y1 - y)

            self.canvas.create_oval(
                left,
                top,
                right,
                bottom,
                outline="blue",
                fill="",
                width=2,
                tags="preview",
            )

    def clear_canvas(self):
        self.shapes.clear()
        self.canvas.delete("all")
        self.preview_id = None

    def show_about(self):
        messagebox.showinfo(
            "About",
            "Lab2 — Graphic Object Editor.\n" 
            "Developed using Python and Tkinter.",
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = GraphicEditor(root)
    root.mainloop()
