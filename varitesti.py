from tkinter import *

root = Tk()
root.title('Väritesti')

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

def pienenna(tamaSkaala):
    nykArvo = tamaSkaala.get()
    tamaSkaala.set(nykArvo - 1)

def suurenna(tamaSkaala):
    nykArvo = tamaSkaala.get()
    tamaSkaala.set(nykArvo + 1)

#säätimet värikomponenttien säätelyyn    
punaSkaala = Scale(root, from_=0, to=255, orient=HORIZONTAL, command=slide, length=300)
viherSkaala = Scale(root, from_=0, to=255, orient=HORIZONTAL, command=slide, length=300)
siniSkaala = Scale(root, from_=0, to=255, orient=HORIZONTAL, command=slide, length=300)

punaSkaala.grid(row=0, column=1)
viherSkaala.grid(row=1, column=1)
siniSkaala.grid(row=2, column=1)

punaLabel = Label(root, text="Punaisen osuus", bg="red")
viherLabel = Label(root, text="Vihreän osuus", bg="green")
siniLabel = Label(root, text="Sinisen osuus", bg="blue")

#Säätönappulat hienovaraisempaan säätöön
punaMinus = Button(root, text="-", command=lambda:pienenna(punaSkaala))
punaPlus = Button(root, text="+", command=lambda:suurenna(punaSkaala))
viherMinus = Button(root, text="-", command=lambda:pienenna(viherSkaala))
viherPlus = Button(root, text="+", command=lambda:suurenna(viherSkaala))
siniMinus = Button(root, text="-", command=lambda:pienenna(siniSkaala))
siniPlus = Button(root, text="+", command=lambda:suurenna(siniSkaala))

#kertoo nykyisen värin RGB-arvon heksadesimaalimuodossa
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

#kenttä, joka näyttää säädetyn värin
nappi = Button(root, text="Sulje", command=root.destroy)
nappi.grid(row=3, column=0, columnspan=2)

kangas = Canvas(root, bg="#000000", height=400, width=400)

kangas.grid(row=4, column=0, columnspan=4)
root.mainloop()
