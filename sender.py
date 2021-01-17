from tkinter import *
import pywhatkit

def whatsapp():
    number1="+91"+number.get()
    message1=message.get()
    hrs1=int(hrs.get())
    min2=int(min1.get())
    
    pywhatkit.sendwhatmsg(number1,message1,hrs1,min2)

window=Tk()
window.title('whatsapp')
window.geometry('500x300')
txt=Label(window,text="Number")
txt.grid(row=0,column=0)
number=Entry(window,width=10)


txt1=Label(window,text="Message")
txt1.grid(row=1,column=0)
message=Entry(window,width=10)


txt2=Label(window,text="hrs")
txt2.grid(row=2,column=0)
hrs=Entry(window,width=10)


txt3=Label(window,text="Min")
txt3.grid(row=3,column=0)
min1=Entry(window,width=10)

min2=min1.get()


number.grid(row=0,column=5)
message.grid(row=1,column=5)
hrs.grid(row=2,column=5)
min1.grid(row=3,column=5)



send=Button(window,text="Send",command=whatsapp)
send.grid(row=5,column=6)
window.mainloop()