# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
from tkinter import *
from tkinter import messagebox
import pyperclip
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    l = random.randint(8,10)
    n = random.randint(2,4)
    s = random.randint(2,4)
    password_letters= [random.choice(letters) for _ in range(l)]
    password_numbers=[random.choice(numbers) for _ in range(n)]
    password_symbols = [random.choice(symbols) for _ in range(s)]
    password_list=password_symbols+password_letters+password_symbols
    random.shuffle(password_list)
    npassword = "".join(password_list)


    ptext.insert(0,npassword)
    pyperclip.copy(npassword)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
def save_file():
    website=web.get()
    email=eid.get()
    password=ptext.get()
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Missing Fields")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered \nEmail:{email}\n Password:{password}\n Is it ok to save")
        if is_ok==1:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} |{password}\n")
                web.delete(0,END)
                ptext.delete(0,END)




window.title("Password Generator")
window.config(padx=20,pady=20)
canvas=Canvas(width=200,height=200)
image_logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image_logo)
canvas.grid(row=0,column=1)
website=Label(text="Website")
website.grid(row=1,column=0)
web=Entry(width=45)
web.grid(row=1,column=1,columnspan=2)
web.focus()
email=Label(text="Email/Username")
email.grid(row=2,column=0)
eid=Entry(width=45)
eid.grid(row=2,column=1,columnspan=2)
eid.insert(END,"vishallimaini@gmail.com")
password=Label(text="Password")
password.grid(row=3,column=0)
ptext=Entry(width=25)
ptext.grid(row=3,column=1)
button=Button(text="Generate Password" ,command=password_gen)
button.grid(row=3,column=2)
add=Button(text="Add",width=40,command=save_file)
add.grid(row=4,column=1,columnspan=2)





















window.mainloop()
