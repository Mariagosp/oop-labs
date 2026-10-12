import tkinter as tk


class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None

        self.widget.bind("<Enter>", self.show)
        self.widget.bind("<Leave>", self.hide)

    def show(self, event=None):
        if self.tooltip is not None:
            return

        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 5

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(
            self.tooltip,
            text=self.text,
            background="#FFF8DC",
            foreground="#222222",
            font=("Arial", 10),
            relief="solid",
            borderwidth=1,
            padx=8,
            pady=4,
        )
        label.pack()

    def hide(self, event=None):
        if self.tooltip is not None:
            self.tooltip.destroy()
            self.tooltip = None
