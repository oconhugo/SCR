
from tkinter import *
import Menu_Frame

#Display the total and buttons
class TotalSection(object):
    def __init__(self, right):
        label4 = Label(right, text="Articulos Seleccionados", width=30, height=2, font=("courier", 17, "bold"))
        label5 = Label(right, text="Articulo          Precio", width=30, height=2, font=("courier", 10, "bold"))
        label4.pack()
        label5.pack()
        box = Frame(right, borderwidth=2)
        total_label = Label(box, text="Total=   " + str(0), width=30, height=2, font=("ariel", 17, "bold"))
        box.pack(side="bottom", expand=True, fill="both", padx=10, pady=10)
        nota = self.newNota(box)
        continuar = Button(box, text="Continuar",height = 4, width=25, bg="lime green", padx=10, pady=10, command= lambda: self.continuar(nota))
        cancelar = Button(box, text="cancelar",height = 4, width=25, bg="fireBrick2", padx=10, pady=10, command= lambda: self.delete())
        continuar.pack(side = "left")
        cancelar.pack( side = "left")

    #Regresa la noata para el taquero
    def newNota(self, box):
        F = Frame(box)
        F.pack()
        L1 = Label(F, text="Nota para el taquero",font=("arial", 10, "bold"))
        L1.pack(side=LEFT)
        E1 = Text(F, bd=3, height=2, width=20)
        E1.pack(side=RIGHT)
        return E1

    #Manda el JSON hacia la otra interfase
    def continuar(self, nota):
        global ORDER
        d = {"Nota": nota.get("1.0", 'end-1c')}
        ORDER.append(d)
        print(ORDER)

    #Reset the values of the JSON
    def delete(self):
        global ORDER
        global GLOBAL_TOTAL
        global ITEM_VAL
        for i in range(len(ORDER)):
            ORDER.pop()
        Menu_Frame.DISB = 0
        Menu_Frame.DISM = 0
        GLOBAL_TOTAL = 0
        for i in range(len(ITEM_VAL)):
            ITEM_VAL.pop()

#Display the selected items
class DisplayItems():
    def printItem(self, x, val, right):
        num = str(val)
        item = {x: val}
        global ORDER
        ORDER.append(item)
        ITEM_VAL.append(val)
        if len(x) < 4:
            label = Label(right, text=x+"                        $"+num, width=40, height=1, font=("courier", 10, "bold"), anchor=W)
        elif len(x) < 8 and len(x) > 4:
            label = Label(right, text=x + "                 $" + num, width=40, height=1, font=("courier", 10, "bold"), anchor=W)
        else:
            label = Label(right, text=x + "         $" + num, width=40, height=1, font=("courier", 10, "bold"), anchor=W)
        label.pack()
        if x != "Dulces" and x!= "Varios" and x!= "Barbacoa":
            self.calculate()

    #calculate the sum of the items
    def calculate(self):
        global ORDER
        total = 0
        for i in ITEM_VAL:
            total = total + i
        global GLOBAL_TOTAL
        GLOBAL_TOTAL = total

    #Check if it is a number. Then convert it
    def convertStr(self, d):
        if len(d)>0:
            dd= int(d)
        else :
            dd= 0
        return dd

    #store the extras and checkbox in the same JSON as the items
    def showTotal(self, right, checkbox, entrys):
        global ORDER
        global GLOBAL_TOTAL
        d = entrys[0].get()
        v = entrys[1].get()
        b = entrys[2].get()
        intd = self.convertStr(d)
        intv = self.convertStr(v)
        intb = self.convertStr(b)
        self.fillEntrys(intd, intv, intb, right)
        dicC = {"Llevar":checkbox.get()}
        ORDER.append(dicC)
        GLOBAL_TOTAL = GLOBAL_TOTAL+intd+intv+intb
        print(ORDER)
        label = Label(right, text="Total= $"+str(GLOBAL_TOTAL), font=("arial", 15, "bold"), height = 4)
        label.pack()

    #Check for the values of the Extras
    def fillEntrys(self, d, v, b, right):
        if d!=0:
            self.printItem("Dulces", d, right)
        if v != 0:
            self.printItem("Varios", v, right)
        if b != 0:
            self.printItem("Barbacoa", b, right)

#global variables
GLOBAL_TOTAL=0
ITEM_VAL = []
ORDER = []