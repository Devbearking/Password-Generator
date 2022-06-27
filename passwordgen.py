from random import *
from tkinter import *

num="0123456789"
alphanum="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(alphanum.lower())
spalphanum="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#@+"

# passlen = int (input ("enter password lenght \n"))
# randPass = []

# print("Select the type of password \nl. Numbers\n2. Alphanum\n3. Special alphanumeric\n")
# Selecttype = int(input())    

# if Selecttype == 1: 
#     for i in range(passlen) :
#         randPass.append (choice (num))
# elif (Selecttype == 2):
#     for i in range(passlen) :
#             randPass.append (choice (alphanum))
# else:
#     for i in range(passlen) :
#         randPass.append (choice (spalphanum))

# result = "".join(randPass)

# print("your random passowrd is : "+result)


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









window = Tk()
window.geometry("800x500")
window.title("Random Password Genetaror")

Progname = Label(window,font=('Kristen ITC',15,'bold'),text="Password Genetrator (^_^)",fg="blue")
Progname.grid(row=1,column=3,padx=200,pady=30)

ChooseType = Label (window,font=('Kristen ITC',15,'bold'),text="Choosetype a type among 3")
ChooseType.place(relx=.03,rely=.25)

Tchoise = StringVar()
NumChoise = Radiobutton(window,font=('cornel',10,'italic'),text ="Numeric", variable = Tchoise,value=num) 
NumChoise.place(relx=.3, rely = .35)
AlphaNumChoise = Radiobutton(window,font=('cornel',10,'italic'),text ="AlphaNumeric", variable = Tchoise,value=alphanum) 
AlphaNumChoise.place(relx=.3, rely = .4)
SpecialChoise = Radiobutton(window,font=('cornel',10,'italic'),text ="Special", variable = Tchoise,value=spalphanum) 
SpecialChoise.place(relx=.3, rely = .45)


size =Label (window,text="Size",font=('Copperplate Gothic',10,'bold'))
size.place(relx=.65 , rely =.4 )

pass_length = Spinbox(window,font_=8,to=50)
pass_length.place(relx=.7 , rely=.4)
pass_length.config(state="readonly")



GenButton = Button(window,text = "Generate",command=Create_Pass)
GenButton.place(relx=.45 , rely=.60)

resultBox = Text(window, height=6, width=85, wrap=WORD)
resultBox.place(relx=.08, rely=.7)






window.mainloop()
