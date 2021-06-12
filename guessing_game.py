import tkinter as tk
top=tk.Tk()
top.title('Guessing_game')
top.geometry("900x900")
top.configure(bg="pink")
t1=tk.Label(top,text="Welcome to Guessing Game",bg="black",fg="red",bd=10,font=("italic",44))
t2=tk.Button(top,text="Let's start the game",bg="orange",fg="black",bd=12,font=("italic",36))

g1=tk.Button(top,text="Guess the Secret number",bg="skyblue",fg="purple",bd=8,font=("italic",25))

import random
def secret():
    global secret_number
    secret_number=random.randint(0,9)
    print(secret_number)
secret()
# print(type(secret_number))

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    # inp = inputtxt.get(1)

    # print(type(inp))
    if inp==str(secret_number) and len(inp)==1:
        lbl.config(text = "Congratulations You have Guessed Secret number  : "+inp)
    elif inp!=str(secret_number) and len(inp)==1:
        lbl.config(text="Wrong Guess\nThe Secret number is : "+str(secret_number))
inputtxt = tk.Text(top,height = 3,width = 10,bg="white",fg="purple",bd=8,font=("italic",16))
printButton = tk.Button(top,text = "CheckBox",bg="lightgreen",fg="blue", command = printInput,font=("italic",28))


# def restart():
#     secret()
#     printButton.config(text="CheckBox")
#     # printInput()


t2.pack()
g1.pack()
inputtxt.pack()
printButton.pack()
lbl = tk.Label(top, text = "",bg="purple",fg="pink",font=("italic",40))
lbl.pack()
# restart1=tk.Button(top,text="RESTART",bg="grey",fg="purple",bd=8,font=("italic",18),command=restart)
# restart1.pack(side="bottom")
top.mainloop()
