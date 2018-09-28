from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("ChackBoard Sums")
window.geometry("600x500")
def clicked(alphabet):
    if ans_btn1["text"]==" ":
        print(alphabet)
        ans_btn1["text"]=alphabet;
    elif ans_btn2["text"]==" " and ans_btn1["text"]!=" ":
        ans_btn2["text"] = alphabet;
    elif ans_btn3["text"]==" " and ans_btn2["text"]!=" ":
        ans_btn3["text"] = alphabet;
    elif ans_btn4["text"]==" " and ans_btn3["text"]!=" ":
        ans_btn4["text"] = alphabet;
    elif ans_btn5["text"]==" " and ans_btn4["text"]!=" ":
        ans_btn5["text"] = alphabet;

def validation():
    var1=ans_btn1["text"]
    opr=ans_btn2["text"]
    var2=ans_btn3["text"]
    equal=ans_btn4["text"]
    ans=ans_btn5["text"];
    if equal=="=":
        if opr=="+":
            if int(var1)+int(var2)==int(ans):
                print_msg();
        if opr=="-":
            if int(var1)-int(var2)==int(ans):
                print_msg();
        if opr=="*":
            if int(var1)*int(var2)==int(ans):
                print_msg();
        if opr=="/":
            if int(var1)/int(var2)==int(ans):
                print_msg();
        if opr=="%":
            if int(var1)%int(var2)==int(ans):
                print_msg();


def print_msg():
    messagebox.showinfo("Congratulations!!!!", "Your answer is correct")
    ans_btn1["text"] = " "
    ans_btn2["text"] = " "
    ans_btn3["text"] = " "
    ans_btn4["text"] = " "
    ans_btn5["text"] = " "


btn1 = Button(window, text="7",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("7"))
btn1.grid(column=1, row=1)
btn2 = Button(window, text="6",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("6"))
btn2.grid(column=2, row=1)
btn3 = Button(window, text="5",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("5"))
btn3.grid(column=3, row=1)
btn4 = Button(window, text="-",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("-"))
btn4.grid(column=4, row=1)
btn5 = Button(window, text="3",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("3"))
btn5.grid(column=5, row=1)

btn1 = Button(window, text="%",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("%"))
btn1.grid(column=1, row=2)
btn2 = Button(window, text="2",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("2"))
btn2.grid(column=2, row=2)
btn3 = Button(window, text="/",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("/"))
btn3.grid(column=3, row=2)
btn4 = Button(window, text="1",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("1"))
btn4.grid(column=4, row=2)
btn5 = Button(window, text="*",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("*"))
btn5.grid(column=5, row=2)

btn1 = Button(window, text="10",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("10"))
btn1.grid(column=1, row=3)
btn2 = Button(window, text="11",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("11"))
btn2.grid(column=2, row=3)
btn3 = Button(window, text="+",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("+"))
btn3.grid(column=3, row=3)
btn4 = Button(window, text="16",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("16"))
btn4.grid(column=4, row=3)
btn5 = Button(window, text="4",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("4"))
btn5.grid(column=5, row=3)

btn1 = Button(window, text="=",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("="))
btn1.grid(column=1, row=4)
btn2 = Button(window, text="1",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("1"))
btn2.grid(column=2, row=4)
btn3 = Button(window, text="3",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("3"))
btn3.grid(column=3, row=4)
btn4 = Button(window, text="8",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("8"))
btn4.grid(column=4, row=4)
btn5 = Button(window, text="14",bg="grey", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("14"))
btn5.grid(column=5, row=4)

label=Label(window,text="Write Answer Here..")
label.grid(column=1,row=5,columnspan=5)

ans_btn1 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
ans_btn1.grid(column=1, row=6)
ans_btn2 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
ans_btn2.grid(column=2, row=6)
ans_btn3 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
ans_btn3.grid(column=3, row=6)
ans_btn4 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
ans_btn4.grid(column=4, row=6)
ans_btn5 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
ans_btn5.grid(column=5, row=6)
ans_submit = Button(window, text="submit",bg="green", fg="white",width=5,height=2,font=('Helvetica','15'),command=validation)
ans_submit.grid(column=6, row=6)


window.mainloop()
