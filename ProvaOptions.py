from NCtk import *
from tkinter import font
from random import randrange

COLORS = ("white", "green", "blue", "yellow", "pink", "grey", "black",
          "cyan", "red", "orange", "gold", "magenta", "purple")
RELIEFS = (SUNKEN, FLAT, RAISED, GROOVE, RIDGE, SOLID)
ANCHORS = (N, E, NW, SE, S, SW, W, NE, CENTER)
JUSTIFIES = (LEFT, CENTER, RIGHT)
CURSORS = ("arrow", "circle", "clock", "cross", "dotbox", "exchange",
           "fleur", "heart", "man", "mouse", "pirate", "plus",
           "shuttle", "sizing", "spider", "spraycan", "target",
           "tcross", "trek", "watch")


def changeBgcolor(event):
    labSample.config(bcolor=spbBgcolor.get())
    
def changeFgcolor(event):
    labSample.config(fcolor=spbFgcolor.get())

def changeRelief(event):
    labSample.config(relief=spbRelief.get())

def changeBorder(event):
    labSample.config(borderwidth=int(spbBorder.get()))

def changeAnchor(event):
    labSample.config(anchor=spbAnchor.get())
    
def changeJustify(event):
    labSample.config(justify=spbJustify.get())

def changeFont(event):
    fsize = randrange(12, 25)
    labSample.config(font=(spbFont.get(), fsize))
    
def changeCursor(event):
    labSample.config(cursor=spbCursor.get())
    

winMain = NCtkMain(200, 180, 640, 480, "Widget attributes")
rfr1 = NCtkRowFrame(winMain, 0, 0, "fill", "fill")
rfr1.add_row(120)
labSample = NCtkLabel(rfr1, 0, 0, "fill", "fill", pad=10, content="This is a sample, because\nit demonstrates widget options")
# you must have an already created window to get fonts
FONTS = font.families()[:min(15, len(font.families()))]
rfr1.config_children("NCtkLabel", bcolor="#E0F0C0", relief=SOLID, border=1)
rfr1.config_children("NCtkSpinbox", bcolor="#A0C0D0", relief=RIDGE)
rfr1.add_row(16)
rfr1.add_row(34)
labBgcolor = NCtkLabel(rfr1, 0, 0, "20%", "fill", pad=(10,2,2,2), content="bcolor")
spbBgcolor = NCtkSpinbox(rfr1, "pack", 0, "30%", "fill", pad=(2,2,10,2), limits=COLORS, command=changeBgcolor)
labFgcolor = NCtkLabel(rfr1, "pack", 0, "20%", "fill", pad=(10,2,2,2), content="fcolor")
spbFgcolor = NCtkSpinbox(rfr1, "pack", 0, "30%", "fill", pad=(2,2,10,2), limits=COLORS, command=changeFgcolor)
rfr1.add_row(34)
labRelief = NCtkLabel(rfr1, 0, 0, "20%", "fill", pad=(10,2,2,2), content="relief")
spbRelief = NCtkSpinbox(rfr1, "pack", 0, "30%", "fill", pad=(2,2,10,2), limits=RELIEFS, command=changeRelief)
labBorder = NCtkLabel(rfr1, "pack", 0, "20%", "fill", pad=(10,2,2,2), content="border")
spbBorder = NCtkSpinbox(rfr1, "pack", 0, "30%", "fill", pad=(2,2,10,2), limits=(0, 6, 1), command=changeBorder)
rfr1.add_row(34)
labAnchor = NCtkLabel(rfr1, 0, 0, "20%", "fill", pad=(10,2,2,2), content="anchor")
spbAnchor = NCtkSpinbox(rfr1, "pack", 0, "30%", "fill", pad=(2,2,10,2), limits=ANCHORS, command=changeAnchor)
labJustify = NCtkLabel(rfr1, "pack", 0, "20%", "fill", pad=(10,2,2,2), content="justify")
spbJustify = NCtkSpinbox(rfr1, "pack", 0, "30%", "fill", pad=(2,2,10,2), limits=JUSTIFIES, command=changeJustify)
rfr1.add_row(34)
labFont = NCtkLabel(rfr1, 0, 0, "20%", "fill", pad=(10,2,2,2), content="font")
spbFont = NCtkSpinbox(rfr1, "pack", 0, "30%", "fill", pad=(2,2,10,2), limits=FONTS, command=changeFont)
labCursor = NCtkLabel(rfr1, "pack", 0, "20%", "fill", pad=(10,2,2,2), content="cursor")
spbCursor = NCtkSpinbox(rfr1, "pack", "pack", "30%", "fill", pad=(2,2,10,2), limits=CURSORS, command=changeCursor)

changeAnchor(None)
changeBgcolor(None)
spbBorder.setcontent(1)
changeCursor(None)
spbFgcolor.setcontent("green")
changeFont(None)
changeJustify(None)
changeRelief(None)

mainloop()