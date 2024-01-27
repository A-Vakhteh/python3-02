from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("900x500+230+100")
root.resizable(0,0)
root.config(background='cyan')
root.title('Vakhteh-1')

def exit():
   i=messagebox.askquestion('Exit','Are you sure want to leave?')
   if(i=='yes'):
        root.destroy()
  
def area():
    c = int(ent_name.get())
    lbl3.config(text=c*c*3.14)
    lbl5.config(text = c*2*3.14)




lbl1 = Label(root, text='Enter Radius : ',font='Montserrat 18 bold',background='cyan',foreground='green')
lbl1.place(x=50,y=30)
ent_name = Entry(root,font='Montserrat ',background='black',foreground='cyan',width=20)
ent_name.place(x=245,y=40)

#====================================
lbl2 = Label(root, text='area : ',font='Montserrat 18 bold',background='cyan',foreground='green')
lbl2.place(x=50,y=100)
lbl3 = Label(root, font='Montserrat 18 bold',background='cyan',foreground='red')
lbl3.place(x=200,y=100)
#========================================
lbl4 = Label(root, text='Environment : ',font='Montserrat 18 bold',background='cyan',foreground='green')
lbl4.place(x=50,y=200)
lbl5 = Label(root,font='Montserrat 18 bold',background='cyan',foreground='red')
lbl5.place(x=270,y=200)
#======================

btn_Show= Button(root, text='Show',background='black',font= 'arial 15 bold',foreground='green',width=10,command=area)
btn_Show.place(x=664,y=144)
btn_exit= Button(root, text='Exit',background='black',font= 'arial 15 bold',foreground='green',width=10,command=exit)
btn_exit.place(x=664,y=200)

lal7 = Label(root, text = 'محاسبه مساحت و محیط دایره',font = 'Aldhabi 45 bold' , bg = 'cyan', fg = 'green')
lal7.place(x=50,y=300)

root.mainloop()