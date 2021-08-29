from tkinter import *
#the UI is made using Tkinter-library of Python
root = Tk()
root.title('Väritesti')

#this function handles actions after the slides are used
def slide(var): 
    redPix = hex(punaSkaala.get())
    if punaSkaala.get() < 16:
        redPix = redPix[::2]
    grnPix = hex(viherSkaala.get())
    if viherSkaala.get() < 16:
        grnPix = grnPix[::2]
    bluPix = hex(siniSkaala.get())
    if siniSkaala.get() < 16:
        bluPix = bluPix[::2]
    #print("#"+redPix[-2:]+grnPix[-2:]+bluPix[-2:])
    kangas = Canvas(root, bg="#"+redPix[-2:]+grnPix[-2:]+bluPix[-2:], height=400, width=400)
    kangas.grid(row=4, column=0, columnspan=4)
    hexaLabel = Label(root, text="#"+redPix[-2:]+grnPix[-2:]+bluPix[-2:])
    hexaLabel.grid(row=5, column=0, columnspan=4)

#this function handles the action of decreasing-button
def pienenna(tamaSkaala): 
    nykArvo = tamaSkaala.get()
    tamaSkaala.set(nykArvo - 1)

#this function handles the action of increasing-button
def suurenna(tamaSkaala): 
    nykArvo = tamaSkaala.get()
    tamaSkaala.set(nykArvo + 1)

#scales for each components of colour    
punaSkaala = Scale(root, from_=0, to=255, orient=HORIZONTAL, command=slide, length=300) #red
viherSkaala = Scale(root, from_=0, to=255, orient=HORIZONTAL, command=slide, length=300) #green
siniSkaala = Scale(root, from_=0, to=255, orient=HORIZONTAL, command=slide, length=300) #blue
#placing the scales on the window
punaSkaala.grid(row=0, column=1)
viherSkaala.grid(row=1, column=1)
siniSkaala.grid(row=2, column=1)

punaLabel = Label(root, text="Punaisen osuus", bg="red")
viherLabel = Label(root, text="Vihreän osuus", bg="green")
siniLabel = Label(root, text="Sinisen osuus", bg="blue")

#buttons for more discreet controlling
punaMinus = Button(root, text="-", command=lambda:pienenna(punaSkaala)) # R-value--
punaPlus = Button(root, text="+", command=lambda:suurenna(punaSkaala)) # R-value++
viherMinus = Button(root, text="-", command=lambda:pienenna(viherSkaala)) # G-value-- 
viherPlus = Button(root, text="+", command=lambda:suurenna(viherSkaala)) # G-value++
siniMinus = Button(root, text="-", command=lambda:pienenna(siniSkaala)) #B-value--
siniPlus = Button(root, text="+", command=lambda:suurenna(siniSkaala)) #B-value++

#tells the RGB value of the current colour in hexadecimals
hexaLabel = Label(root, text="#000000")

punaLabel.grid(row=0, column=0)
viherLabel.grid(row=1, column=0)
siniLabel.grid(row=2, column=0)

punaMinus.grid(row=0, column=2)
punaPlus.grid(row=0, column=3)
viherMinus.grid(row=1, column=2)
viherPlus.grid(row=1, column=3)
siniMinus.grid(row=2, column=2)
siniPlus.grid(row=2, column=3)

hexaLabel.grid(row=5, column=0, columnspan=4)

nappi = Button(root, text="Sulje", command=root.destroy)
nappi.grid(row=3, column=0, columnspan=2)

#this canvas shows the colour made of RGB-parameters
kangas = Canvas(root, bg="#000000", height=400, width=400)

kangas.grid(row=4, column=0, columnspan=4)
root.mainloop()
