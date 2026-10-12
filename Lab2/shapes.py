from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self, canvas):
        pass


class Point(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, canvas):
        radius = 3
        canvas.create_oval(
            self.x - radius,
            self.y - radius,
            self.x + radius,
            self.y + radius,
            fill="black",
            outline="black",
        )


class Line(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="black", width=2)


class Rectangle(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, canvas):
        canvas.create_rectangle(
            self.x1, self.y1, self.x2, self.y2, outline="black", fill="yellow", width=2
        )


class Ellipse(Shape):
    def __init__(self, cx, cy, x, y):
        self.cx = cx
        self.cy = cy
        self.x = x
        self.y = y

    def get_bounds(self):
        opposite_x = 2 * self.cx - self.x
        opposite_y = 2 * self.cy - self.y

        return (
            min(opposite_x, self.x),
            min(opposite_y, self.y),
            max(opposite_x, self.x),
            max(opposite_y, self.y),
        )

    def draw(self, canvas):
        left, top, right, bottom = self.get_bounds()

        canvas.create_oval(
            left,
            top,
            right,
            bottom,
            outline="black",
            fill="gray",
            width=2,
        )
