from tkinter import font
from tooltip import CreateToolTip

import numpy as np
from DataStructure.Matrices.transforms import translation
from shutil import disk_usage
from tkscrolledframe import ScrolledFrame, widget
from Screen import Screen
import tkinter as tk
from tkinter import Canvas, Frame, Scrollbar, ttk
from tkinter.constants import ALL, E, N, NS, RIGHT, S, VERTICAL, W, Y
from tkinter import messagebox

class VerticalScrolledFrame:
    def __init__(self, master, width, height, window, **kwargs):
        bg = kwargs.pop('bg', kwargs.pop('background', None))
        self.outer = tk.Frame(master, **kwargs)
        self.vsb = tk.Scrollbar(self.outer, orient=tk.VERTICAL)
        self.vsb.pack(fill=tk.Y, side=tk.RIGHT) 
        if window == 0:
            self.canvas = tk.Canvas(self.outer, highlightthickness=0, width=width, height=int(height * 0.3), bg=bg)
        elif window == 1:
            self.canvas = tk.Canvas(self.outer, highlightthickness=0, width=width, height=int(height * 0.2), bg=bg)
        elif window == 2:
            self.canvas = tk.Canvas(self.outer, highlightthickness=0, width=width, height=int(height * 0.3), bg=bg)
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

        ttk.Label(self.title_frame, text=text).pack(side="left", fill="x", expand=1, padx=50)

        self.toggle_button = ttk.Checkbutton(self.title_frame, width=2, text='+', command=self.toggle,
                                             variable=self.show, style='Toolbutton')
        self.toggle_button.pack(side="left")

        if text == "Object Information":
            self.sub_frame = VerticalScrolledFrame(self, width, height, borderwidth=1, window=0, relief=tk.SUNKEN)
        if text == "Projection":
            self.sub_frame = VerticalScrolledFrame(self, width, height, borderwidth=1, window=1, relief=tk.SUNKEN)
        if text == "Lighting and Shading":
            self.sub_frame = VerticalScrolledFrame(self, width, height, borderwidth=1, window=2, relief=tk.SUNKEN)
            print("I am called for sub_frame")

    def toggle(self):
        if bool(self.show.get()):
            self.sub_frame.pack(fill="x", expand=1)
        else:
            self.sub_frame.forget()

def readRadioButton(_, __, ___):
    if rbProjection.get() == 0:
        txtPx['state'] = tk.DISABLED
        txtPy['state'] = tk.DISABLED
        txtPz['state'] = tk.DISABLED
    else:
        txtPx['state'] = tk.NORMAL  # Changed to tk.NORMAL to reflect the correct state
        txtPy['state'] = tk.NORMAL
        txtPz['state'] = tk.NORMAL

def buttonObject(_, __, ___):
    if drawing.objectSelected is not None:
        btnUpdateObject['state'] = tk.NORMAL  # Changed to tk.NORMAL to reflect the correct state
        btnUpdateObject['cursor'] = "hand2"
        btnCreateObject['state'] = tk.DISABLED
        btnCreateObject['cursor'] = "arrow"
    else:
        btnUpdateObject['state'] = tk.DISABLED
        btnUpdateObject['cursor'] = "arrow"
        btnCreateObject['state'] = tk.NORMAL  # Changed to tk.NORMAL to reflect the correct state
        btnCreateObject['cursor'] = "hand2"

def clearScreen():
    drawing.clearAll()

def sendUI(values):
    txtNumSides.delete(0, tk.END)
    txtNumSides.insert(0, str(values[0]))
    txtBaseRadius.delete(0, tk.END)
    txtBaseRadius.insert(0, str(values[1]))
    txtTopRadius.delete(0, tk.END)
    txtTopRadius.insert(0, str(values[2]))
    txtHeight.delete(0, tk.END)
    txtHeight.insert(0, str(values[3]))
    
    txtN.delete(0, tk.END)
    txtN.insert(0, str(values[4]))
    txtKaR.delete(0, tk.END)
    txtKaR.insert(0, str(values[5]))
    txtKaG.delete(0, tk.END)
    txtKaG.insert(0, str(values[6]))
    txtKaB.delete(0, tk.END)
    txtKaB.insert(0, str(values[7]))
    txtKdR.delete(0, tk.END)
    txtKdR.insert(0, str(values[8]))
    txtKdG.delete(0, tk.END)
    txtKdG.insert(0, str(values[9]))
    txtKdB.delete(0, tk.END)
    txtKdB.insert(0, str(values[10]))
    txtKsR.delete(0, tk.END)
    txtKsR.insert(0, str(values[11]))
    txtKsG.delete(0, tk.END)
    txtKsG.insert(0, str(values[12]))
    txtKsB.delete(0, tk.END)
    txtKsB.insert(0, str(values[13]))

translationValue = 5
scaleLessValue = 0.9
scaleMoreValue = 1.111111
rotationValue = 5

def move_x_left(event):
    if drawing.objectSelected is not None:
        drawing.moveObject(-translationValue, 0, 0)
        sendUI(drawing.getAttributes())

def move_x_right(event):
    if drawing.objectSelected is not None:
        drawing.moveObject(translationValue, 0, 0)
        sendUI(drawing.getAttributes())

def move_z_front(event):
    if drawing.objectSelected is not None:
        drawing.moveObject(0, 0, translationValue)
        sendUI(drawing.getAttributes())

def move_z_back(event):
    if drawing.objectSelected is not None:
        drawing.moveObject(0, 0, -translationValue)
        sendUI(drawing.getAttributes())

def move_y_up(event):
    if drawing.objectSelected is not None:
        drawing.moveObject(0, translationValue, 0)
        sendUI(drawing.getAttributes())

def move_y_down(event):
    if drawing.objectSelected is not None:
        drawing.moveObject(0, -translationValue, 0)
        sendUI(drawing.getAttributes())

def scale_x_less(event):
    if drawing.objectSelected is not None:
        drawing.scaleObject(scaleLessValue, 1, 1)
        sendUI(drawing.getAttributes())

def scale_x_more(event):
    if drawing.objectSelected is not None:
        drawing.scaleObject(scaleMoreValue, 1, 1)
        sendUI(drawing.getAttributes())

def scale_z_less(event):
    if drawing.objectSelected is not None:
        drawing.scaleObject(1, 1, scaleLessValue)
        sendUI(drawing.getAttributes())

def scale_z_more(event):
    if drawing.objectSelected is not None:
        drawing.scaleObject(1, 1, scaleMoreValue)
        sendUI(drawing.getAttributes())

def scale_y_less(event):
    if drawing.objectSelected is not None:
        drawing.scaleObject(1, scaleLessValue, 1)
        sendUI(drawing.getAttributes())

def scale_y_more(event):
    if drawing.objectSelected is not None:
        drawing.scaleObject(1, scaleMoreValue, 1)
        sendUI(drawing.getAttributes())

def rot_x_left(event):
    if drawing.objectSelected is not None:
        drawing.rotateObjectX(-rotationValue)
        sendUI(drawing.getAttributes())

def rot_x_right(event):
    if drawing.objectSelected is not None:
        drawing.rotateObjectX(rotationValue)
        sendUI(drawing.getAttributes())

def rot_z_front(event):
    if drawing.objectSelected is not None:
        drawing.rotateObjectZ(rotationValue)
        sendUI(drawing.getAttributes())

def rot_z_back(event):
    if drawing.objectSelected is not None:
        drawing.rotateObjectZ(-rotationValue)
        sendUI(drawing.getAttributes())

def rot_y_up(event):
    if drawing.objectSelected is not None:
        drawing.rotateObjectY(rotationValue)
        sendUI(drawing.getAttributes())

def rot_y_down(event):
    if drawing.objectSelected is not None:
        drawing.rotateObjectY(-rotationValue)
        sendUI(drawing.getAttributes())

def clearObjectInfo():
    txtNumSides.delete(0, tk.END)
    txtHeight.delete(0, tk.END)
    txtBaseRadius.delete(0, tk.END)
    txtTopRadius.delete(0, tk.END)
    txtKaR.delete(0, tk.END)
    txtKaG.delete(0, tk.END)
    txtKaB.delete(0, tk.END)
    txtKdR.delete(0, tk.END)
    txtKdG.delete(0, tk.END)
    txtKdB.delete(0, tk.END)
    txtKsR.delete(0, tk.END)
    txtKsG.delete(0, tk.END)
    txtKsB.delete(0, tk.END)
    txtN.delete(0, tk.END)

def selectingObject(event):
    if drawing.canvas.find_withtag("current") and event.widget.gettags("current")[0] == "object":
        selected_object = drawing.objectSelection(drawing.canvas.find_withtag("current")[0])
        sendUI(drawing.getAttributes())
        txtNumSides['state'] = tk.DISABLED
        txtHeight['state'] = tk.DISABLED
        txtBaseRadius['state'] = tk.DISABLED
        txtTopRadius['state'] = tk.DISABLED
    else:
        drawing.objectSelected = None
        txtNumSides['state'] = tk.NORMAL
        txtHeight['state'] = tk.NORMAL
        txtBaseRadius['state'] = tk.NORMAL
        txtTopRadius['state'] = tk.NORMAL
        clearObjectInfo()
    #drawing.draw()
    drawing.Draw()
    buttonObject(0, 0, 0)

def updateObject():
    kaR = isEmpty(txtKaR.get())
    kaG = isEmpty(txtKaG.get())
    kaB = isEmpty(txtKaB.get())
    kdR = isEmpty(txtKdR.get())
    kdG = isEmpty(txtKdG.get())
    kdB = isEmpty(txtKdB.get())
    ksR = isEmpty(txtKsR.get())
    ksG = isEmpty(txtKsG.get())
    ksB = isEmpty(txtKsB.get())
    n = isEmpty(txtN.get())

    ka = [kaR, kaG, kaB]
    kd = [kdR, kdG, kdB]
    ks = [ksR, ksG, ksB]
    drawing.updateObject(ka, kd, ks, n)

def objectClick():
    numSides = int(isEmpty(txtNumSides.get()))
    height = isEmpty(txtHeight.get())
    baseRadius = isEmpty(txtBaseRadius.get())
    topRadius = isEmpty(txtTopRadius.get())
    kaR = isEmpty(txtKaR.get())
    kaG = isEmpty(txtKaG.get())
    kaB = isEmpty(txtKaB.get())
    kdR = isEmpty(txtKdR.get())
    kdG = isEmpty(txtKdG.get())
    kdB = isEmpty(txtKdB.get())
    ksR = isEmpty(txtKsR.get())
    ksG = isEmpty(txtKsG.get())
    ksB = isEmpty(txtKsB.get())
    n = isEmpty(txtN.get())

    if numSides == -1:
        messagebox.showerror("Error", "Fill in all fields!")
        return 0

    if int(height) == -1 or int(baseRadius) == -1 or int(topRadius) == -1 or int(kaR) == -1 or int(kaG) == -1 or \
       int(kaB) == -1 or int(kdR) == -1 or int(kdG) == -1 or int(kdB) == -1 or int(ksR) == -1 or int(ksG) == -1 or int(ksB) == -1 or int(n) == -1:
        messagebox.showerror("Error", "Fill in all fields!")
        return 0

    if numSides < 3:
        numSides = 3

    ka = [kaR, kaG, kaB]
    kd = [kdR, kdG, kdB]
    ks = [ksR, ksG, ksB]

    drawing.AddObjects(baseRadius, topRadius, numSides, height, ka, kd, ks, n)
    clearObjectInfo()

def projectionSet(values):
    txtVRPx.delete(0, tk.END)
    txtVRPx.insert(0, str(values[0]))
    txtVRPy.delete(0, tk.END)
    txtVRPy.insert(0, str(values[1]))
    txtVRPz.delete(0, tk.END)
    txtVRPz.insert(0, str(values[2]))
    txtPx.delete(0, tk.END)
    txtPx.insert(0, str(values[3]))
    txtPy.delete(0, tk.END)
    txtPy.insert(0, str(values[4]))
    txtPz.delete(0, tk.END)
    txtPz.insert(0, str(values[5]))
    txtViewUpx.delete(0, tk.END)
    txtViewUpx.insert(0, str(values[6]))
    txtViewUpy.delete(0, tk.END)
    txtViewUpy.insert(0, str(values[7]))
    txtViewUpz.delete(0, tk.END)
    txtViewUpz.insert(0, str(values[8]))
    txtNear.delete(0, tk.END)
    txtNear.insert(0, str(values[9]))
    txtFar.delete(0, tk.END)
    txtFar.insert(0, str(values[10]))
    txtProjectionPlane.delete(0, tk.END)
    txtProjectionPlane.insert(0, str(values[11]))
    txtWorldLimitsxMin.delete(0, tk.END)
    txtWorldLimitsxMin.insert(0, str(values[12]))
    txtWorldLimitsxMin.delete(0, tk.END)
    txtWorldLimitsxMin.insert(0, str(values[13]))
    txtWorldLimitsxMin.delete(0, tk.END)
    txtWorldLimitsyMin.insert(0, str(values[14]))
    txtWorldLimitsyMin.delete(0, tk.END)
    txtWorldLimitsyMin.insert(0, str(values[15]))
    txtViewportLimitsxMin.delete(0, tk.END)
    txtViewportLimitsxMin.insert(0, str(values[16]))
    txtViewportLimitsxMax.delete(0, tk.END)
    txtViewportLimitsxMax.insert(0, str(values[17]))
    txtViewportLimitsyMin.delete(0, tk.END)
    txtViewportLimitsyMin.insert(0, str(values[18]))
    txtViewportLimitsyMax.delete(0, tk.END)
    txtViewportLimitsyMax.insert(0, str(values[19]))
    txtIAR.delete(0, tk.END)
    txtIAR.insert(0, str(values[20][0]))
    txtIAG.delete(0, tk.END)
    txtIAG.insert(0, str(values[20][1]))
    txtIAB.delete(0, tk.END)
    txtIAB.insert(0, str(values[20][2]))
    txtIR.delete(0, tk.END)
    txtIR.insert(0, str(values[21][0]))
    txtIG.delete(0, tk.END)
    txtIG.insert(0, str(values[21][1]))
    txtIB.delete(0, tk.END)
    txtIB.insert(0, str(values[21][2]))
    txtIx.delete(0, tk.END)
    txtIx.insert(0, str(values[22][0]))
    txtIy.delete(0, tk.END)
    txtIy.insert(0, str(values[22][1]))
    txtIz.delete(0, tk.END)
    txtIz.insert(0, str(values[22][2]))

def projectionClick():
    # rbProjection = 0 -> perspective; rbProjection = 1 -> axonometric
    projection = bool(int(rbProjection.get()))
    vrpX = isEmpty(txtVRPx.get())
    vrpY = isEmpty(txtVRPy.get())
    vrpZ = isEmpty(txtVRPz.get())
    pX = isEmpty(txtPx.get())
    pY = isEmpty(txtPy.get())
    pZ = isEmpty(txtPz.get())
    viewUpX = isEmpty(txtViewUpx.get())
    viewUpY = isEmpty(txtViewUpy.get())
    viewUpZ = isEmpty(txtViewUpz.get())
    near = isEmpty(txtNear.get())
    far = isEmpty(txtFar.get())
    projectionPlane = isEmpty(txtProjectionPlane.get())
    worldLimitXMin = isEmpty(txtWorldLimitsxMin.get())
    worldLimitXMax = isEmpty(txtWorldLimitsxMax.get())
    worldLimitYMin = isEmpty(txtWorldLimitsyMin.get())
    worldLimitYMax = isEmpty(txtWorldLimitsyMax.get())
    projPlaneLimitXMin = isEmpty(txtViewportLimitsxMin.get())
    projPlaneLimitXMax = isEmpty(txtViewportLimitsxMax.get())
    projPlaneLimitYMin = isEmpty(txtViewportLimitsyMin.get())
    projPlaneLimitYMax = isEmpty(txtViewportLimitsyMax.get())

    #drawing.redoPipeline(projection, vrpX, vrpY, vrpZ, pX, pY, pZ, viewUpX, viewUpY, viewUpZ, near, far, projectionPlane,
    #                     worldLimitXMin, worldLimitXMax, worldLimitYMin, worldLimitYMax, projPlaneLimitXMin, projPlaneLimitXMax, projPlaneLimitYMin, projPlaneLimitYMax)
    drawing.RedoPipeline(projection, vrpX, vrpY, vrpZ, pX, pY, pZ, viewUpX, viewUpY, viewUpZ, near, far, projectionPlane,
                         worldLimitXMin, worldLimitXMax, worldLimitYMin, worldLimitYMax, projPlaneLimitXMin, projPlaneLimitXMax, projPlaneLimitYMin, projPlaneLimitYMax)

    projectionSet(drawing.getProjection())
    updateAxes()

def illuminationClick():
    # shading = 0 -> constant; shading = 1 -> Gouraud; shading = 2 -> Phong
    shading = int(rbShading.get())
    iaR = isEmpty(txtIAR.get())
    iaG = isEmpty(txtIAG.get())
    iaB = isEmpty(txtIAB.get())
    iR = isEmpty(txtIR.get())
    iG = isEmpty(txtIG.get())
    iB = isEmpty(txtIB.get())
    iX = isEmpty(txtIx.get())
    iY = isEmpty(txtIy.get())
    iZ = isEmpty(txtIz.get())

    ila = [iaR, iaG, iaB]
    il = [iR, iG, iB]
    lightSource = np.array([iX, iY, iZ])

    #drawing.changeIllumination(shading, ila, il, lightSource)
    drawing.ChangeIllumination(shading, ila, il, lightSource)

def isEmpty(string):
    if string == "":
        return -1
    return float(string)

def updateAxes():
    #axesPosition = drawing.getAxesPosition()
    axesPosition = drawing.PosEixos()
    axisx = axesPosition[0]
    axisy = axesPosition[1]
    axisz = axesPosition[2]
    axisX.place(x=axisx[0], y=axisx[1]-20)
    axisY.place(x=axisy[0], y=axisy[1]-20)
    axisZ.place(x=axisz[0], y=axisz[1]-20)

if __name__ == "__main__":
    window = tk.Tk()
    window.title('The Marvelous Polygoneer')
    width = 1280
    height = 750
    window.geometry('{}x{}+{}+{}'.format(1280, 690, 0, 0))
    window.resizable(0, 0)
    
    # Creating Frames
    frameDrawingInterface = tk.Frame(window, highlightbackground="black", highlightthickness=1, width=int(width*0.7), height=int(height*0.88))
    frameDrawingInterface.place(x=int(width*0.01), y=int(height * 0.01))

    userInterface = tk.Frame(window, highlightbackground="black", highlightthickness=1, width=300, height=int(height*0.9))
    userInterface.place(x=width-310, y=int(height * 0.01))
    userInterface.pack_propagate(0)

    # Creating Canvas
    drawing = Screen(frameDrawingInterface, width-(330+width*0.01), height-20) 
    drawing.canvas.pack()

    btnLimpar = ttk.Button(window, text="Limpar", width=15, command=clearScreen, cursor="hand2") 
    btnLimpar.place(x=width-(410+width*0.01), y=int(height * 0.88))

    txtIntegrantes = ttk.Label(window, text='Desenvolvido por: Lucas Veit, Mateus Karvat e Roberta Alcantara')
    txtIntegrantes.place(x=10,  y=int(height * 0.89))

    drawing.canvas.bind('<Button-1>', selectingObject)

    drawing.canvas.bind_all('<q>', move_x_left)
    drawing.canvas.bind_all('<a>', move_x_right)
    drawing.canvas.bind_all('<w>', move_z_front)
    drawing.canvas.bind_all('<s>', move_z_back)
    drawing.canvas.bind_all('<e>', move_y_up)
    drawing.canvas.bind_all('<d>', move_y_down)

    drawing.canvas.bind_all('<r>', scale_x_less)
    drawing.canvas.bind_all('<f>', scale_x_more)
    drawing.canvas.bind_all('<t>', scale_z_less)
    drawing.canvas.bind_all('<g>', scale_z_more)
    drawing.canvas.bind_all('<y>', scale_y_less)
    drawing.canvas.bind_all('<h>', scale_y_more)

    drawing.canvas.bind_all('<u>', rot_x_left)
    drawing.canvas.bind_all('<j>', rot_x_right)
    drawing.canvas.bind_all('<i>', rot_z_front)
    drawing.canvas.bind_all('<k>', rot_z_back)
    drawing.canvas.bind_all('<o>', rot_y_up)
    drawing.canvas.bind_all('<l>', rot_y_down)

    rbProjection = tk.IntVar()
    rbProjection.set(0)
    rbShading = tk.IntVar()
    rbShading.set(0)
    textNumSides = tk.StringVar()
    textNumSides.set("")

    t = ToggledFrame(userInterface, width, height, text='Object Information', relief="raised", borderwidth=1)
    t.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    labelBaseRadius = ttk.Label(t.sub_frame, text='Base Radius')
    txtBaseRadius = ttk.Entry(t.sub_frame, name="txtBaseRadius", width=15)
    labelTopRadius = ttk.Label(t.sub_frame, text='Top Radius')
    txtTopRadius = ttk.Entry(t.sub_frame, name="txtTopRadius", width=15)
    labelNumSides = ttk.Label(t.sub_frame, text='Number of Sides')
    txtNumSides = ttk.Entry(t.sub_frame, name="txtNumSides", width=15, textvariable=textNumSides)
    labelHeight = ttk.Label(t.sub_frame, text='Height')
    txtHeight = ttk.Entry(t.sub_frame, name="txtHeight", width=15)
    btnCreateObject = ttk.Button(t.sub_frame, text="Create Object", width=15, command=objectClick)
    btnUpdateObject = ttk.Button(t.sub_frame, text="Update Object", width=15, command=updateObject)

    labelN = ttk.Label(t.sub_frame, text='n')
    txtN = ttk.Entry(t.sub_frame, name="n", width=15)

    labelKa = ttk.Label(t.sub_frame, text="Ka*", font="-weight bold -size 9", cursor="hand2")
    labelKaR = ttk.Label(t.sub_frame, text='R')
    txtKaR = ttk.Entry(t.sub_frame, name="kaR", width=15)
    labelKaG = ttk.Label(t.sub_frame, text='G')
    txtKaG = ttk.Entry(t.sub_frame, name="kaG", width=15)
    labelKaB = ttk.Label(t.sub_frame, text='B')
    txtKaB = ttk.Entry(t.sub_frame, name="kaB", width=15)

    labelKd = ttk.Label(t.sub_frame, text="Kd*", font="-weight bold -size 9", cursor="hand2")
    labelKdR = ttk.Label(t.sub_frame, text='R')
    txtKdR = ttk.Entry(t.sub_frame, name="kdR", width=15)
    labelKdG = ttk.Label(t.sub_frame, text='G')
    txtKdG = ttk.Entry(t.sub_frame, name="kdG", width=15)
    labelKdB = ttk.Label(t.sub_frame, text='B')
    txtKdB = ttk.Entry(t.sub_frame, name="kdB", width=15)

    labelKs = ttk.Label(t.sub_frame, text="Ks*", font="-weight bold -size 9", cursor="hand2")
    labelKsR = ttk.Label(t.sub_frame, text='R')
    txtKsR = ttk.Entry(t.sub_frame, name="ksR", width=15)
    labelKsG = ttk.Label(t.sub_frame, text='G')
    txtKsG = ttk.Entry(t.sub_frame, name="ksG", width=15)
    labelKsB = ttk.Label(t.sub_frame, text='B')
    txtKsB = ttk.Entry(t.sub_frame, name="ksB", width=15)

    labelNumSides.grid(row=1, column=1, padx=10, pady=1)
    txtNumSides.grid(row=1, column=2, padx=1, pady=1)
    labelBaseRadius.grid(row=2, column=1, padx=1, pady=1)
    txtBaseRadius.grid(row=2, column=2, padx=1, pady=1)
    labelTopRadius.grid(row=3, column=1, padx=1, pady=1)
    txtTopRadius.grid(row=3, column=2, padx=1, pady=1)
    labelHeight.grid(row=5, column=1, padx=1, pady=1)
    txtHeight.grid(row=5, column=2, padx=1, pady=1)

    labelN.grid(row=6, column=1, padx=1, pady=1)
    txtN.grid(row=6, column=2, padx=1, pady=1)
    labelKa.grid(row=7, column=1, padx=10, pady=2, sticky=W)
    labelKaR.grid(row=8, column=1, padx=1, pady=1)
    txtKaR.grid(row=8, column=2, padx=1, pady=1)
    labelKaG.grid(row=9, column=1, padx=1, pady=1)
    txtKaG.grid(row=9, column=2, padx=1, pady=1)
    labelKaB.grid(row=10, column=1, padx=1, pady=1)
    txtKaB.grid(row=10, column=2, padx=1, pady=1)

    labelKd.grid(row=11, column=1, padx=10, pady=2, sticky=W)
    labelKdR.grid(row=12, column=1, padx=1, pady=1)
    txtKdR.grid(row=12, column=2, padx=1, pady=1)
    labelKdG.grid(row=13, column=1, padx=1, pady=1)
    txtKdG.grid(row=13, column=2, padx=1, pady=1)
    labelKdB.grid(row=14, column=1, padx=1, pady=1)
    txtKdB.grid(row=14, column=2, padx=1, pady=1)

    labelKs.grid(row=15, column=1, padx=10, pady=2, sticky=W)
    labelKsR.grid(row=16, column=1, padx=1, pady=1)
    txtKsR.grid(row=16, column=2, padx=1, pady=1)
    labelKsG.grid(row=17, column=1, padx=1, pady=1)
    txtKsG.grid(row=17, column=2, padx=1, pady=1)
    labelKsB.grid(row=18, column=1, padx=1, pady=1)
    txtKsB.grid(row=18, column=2, padx=1, pady=1)

    btnCreateObject.grid(row=19, column=1, padx=4, pady=8)
    btnUpdateObject.grid(row=19, column=2, padx=4, pady=8)

    tipKa = CreateToolTip(labelKa, "Values between 0 and 255")
    tipKd = CreateToolTip(labelKd, "Values between 0 and 255")
    tipKs = CreateToolTip(labelKs, "Values between 0 and 255")

    textNumSides.trace('w', buttonObject)
    t2 = ToggledFrame(userInterface, width, height, text='Projection', relief="raised", borderwidth=1)
    t2.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    labelProjectionType = ttk.Label(t2.sub_frame, text="Projection Type", font="-weight bold -size 9")
    rbAxonometric = ttk.Radiobutton(t2.sub_frame, text="Axonometric", variable=rbProjection, value=0, cursor="hand2")
    rbPerspective = ttk.Radiobutton(t2.sub_frame, text="Perspective", variable=rbProjection, value=1, cursor="hand2")

    labelVRP = ttk.Label(t2.sub_frame, text="VRP", font="-weight bold -size 9")
    labelVRPx = ttk.Label(t2.sub_frame, text="X")
    txtVRPx = ttk.Entry(t2.sub_frame, name="txtVRPx", width=15)
    labelVRPy = ttk.Label(t2.sub_frame, text="Y")
    txtVRPy= ttk.Entry(t2.sub_frame, name="txtVRPy", width=15)
    labelVRPz = ttk.Label(t2.sub_frame, text="Z")
    txtVRPz = ttk.Entry(t2.sub_frame, name="txtVRPz", width=15)

    labelP = ttk.Label(t2.sub_frame, text="Vector P", font="-weight bold -size 9")
    labelPx = ttk.Label(t2.sub_frame, text="X")
    txtPx = ttk.Entry(t2.sub_frame, name="txtPx", width=15)
    labelPy = ttk.Label(t2.sub_frame, text="Y")
    txtPy= ttk.Entry(t2.sub_frame, name="txtPy", width=15)
    labelPz = ttk.Label(t2.sub_frame, text="Z")
    txtPz = ttk.Entry(t2.sub_frame, name="txtPz", width=15)

    labelViewUp = ttk.Label(t2.sub_frame, text="View-up Vector", font="-weight bold -size 9")
    labelViewUpx = ttk.Label(t2.sub_frame, text="X")
    txtViewUpx = ttk.Entry(t2.sub_frame, name="txtViewUpx", width=15)
    labelViewUpy = ttk.Label(t2.sub_frame, text="Y")
    txtViewUpy= ttk.Entry(t2.sub_frame, name="txtViewUpy", width=15)
    labelViewUpz = ttk.Label(t2.sub_frame, text="Z")
    txtViewUpz = ttk.Entry(t2.sub_frame, name="txtViewUpz", width=15)

    labelDistances = ttk.Label(t2.sub_frame, text="Distances", font="-weight bold -size 9")
    labelNear = ttk.Label(t2.sub_frame, text="Near Plane")
    txtNear = ttk.Entry(t2.sub_frame, name="txtNear", width=15)
    labelFar = ttk.Label(t2.sub_frame, text="Far Plane")
    txtFar= ttk.Entry(t2.sub_frame, name="txtFar", width=15)
    labelProjectionPlane = ttk.Label(t2.sub_frame, text="Projection Plane")
    txtProjectionPlane = ttk.Entry(t2.sub_frame, name="txtProjectionPlane", width=15)

    labelWorldLimits = ttk.Label(t2.sub_frame, text="Window Limits", font="-weight bold -size 9")
    labelWorldLimitsxMin = ttk.Label(t2.sub_frame, text="X min")
    txtWorldLimitsxMin = ttk.Entry(t2.sub_frame, name="txtWorldLimitsxMin", width=15)
    labelWorldLimitsxMax = ttk.Label(t2.sub_frame, text="X max")
    txtWorldLimitsxMax = ttk.Entry(t2.sub_frame, name="txtWorldLimitsxMax", width=15)
    labelWorldLimitsyMin = ttk.Label(t2.sub_frame, text="Y min")
    txtWorldLimitsyMin = ttk.Entry(t2.sub_frame, name="txtWorldLimitsyMin", width=15)
    labelWorldLimitsyMax = ttk.Label(t2.sub_frame, text="Y max")
    txtWorldLimitsyMax = ttk.Entry(t2.sub_frame, name="txtWorldLimitsyMax", width=15)

    labelViewportLimits = ttk.Label(t2.sub_frame, text="Viewport Limits", font="-weight bold -size 9")
    labelViewportLimitsxMin = ttk.Label(t2.sub_frame, text="X min*", cursor="hand2")
    txtViewportLimitsxMin = ttk.Entry(t2.sub_frame, name="txtViewportLimitsxMin", width=15)
    labelViewportLimitsxMax = ttk.Label(t2.sub_frame, text="X max*", cursor="hand2")
    txtViewportLimitsxMax = ttk.Entry(t2.sub_frame, name="txtViewportLimitsxMax", width=15)
    labelViewportLimitsyMin = ttk.Label(t2.sub_frame, text="Y min*", cursor="hand2")
    txtViewportLimitsyMin = ttk.Entry(t2.sub_frame, name="txtViewportLimitsyMin", width=15)
    labelViewportLimitsyMax = ttk.Label(t2.sub_frame, text="Y max*", cursor="hand2")
    txtViewportLimitsyMax = ttk.Entry(t2.sub_frame, name="txtViewportLimitsyMax", width=15)
    btnChangeScene = ttk.Button(t2.sub_frame, text="Change Scene", width=15, command=projectionClick, cursor="hand2")

    tipViewportXmin = CreateToolTip(labelViewportLimitsxMin, "Values >= 0")
    tipViewportXmax = CreateToolTip(labelViewportLimitsxMax, "Values >=0 and <=937")
    tipViewportYmin = CreateToolTip(labelViewportLimitsyMin, "Values >= 0")
    tipViewportYmax = CreateToolTip(labelViewportLimitsyMax, "Values >=0 and <=642")

    labelProjectionType.grid(row=1, column=1, padx=1, pady=2)
    rbAxonometric.grid(row=2, column=1, padx=5, pady=2)
    rbPerspective.grid(row=2, column=2, padx=5, pady=2)

    labelVRP.grid(row=3, column=1, padx=10, pady=2, sticky=W)
    labelVRPx.grid(row=4, column=1, padx=1, pady=1)
    txtVRPx.grid(row=4, column=2, padx=1, pady=1)
    labelVRPy.grid(row=5, column=1, padx=1, pady=1)
    txtVRPy.grid(row=5, column=2, padx=1, pady=1)
    labelVRPz.grid(row=6, column=1, padx=1, pady=1)
    txtVRPz.grid(row=6, column=2, padx=1, pady=1)

    labelP.grid(row=7, column=1, padx=10, pady=2, sticky=W)
    labelPx.grid(row=8, column=1, padx=1, pady=1)
    txtPx.grid(row=8, column=2, padx=1, pady=1)
    labelPy.grid(row=9, column=1, padx=1, pady=1)
    txtPy.grid(row=9, column=2, padx=1, pady=1)
    labelPz.grid(row=10, column=1, padx=1, pady=1)
    txtPz.grid(row=10, column=2, padx=1, pady=1)

    labelViewUp.grid(row=11, column=1, padx=10, pady=2, sticky=W)
    labelViewUpx.grid(row=12, column=1, padx=1, pady=1)
    txtViewUpx.grid(row=12, column=2, padx=1, pady=1)
    labelViewUpy.grid(row=13, column=1, padx=1, pady=1)
    txtViewUpy.grid(row=13, column=2, padx=1, pady=1)
    labelViewUpz.grid(row=14, column=1, padx=1, pady=1)
    txtViewUpz.grid(row=14, column=2, padx=1, pady=1)

    labelDistances.grid(row=15, column=1, padx=10, pady=2, sticky=W)
    labelNear.grid(row=16, column=1, padx=1, pady=1)
    txtNear.grid(row=16, column=2, padx=1, pady=1)
    labelFar.grid(row=17, column=1, padx=1, pady=1)
    txtFar.grid(row=17, column=2, padx=1, pady=1)
    labelProjectionPlane.grid(row=18, column=1, padx=1, pady=1)
    txtProjectionPlane.grid(row=18, column=2, padx=1, pady=1)

    labelWorldLimits.grid(row=19, column=1, padx=10, pady=4, sticky=W)
    labelWorldLimitsxMin.grid(row=20, column=1, padx=1, pady=1)
    txtWorldLimitsxMin.grid(row=20, column=2, padx=1, pady=1)
    labelWorldLimitsxMax.grid(row=21, column=1, padx=1, pady=1)
    txtWorldLimitsxMax.grid(row=21, column=2, padx=1, pady=1)
    labelWorldLimitsyMin.grid(row=22, column=1, padx=1, pady=1)
    txtWorldLimitsyMin.grid(row=22, column=2, padx=1, pady=1)
    labelWorldLimitsyMax.grid(row=23, column=1, padx=1, pady=1)
    txtWorldLimitsyMax.grid(row=23, column=2, padx=1, pady=1)

    labelViewportLimits.grid(row=24, column=1, padx=10, pady=4, sticky=W)
    labelViewportLimitsxMin.grid(row=25, column=1, padx=1, pady=1)
    txtViewportLimitsxMin.grid(row=25, column=2, padx=1, pady=1)
    labelViewportLimitsxMax.grid(row=26, column=1, padx=1, pady=1)
    txtViewportLimitsxMax.grid(row=26, column=2, padx=1, pady=1)
    labelViewportLimitsyMin.grid(row=27, column=1, padx=1, pady=1)
    txtViewportLimitsyMin.grid(row=27, column=2, padx=1, pady=1)
    labelViewportLimitsyMax.grid(row=28, column=1, padx=1, pady=1)
    txtViewportLimitsyMax.grid(row=28, column=2, padx=1, pady=1)
    btnChangeScene.grid(row=29, column=1, padx=4, pady=8, columnspan=2)

    labelViewportLimits = ttk.Label(t2.sub_frame, text="Viewport Limits", font="-weight bold -size 9")
    labelViewportLimitsxMin = ttk.Label(t2.sub_frame, text="X min*", cursor="hand2")
    txtViewportLimitsxMin = ttk.Entry(t2.sub_frame, name="txtViewportLimitsxMin", width=15)
    labelViewportLimitsxMax = ttk.Label(t2.sub_frame, text="X max*", cursor="hand2")
    txtViewportLimitsxMax = ttk.Entry(t2.sub_frame, name="txtViewportLimitsxMax", width=15)
    labelViewportLimitsyMin = ttk.Label(t2.sub_frame, text="Y min*", cursor="hand2")
    txtViewportLimitsyMin = ttk.Entry(t2.sub_frame, name="txtViewportLimitsyMin", width=15)
    labelViewportLimitsyMax = ttk.Label(t2.sub_frame, text="Y max*", cursor="hand2")
    txtViewportLimitsyMax = ttk.Entry(t2.sub_frame, name="txtViewportLimitsyMax", width=15)
    btnChangeScene = ttk.Button(t2.sub_frame, text="Change Scene", width=15, command=projectionClick, cursor="hand2")

    tipViewportXmin = CreateToolTip(labelViewportLimitsxMin, "Values >= 0")
    tipViewportXmax = CreateToolTip(labelViewportLimitsxMax, "Values >=0 and <=937")
    tipViewportYmin = CreateToolTip(labelViewportLimitsyMin, "Values >= 0")
    tipViewportYmax = CreateToolTip(labelViewportLimitsyMax, "Values >=0 and <=642")

    # Assuming these variables are defined and configured elsewhere
    labelProjectionType.grid(row=1, column=1, padx=1, pady=2)
    rbAxonometric.grid(row=2, column=1, padx=5, pady=2)
    rbPerspective.grid(row=2, column=2, padx=5, pady=2)

    labelVRP.grid(row=3, column=1, padx=10, pady=2, sticky=W)
    labelVRPx.grid(row=4, column=1, padx=1, pady=1)
    txtVRPx.grid(row=4, column=2, padx=1, pady=1)
    labelVRPy.grid(row=5, column=1, padx=1, pady=1)
    txtVRPy.grid(row=5, column=2, padx=1, pady=1)
    labelVRPz.grid(row=6, column=1, padx=1, pady=1)
    txtVRPz.grid(row=6, column=2, padx=1, pady=1)

    labelP.grid(row=7, column=1, padx=10, pady=2, sticky=W)
    labelPx.grid(row=8, column=1, padx=1, pady=1)
    txtPx.grid(row=8, column=2, padx=1, pady=1)
    labelPy.grid(row=9, column=1, padx=1, pady=1)
    txtPy.grid(row=9, column=2, padx=1, pady=1)
    labelPz.grid(row=10, column=1, padx=1, pady=1)
    txtPz.grid(row=10, column=2, padx=1, pady=1)

    labelViewUp.grid(row=11, column=1, padx=10, pady=2, sticky=W)
    labelViewUpx.grid(row=12, column=1, padx=1, pady=1)
    txtViewUpx.grid(row=12, column=2, padx=1, pady=1)
    labelViewUpy.grid(row=13, column=1, padx=1, pady=1)
    txtViewUpy.grid(row=13, column=2, padx=1, pady=1)
    labelViewUpz.grid(row=14, column=1, padx=1, pady=1)
    txtViewUpz.grid(row=14, column=2, padx=1, pady=1)

    labelDistances.grid(row=15, column=1, padx=10, pady=2, sticky=W)
    labelNear.grid(row=16, column=1, padx=1, pady=1)
    txtNear.grid(row=16, column=2, padx=1, pady=1)
    labelFar.grid(row=17, column=1, padx=1, pady=1)
    txtFar.grid(row=17, column=2, padx=1, pady=1)
    labelProjectionPlane.grid(row=18, column=1, padx=1, pady=1)
    txtProjectionPlane.grid(row=18, column=2, padx=1, pady=1)

    labelWorldLimits.grid(row=19, column=1, padx=10, pady=4, sticky=W)
    labelWorldLimitsxMin.grid(row=20, column=1, padx=1, pady=1)
    txtWorldLimitsxMin.grid(row=20, column=2, padx=1, pady=1)
    labelWorldLimitsxMax.grid(row=21, column=1, padx=1, pady=1)
    txtWorldLimitsxMax.grid(row=21, column=2, padx=1, pady=1)
    labelWorldLimitsyMin.grid(row=22, column=1, padx=1, pady=1)
    txtWorldLimitsyMin.grid(row=22, column=2, padx=1, pady=1)
    labelWorldLimitsyMax.grid(row=23, column=1, padx=1, pady=1)
    txtWorldLimitsyMax.grid(row=23, column=2, padx=1, pady=1)

    labelViewportLimits.grid(row=24, column=1, padx=10, pady=4, sticky=W)
    labelViewportLimitsxMin.grid(row=25, column=1, padx=1, pady=1)
    txtViewportLimitsxMin.grid(row=25, column=2, padx=1, pady=1)
    labelViewportLimitsxMax.grid(row=26, column=1, padx=1, pady=1)
    txtViewportLimitsxMax.grid(row=26, column=2, padx=1, pady=1)
    labelViewportLimitsyMin.grid(row=27, column=1, padx=1, pady=1)
    txtViewportLimitsyMin.grid(row=27, column=2, padx=1, pady=1)
    labelViewportLimitsyMax.grid(row=28, column=1, padx=1, pady=1)
    txtViewportLimitsyMax.grid(row=28, column=2, padx=1, pady=1)
    btnChangeScene.grid(row=29, column=1, padx=4, pady=8, columnspan=2)

    rbProjection.trace('w', readRadioButton)

    t3 = ToggledFrame(userInterface, width, height, text='Lighting and Shading', relief="raised", borderwidth=1)
    t3.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    labelIllumination = ttk.Label(t3.sub_frame, text="Illumination", font="-weight bold -size 9")

    labelAmbientLight = ttk.Label(t3.sub_frame, text="Ambient Light*", font="-weight bold -size 9", cursor="hand2")
    labelIAR = ttk.Label(t3.sub_frame, text='R')
    txtIAR = ttk.Entry(t3.sub_frame, name="iaR", width=15)
    labelIAG = ttk.Label(t3.sub_frame, text='G')
    txtIAG = ttk.Entry(t3.sub_frame, name="iaG", width=15)
    labelIAB = ttk.Label(t3.sub_frame, text='B')
    txtIAB = ttk.Entry(t3.sub_frame, name="iaB", width=15)

    labelLightSource = ttk.Label(t3.sub_frame, text="Light Source*", font="-weight bold -size 9", cursor="hand2")
    labelIR = ttk.Label(t3.sub_frame, text='R')
    txtIR = ttk.Entry(t3.sub_frame, name="iR", width=15)
    labelIG = ttk.Label(t3.sub_frame, text='G')
    txtIG = ttk.Entry(t3.sub_frame, name="iG", width=15)
    labelIB = ttk.Label(t3.sub_frame, text='B')
    txtIB = ttk.Entry(t3.sub_frame, name="iB", width=15)

    labelLightSourcePos = ttk.Label(t3.sub_frame, text="Light Source Coordinates", font="-weight bold -size 9")
    labelIx = ttk.Label(t3.sub_frame, text='x')
    txtIx = ttk.Entry(t3.sub_frame, name="ix", width=15)
    labelIy = ttk.Label(t3.sub_frame, text='y')
    txtIy = ttk.Entry(t3.sub_frame, name="iy", width=15)
    labelIz = ttk.Label(t3.sub_frame, text='z')
    txtIz = ttk.Entry(t3.sub_frame, name="iz", width=15)

    labelShadingType = ttk.Label(t3.sub_frame, text="Shading Type", font="-weight bold -size 9")
    rbConstant = ttk.Radiobutton(t3.sub_frame, text="Constant", variable=rbShading, value=0, cursor="hand2")
    rbGouraud = ttk.Radiobutton(t3.sub_frame, text="Gouraud", variable=rbShading, value=1, cursor="hand2")
    rbPhong = ttk.Radiobutton(t3.sub_frame, text="Phong", variable=rbShading, value=2, cursor="hand2")
    btnChangeLighting = ttk.Button(t3.sub_frame,text="Change Illum/Shad", width=20, command=illuminationClick, cursor="hand2")

    rbGouraud['state'] = tk.DISABLED
    rbPhong['state'] = tk.DISABLED

    tipAmbientLight = CreateToolTip(labelAmbientLight, "Values between 0 and 255")
    tipLightSource = CreateToolTip(labelLightSource, "Values between 0 and 255")

    labelShadingType.grid(row=1, column=1, padx=12, pady=4, sticky=W)
    rbConstant.grid(row=2, column=1, padx=25, pady=1, sticky=W)
    rbGouraud.grid(row=3, column=1, padx=25, pady=1, sticky=W)
    rbPhong.grid(row=4, column=1, padx=25, pady=1, sticky=W)

    labelAmbientLight.grid(row=5, column=1, padx=10, pady=2, sticky=W)
    labelIAR.grid(row=6, column=1, padx=1, pady=1)
    txtIAR.grid(row=6, column=2, padx=1, pady=1)
    labelIAG.grid(row=7, column=1, padx=1, pady=1)
    txtIAG.grid(row=7, column=2, padx=1, pady=1)
    labelIAB.grid(row=8, column=1, padx=1, pady=1)
    txtIAB.grid(row=8, column=2, padx=1, pady=1)

    labelLightSource.grid(row=9, column=1, padx=10, pady=2, sticky=W)
    labelIR.grid(row=10, column=1, padx=1, pady=1)
    txtIR.grid(row=10, column=2, padx=1, pady=1)
    labelIG.grid(row=11, column=1, padx=1, pady=1)
    txtIG.grid(row=11, column=2, padx=1, pady=1)
    labelIB.grid(row=12, column=1, padx=1, pady=1)
    txtIB.grid(row=12, column=2, padx=1, pady=1)
    labelLightSourcePos.grid(row=13, column=1, padx=10, pady=2, sticky=W)
    labelIx.grid(row=14, column=1, padx=1, pady=1)
    txtIx.grid(row=14, column=2, padx=1, pady=1)
    labelIy.grid(row=15, column=1, padx=1, pady=1)
    txtIy.grid(row=15, column=2, padx=1, pady=1)
    labelIz.grid(row=16, column=1, padx=1, pady=1)
    txtIz.grid(row=16, column=2, padx=1, pady=1)

    btnChangeLighting.grid(row=17, column=1, padx=4, pady=8, columnspan=2)

    buttonObject(1, 1, 1)
    projectionSet(drawing.GetProjecao())

    txtPx['state'] = tk.DISABLED
    txtPy['state'] = tk.DISABLED
    txtPz['state'] = tk.DISABLED

    axisX = ttk.Label(frameDrawingInterface, text="X", foreground="#FF0000", background="#CCCCCC")
    axisY = ttk.Label(frameDrawingInterface, text="Y", foreground="#00FF00", background="#CCCCCC")
    axisZ = ttk.Label(frameDrawingInterface, text="Z", foreground="#0000FF", background="#CCCCCC")

    updateAxes()

    window.mainloop()