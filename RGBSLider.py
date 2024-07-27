import tkinter as tk
from tkinter import ttk

class RGBSliderApp:
    def __init__(self):
        pass

    def sliders(self, sub_frame, row = 0, column = 0):
        self.labelKaR = ttk.Label(sub_frame, text='R', foreground='red')
        self.labelKaR.grid(row=row + 1, column= column, padx = 1, pady = 1)
        self.scale_r = tk.Scale(sub_frame, from_=0, to=255, orient='horizontal', troughcolor='red')
        self.scale_r.grid(row=row + 1, column=column + 1, padx = 1, pady = 1)

        self.labelKaG = ttk.Label(sub_frame, text='G', foreground='green')
        self.labelKaG.grid(row=row + 2, column=column, padx = 1, pady = 1)
        self.scale_g = tk.Scale(sub_frame, from_=0, to=255, orient='horizontal', troughcolor='green')
        self.scale_g.grid(row=row + 2, column=column + 1, padx = 1, pady = 1)

        self.labelKaB = ttk.Label(sub_frame, text='B', foreground='blue')
        self.labelKaB.grid(row=row + 3, column=column, padx = 1, pady = 1)
        self.scale_b = tk.Scale(sub_frame, from_=0, to=255, orient='horizontal', troughcolor='blue')
        self.scale_b.grid(row=row + 3, column=column + 1, padx = 1, pady = 1)

        return self.scale_r, self.scale_g, self.scale_b

    def reset(self):
        self.scale_r.set(self.scale_r.cget('from'))
        self.scale_g.set(self.scale_g.cget('from'))
        self.scale_b.set(self.scale_b.cget('from'))

"""def main():
    root = tk.Tk()
    root.title("RGB Scale")
    app = RGBSliderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()"""
