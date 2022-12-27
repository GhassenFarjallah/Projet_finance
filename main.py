from tkinter import * 
from  tkinter import ttk
from datetime import date

import datetime







def Date_valeur(Date_oper,Oper):
    #mois= ['0','1','2','3','4','5','6','7','8','9','10','11','12']
    #jour = ['0','31','30','31','30','31','30','31','31','30','31','30','31']
    LDO=Date_oper.split('/')
    jour_oper = int(LDO[0])
    mois_oper = int(LDO[1])
    annee_oper = int(LDO[2])
    date=datetime.date(annee_oper, mois_oper, jour_oper)
    if (Oper =="V"):
        date = date + datetime.timedelta(days=7)
         
    else:
        date = date - datetime.timedelta(days=7)
    LDO=str(date).split('-')

    return str(LDO[2])+"/"+str(LDO[1])+"/"+str(LDO[0])



def soldeF(C,VR,Oper,Date_val1,Date_2):
    if VR=="R":Oper=-1*Oper
    #Date_val1 : date valeur de la ligne precedente(operation precedente)
    #Date_2 : date operation de la ligne courante(operation courante)
    #Date_val2 : date valeur de la ligne courante
    #Oper: operation courante
    global TRE

    L1=Date_val1.split("/")
    jour_val1 = L1[0]
    mois_val1 = L1[1]
    annee_val1 = L1[2]
    

    Date_val2 = Date_valeur(Date_2,VR)  
    L2=Date_val2.split("/")  
    jour_val2 = L2[0]
    mois_val2 = L2[1] 
    annee_val2 = L2[2]

    
    
    a2 = int(annee_val2)
    mm2 = int(mois_val2)
    jj2 = int(jour_val2)
    

    
    a1 = int(annee_val1)
    mm1 = int(mois_val1)
    jj1 = int(jour_val1)


    nb_jours = abs(int( (date(a2,mm2,jj2)-date(a1,mm1,jj1)).total_seconds()/(24*60*60)))
    #nb_jours = date(int(jour_val1),int(mois_val1),int(annee_val1))-date(int(jour_val2),int(mois_val2),int(annee_val2))
    solde_apres_oper = (TRE*C*nb_jours)/36000
    return solde_apres_oper+C+Oper













#validation puis calcul
def function():
    global TRE,date_debut,date_fin,solde,TRE,iid
    global label_solde,label_TRE,label_date_douverture
    global solde_var,TRE_var,date_douverture_var
    global entree_solde,entree_TRE,entree_date_douverture
    global continueButton,submitButton,ajout_operation_button,confirmer_ajout_button
    global table
    global fenetre,ajout_fenetre
    global row_names
    global une_operation_grid,operation


    
    booll=True
    try:
        solde = float(solde_var.get())
        label_solde.configure(fg='black')
        
    except :
        solde=""
        booll=False
        label_solde.configure(fg='red')
    if solde!="":
        label_solde.config(text="Votre solde est: {}".format(solde))

    try:
        label_TRE.configure(fg='black')
        TRE=float(TRE_var.get())
    except: 
        TRE=""
        label_TRE.configure(fg='red')
        booll=False
    if TRE!="":
        label_TRE.config(text="TRE : {}".format(TRE))

    date_format = '%d/%m/%Y'


    try:
        label_date_douverture.configure(fg='black')
        date_douverture=date_douverture_var.get()
        dateObject = datetime.datetime.strptime(date_douverture, date_format)
        

    except:
        label_date_douverture.configure(fg='red')
        booll=False 

    if (booll) :
        #remove the solde and tre and valider button and date dinscription
        entree_solde.place_forget()
        entree_TRE.place_forget()
        continueButton.place_forget()
        submitButton.place_forget()
        entree_date_douverture.place_forget()
        label_date_douverture.place_forget()
        #####
        label_TRE.place(relx=0.35, rely=0.05, anchor=NW)

        ajout_operation_button = Button(fenetre, text="Ajout Operation", command=ajout,bg='#fff',font=12, fg='#060b11')
        ajout_operation_button.place(relx=0.05, rely=0.15, anchor=NW)
        operation=['','','','','','']
        operation[0]=iid
        operation[1]="V"
        operation[2]=round(solde, 2)
        operation[3]=round(solde, 2)
        operation[4]=date_douverture
        operation[5]=date_douverture

        table.insert(parent='',index='end',iid=iid,text='',values=operation)
        iid+=1


def start():
    global TRE,date_debut,date_fin,solde,TRE,iid
    global label_solde,label_TRE,label_date_douverture
    global solde_var,TRE_var,date_douverture_var
    global entree_solde,entree_TRE,entree_date_douverture
    global continueButton,submitButton,ajout_operation_button,confirmer_ajout_button
    global table
    global fenetre,ajout_fenetre
    global row_names
    global une_operation_grid,operation

    #remove the welcome screen part
    label.place_forget()
    continueButton.place_forget()
    #####
    #solde
    solde_var=StringVar()
    label_solde = Label(fenetre, text="Entrée votre solde",bg='white', fg='#060b11',font=5)
    label_solde.place(relx=0.05, rely=0.05, anchor=NW)
    entree_solde =Entry(fenetre,textvariable=solde_var,font=5)
    entree_solde.insert(0, "300")
    entree_solde.place(relx=0.05, rely=0.1, anchor=NW)

    #tre
    TRE_var=StringVar()
    label_TRE = Label(fenetre, text="Entrée TRE",bg='white', fg='#060b11',font=5)
    label_TRE.place(relx=0.05, rely=0.15, anchor=NW)
    entree_TRE =Entry(fenetre,textvariable=TRE_var,font=5)
    entree_TRE.insert(0,"2.25")
    entree_TRE.place(relx=0.05, rely=0.2, anchor=NW)

    #date d'ouverture du compte
    date_douverture_var=StringVar()
    
    label_date_douverture = Label(fenetre, text="Entrée la date d'ouverture du compte",bg='white', fg='#060b11',font=5)
    label_date_douverture.place(relx=0.05, rely=0.25, anchor=NW)
    entree_date_douverture =Entry(fenetre,textvariable=date_douverture_var,font=5)
    entree_date_douverture.insert(0,"12/03/2000")
    entree_date_douverture.place(relx=0.05, rely=0.3, anchor=NW)



    #bouton_validation_et_calcul
    submitButton = Button(fenetre, text="Valider", command=function,bg='white', fg='#060b11',font=5)
    submitButton.place(relx=0.05, rely=0.35, anchor=NW)

    #table initialisation
    table_frame = Frame(fenetre)
    table_frame.place(relx=0.5, rely=0.88, anchor=S)

    table = ttk.Treeview(table_frame)
    style = ttk.Style()
    style.configure("Treeview.Heading", font=(None, 14))
    style.configure('.', font=(None, 12))
    table['columns'] = ('Operation_N°', 'V/R','Operation', 'Solde', 'Date_operation', 'Date_valeur')

    table.column("#0", width=0,  stretch=NO)
    table.column('Operation_N°',anchor=CENTER, width=50)
    table.column('V/R',anchor=CENTER,width=50)
    table.column('Operation',anchor=CENTER,width=100)
    table.column('Solde',anchor=CENTER,width=100)
    table.column('Date_operation',anchor=CENTER,width=140)
    table.column('Date_valeur',anchor=CENTER,width=130)

    table.heading("#0",text="",anchor=CENTER)
    table.heading('Operation_N°',text='N°',anchor=CENTER)
    table.heading('V/R',text='V/R',anchor=CENTER)
    table.heading('Operation',text='Operation',anchor=CENTER)
    table.heading('Solde',text='Solde',anchor=CENTER)
    table.heading('Date_operation',text='Date opération',anchor=CENTER)
    table.heading('Date_valeur',text='Date valeur',anchor=CENTER)

    # table.insert(parent='',index='end',iid=0,text='',values=('1','V','101564','101564','12/12/2022', '12/24/2022'))
    # table.insert(parent='',index='end',iid=1,text='',values=('2','R','105422','101564','12/12/2022', '12/24/2022'))
    # table.insert(parent='',index='end',iid=2,text='',values=('3','V','103','101564', '12/12/2022', '12/24/2022'))
    # table.insert(parent='',index='end',iid=3,text='',values=('4','V','254104','101564','12/12/2022' , '12/24/2022'))
    # table.insert(parent='',index='end',iid=4,text='',values=('5','V','12505','101564','12/12/2022', '12/24/2022'))
    # table.insert(parent='',index='end',iid=5,text='',values=('6','R','12506','101564','12/12/2022' , '12/24/2022'))

    table.pack()
    
def ajout():
    global TRE,date_debut,date_fin,solde,TRE,iid
    global label_solde,label_TRE,label_date_douverture
    global solde_var,TRE_var,date_douverture_var
    global entree_solde,entree_TRE,entree_date_douverture
    global continueButton,submitButton,ajout_operation_button,confirmer_ajout_button
    global table
    global fenetre,ajout_fenetre
    global row_names
    global une_operation_grid,operation


    ajout_fenetre=Tk()
    ajout_fenetre.iconbitmap("icon.ico")
    ajout_fenetre.title("Ajout Operation")
    row_names=["Versement ou Retrait","Operation","Date Operation"]
    for i in range(1):
        for j in range(3):
            e = Label(ajout_fenetre,text=row_names[j],font=4)
            e.grid(row=i, column=j, sticky=NSEW)

    une_operation_grid = []
    for j in range(3):
        e = Entry(ajout_fenetre,relief=RIDGE,font=4)
        e.grid(row=2, column=j, sticky=NSEW)
        if j==0:e.insert(END, "R")
        if j==1:e.insert(END, "100")
        if j==2:e.insert(END, "30/06/2000")
        une_operation_grid.append(e)
    
    
    confirmer_ajout_button = Button(ajout_fenetre, text="Confirmer", command=confirmer_ajout,bg='#fff',font=12, fg='#060b11')
    confirmer_ajout_button.grid(row=3, column=0 )



def confirmer_ajout():
    global TRE,date_debut,date_fin,solde,TRE,iid
    global label_solde,label_TRE,label_date_douverture
    global solde_var,TRE_var,date_douverture_var
    global entree_solde,entree_TRE,entree_date_douverture
    global continueButton,submitButton,ajout_operation_button,confirmer_ajout_button
    global table
    global fenetre,ajout_fenetre
    global row_names
    global une_operation_grid,operation

    operation[0]=iid
    
    
    ValidInput=True
    i=0
    for col in une_operation_grid:
        try :
            if i==0 :
                if ("ver" in str(col.get()).lower() or "v" in str(col.get()).lower()):operation[1]="V"
                elif "r" in str(col.get()).lower():operation[1]="R"

                else :ValidInput=False
            if i==1:
                try:
                    operation[2]=float(col.get())        
                except:
                    ValidInput=False
            if i==2:

                date_format = '%d/%m/%Y'

                # using try-except blocks for handling the exceptions
                try:
                    date_operation=col.get()
                    # formatting the date using strptime() function
                    dateObject = datetime.datetime.strptime(date_operation, date_format)
                    operation[4]=date_operation
                except:
                    ValidInput=False
            
        except:
            ValidInput=False
        if not ValidInput:break
        i+=1

    if ValidInput:
        ajout_fenetre.destroy()
        Date_val1=operation[5]
        operation[3]=round(soldeF(solde,operation[1],operation[2],Date_val1,operation[4]),2)
        operation[5]=Date_valeur(date_operation,operation[1])
        solde=operation[3]
        table.insert(parent='',index='end',iid=iid,text='',values=operation)
        label_solde.config(text="Votre solde est: {}".format(solde))
        iid+=1
    else:
        label_invaled_input = Label(ajout_fenetre, text="Erreur, verifier vos données dans la case {}".format(1+i),bg='#fff',font=12, fg='#FF0000')
        label_invaled_input.grid(row=3, column=1 )

solde=0
TRE=0
iid=1
#initialisation 
fenetre = Tk()
fenetre.geometry("1050x650")
# Add image file
bg = PhotoImage(file = "Main_bg.png")
# Show image using label
label1 = Label( fenetre, image = bg,width=1700,height=1000)
label1.place(x = 0, y = 0)
#icon
fenetre.iconbitmap("icon.ico")


#menu bar
# Create menubar by setting the color
menubar = Menu(fenetre, background='#060b11', fg='white')
#app title
fenetre.title("Projet Finance")

# Declare file and edit for showing in menubar
file = Menu(menubar, tearoff=False, background='#060b11',fg='white')
  
# Add commands in in file menu
file.add_command(label="Exit", command=fenetre.quit)
# Display the file and edit declared in previous step
menubar.add_cascade(label="File", menu=file,background='#060b11')
fenetre.config(menu=menubar)

#bienvenue text
label = Label(fenetre, text="Bienvenue !",bg='white', fg='#060b11',font=('Helvetica bold', 40))
label.place(relx=0.5, rely=0.47, anchor=CENTER)
#continue button
continueButton = Button(fenetre, text="Continuer", command=start,bg='#fff',font=12, fg='#060b11')
continueButton.place(relx=0.5, rely=0.57, anchor=CENTER)
txt="Projet réaliser par :\nSaad Mohamed Khalil & Farjallah Ghassen.\n"
label_names = Label(fenetre, text=txt,bg='#fff', fg='#000',font=('Helvetica bold', 12),highlightbackground="black",highlightthickness=2)
label_names.place(relx=0.98, rely=0.99, anchor=SE)







fenetre.mainloop()



