from distutils.cmd import Command
from pymongo import MongoClient

from tkinter import *
from tkinter import messagebox


##Creo funzione aggiunta informazioni

 






def create():
    match = match_name.get()
    home = home_name.get()
    pappa=pappa_name.get()
    row={'match':match,'home':home,'pappa':pappa}
    collezione.insert_one(row)

def exi():
    login_screen.destroy()

def addinfo():
    global root
    global match_name
    global home_name
    global pappa_name
    global collezione

    client=MongoClient('192.168.195.109',username=username1,password=password1,authSource='tagging')
    db=client.tagging
    collezione=db.matches

    root=Toplevel(login_screen)
    root.title("INSERIMENTO INFORMAZIONI")
    root.geometry("5000x2500")

    l = Label(root, text="Match:")
    l.grid(row=1,column=1)
    l = Label(root, text="Home:")
    l.grid(row=2, column=1)
    l = Label(root, text="pappa:")
    l.grid(row=3, column=1)
    match_name = Entry(root)
    match_name.grid(row=1, column=2)
    home_name = Entry(root)
    home_name.grid(row=2, column=2)
    pappa_name = Entry(root)
    pappa_name.grid(row=3, column=2)
    b = Button(root, text="Inserisci info", command=create)
    exit=Button(root, text="Clicca se hai finito", command=exi)
    b.grid(row=6, column=3) 
    exit.grid(row=1,column=8)


# Implementazione verifica di login



def login_verify():
    global username1
    global password1
    username1 = username_verify.get()
    password1 = password_verify.get()
    id1=id_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)


    if(username1 == "donato@auth" and password1 == "donGal001"):

        addinfo()

    elif(username1 == "emanuele@auth" and password1 == "emaMir002"):
        addinfo()

    elif(username1 == "lorenzo@auth" and password1 == "lorTar003"):
        addinfo()


    elif(username1 == "andrea@auth" and password1 == "andMau004"):
        addinfo()


    elif(username1 == "marco@auth" and password1 == "marCan005"):
        addinfo()


    elif(username1 == "mario@auth" and password1 == "marNic006"):
        addinfo()
    else :
        user_not_found()
    

    
    

# Designing popup per credenziali utente sbagliate
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Cancellamento popup


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing finestra di login 


def login():
    global login_screen
    login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("600x300")
    Label(login_screen, text="Inserisci Username e Password per accedere all'inserimento dei dati").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify
    global id_verify

    username_verify = StringVar()
    password_verify = StringVar()
    id_verify=StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Id * ").pack()
    id_entry = Entry(login_screen, textvariable=id_verify)
    id_entry.pack()
    Label(login_screen, text="").pack()

    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
    login_screen.mainloop()



login()

'''



client=MongoClient('192.168.195.109',username='emanuele@auth',password='emaMir002',authSource='tagging')
db=client.tagging
collezione=db.matches




#row={'match':'Casa','home':'home','pappa':'pappa','id':'3'}

#collezione.insert_one(row)



#for i in collezione.find({"id" : '3'}):
    print(i['match'])




key = '3'

if collezione.count_documents({'id':key}):
    print("item is existed")
    for i in collezione.find({"id" : key}):
        cas=i['match']
    client.close()
    client=MongoClient('192.168.195.109',username='emanuele@auth',password='emaMir002',authSource='tagging')
    db=client.tagging
    collezione=db.events
    row={'match':'Casa','home':'home','pappa':'pappa','id':'3','casa':cas}
    collezione.insert_one(row)






else:
    print("item is not existed")


print(cas)

'''