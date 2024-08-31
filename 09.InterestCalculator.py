from tkinter import *

def clear_all() :
	P_amount.delete(0, END)
	int_rate.delete(0, END)
	period.delete(0, END)
	total.delete(0, END)
	P_amount.focus_set()


def calculate_ci():
	P = int(P_amount.get())
	R = float(int_rate.get())
	T = int(period.get())
	CI = P * (pow((1 + R / 100), T))
	total.insert(10, CI)

 
if __name__ == "__main__" :

	root = Tk()
	root.configure(background = 'light green')
	root.geometry("400x250")
	root.title("Compound Interest Calculator")
	lab1 = Label(root, text = "Principle Amount(Rs) : ",fg = 'black', bg = 'red')
	lab2 = Label(root, text = "Rate(%) : ", fg = 'black', bg = 'red')
	lab3 = Label(root, text = "Time(years) : ", fg = 'black', bg = 'red')
	lab4 = Label(root, text = "Compound Interest : ", fg = 'black', bg = 'red')
	lab1.grid(row = 1, column = 0, padx = 10, pady = 10)
	lab2.grid(row = 2, column = 0, padx = 10, pady = 10)
	lab3.grid(row = 3, column = 0, padx = 10, pady = 10)
	lab4.grid(row = 5, column = 0, padx = 10, pady = 10)
	P_amount = Entry(root)
	int_rate = Entry(root)
	period = Entry(root)
	total = Entry(root)
	P_amount.grid(row = 1, column = 1, padx = 10, pady = 10)
	int_rate.grid(row = 2, column = 1, padx = 10, pady = 10)
	period.grid(row = 3, column = 1, padx = 10, pady = 10)
	total.grid(row = 5, column = 1, padx = 10, pady = 10)
	bt1 = Button(root, text = "Submit", bg = "red", fg = "black", command = calculate_ci)
	bt2 = Button(root, text = "Clear", bg = "red", 	fg = "black", command = clear_all)
	bt1.grid(row = 4, column = 1, pady = 10)
	bt2.grid(row = 6, column = 1, pady = 10)
	root.mainloop()
	
