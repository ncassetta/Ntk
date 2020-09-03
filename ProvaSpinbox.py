from NCtk import *

CITTA = ("Bari", "Bologna", "Firenze", "Milano", "Napoli", "Palermo",
         "Roma", "Torino", "Venezia")

def changelabel(event):
    w = event.widget
    if w == spb1:
        lab1.config(fcolor="dark blue")
        lab1.settext("Selected city: " + w.gettext())
    else:
        lab1.config(fcolor="brown")
        lab1.settext("Selected number: " + w.gettext())


winMain = NCtkWindow(200, 150, 640, 480, "Spinbox")
spb1 = NCtkSpinbox(winMain, 20, 20, 120, 30, CITTA, changelabel)
spb2 = NCtkSpinbox(winMain, 20, 100, 120, 30, (1.0, 10.0, 0.5), changelabel)
lab1 = NCtkLabel(winMain, 0, 180, "fill", 80, pad=(20, 0))
lab1.config(bcolor="pink", text="Try the spinboxes!", anchor=CENTER, font=("Arial", 16))
#print(spb1.gettext())

mainloop()
