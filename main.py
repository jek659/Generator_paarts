import tkinter
import openpyscad as ops

def click():
    w = E1.get()
    h = E2.get()
    f_name = E3.get()
    if(len(w) != 0 and len(h) !=0 and len(f_name) != 0):
        if(len(w)<3 and len(h)<3):
            f = 0
            try:
                w = int(w)
                h = int(h)
                f = 1
            except ValueError:
                L5.config(text = "Error:Введите числа",fg = "red")
            if(f == 1):
                model = gen(w,h)
                model.write(f_name+".scad")
                L5.config(text = "Деталь готова",fg = "green")
        else:
            L5.config(text = "Error:Данные переполнены",fg = "red")
    else:
        L5.config(text = "Error:Введите данные",fg = "red")

def gen(w,h):
    base = ops.Square([w*10,h*10])
    res = ops.Difference()
    res.append(base)
    for i in range(w):
        for j in range(h):
            c = ops.Circle(1.5,3,50)
            c = c.translate([5+i*10,5+j*10,0])
            res.append(c)
    return res
#Создание окна
root = tkinter.Tk()
root.geometry("300x300+200+200")
root.title("GeNa 3000")
#Создание виджетов
L1 = tkinter.Label(text ="Generator Parts",font = ("Terminal",24))
L2 = tkinter.Label(text ="Количество отверстий в ширину")
L3 = tkinter.Label(text ="Количество отверстий в длину")
L4 = tkinter.Label(text ="Имя файла")
L5 = tkinter.Label()
E1 = tkinter.Entry()
E2 = tkinter.Entry()
E3 = tkinter.Entry()
B1 = tkinter.Button(text = "Создать деталь",command = click)
#Размещение виджетов
L1.pack()
L2.pack()
E1.pack()
L3.pack()
E2.pack()
L4.pack()
E3.pack()
B1.pack()
L5.pack()
root.mainloop()