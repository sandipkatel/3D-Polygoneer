import tkinter as tk
from tkinter import ttk

class RGBSliderApp:
    def __init__(self, parent):
        self.sub_frame = ttk.Frame(parent, padding="10")
        self.sub_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.init_ka_sliders()
        #self.init_ks_sliders()

    def init_ka_sliders(self):
        self.labelKaR = ttk.Label(self.sub_frame, text='R', foreground='red')
        self.labelKaR.grid(row=1, column=0, padx=5)
        self.scale_r = tk.Scale(self.sub_frame, from_=0, to=255, orient='horizontal', troughcolor='red', command=self.update_entries)
        self.scale_r.grid(row=1, column=1, padx=5)

        self.labelKaG = ttk.Label(self.sub_frame, text='G', foreground='green')
        self.labelKaG.grid(row=2, column=0, padx=5)
        self.scale_g = tk.Scale(self.sub_frame, from_=0, to=255, orient='horizontal', troughcolor='green', command=self.update_entries)
        self.scale_g.grid(row=2, column=1, padx=5)

        self.labelKaB = ttk.Label(self.sub_frame, text='B', foreground='blue')
        self.labelKaB.grid(row=3, column=0, padx=5)
        self.scale_b = tk.Scale(self.sub_frame, from_=0, to=255, orient='horizontal', troughcolor='blue', command=self.update_entries)
        self.scale_b.grid(row=3, column=1, padx=5)

    def update_entries(self, value):
        print(type(self.scale_r))
        return self.scale_r.get(), self.scale_g.get(), self.scale_b.get()
        """self.txtKsR.delete(0, tk.END)
        self.txtKsR.insert(1, str(self.scale_r.get()))

        self.txtKsG.delete(0, tk.END)
        self.txtKsG.insert(0, str(self.scale_g.get()))

        self.txtKsB.delete(0, tk.END)
        self.txtKsB.insert(0, str(self.scale_b.get()))"""

root = tk.Tk()
root.title("RGB Scale")
app = RGBSliderApp(root)
root.mainloop()
