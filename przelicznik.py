from tkinter import *


calButtonTxt = "Przelicz"
ccc1= ""
ccc2 = ""
ccc3 = ""
ccc = "Wybierz produkt, jednostki i ilość"
product = ""
fc = ""
sc = ""

# 0: mąka pszenna, 1: cukier/ryż, 2: woda/wino/ocet, 3: bułka tarta

units = {0:(1, 0.001, 1.47, 0.00588),1:(1, 0.001, 1.13636, 0.00454544), 2: (1, 0.001, 1, 0.004), 3: (1, 0.001, 1.66667, 0.00667)} # g, kg, ml, szklanki

# units = [1.47,1.13636,1,1.66667]

def firstselect(evt):
    global ccc1,ccc, product
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    #stat.set(ccc + "%d: %s z " % (index, value))
    ccc1 = str(value)+": "
    ccc = ccc1+ccc2+" na "+ccc3
    stat.set(ccc)
    product = index





def secondselect(evt):
    global ccc2,ccc, fc
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    #stat.set(ccc + "%d: %s z " % (index, value))
    ccc2 = str(value)
    ccc = ccc1+ccc2+" na "+ccc3
    stat.set(ccc)
    fc = index #First Choice



def thirdselect(evt):
    global ccc3,ccc, sc
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    #stat.set(ccc + "%d: %s z " % (index, value))
    ccc3 = str(value)
    ccc = ccc1+ccc2+" na "+ccc3
    stat.set(ccc)
    sc = index #second choice


def calc(evt):
    global ccc
    ev = e.get() #entered value
    c = units.get(product) # choice
    try:
        ev = float(ev)


        if product != "" and fc != "" and sc != "":

            calculation = round(((float(ev))/float(c[fc]))*float(c[sc]),2)

            ccc = ccc1+" "+str(ev)+" "+ccc2[-4:]+" to "+str(calculation)+" "+ccc3[-4:]

        else:
            ccc = "Wprowadź poprawnie wszystkie dane!"

    except ValueError:
        ccc = "Wprowadź poprawne dane!"

    stat.set(ccc)

def clearbox(evt):
    e.delete(0,END)
    e.focus()


win = Tk()
#win.geometry("775x325")
win.wm_title("Kuchenny przelicznik wag 0.1")
win.resizable(width=FALSE, height=FALSE)

topFrame = Frame(win,width=1000)
#topFrame.pack(fill=BOTH)
topFrame.grid(row=0,columnspan=2)

pFrame = Frame(win)
#pFrame.pack(side=BOTTOM)
pFrame.grid(row=1,column=1)
'''
bottomFrame = Frame(win,width=1000)
#bottomFrame.pack(side=BOTTOM,fill=BOTH)
bottomFrame.grid(row=1,column=2)
'''
middleFrame = Frame(win,width=1000)
#middleFrame.pack(fill=BOTH)
middleFrame.grid(row=1)

theLabel = Label(topFrame, text="Wybierz produkt, jednostki i ilość:", justify=LEFT, anchor=W)
theLabel.pack(side=BOTTOM, fill=X)

stat = StringVar()
status = Label(topFrame, textvariable=stat, bd=1, relief=SUNKEN, font = "Helvetica 15 bold",width=70)
stat.set(ccc)
status.pack(fill=X, expand=True, side=TOP, ipady=10)

'''
l = Label(bottomFrame, text="Wprowadź ilość:")
l.pack()
'''
v = StringVar()
e = Entry(pFrame,textvariable=v,font = "Helvetica 20 bold", width=15, justify=RIGHT)
e.grid(row=0, column=0, columnspan=6)
e.bind('<Button-1>', clearbox)
e.focus()
'''
calButton = Button(bottomFrame, text=calButtonTxt)
calButton.pack(side=LEFT, fill=X,expand=True)
calButton.bind('<Button-1>', calc)
'''
win.bind("<Return>", calc)
win.bind("<KP_Enter>", calc)



lb1 = Listbox(middleFrame, exportselection=0,height=15)
lb1.pack(side=LEFT, fill=BOTH, expand=True)
lb1.insert(END,"mąka pszenna")
lb1.insert(END,"cukier/ryż")
lb1.insert(END,"woda/wino/ocet")
lb1.insert(END,"koncentrat pomidorowy")

sb1 = Scrollbar(middleFrame,orient=VERTICAL)
sb1.pack(side=LEFT,fill=BOTH)

sb1.configure(command=lb1.yview)
lb1.configure(yscrollcommand=sb1.set)

lb1.bind('<<ListboxSelect>>', firstselect)

lb2 = Listbox(middleFrame, exportselection=0)
lb2.pack(side=LEFT, fill=BOTH, expand=True)
lb2.insert(END,"gram [g]")
lb2.insert(END,"kilogram [kg]")
lb2.insert(END,"mililitr [ml]")
lb2.insert(END,"szklanka [sk]")

sb2= Scrollbar(middleFrame,orient=VERTICAL)
sb2.pack(side=LEFT,fill=BOTH)

sb2.configure(command=lb2.yview)
lb2.configure(yscrollcommand=sb2.set)

lb2.bind('<<ListboxSelect>>', secondselect)

lb3 = Listbox(middleFrame, exportselection=0)
lb3.pack(side=LEFT, fill=BOTH, expand=True)
lb3.insert(END,"gram [g]")
lb3.insert(END,"kilogram [kg]")
lb3.insert(END,"mililitr [ml]")
lb3.insert(END,"szklanka [sk]")

sb3 = Scrollbar(middleFrame,orient=VERTICAL)
sb3.pack(side=LEFT,fill=BOTH)

sb3.configure(command=lb3.yview)
lb3.configure(yscrollcommand=sb3.set)

lb3.bind('<<ListboxSelect>>', thirdselect)

def num_press(num):
        if num == "C":
            e.delete(0,END)
            e.focus()
        elif num == ",":
            e.insert(END,".")
        else:

            e.insert(END, num)
            e.focus()
bttn = []
numbers="789456123C0."
i = 0
for j in range(1,5):
    for k in range(3):
        bttn.append(Button(pFrame, text = numbers[i], font = "Helvetica 15 bold", height = 1, width = 1))
        bttn[i].grid(row = j, column = k, pady = 2, padx = 2)
        bttn[i]["command"] = lambda x = numbers[i]: num_press(x)
        i += 1

cbutton = Button(pFrame, text = "Przelicz", font = "Helvetica 10 bold", height = 9, width = 9)
cbutton.grid(row = 1, column = 5, columnspan = 4, rowspan = 4, pady = 2, padx=2)
cbutton.bind('<Button-1>', calc)
#theLabel1 = Label(bottomFrame, text="Wybierz produkt i jednostki:", justify=LEFT, anchor=W)
#theLabel1.grid(row = 0, column = 1)
#theLabel1.pack()



win.mainloop()