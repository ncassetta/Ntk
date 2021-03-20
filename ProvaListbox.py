from NCtk import *


lines = ("Uno", "Due", "Tre", "Quattro", "Cinque", "Sei", "Sette", "Otto",
         "Nove", "Dieci", "Undici", "Dodici", "Tredici", "Quattordici")
modes = ("single", "browse", "multiple", "extended")
explmodes = ("single mode : you can select only one item at once, clicking on it in the listbox",
             "browse mode : you can select only an item at once, clicking on it or dragging with the mouse",
             "multiple mode : you can select multiple items, clicking on them; clicking on a selected item " +
             "unselects it",
             "extended mode : you can select multiple items, clicking, dragging the mouse and using the" +
             "<CTRL> or <SHIFT> keys")


def addtolbox(event):
    nitems = lstTest.size()
    if nitems < len(lines):
        lstTest.insert(nitems, lines[nitems])
        
def delfromlbox(event):
    if lstTest.size() > 0:
        lstTest.delete(END)
        testchanged(None)
        
        
def testchanged(event):
    sel = lstTest.getselected()
    print("testchanged with index", sel)
    if len(sel) == 0:
        s = "none"
    else:
        s = ""
        for i in sel:
            s += "{}, ".format(i)
        s = s[:-2]
    labSel.setcontent("Selected: " + s) 

def selchanged(event):
    #lstMode.update()
    lstTest.select_clear(0, END)
    testchanged(None)
    sel = lstMode.getselected()
    print("selchanged() called with index", sel)
    if len(sel):
        labExplain.setcontent(explmodes[sel[0]])
        lstTest.config(selectmode=modes[sel[0]])
    

winMain = NCtkMain(200, 150, 600, 450, "NCtkListbox widget sample")
hfr1 = NCtkHorFrame(winMain, 0, 0, "fill", "fill")
vfr1 = NCtkVerFrame(hfr1, 0, 0, "50%", "fill")
vfr2 = NCtkVerFrame(hfr1, "pack", 0, "fill", "fill")
labTest = NCtkLabel(vfr1, 0, 0, "fill", 40, pad=(10, 10, 10, 5), content="Try to select items")
labTest.config(bcolor="light green", fcolor="blue", relief=SOLID, borderwidth=1, anchor=CENTER)
lstTest = NCtkListbox(vfr1, 0, "pack", "fill", -80, pad=(10, 5, 10, 40), command=testchanged)
lstTest.config(bcolor="blue", fcolor="yellow", sfcolor="maroon", sbcolor="light blue", 
               relief=RIDGE, font=("TkDefaultFont", 14))
labSel = NCtkLabel(vfr1, 0, "pack", "fill", 40, pad=(10, 5))
labSel.config(bcolor="light green", fcolor="blue", relief=SOLID, borderwidth=1)
testchanged(None)
hfr2 = NCtkHorFrame(vfr1, "center", "pack", "80%", "fill")
butAdd = NCtkButton(hfr2, "15%", 0, "35%", "fill", pad=(5,5, 5, 10), content="Add item",
                    command=addtolbox) 
butDel = NCtkButton(hfr2, "pack", "pack", "35%", "fill", pad=(5, 5, 5, 10), content="Del item",
                    command =delfromlbox)
labMode = NCtkLabel(vfr2, 0, 0, "fill", 40, pad=(10, 10, 10, 5), content="Listbox Mode")
labMode.config(bcolor="light green", fcolor="blue", relief=SOLID, borderwidth=1, anchor=CENTER)
lstMode = NCtkListbox(vfr2, 0, "pack", "fill", 120, pad=(10, 5), command=selchanged, items=modes)
lstMode.config(bcolor="cyan", fcolor="brown", font=("TkDefaultFont", 14), relief=RIDGE)
labExplain=NCtkLabel(vfr2, 0, "pack", "fill", "fill", pad=(10, 10), content=explmodes[0])
labExplain.config(anchor=NW)
#print (labExplain.getwinfo("fpixels", 20))

mainloop()