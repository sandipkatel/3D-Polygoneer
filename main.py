
from tooltip import CreateToolTip
import numpy as np
from Screen import Screen
import tkinter as tk
from tkinter import Frame, ttk, messagebox
from tkinter.constants import W
from frames import ToggledFrame
from RGBSlider import RGBSliderApp


def readRadiusButton(_, __, ___):
    if (rbProjection.get() == 0):
        txtPx['state'] = tk.DISABLED
        txtPy['state'] = tk.DISABLED
        txtPz['state'] = tk.DISABLED
    else:
        txtPx['state'] = tk.NORMAL
        txtPy['state'] = tk.NORMAL
        txtPz['state'] = tk.NORMAL


def buttonObject(_, __, ___):
    if (drawing.objectSelected is not None):
        btnUpdateObject['state'] = tk.NORMAL
        btnUpdateObject['cursor'] = "hand2"
        btnCreateObject['state'] = tk.DISABLED
        btnCreateObject['cursor'] = "arrow"
    else:
        btnUpdateObject['state'] = tk.DISABLED
        btnUpdateObject['cursor'] = "arrow"
        btnCreateObject['state'] = tk.NORMAL
        btnCreateObject['cursor'] = "hand2"


def ClearScreen():
    drawing.ClearAll()


def SendUI(values):
    txtNumSides.delete(0, tk.END)
    txtNumSides.insert(0, str(values[0]))
    txtBaseRadius.delete(0, tk.END)
    txtBaseRadius.insert(0, str(values[1]))
    txtTopRadius.delete(0, tk.END)
    txtTopRadius.insert(0, str(values[2]))
    txtHeight.delete(0, tk.END)
    txtHeight.insert(0, str(values[3]))

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


def SelectingObject(event):
    if drawing.canvas.find_withtag("current") and event.widget.gettags("current")[0] == "object":
        object = drawing.ObjectSelection(
            drawing.canvas.find_withtag("current")[0])
        SendUI(drawing.GetAttributes())
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

    ka = [kaR, kaG, kaB]
    kd = [kdR, kdG, kdB]
    ks = [ksR, ksG, ksB]
    drawing.UpdateObject(ka, kd, ks)


def objectClick():
    NumSides = int(isEmpty(txtNumSides.get()))
    Height = isEmpty(txtHeight.get())
    BaseRadius = isEmpty(txtBaseRadius.get())
    TopRadius = isEmpty(txtTopRadius.get())
    kaR = isEmpty(txtKaR.get())
    kaG = isEmpty(txtKaG.get())
    kaB = isEmpty(txtKaB.get())
    kdR = isEmpty(txtKdR.get())
    kdG = isEmpty(txtKdG.get())
    kdB = isEmpty(txtKdB.get())
    ksR = isEmpty(txtKsR.get())
    ksG = isEmpty(txtKsG.get())
    ksB = isEmpty(txtKsB.get())

    if (NumSides == -1):
        messagebox.showerror("Error", "Fill in all fields!")
        return 0

    if (int(Height) == -1 or int(BaseRadius) == -1 or int(TopRadius) == -1 or int(kaR) == -1 or int(kaG) == -1 or
    int(kaB) == -1 or int(kdR) == -1 or int(kdG) == -1 or int(kdB) == -1 or int(ksR) == -1 or int(ksG) == -1 or int(ksB) == -1):
        messagebox.showerror("Error", "Fill in all fields!")
        return 0

    if (NumSides < 3):
        NumSides = 3

    ka = [kaR, kaG, kaB]
    kd = [kdR, kdG, kdB]
    ks = [ksR, ksG, ksB]

    drawing.AddObjects(BaseRadius, TopRadius, NumSides, Height, ka, kd, ks)
    clearObjectInfo()


def ProjectionSet(values):
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
    txtWorldLimitsxMax.delete(0, tk.END)
    txtWorldLimitsxMax.insert(0, str(values[13]))
    txtWorldLimitsyMin.delete(0, tk.END)
    txtWorldLimitsyMin.insert(0, str(values[14]))
    txtWorldLimitsyMax.delete(0, tk.END)
    txtWorldLimitsyMax.insert(0, str(values[15]))
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


def ProjectionClick():
    # rbProjection = 0 -> perspectiva; rbProjection = 1 -> axonometrica
    Projection = bool(int(rbProjection.get()))
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
    planoProj = isEmpty(txtProjectionPlane.get())
    mundoxMin = isEmpty(txtWorldLimitsxMin.get())
    mundoxMax = isEmpty(txtWorldLimitsxMax.get())
    mundoyMin = isEmpty(txtWorldLimitsyMin.get())
    mundoyMax = isEmpty(txtWorldLimitsyMax.get())
    planoProjxMin = isEmpty(txtViewportLimitsxMin.get())
    planoProjxMax = isEmpty(txtViewportLimitsxMax.get())
    planoProjyMin = isEmpty(txtViewportLimitsyMin.get())
    planoProjyMax = isEmpty(txtViewportLimitsyMax.get())

    drawing.RedoPipeline(Projection, vrpX, vrpY, vrpZ, pX, pY, pZ, viewUpX, viewUpY, viewUpZ, near, far, planoProj,
                         mundoxMin, mundoxMax, mundoyMin, mundoyMax, planoProjxMin, planoProjxMax, planoProjyMin, planoProjyMax)

    ProjectionSet(drawing.GetProjection())
    updateAxes()


def iluminacaoClick():
    # Shading = 0 -> Constant; Shading = 1 -> gourad; Shading = 2 -> phong
    Shading = int(rbShading.get())
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
    fonteLuz = np.array([iX, iY, iZ])

    drawing.ChangeIlumination(Shading, ila, il, fonteLuz)


def isEmpty(string):
    if (string == ""):
        return -1
    return float(string)


def updateAxes():
    posicaoEixos = drawing.PosEixos()
    eixoX = posicaoEixos[0]
    eixoY = posicaoEixos[1]
    eixoZ = posicaoEixos[2]
    axisX.place(x=eixoX[0], y=eixoX[1]-20)
    axisY.place(x=eixoY[0], y=eixoY[1]-20)
    axisZ.place(x=eixoZ[0], y=eixoZ[1]-20)


if __name__ == "__main__":
    from transformations import Transformation
    window = tk.Tk()
    window.title('The Marvelous Polygoneer')
    width = 1280
    height = 750
    window.geometry('{}x{}+{}+{}'.format(1280, 690, 0, 0))
    window.resizable(0, 0)

    # Making Frame
    frameDrawingInterface = Frame(window,  highlightbackground="black",
                                  highlightthickness=1, width=int(width*0.7), height=int(height*0.88))
    frameDrawingInterface.place(x=int(width*0.01), y=int(height * 0.01))

    # Creating the window with user interface
    userInterface = Frame(window, highlightbackground="black",
                          highlightthickness=1, width=300, height=int(height*0.9))
    userInterface.place(x=width-310, y=int(height * 0.01))
    userInterface.pack_propagate(0)

    # Making the canvas
    drawing = Screen(frameDrawingInterface, width-(330+width*0.01), height-20)
    drawing.canvas.pack()

    btnClear = ttk.Button(window, text="Clear", width=15,
                           command=ClearScreen, cursor="hand2")
    btnClear.place(x=width-(410+width*0.01), y=int(height * 0.88))

    txtIntegrantes = ttk.Label(
        window, text='"Developed by: Sandip Katel, Saphal Rimal, Sharad Pokharel, and Sijan Joshi')
    txtIntegrantes.place(x=10,  y=int(height * 0.89))

    drawing.canvas.bind('<Button-1>', SelectingObject)

    t1 = Transformation()

    drawing.canvas.bind_all(
        '<q>', lambda event: t1.move_x_left(event, drawing))
    drawing.canvas.bind_all(
        '<a>', lambda event: t1.move_x_right(event, drawing))
    drawing.canvas.bind_all(
        '<w>', lambda event: t1.move_z_front(event, drawing))
    drawing.canvas.bind_all(
        '<s>', lambda event: t1.move_z_back(event, drawing))
    drawing.canvas.bind_all('<e>', lambda event: t1.move_y_up(event, drawing))
    drawing.canvas.bind_all(
        '<d>', lambda event: t1.move_y_down(event, drawing))

    drawing.canvas.bind_all(
        '<r>', lambda event: t1.scale_x_less(event, drawing))
    drawing.canvas.bind_all(
        '<f>', lambda event: t1.scale_x_more(event, drawing))
    drawing.canvas.bind_all(
        '<t>', lambda event: t1.scale_z_less(event, drawing))
    drawing.canvas.bind_all(
        '<g>', lambda event: t1.scale_z_more(event, drawing))
    drawing.canvas.bind_all(
        '<y>', lambda event: t1.scale_y_less(event, drawing))
    drawing.canvas.bind_all(
        '<h>', lambda event: t1.scale_y_more(event, drawing))

    drawing.canvas.bind_all('<u>', lambda event: t1.rot_x_left(event, drawing))
    drawing.canvas.bind_all(
        '<j>', lambda event: t1.rot_x_right(event, drawing))
    drawing.canvas.bind_all(
        '<i>', lambda event: t1.rot_z_front(event, drawing))
    drawing.canvas.bind_all('<k>', lambda event: t1.rot_z_back(event, drawing))
    drawing.canvas.bind_all('<o>', lambda event: t1.rot_y_up(event, drawing))
    drawing.canvas.bind_all('<l>', lambda event: t1.rot_y_down(event, drawing))

    rbProjection = tk.IntVar()
    rbProjection.set(0)
    rbShading = tk.IntVar()
    rbShading.set(0)
    textNumSides = tk.StringVar()
    textNumSides.set("")

    t = ToggledFrame(userInterface, width, height,
                     text='Object Information', relief="raised", borderwidth=1)
    t.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    labelBaseRadius = ttk.Label(t.sub_frame, text='Base Radius')
    txtBaseRadius = ttk.Entry(t.sub_frame, name="txtBaseRadius", width=15)
    labelTopRadius = ttk.Label(t.sub_frame, text='Top Radius')
    txtTopRadius = ttk.Entry(t.sub_frame, name="txtTopRadius", width=15)
    labelNumSides = ttk.Label(t.sub_frame, text='Number of Sides')
    txtNumSides = ttk.Entry(t.sub_frame, name="txtNumSides",
                            width=15, textvariable=textNumSides)
    labelHeight = ttk.Label(t.sub_frame, text='Height')
    txtHeight = ttk.Entry(t.sub_frame, name="txtHeight", width=15)
    btnCreateObject = ttk.Button(
        t.sub_frame, text="Create Object", width=15, command=objectClick)
    btnUpdateObject = ttk.Button(
        t.sub_frame, text="Update Object", width=15, command=updateObject)

    slide = RGBSliderApp()

    labelKa = ttk.Label(t.sub_frame, text="Ka*",
                        font="-weight bold -size 9", cursor="hand2")
    """labelKaR = ttk.Label(t.sub_frame, text='R')
    txtKaR = ttk.Entry(t.sub_frame, name="kaR", width=15)
    labelKaG = ttk.Label(t.sub_frame, text='G')
    txtKaG = ttk.Entry(t.sub_frame, name="kaG", width=15)
    labelKaB = ttk.Label(t.sub_frame, text='B')
    txtKaB = ttk.Entry(t.sub_frame, name="kaB", width=15)"""

    labelKd = ttk.Label(t.sub_frame, text="Kd*",
                        font="-weight bold -size 9", cursor="hand2")
    """labelKdR = ttk.Label(t.sub_frame, text='R')
    txtKdR = ttk.Entry(t.sub_frame, name="kdR", width=15)
    labelKdG = ttk.Label(t.sub_frame, text='G')
    txtKdG = ttk.Entry(t.sub_frame, name="kdG", width=15)
    labelKdB = ttk.Label(t.sub_frame, text='B')
    txtKdB = ttk.Entry(t.sub_frame, name="kdB", width=15)"""

    labelKs = ttk.Label(t.sub_frame, text="Ks*",
                        font="-weight bold -size 9", cursor="hand2")
    """labelKsR = ttk.Label(t.sub_frame, text='R')
    txtKsR = ttk.Entry(t.sub_frame, name="ksR", width=15)
    labelKsG = ttk.Label(t.sub_frame, text='G')
    txtKsG = ttk.Entry(t.sub_frame, name="ksG", width=15)
    labelKsB = ttk.Label(t.sub_frame, text='B')
    txtKsB = ttk.Entry(t.sub_frame, name="ksB", width=15)"""

    labelNumSides.grid(row=1, column=1, padx=10, pady=1)
    txtNumSides.grid(row=1, column=2, padx=1, pady=1)
    labelBaseRadius.grid(row=2, column=1, padx=1, pady=1)
    txtBaseRadius.grid(row=2, column=2, padx=1, pady=1)
    labelTopRadius.grid(row=3, column=1, padx=1, pady=1)
    txtTopRadius.grid(row=3, column=2, padx=1, pady=1)
    labelHeight.grid(row=5, column=1, padx=1, pady=1)
    txtHeight.grid(row=5, column=2, padx=1, pady=1)

    labelKa.grid(row=7, column=1,  padx=10, pady=2, sticky=W)
    txtKaR, txtKaG, txtKaB = slide.sliders(t.sub_frame, 7, 1)
    """labelKaR.grid(row=8, column=1, padx=1, pady=1)
    txtKaR.grid(row=8, column=2, padx=1, pady=1)
    labelKaG.grid(row=9, column=1, padx=1, pady=1)
    txtKaG.grid(row=9, column=2, padx=1, pady=1)
    labelKaB.grid(row=10, column=1, padx=1, pady=1)
    txtKaB.grid(row=10, column=2, padx=1, pady=1)"""

    labelKd.grid(row=11, column=1,  padx=10, pady=2, sticky=W)
    txtKdR, txtKdG, txtKdB = slide.sliders(t.sub_frame, 10, 1)
    """labelKdR.grid(row=12, column=1, padx=1, pady=1)
    txtKdR.grid(row=12, column=2, padx=1, pady=1)
    labelKdG.grid(row=13, column=1, padx=1, pady=1)
    txtKdG.grid(row=13, column=2, padx=1, pady=1)
    labelKdB.grid(row=14, column=1, padx=1, pady=1)
    txtKdB.grid(row=14, column=2, padx=1, pady=1)"""

    labelKs.grid(row=15, column=1,  padx=10, pady=2, sticky=W)
    txtKsR, txtKsG, txtKsB = slide.sliders(t.sub_frame, 14, 1)
    """labelKsR.grid(row=16, column=1, padx=1, pady=1)
    txtKsR.grid(row=16, column=2, padx=1, pady=1)
    labelKsG.grid(row=17, column=1, padx=1, pady=1)
    txtKsG.grid(row=17, column=2, padx=1, pady=1)
    labelKsB.grid(row=18, column=1, padx=1, pady=1)
    txtKsB.grid(row=18, column=2, padx=1, pady=1)"""

    btnCreateObject.grid(row=19, column=1, padx=4, pady=8)
    btnUpdateObject.grid(row=19, column=2, padx=4, pady=8)

    tipKa = CreateToolTip(labelKa, "Values between 0 and 255")
    tipKd = CreateToolTip(labelKd, "Values between 0 and 255")
    tipKs = CreateToolTip(labelKs, "Values between 0 and 255")

    textNumSides.trace('w', buttonObject)
    t2 = ToggledFrame(userInterface, width, height,
                      text='Projection', relief="raised", borderwidth=1)
    t2.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    labelProjectionType = ttk.Label(
        t2.sub_frame, text="Projection Type", font="-weight bold -size 9")
    rbAxonometrica = ttk.Radiobutton(
        t2.sub_frame, text="Axonometric", variable=rbProjection, value=0, cursor="hand2")
    rbPerspectiva = ttk.Radiobutton(
        t2.sub_frame, text="Perspective", variable=rbProjection, value=1, cursor="hand2")

    labelVRP = ttk.Label(t2.sub_frame, text="VRP", font="-weight bold -size 9")
    labelVRPx = ttk.Label(t2.sub_frame, text="X")
    txtVRPx = ttk.Entry(t2.sub_frame, name="txtVRPx", width=15)
    labelVRPy = ttk.Label(t2.sub_frame, text="Y")
    txtVRPy = ttk.Entry(t2.sub_frame, name="txtVRPy", width=15)
    labelVRPz = ttk.Label(t2.sub_frame, text="Z")
    txtVRPz = ttk.Entry(t2.sub_frame, name="txtVRPz", width=15)

    labelP = ttk.Label(t2.sub_frame, text="Vector P",
                       font="-weight bold -size 9")
    labelPx = ttk.Label(t2.sub_frame, text="X")
    txtPx = ttk.Entry(t2.sub_frame, name="txtPx", width=15)
    labelPy = ttk.Label(t2.sub_frame, text="Y")
    txtPy = ttk.Entry(t2.sub_frame, name="txtPy", width=15)
    labelPz = ttk.Label(t2.sub_frame, text="Z")
    txtPz = ttk.Entry(t2.sub_frame, name="txtPz", width=15)

    labelViewUp = ttk.Label(
        t2.sub_frame, text="View-Up Vector", font="-weight bold -size 9")
    labelViewUpx = ttk.Label(t2.sub_frame, text="X")
    txtViewUpx = ttk.Entry(t2.sub_frame, name="txtViewUpx", width=15)
    labelViewUpy = ttk.Label(t2.sub_frame, text="Y")
    txtViewUpy = ttk.Entry(t2.sub_frame, name="txtViewUpy", width=15)
    labelViewUpz = ttk.Label(t2.sub_frame, text="Z")
    txtViewUpz = ttk.Entry(t2.sub_frame, name="txtViewUpz", width=15)

    labelDistancia = ttk.Label(
        t2.sub_frame, text="Distances", font="-weight bold -size 9")
    labelNear = ttk.Label(t2.sub_frame, text="Near Plane")
    txtNear = ttk.Entry(t2.sub_frame, name="txtNear", width=15)
    labelFar = ttk.Label(t2.sub_frame, text="Far Plane")
    txtFar = ttk.Entry(t2.sub_frame, name="txtFar", width=15)
    labelProjectionPlane = ttk.Label(t2.sub_frame, text="Projection Plane")
    txtProjectionPlane = ttk.Entry(
        t2.sub_frame, name="txtProjectionPlane", width=15)

    labelWorldLimits = ttk.Label(
        t2.sub_frame, text="Window Limits", font="-weight bold -size 9")
    labelWorldLimitsxMin = ttk.Label(t2.sub_frame, text="X min")
    txtWorldLimitsxMin = ttk.Entry(t2.sub_frame, name="txtWorldLimitsxMin", width=15)
    labelWorldLimitsxMax = ttk.Label(t2.sub_frame, text="X max")
    txtWorldLimitsxMax = ttk.Entry(t2.sub_frame, name="txtWorldLimitsxMax", width=15)
    labelWorldLimitsyMin = ttk.Label(t2.sub_frame, text="Y min")
    txtWorldLimitsyMin = ttk.Entry(t2.sub_frame, name="txtWorldLimitsyMin", width=15)
    labelWorldLimitsyMax = ttk.Label(t2.sub_frame, text="Y max")
    txtWorldLimitsyMax = ttk.Entry(t2.sub_frame, name="txtWorldLimitsyMax", width=15)

    labelViewportLimits = ttk.Label(
        t2.sub_frame, text="Viewport Limits", font="-weight bold -size 9")
    labelViewportLimitsxMin = ttk.Label(
        t2.sub_frame, text="X min*", cursor="hand2")
    txtViewportLimitsxMin = ttk.Entry(
        t2.sub_frame, name="txtViewportLimitsxMin", width=15)
    labelViewportLimitsxMax = ttk.Label(
        t2.sub_frame, text="X max*", cursor="hand2")
    txtViewportLimitsxMax = ttk.Entry(
        t2.sub_frame, name="txtViewportLimitsxMax", width=15)
    labelViewportLimitsyMin = ttk.Label(
        t2.sub_frame, text="Y min*", cursor="hand2")
    txtViewportLimitsyMin = ttk.Entry(
        t2.sub_frame, name="txtViewportLimitsyMin", width=15)
    labelViewportLimitsyMax = ttk.Label(
        t2.sub_frame, text="Y max*", cursor="hand2")
    txtViewportLimitsyMax = ttk.Entry(
        t2.sub_frame, name="txtViewportLimitsyMax", width=15)
    btnAlterarCena = ttk.Button(
        t2.sub_frame, text="Change Scene", width=15, command=ProjectionClick, cursor="hand2")

    tipViewPortXmin = CreateToolTip(labelViewportLimitsxMin, "Values >= 0")
    tipViewPortXmax = CreateToolTip(
        labelViewportLimitsxMax, "0 <= Values <=937")
    tipViewPortYmin = CreateToolTip(labelViewportLimitsyMin, "Values >= 0")
    tipViewPortYmax = CreateToolTip(
        labelViewportLimitsyMax, "0 <= Values <=642")

    labelProjectionType.grid(row=1, column=1, padx=1, pady=2)
    rbAxonometrica.grid(row=2, column=1, padx=5, pady=2)
    rbPerspectiva.grid(row=2, column=2, padx=5, pady=2)

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

    labelDistancia.grid(row=15, column=1, padx=10, pady=2, sticky=W)
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
    btnAlterarCena.grid(row=29, column=1, padx=4, pady=8, columnspan=2)


    t3 = ToggledFrame(userInterface, width, height,
                      text='Lighting and Shading', relief="raised", borderwidth=1)
    t3.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    labelIluminacao = ttk.Label(
        t3.sub_frame, text="Illumination", font="-weight bold -size 9")

    labelAmbientLight = ttk.Label(
        t3.sub_frame, text="Ambient Light*", font="-weight bold -size 9", cursor="hand2")
    labelIAR = ttk.Label(t3.sub_frame, text='R')
    txtIAR = ttk.Entry(t3.sub_frame, name="iaR", width=15)
    labelIAG = ttk.Label(t3.sub_frame, text='G')
    txtIAG = ttk.Entry(t3.sub_frame, name="iaG", width=15)
    labelIAB = ttk.Label(t3.sub_frame, text='B')
    txtIAB = ttk.Entry(t3.sub_frame, name="iaB", width=15)

    labelLightSource = ttk.Label(
        t3.sub_frame, text="Light Source*", font="-weight bold -size 9", cursor="hand2")
    labelIR = ttk.Label(t3.sub_frame, text='R')
    txtIR = ttk.Entry(t3.sub_frame, name="iR", width=15)
    labelIG = ttk.Label(t3.sub_frame, text='G')
    txtIG = ttk.Entry(t3.sub_frame, name="iG", width=15)
    labelIB = ttk.Label(t3.sub_frame, text='B')
    txtIB = ttk.Entry(t3.sub_frame, name="iB", width=15)

    labelPosLightSource = ttk.Label(
        t3.sub_frame, text="Light Source Coordinates", font="-weight bold -size 9")
    labelIx = ttk.Label(t3.sub_frame, text='x')
    txtIx = ttk.Entry(t3.sub_frame, name="ix", width=15)
    labelIy = ttk.Label(t3.sub_frame, text='y')
    txtIy = ttk.Entry(t3.sub_frame, name="iy", width=15)
    labelIz = ttk.Label(t3.sub_frame, text='z')
    txtIz = ttk.Entry(t3.sub_frame, name="iz", width=15)

    labelShadingType = ttk.Label(
        t3.sub_frame, text="Shading Type", font="-weight bold -size 9")
    rbConstant = ttk.Radiobutton(
        t3.sub_frame, text="Constant Shading", variable=rbShading, value=0, cursor="hand2")
    rbGouraud = ttk.Radiobutton(
        t3.sub_frame, text="Gouraud Shading", variable=rbShading, value=1, cursor="hand2")
    rbPhong = ttk.Radiobutton(
        t3.sub_frame, text="Phong Shading", variable=rbShading, value=2, cursor="hand2")
    btnAlterarIluminacao = ttk.Button(
        t3.sub_frame, text="Change Illum/Shad", width=20, command=iluminacaoClick, cursor="hand2")

    rbGouraud['state'] = tk.DISABLED
    rbPhong['state'] = tk.DISABLED

    tipAmbientLight = CreateToolTip(labelAmbientLight, "Values between 0 and 255")
    tipLightSource = CreateToolTip(
        labelLightSource, "Values between 0 and 255")

    labelShadingType.grid(row=1, column=1, padx=12, pady=4, sticky=W)
    rbConstant.grid(row=2, column=1, padx=25, pady=1, sticky=W)
    rbGouraud.grid(row=3, column=1, padx=25, pady=1, sticky=W)
    rbPhong.grid(row=4, column=1, padx=25, pady=1, sticky=W)

    labelAmbientLight.grid(row=5, column=1,  padx=10, pady=2, sticky=W)
    labelIAR.grid(row=6, column=1, padx=1, pady=1)
    txtIAR.grid(row=6, column=2, padx=1, pady=1)
    labelIAG.grid(row=7, column=1, padx=1, pady=1)
    txtIAG.grid(row=7, column=2, padx=1, pady=1)
    labelIAB.grid(row=8, column=1, padx=1, pady=1)
    txtIAB.grid(row=8, column=2, padx=1, pady=1)

    labelLightSource.grid(row=9, column=1,  padx=10, pady=2, sticky=W)
    labelIR.grid(row=10, column=1, padx=1, pady=1)
    txtIR.grid(row=10, column=2, padx=1, pady=1)
    labelIG.grid(row=11, column=1, padx=1, pady=1)
    txtIG.grid(row=11, column=2, padx=1, pady=1)
    labelIB.grid(row=12, column=1, padx=1, pady=1)
    txtIB.grid(row=12, column=2, padx=1, pady=1)
    labelPosLightSource.grid(row=13, column=1, padx=10, pady=2, sticky=W)
    labelIx.grid(row=14, column=1, padx=1, pady=1)
    txtIx.grid(row=14, column=2, padx=1, pady=1)
    labelIy.grid(row=15, column=1, padx=1, pady=1)
    txtIy.grid(row=15, column=2, padx=1, pady=1)
    labelIz.grid(row=16, column=1, padx=1, pady=1)
    txtIz.grid(row=16, column=2, padx=1, pady=1)

    btnAlterarIluminacao.grid(row=17, column=1, padx=4, pady=8, columnspan=2)

    buttonObject(1, 1, 1)
    ProjectionSet(drawing.GetProjection())

    txtPx['state'] = tk.DISABLED
    txtPy['state'] = tk.DISABLED
    txtPz['state'] = tk.DISABLED

    axisX = ttk.Label(frameDrawingInterface, text="X",
                      foreground="#FF0000", background="#CCCCCC")
    axisY = ttk.Label(frameDrawingInterface, text="Y",
                      foreground="#00FF00", background="#CCCCCC")
    axisZ = ttk.Label(frameDrawingInterface, text="Z",
                      foreground="#0000FF", background="#CCCCCC")

    updateAxes()

    window.mainloop()
