```mermaid

classDiagram
    direction TB

    class Shape {
        <<abstract>>
        +draw(canvas)*
    }

    class Point {
        -x
        -y
        +__init__(x, y)
        +draw(canvas)
    }

    class Line {
        -x1
        -y1
        -x2
        -y2
        +__init__(x1, y1, x2, y2)
        +draw(canvas)
    }

    class Rectangle {
        -cx
        -cy
        -x
        -y
        +__init__(cx, cy, x, y)
        +get_bounds()
        +draw(canvas)
    }

    class Ellipse {
        -x1
        -y1
        -x2
        -y2
        +__init__(x1, y1, x2, y2)
        +draw(canvas)
    }

    class GraphicEditor {
        -root
        -shapes : Shape*[107]
        -max_shapes = 107
        -shape_count
        -current_shape
        -drawing_shape
        -tool_buttons
        -tool_icons
        -icons
        +create_menu()
        +create_toolbar()
        +update_toolbar()
        +update_shape_indicator()
        +create_canvas()
        +select_shape()
        +select_shape_by_name(shape_name)
        +bind_mouse_events()
        +on_mouse_down(event)
        +on_mouse_move(event)
        +on_mouse_up(event)
        +draw_preview(x, y)
        +clear_canvas()
        +show_about()
    }

    class ToolTip {
        -widget
        -text
        -tooltip
        +__init__(widget, text)
        +show(event)
        +hide(event)
    }

    Shape <|-- Point
    Shape <|-- Line
    Shape <|-- Rectangle
    Shape <|-- Ellipse

    GraphicEditor "1" o-- "107" Shape : shapes
    GraphicEditor ..> Point : creates
    GraphicEditor ..> Line : creates
    GraphicEditor ..> Rectangle : creates
    GraphicEditor ..> Ellipse : creates
    GraphicEditor ..> ToolTip : uses
```
