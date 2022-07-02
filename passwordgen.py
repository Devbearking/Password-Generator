from random import *
from tkinter import *

num="0123456789"
alphanum="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(alphanum.lower())
spalphanum="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#@+"

def Create_Pass():
    TheChoise = Tchoise.get()

    if TheChoise =="":
        resultBox.delete(0.0,END)
        resultBox.insert(END,"\n Select the type of password you'd like")

    lenght = int(pass_length.get())
    randPass = []
    for i in range(lenght):
        randPass.append(choice(TheChoise))
    
    result = "".join(randPass)

    TheResult = "\n *** Your Password is : "+result+" ***\n"

    resultBox.delete(0.0,END)
    resultBox.insert(END,TheResult)




def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb




window = Tk()
window.config(bg=rgb_hack((173,216,230)))
window.geometry("800x500")
window.title("Random Password Genetaror")

Progname = Label(window,font=('Comic Sans MS',15,'bold'),text="Password Genetrator",fg="blue",bg='SkyBlue')
Progname.grid(row=1,column=3,padx=200,pady=30)

ChooseType = Label (window,font=('Comic Sans MS',15,'bold'),text="Choosetype a type among 3",bg='SkyBlue')
ChooseType.place(relx=.1,rely=.25)

Tchoise = StringVar()
NumChoise = Radiobutton(window,font=('cornel',10,'italic'),text ="Numeric", variable = Tchoise,value=num,bg='SkyBlue')
NumChoise.place(relx=.1, rely = .35)
AlphaNumChoise = Radiobutton(window,font=('cornel',10,'italic'),text ="AlphaNumeric", variable = Tchoise,value=alphanum,bg='SkyBlue')
AlphaNumChoise.place(relx=.1, rely = .4)
SpecialChoise = Radiobutton(window,font=('cornel',10,'italic'),text ="Special", variable = Tchoise,value=spalphanum,bg='SkyBlue')
SpecialChoise.place(relx=.1, rely = .45)


size =Label (window,text="Size",font=('Copperplate Gothic',10,'bold'),bg='SkyBlue')
size.place(relx=.55 , rely =.4 )

pass_length = Spinbox(window,font=8,to=50)
pass_length.place(relx=.6 , rely=.4)
pass_length.config(state="readonly")



GenButton = Button(window,text = "Generate",command=Create_Pass,bg='SkyBlue')
GenButton.place(relx=.45 , rely=.60)

resultBox = Text(window, height=6, width=85, wrap=WORD,bg='SkyBlue')
resultBox.place(relx=.08, rely=.7)






window.mainloop()
