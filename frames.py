
import tkinter as tk
from tkinter import ttk


class VerticalScrolledFrame:
    def __init__(self, master, width, height, janela, **kwargs):
        bg = kwargs.pop('bg', kwargs.pop('background', None))
        self.outer = tk.Frame(master, **kwargs)
        self.vsb = tk.Scrollbar(self.outer, orient=tk.VERTICAL)
        self.vsb.pack(fill=tk.Y, side=tk.RIGHT)
        if (janela == 0):
            self.canvas = tk.Canvas(
                self.outer, highlightthickness=0, width=width, height=int(height * 0.3), bg=bg)
        if (janela == 1):
            self.canvas = tk.Canvas(
                self.outer, highlightthickness=0, width=width, height=int(height * 0.2), bg=bg)
        if (janela == 2):
            self.canvas = tk.Canvas(
                self.outer, highlightthickness=0, width=width, height=int(height * 0.3), bg=bg)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas['yscrollcommand'] = self.vsb.set

        self.canvas.bind("<Enter>", self._bind_mouse)
        self.canvas.bind("<Leave>", self._unbind_mouse)
        self.vsb['command'] = self.canvas.yview
        self.inner = tk.Frame(self.canvas, bg=bg)

        self.canvas.create_window(4, 4, window=self.inner, anchor='nw')
        self.inner.bind("<Configure>", self._on_frame_configure)
        self.outer_attr = set(dir(tk.Widget))

    def __getattr__(self, item):
        if item in self.outer_attr:
            return getattr(self.outer, item)
        else:
            return getattr(self.inner, item)

    def _on_frame_configure(self, event=None):
        x1, y1, x2, y2 = self.canvas.bbox("all")
        height = self.canvas.winfo_height()
        self.canvas.config(scrollregion=(0, 0, x2, max(y2, height)))

    def _bind_mouse(self, event=None):
        self.canvas.bind_all("<4>", self._on_mousewheel)
        self.canvas.bind_all("<5>", self._on_mousewheel)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mouse(self, event=None):
        self.canvas.unbind_all("<4>")
        self.canvas.unbind_all("<5>")
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        if event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")

    def __str__(self):
        return str(self.outer)


class ToggledFrame(tk.Frame):

    def __init__(self, parent, width, height, text="", *args, **options):
        tk.Frame.__init__(self, parent, *args, **options)

        self.show = tk.IntVar()
        self.show.set(0)

        self.title_frame = ttk.Frame(self)
        self.title_frame.pack(fill="x", expand=1)

        ttk.Label(self.title_frame, text=text).pack(
            side="left", fill="x", expand=1, padx=50)

        self.toggle_button = ttk.Checkbutton(self.title_frame, width=2, text='+', command=self.toggle,
                                             variable=self.show, style='Toolbutton')
        self.toggle_button.pack(side="left")

        if (text == "Object Information"):
            self.sub_frame = VerticalScrolledFrame(
                self, width, height, borderwidth=1, janela=0, relief=tk.SUNKEN)
        if (text == "Projection"):
            self.sub_frame = VerticalScrolledFrame(
                self, width, height, borderwidth=1, janela=1, relief=tk.SUNKEN)
        if (text == "Lighting and Shading"):
            self.sub_frame = VerticalScrolledFrame(
                self, width, height, borderwidth=1, janela=2, relief=tk.SUNKEN)

    def toggle(self):
        if bool(self.show.get()):
            self.sub_frame.pack(fill=tk.BOTH, expand=True)  # fill window
            self.toggle_button.configure(text='-')
        else:
            self.sub_frame.forget()
            self.toggle_button.configure(text='+')
