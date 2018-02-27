from tkinter import *
import random
import time

root = Tk()
w = 1600
h = 800
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d'% (w, h, x, y))
root.title("Cafe Management")

text_Input = StringVar()
operator = ''


Tops = Frame(root, width = 1600,height = 50,  bg = "powder blue", relief = SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800, height = 700, relief = SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300,height = 700,relief = SUNKEN)
f2.pack(side=RIGHT)
#+++++++++++++++++++++++++++++++++  TIME ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

localTime = time.asctime(time.localtime(time.time())) #date time function
#++++++++++++++++++++++++++++++++   INFORMATION +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
lblInfo = Label(Tops, font = ('Arial',50,'bold'), text = "Simple Cafeteria Management System", fg= "Steel Blue", bd=10, anchor = 'w')
lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font = ('Arial',25,'bold'), text = localTime, fg= "Steel Blue", bd=10, anchor = 'w')
lblInfo.grid(row=1, column=0)

#++++++++++++++++++++++++++++++++++ CALCULATOR  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ''
    text_Input.set('')

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ''

def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    CostOfFries= float(Fries.get())
    CostOfDrinks = float(Drinks.get())
    CostOfBurger = float(Burger.get())
    CostOfFillet = float(Fillet.get())
    CostOfCheese = float(Cheese.get())
    CostOfChicken = float(Chicken.get())


    CoF = CostOfFries * 0.99
    CoD = CostOfDrinks * 1.00
    CoFilet = CostOfFillet * 2.99
    CoBurger = CostOfBurger * 2.87
    CoChicBurger = CostOfChicken * 2.89
    CoCheese_burger = CostOfCheese * 2.69

    CostOfMeal = '$', str('%.2f' % (CoF+CoD+CoFilet+CoBurger+CoChicBurger+CoCheese_burger))


    PayTax = ((CoF+CoD+CoFilet+CoBurger+CoChicBurger+CoCheese_burger) * 0.16)

    TotalCost =  (CoF+CoD+CoFilet+CoBurger+CoChicBurger+CoCheese_burger)

    Ser_charge = ((CoF+CoD+CoFilet+CoBurger+CoChicBurger+CoCheese_burger)/99)

    Service = '$', str('%.2f' % Ser_charge)

    OverallCost = '$', str('%.2f' % (PayTax+TotalCost+Ser_charge))

    PaidTax = '$', str('%.2f' % PayTax)

    Service_charge.set(Service)
    Cost.set(CostOfMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostOfMeal)
    Total.set(OverallCost)

def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Fillet.set("")
    Chicken.set("")
    Cost.set("")
    Cheese.set("")
    SubTotal.set("")
    Total.set("")
    Service_charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")





txtDisplay = Entry(f2, font = ('Arial', 20, 'bold'), textvariable=text_Input, bd= 30, insertwidth= 4, bg = "powder blue", justify = 'right')
txtDisplay.grid(columnspan = 4)
#--------------------------------------------------Row 2 ---------------------------------------------------------------------------------


btn7 = Button(f2, padx=16, bd = 8, fg='black', font=('arial', 20, 'bold'), text = "7", bg ='powder blue', command = lambda: btnClick(7))
btn7.grid(row=2, column=0)

btn8 = Button(f2, padx=16, bd = 8, fg='black', font=('arial', 20, 'bold'), text = "8", bg ='powder blue', command = lambda: btnClick(8)).grid(row=2, column=1)

btn9 = Button(f2, padx=16, bd = 8, fg='black', font=('arial', 20, 'bold'), text = "9", bg ='powder blue', command = lambda: btnClick(9)).grid(row=2, column=2)

Addition = Button(f2, padx=16, bd = 8, fg='black', font=('arial', 20, 'bold'), text = "+", bg ='powder blue', command = lambda: btnClick('+')).grid(row=2, column=3)


#---------------------------------------------------Row 3 ------------------------------------------------------------------------------------


btn4 = Button(f2, padx=16, bd = 8, fg='black', font=('arial', 20, 'bold'), text = "4", bg ='powder blue', command = lambda: btnClick(4))
btn4.grid(row=3, column=0)

btn5 = Button(f2, padx=16, bd = 8, fg='black', font=('arial', 20, 'bold'), text = "5", bg ='powder blue', command = lambda: btnClick(5)).grid(row=3, column=1)

btn6 = Button(f2, padx=16, bd = 8, fg='black', font=('arial', 20, 'bold'), text = "6", bg ='powder blue', command = lambda: btnClick(6)).grid(row=3, column=2)

Subtraction = Button(f2, padx=16, bd = 8, fg='black', font=('arial', 20, 'bold'), text = "-", bg ='powder blue', command = lambda: btnClick('-')).grid(row=3, column=3)

#----------------------------------------------------Row 4 ----------------------------------------------------------------------------------


btn1 = Button(f2, padx=16, bd = 8, fg='black', font=('arial', 20, 'bold'), text = "1", bg ='powder blue', command = lambda: btnClick(1)).grid(row=4, column=0)

btn2 = Button(f2, padx=16, bd = 8, fg='black', font=('arial', 20, 'bold'), text = "2", bg ='powder blue', command = lambda: btnClick(2)).grid(row=4, column=1)

btn3 = Button(f2, padx=16, bd = 8, fg='black', font=('arial', 20, 'bold'), text = "3", bg ='powder blue', command = lambda: btnClick(3)).grid(row=4, column=2)

Multiply = Button(f2, padx=16, bd = 8, fg='black', font=('arial', 20, 'bold'), text = "*", bg ='powder blue', command = lambda: btnClick('*')).grid(row=4, column=3)

#---------------------------------------------------- Row 5 ----------------------------------------------------------------------------------

btn0 = Button(f2, padx=16, bd = 8, fg='black', font=('arial', 20, 'bold'), text = "0", bg ='powder blue', command = lambda: btnClick(0)).grid(row=5, column=0)

btnClear = Button(f2, padx=16, bd = 8, fg='black', font=('arial', 20, 'bold'), text = "C",bg ='powder blue', command = lambda: btnClearDisplay()) .grid(row=5, column=1)

btnEquals = Button(f2, padx=16, bd = 8, fg='black', font=('arial', 20, 'bold'), text = "=", bg ='powder blue', command = btnEqualsInput).grid(row=5, column=2)

Division = Button(f2, padx=16, bd = 8, fg='black', font=('arial', 20, 'bold'), text = "/", bg ='powder blue', command = lambda: btnClick('/')).grid(row=5, column=3)

#========================================================== Orders 1============================================================================

rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Fillet = StringVar()
Chicken = StringVar()
Cost  = StringVar()
Cheese = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_charge = StringVar()
Drinks = StringVar()
Tax= StringVar()
cost = StringVar()


lblReference = Label(f1, font = ('Arial', 16, 'bold'), text= 'Reference', bd= 16, anchor = 'w').grid(row=0,column=0)
textReference = Entry(f1,font = ('Arial', 16, 'bold'), textvariable=rand, bd= 10, insertwidth= 4, bg = "powder blue", justify = 'right').grid(row=0,column=1)

lblFries = Label(f1, font = ('Arial', 16, 'bold'), text= 'Large Fries', bd= 16, anchor = 'w').grid(row=1,column=0)
textFries = Entry(f1,font = ('Arial', 16, 'bold'), textvariable=Fries, bd= 10, insertwidth= 4, bg = "powder blue", justify = 'right').grid(row=1,column=1)

lblBurger = Label(f1, font = ('Arial', 16, 'bold'), text= 'Burger Meal', bd= 16, anchor = 'w').grid(row=2,column=0)
textBurger = Entry(f1,font = ('Arial', 16, 'bold'), textvariable=Burger, bd= 10, insertwidth= 4, bg = "powder blue", justify = 'right').grid(row=2,column=1)

lblFillet = Label(f1, font = ('Arial', 16, 'bold'), text= 'Fillet_o_Meal', bd= 16, anchor = 'w').grid(row=3,column=0)
textFillet = Entry(f1,font = ('Arial', 16, 'bold'), textvariable=Fillet, bd= 10, insertwidth= 4, bg = "powder blue", justify = 'right').grid(row=3,column=1)

lblChicken = Label(f1, font = ('Arial', 16, 'bold'), text= 'Chicken Meal', bd= 16, anchor = 'w').grid(row=4,column=0)
textChicken = Entry(f1,font = ('Arial', 16, 'bold'), textvariable=Chicken, bd= 10, insertwidth= 4, bg = "powder blue", justify = 'right').grid(row=4,column=1)

lblCheese = Label(f1, font = ('Arial', 16, 'bold'), text= 'Cheese Meal', bd= 16, anchor = 'w',).grid(row=5,column=0)
textCheese = Entry(f1,font = ('Arial', 16, 'bold'), textvariable=Cheese, bd= 10, insertwidth= 4, bg = "powder blue", justify = 'right').grid(row=5,column=1)


#========================================================== Orders 1=======================================================================================

lblDrinks = Label(f1, font = ('Arial', 16, 'bold'), text= 'Drinks', bd= 16, anchor = 'w').grid(row=0,column=2)
textDrinks = Entry(f1, font=('Arial', 16, 'bold'), textvariable=Drinks, bd= 10, insertwidth= 4, bg = "#ffffff", justify = 'right').grid(row=0,column=3)

lblCost = Label(f1, font = ('Arial', 16, 'bold'), text= 'Cost of Meal', bd= 16, anchor = 'w').grid(row=1,column=2)
textCost = Entry(f1,font = ('Arial', 16, 'bold'), textvariable=Cost, bd= 10, insertwidth=4, bg="#ffffff", justify='right').grid(row=1,column=3)

lblService = Label(f1, font = ('Arial', 16, 'bold'), text= 'Service Charge', bd= 16, anchor = 'w').grid(row=2,column=2)
textService = Entry(f1,font = ('Arial', 16, 'bold'), textvariable=Service_charge, bd= 10, insertwidth= 4, bg = "#ffffff", justify = 'right').grid(row=2,column=3)

lblStateTax = Label(f1, font = ('Arial', 16, 'bold'), text= 'State Tax', bd= 16, anchor = 'w').grid(row=3,column=2)
textStateTax = Entry(f1,font = ('Arial', 16, 'bold'), textvariable=Tax, bd= 10, insertwidth= 4, bg = "#ffffff", justify = 'right').grid(row=3,column=3)

lblSubTotal = Label(f1, font = ('Arial', 16, 'bold'), text= 'Sub Total', bd= 16, anchor = 'w').grid(row=4,column=2)
textSubTotal = Entry(f1,font = ('Arial', 16, 'bold'), textvariable=SubTotal, bd= 10, insertwidth= 4, bg = "#ffffff", justify = 'right').grid(row=4,column=3)

lblTotalCost = Label(f1, font = ('Arial', 16, 'bold'), text= 'Total Cost', bd= 16, anchor = 'w',).grid(row=5,column=2)
textTotalCost = Entry(f1,font = ('Arial', 16, 'bold'), textvariable=Total, bd= 10, insertwidth= 4, bg = "#ffffff", justify = 'right').grid(row=5,column=3)

#========================================================== Buttons 1======================================================================================


btnTotal = Button(f1, padx=16, pady = 8, bd = 16, fg='black', font=('arial', 20, 'bold'), width = 10, text = "Total", bg ='powder blue', command = Ref).grid(row=7, column=1)
btnReset = Button(f1, padx=16, pady = 8, bd = 16, fg='black', font=('arial', 20, 'bold'), width = 10, text = "Reset", bg ='powder blue', command = Reset).grid(row=7, column=2)
btnExit = Button(f1, padx=16, pady = 8, bd = 16, fg='black', font=('arial', 20, 'bold'), width = 10, text = "Exit", bg ='powder blue', command = qExit).grid(row=7, column=3)
root.mainloop()

