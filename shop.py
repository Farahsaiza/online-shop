import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk 
import mysql.connector

connection = mysql.connector.connect(host='localhost',port='3306', user='root',password='******',database='farahshop')
c= connection.cursor()

global nameentry
global lastentry
global adentry
global emailtry
global phoneentry
global qtentry
global cardtry
global pourtry
global colorentry
global itemchoosen
global sizechoosen
global Paimentent
global  promoen


class  id():
    idcust=0
    def __init__(self):
        id.idcust= id.idcust+1

def buy():
    global idc
    idc=id.idcust
    idc= idc+1
    

   
    top = Toplevel()
    top.title("BUY NOW")
    top.geometry("1000x600")
    top.config(bg="#D8AC9C")
    global nameentry
    global lastentry
    global adentry
    global emailtry
    global phoneentry
    global qtentry
    global cardtry
    global pourtry
    global colorentry
    global itemchoosen
    global sizechoosen
    global Paimentent
    global  promoen

    promoen= tk.StringVar()
    promoen.set("Yes No")

    def choice_var():
        p=promoen.get()
        if  p== "Yes":
            pourtry.config(state=tk.NORMAL)

        else:
            pourtry.config(state=tk.DISABLED)

    def regist():
        

        global prix
        it=itemchoosen.get()
        qt=qtentry.get()
        if it == "Beige Pant" or it=="green T-shirt" or it=="wedding shoes":
            prix =  300 * int(qt)
        elif it =="green Pant":
            prix =  350 * int(qt)
        elif it =="bluesky dress":
            prix =  400 * int(qt)
        elif it =="black dress":
            prix =  750 * int(qt)
        elif it =="Brown bag":
            prix =  500 * int(qt)
        elif it =="hair accessories":
            prix =  120 * int(qt)
        elif it =="pink shoes":
            prix =  290 * int(qt)
        elif it =="beige hat":
            prix =  150 * int(qt)
        elif it=="long skirt" or it=="striped shirt":
            prix =  250 * int(qt)
        
        pricetry.config(text=prix)
        
    # Beige Pant',' green Pant',' black dress',' bluesky dress',' long skirt',' striped shirt',' green T-shirt',' wedding shoes',' Brown bag',' hair accessories',' pink shoes',' beige hat') 
        
        global finalprice
        pourcentage=promoen.get()
        po=pourtry.get()
        if pourcentage == "Yes":
            finalprice  = (prix - (prix*(int(po)/100)))
        else:
            finalprice = prix
        
        finaltry.config(text=finalprice)





        First=nameentry.get()
        last=lastentry.get()
        adresse=adentry.get()
        email=emailtry.get()
        phone=phoneentry.get()
        card=cardtry.get()
        promo=pourtry.get()
        item=itemchoosen.get()
        q=qtentry.get()
        col=colorentry.get()
        size=sizechoosen.get()
        pay=Paimentent.get()
        code=promoen.get()




        tablePersonal.insert("",'end', values=(  First , last, adresse,email , phone,item,q,col,size,pay,card,code,promo,finalprice))
        

        connection = mysql.connector.connect(host='localhost',port='3306', user='root',password='Farah@123',database='farahshop')
        c= connection.cursor()

        
        FirstName=nameentry.get()
        LastName=lastentry.get()
        Adresse=adentry.get()
        Email=emailtry.get()
        PhoneNumber=phoneentry.get()
        cardNumber=cardtry.get()
        discount=pourtry.get()
        item=itemchoosen.get()
        quantity=qtentry.get()
        color=colorentry.get()
        size=sizechoosen.get()
        payment=Paimentent.get()
        codePromo=promoen.get()

        data = "INSERT INTO customer(FirstName,LastName,Adresse,Email,PhoneNumber,Item,Quantity,Color,Size,PaymentType,CardNumber,CodePromo,Discount,Price) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        vals=(FirstName, LastName,Adresse,Email,PhoneNumber,item,quantity,color,size,payment,cardNumber,codePromo,discount,finalprice)         
        c.execute(data,vals)
        connection.commit()
        c.close()
        connection.close()


    def products():
        global emailentry
        def  slct():

            x=emailentry.get()
            sql=("SELECT Item , Quantity , Color , Size , Price , Date FROM customer  WHERE Email =%s ")
            vals=(x,)
            c.execute(sql,vals)
            result=c.fetchall()

            

            for row in result:
                a=str((row[0]))
                b=str((row[1]))
                g=str((row[2]))
                d=str((row[3]))
                e=str((row[4]))
                f=str((row[5]))
                prod.insert("",END, values=(a,b,g,d,e,f))


        canv1 = Canvas(top ,bg="#D8AC9C",cursor="heart",highlightthickness=0)
        canv1.place(x=0,y=80,height=400,width=1500)

        title=  tk.Label(top, text="We appreciate your choice - thank you for giving us a voice.",font="Vivaldi 20 bold", fg="#F4EEED" , bg="#D8AC9C" )
        title.place(x=450 ,y=70)

        info=Label(top, text="To see  your products please fill out the fields below :",bg="#D8AC9C",fg="#F4EEED" ,font="courier 16 ")
        info.place(x=10,y=130)

        name = Label(top,text = "First Name ",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
        name.place (x=10,y=200)
        P = Label(top,text = ":",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
        P.place (x=130,y=200)
        nameentry= Entry(top,  bg="#F4EEED" , fg="black",font="Courier 12 ")
        nameentry.place(x=150,y=200,width=200)

        last = Label(top,text="Last Name",bg="#D8AC9C",fg="#F4EEED",font="courier 14 ")
        last.place( x=390 , y=200)
        P = Label(top,text = ":",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
        P.place (x=510,y=200)
        lastentry= Entry(top,bg="#F4EEED",fg="black",font="courier 12 ")
        lastentry.place(x=530,y=200,width=200)

        Email = Label(top,text="Your Email",bg="#D8AC9C",fg="#F4EEED",font="courier 14 ")
        Email.place( x=10 , y=250)
        P = Label(top,text = ":",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
        P.place (x=130,y=250)
        emailentry= Entry(top,bg="#F4EEED",fg="black",font="courier 12 ")
        emailentry.place(x=150,y=250,width=580)

        
        


        
        
            


        style = ttk.Style()
        style.theme_use('clam')
        style.map('Treeview',background=[('selected',"#D8AC9C")])

        prod = ttk.Treeview(top ,cursor="heart", columns=('Item','Quantity','Color','Size','Price','Date')  , show='headings')
        prod.heading('Item' , text=  ' Item')
        prod.heading('Quantity' , text= 'Quantity')
        prod.heading('Color' , text= 'Color')
        prod.heading('Size' , text= ' Size')
        prod.heading('Price' , text= ' Price')
        prod.heading('Date' , text= ' Date')

        prod.place(x=5 , y=350,height=300,width=1350)
        select=tk.Button(top, text="SEE MY PRODUCTS",font="terminal 15 " ,bg="#EFD9D1",borderwidth=2,  cursor="heart",fg="#999B84",padx=10,command=slct , activebackground="#EFD9D1")
        select.place(x=400  ,  y=300)

    
    def deltreev():
        # selected_item = tablePersonal.selection()[0] ## get selected item

        selected = tablePersonal.selection()[0]
        

        x = emailtry.get()
        sql = "DELETE FROM customer WHERE Email = %s"
        vals=(x,)
        c.execute(sql,vals)
        connection.commit() 
        tablePersonal.delete(selected)

    def clear():
        nameentry.delete(0,END)
        lastentry.delete(0,END)
        adentry.delete(0,END)
        emailtry.delete(0,END)
        phoneentry.delete(0,END)
        cardtry.delete(0,END)
        itemchoosen.delete(0,END)
        qtentry.delete(0,END)
        sizechoosen.delete(0,END)
        pourtry.delete(0,END)
        finaltry.config(text=0)
        pricetry.config(text=0)
        promoen.set(None)
        colorentry.set(None)
        Paimentent.set(None)



        
    # def display():
    #     c.execute="SELECT FirstName,LastName,Adresse,Email,PhoneNumber,Item,Quantity,Color,Size,PaymentType,CardNumber,CodePromo,Discount,Price FROM customer"
    #     result=c.fetchall

    #     for row in result : 
    #         a=str((row[0]))
    #         b=str((row[1]))
    #         g=str((row[2]))
    #         d=str((row[3]))
    #         e=str((row[4]))
    #         f=str((row[5]))
    #         g=str((row[6]))
    #         h=str((row[7]))
    #         i=str((row[8]))
    #         j=str((row[9]))
    #         k=str((row[10]))
    #         l=str((row[11]))
    #         m=str((row[12]))
    #         n=str((row[13]))
            
    #         tablePersonal.insert("",'end', values=(a,b,g,d,e,f,g,h,i,j,k,l,m,n))



        


    def ext():
        def ex():
         top.destroy()
         top1.destroy()


        top1 = Toplevel()
        top1.title("EXIT")
        top1.geometry("300x200")
        top1.config(bg="#D8AC9C")

        text=tk.Label(top1,text="Thank you",font="Vivaldi 30 bold" ,cursor="heart",  bg="#D8AC9C", fg="#999B84", padx=10)
        text.pack(side="top")
        text2=tk.Label(top1,text="for your order",font="terminal 15 " ,bg="#D8AC9C",borderwidth=0,  cursor="heart",fg="#999B84",padx=10,command=None , activebackground="#EFD9D1")
        text2.pack()

        EXITbt=tk.Button(top1, text="EXIT",font="terminal 15 " ,bg="#EFD9D1",borderwidth=2,  cursor="heart",fg="#999B84",padx=10,command=ex , activebackground="#EFD9D1")
        EXITbt.place(x=120  ,  y=100)

    




    topframe  =  tk.Frame(top , bg="#EFD9D1", height=80)
    topframe.pack(side="top" , fill=tk.X)

    logo= tk.Label(topframe, text="FarahShop" , font="Vivaldi 20 bold" ,cursor="heart",  bg="#EFD9D1", fg="#999B84",height=2 , padx=20)
    logo.pack(side="left")

    navbtn1= tk.Button(topframe, text="HOME",font="terminal 15 " ,bg="#EFD9D1",borderwidth=0,  cursor="heart" ,fg="#999B84",padx=10,command=None , activebackground="#EFD9D1")
    navbtn1.place(x=1130  ,  y=23)

    navbtn2= tk.Button(topframe, text="BUY NOW",font="terminal 15 " ,bg="#EFD9D1",borderwidth=0,  cursor="heart",fg="#999B84",padx=10,command=None , activebackground="#EFD9D1")
    navbtn2.place(x=1200  ,  y=23)

    navbtn3= tk.Button(topframe, text="EXIT",font="terminal 15 " ,bg="#EFD9D1",borderwidth=0,  cursor="heart",fg="#999B84",padx=10,command=ext, activebackground="#EFD9D1")
    navbtn3.place(x=1300  ,  y=23)

    #personal data
    
    title1=tk.Label(top, text="Personal data:", fg="#999B84", font=" Courier 18 bold",bg="#D8AC9C")
    title1.place(x=30,y=80)

   
    name = Label(top,text = "First Name ",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
    name.place (x=30,y=110)
    P = Label(top,text = ":",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
    P.place (x=180,y=110)
    nameentry= Entry(top,  bg="#F4EEED" , fg="black",font="Courier 12 ")
    nameentry.place(x=200,y=110)

    last = Label(top,text="Last Name",bg="#D8AC9C",fg="#F4EEED",font="courier 14 ")
    last.place( x=30 , y=140)
    P = Label(top,text = ":",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
    P.place (x=180,y=140)
    lastentry= Entry(top,bg="#F4EEED",fg="black",font="courier 12 ")
    lastentry.place(x=200,y=140,width=200)

    ad = Label(top,text="Adresse",bg="#D8AC9C",fg="#F4EEED",font="courier 14 ")
    ad.place( x=30 , y=170)
    P = Label(top,text = ":",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
    P.place (x=180,y=170)
    adentry= Entry(top,bg="#F4EEED",fg="black",font="courier 12 ")
    adentry.place(x=200,y=170,width=200)

    email = Label(top,text="Email",bg="#D8AC9C",fg="#F4EEED",font="courier 14 ")
    email.place( x=30 , y=200)
    P = Label(top,text = ":",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
    P.place (x=180,y=200)
    emailtry= Entry(top,bg="#F4EEED",fg="black",font="courier 12 ")
    emailtry.place(x=200,y=200,width=200)

    phone = Label(top,text="Phone Number",bg="#D8AC9C",fg="#F4EEED",font="courier 14 ")
    phone.place( x=30 , y=230)
    P = Label(top,text = ":",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
    P.place (x=180,y=230)
    phoneentry= Entry(top,bg="#F4EEED",fg="black",font="courier 12 ")
    phoneentry.place(x=200,y=230,width=200)

    #item info

    title2=tk.Label(top, text="Items info:", fg="#999B84", font=" Courier 18 bold",bg="#D8AC9C")
    title2.place(x=520,y=80)


    item = Label(top,text = "select item ",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
    item.place (x=530,y=110)
    P = Label(top,text = ":",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
    P.place (x=680,y=110)
    n = tk.StringVar() 

    style = ttk.Style()

    style.configure("TCombobox", fieldbackground= "#F4EEED" ,background= "white", fg="#D8AC9C")

    itemchoosen = ttk.Combobox(top, width = 27, textvariable = n, ) 
    itemchoosen['values'] = ('Beige Pant','green Pant','black dress','bluesky dress','long skirt','striped shirt','green T-shirt','wedding shoes','Brown bag','hair accessories','pink shoes','beige hat') 
    itemchoosen.place(x=700,y=110)
    itemchoosen.current()

    Quantite = Label(top,text="Quantity",bg="#D8AC9C",fg="#F4EEED",font="courier 14 ")
    Quantite.place( x=530 , y=140)
    P = Label(top,text = ":",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
    P.place (x=680,y=140)
    qtentry= Entry(top,bg="#F4EEED",fg="black",font="courier 12 ")
    qtentry.place(x=700,y=140,width=182)

    color = Label(top,text="Color",bg="#D8AC9C",fg="#F4EEED" ,font="courier 14 ")
    color.place(x=530 ,y=170)
    P = Label(top,text = ":",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
    P.place (x=680,y=170)


    colorentry = StringVar()
    colorentry.set(None)


    brown = Radiobutton(top,text="" ,variable= colorentry,bg="#D8AC9C", value="brown")
    brown.place(x=700,y=172)
    browntr= Entry(top,bg="#6B240C" )
    browntr.place(x=720,y=174 ,width=20)

    green = Radiobutton(top,text="",variable= colorentry,bg="#D8AC9C", value="green")
    green.place(x=750,y=172)
    greentr= Entry(top,bg="#898121" );
    greentr.place(x=770,y=174 ,width=20)

    pink = Radiobutton(top,text="",variable= colorentry,bg="#D8AC9C", value="pink")
    pink.place(x=800,y=172)
    pinktr= Entry(top,bg="#FF407D" )
    pinktr.place(x=820,y=174 ,width=20)

    blue = Radiobutton(top,text="",variable= colorentry,bg="#D8AC9C", value="blue")
    blue.place(x=850,y=172)
    bluetr= Entry(top,bg="#67C6E3" )
    bluetr.place(x=870,y=174 ,width=20)

    purple = Radiobutton(top,text="",variable= colorentry,bg="#D8AC9C", value="purple")
    purple.place(x=900,y=172)
    mauvetr= Entry(top,bg="#E1AFD1" )
    mauvetr.place(x=920,y=174 ,width=20)

    size = Label(top,text = "size ",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
    size.place (x=530,y=200)
    P = Label(top,text = ":",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
    P.place (x=680,y=200)
    s = tk.StringVar() 
    sizechoosen = ttk.Combobox(top, width = 27, textvariable = s ) 
    sizechoosen['values'] = ('XXS','XS',' S',' M',' L',' XL',' XXL',' XXXL',' XXXXL') 
    sizechoosen.place(x=700,y=200)
    sizechoosen.current()

    prix=0
    price = Label(top,text = "Price ",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
    price.place (x=530,y=230)
    P = Label(top,text = ":",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
    P.place (x=680,y=230)
    pricetry= Label(top,text=prix ,  bg="#D8AC9C" , fg="black",font="Courier 14 ")
    pricetry.place(x=700,y=230)
    dh=Label(top,text = "DH ",bg="#D8AC9C",fg="black",font="courier 14 " )
    dh.place(x=750,y=230)

    #payment

    title3=tk.Label(top, text="payment:", fg="#999B84", font=" Courier 18 bold",bg="#D8AC9C")
    title3.place(x=980,y=80)

    Paiment= Label(top,text="Paiment methods",bg="#D8AC9C",fg="#F4EEED" ,font="courier 14 ").place(x=985 ,y=110)
    P = Label(top,text = ":",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
    P.place (x=1157,y=110)
    Paimentent = StringVar()
    Paimentent.set(None)

    visa= Radiobutton(top,text="visa" ,variable= Paimentent,bg="#D8AC9C", value="visa")
    visa.place(x=1167,y=112)

    master= Radiobutton(top,text="Master Card" ,variable= Paimentent,bg="#D8AC9C", value="master")
    master.place(x=1210,y=112)

    py= Radiobutton(top,text="PayPal" ,variable= Paimentent,bg="#D8AC9C", value="py")
    py.place(x=1300,y=112)

    card= Label(top,text="Card number",bg="#D8AC9C",fg="#F4EEED" ,font="courier 14 ").place(x=985 ,y=140)
    P = Label(top,text = ":",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
    P.place (x=1157,y=140)
    cardtry= Entry(top,bg="#F4EEED",fg="black",font="courier 12 ")
    cardtry.place(x=1170,y=140,width=160)

    promo= Label(top,text="Code Promo",bg="#D8AC9C",fg="#F4EEED" ,font="courier 14 ").place(x=985 ,y=170)
    P = Label(top,text = ":",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
    P.place (x=1157,y=170)

    promoen = StringVar()
    promoen.set(None)

    yes= Radiobutton(top,text="Yes" ,variable= promoen,bg="#D8AC9C", value="Yes",command=choice_var )
    yes.place(x=1190,y=172)

    no= Radiobutton(top,text="No" ,variable= promoen,bg="#D8AC9C", value="No",command=choice_var )
    no.place(x=1250,y=172)

    pour = Label(top,text="Discount amount",bg="#D8AC9C",fg="#F4EEED",font="courier 14 ")
    pour.place( x=985 , y=200)
    P = Label(top,text = ":",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
    P.place (x=1157,y=200)
    pourtry= Entry(top,bg="#F4EEED",fg="black",font="courier 12 ")
    pourtry.place(x=1170,y=200,width=160)
    sign=Label(top,text = "%",bg="#D8AC9C",fg="black",font="courier 14 " )
    sign.place(x=1320, y=200)

    finalprice=0
    final = Label(top,text="Final price",bg="#D8AC9C",fg="#F4EEED",font="courier 14 ")
    final.place( x=985 , y=230)
    P = Label(top,text = ":",bg="#D8AC9C",fg="#F4EEED",font="courier 14 " )
    P.place (x=1157,y=230)
    finaltry= Label(top,text=finalprice,bg="#D8AC9C",fg="black",font="courier 14 ")
    finaltry.place(x=1170,y=230)
    d=Label(top,text = "DH ",bg="#D8AC9C",fg="black",font="courier 14 " )
    d.place(x=1250,y=230)


    


    #treeview

    style = ttk.Style()
    style.theme_use('clam')
    style.map('Treeview',background=[('selected',"#D8AC9C")])

    tablePersonal = ttk.Treeview(top ,cursor="heart", columns=('First name','Last name','Adresse','Email','Phone number','Item','Quantity','Color','size','payment','Card number','Code promo','Discount','Price')  , show='headings')
    tablePersonal.heading('First name' , text= ' First name')
    tablePersonal.heading('Last name' , text= ' Last name')
    tablePersonal.heading('Adresse' , text= ' Adresse')
    tablePersonal.heading('Email' , text=  ' Email')
    tablePersonal.heading('Phone number' , text= ' Phone number')
    tablePersonal.heading('Item' , text=  ' Item')
    tablePersonal.heading('Quantity' , text= 'Quantity')
    tablePersonal.heading('Color' , text= 'Color')
    tablePersonal.heading('size' , text= ' size')
    tablePersonal.heading('payment' , text= ' payment')
    tablePersonal.heading('Card number' , text= 'Card number')
    tablePersonal.heading('Code promo' , text= 'Code promo')
    tablePersonal.heading('Discount' , text= ' Discount')
    tablePersonal.heading('Price' , text= ' Price')

    tablePersonal.place(x=5 , y=350,height=300,width=1350)
    


    #button
    register=tk.Button(top, text="REGISTER",font="terminal 15 " ,bg="#EFD9D1",borderwidth=2,  cursor="heart",fg="#999B84",padx=10,command=regist , activebackground="#EFD9D1")
    register.place(x=50  ,  y=300)

    clearbt=tk.Button(top, text="Clear",font="terminal 15 " ,bg="#EFD9D1",borderwidth=2,  cursor="heart",fg="#999B84",padx=10,command=clear , activebackground="#EFD9D1")
    clearbt.place(x=350  ,  y=300)

    EXITbt=tk.Button(top, text="EXIT",font="terminal 15 " ,bg="#EFD9D1",borderwidth=2,  cursor="heart",fg="#999B84",padx=10,command=exit , activebackground="#EFD9D1")
    EXITbt.place(x=650  ,  y=300)

    deltre=tk.Button(top, text="DELETE",font="terminal 15 " ,bg="#EFD9D1",borderwidth=2,  cursor="heart",fg="#999B84",padx=10,command=deltreev, activebackground="#EFD9D1")
    deltre.place(x=950  ,  y=300)

    product=tk.Button(top, text="SEE MY PRODUCT",font="terminal 15 " ,bg="#EFD9D1",borderwidth=2,  cursor="heart",fg="#999B84",padx=10,command=products, activebackground="#EFD9D1")
    product.place(x=1150  ,  y=300)























    top.mainloop()


def exit():
    def ex():
        root.destroy()


    top = Toplevel()
    top.title("EXIT")
    top.geometry("300x200")
    top.config(bg="#D8AC9C")

    text=tk.Label(top,text="Thank you",font="Vivaldi 30 bold" ,cursor="heart",  bg="#D8AC9C", fg="#999B84", padx=10)
    text.pack(side="top")
    text2=tk.Label(top,text="for your order",font="terminal 15 " ,bg="#D8AC9C",borderwidth=0,  cursor="heart",fg="#999B84",padx=10,command=None , activebackground="#EFD9D1")
    text2.pack()

    EXITbt=tk.Button(top, text="EXIT",font="terminal 15 " ,bg="#EFD9D1",borderwidth=2,  cursor="heart",fg="#999B84",padx=10,command=ex , activebackground="#EFD9D1")
    EXITbt.place(x=120  ,  y=100)




    


root = tk . Tk()
root.title("FarahShop")
root.geometry("1000x600")
root.config(bg="#D8AC9C")







#EFD9D1
topframe  =  tk.Frame(root , bg="#EFD9D1", height=80)
topframe.pack(side="top" , fill=tk.X)

logo= tk.Label(topframe, text="FarahShop" , font="Vivaldi 20 bold" ,cursor="heart",  bg="#EFD9D1", fg="#999B84",height=2 , padx=20)
logo.pack(side="left")

navbtn1= tk.Button(topframe, text="HOME",font="terminal 15 " ,bg="#EFD9D1",borderwidth=0,  cursor="heart" ,fg="#999B84",padx=10,command=None , activebackground="#EFD9D1")
navbtn1.place(x=1130  ,  y=23)

navbtn2= tk.Button(topframe, text="BUY NOW",font="terminal 15 " ,bg="#EFD9D1",borderwidth=0,  cursor="heart",fg="#999B84",padx=10,command=buy, activebackground="#EFD9D1")
navbtn2.place(x=1200  ,  y=23)

navbtn3= tk.Button(topframe, text="EXIT",font="terminal 15 " ,bg="#EFD9D1",borderwidth=0,  cursor="heart",fg="#999B84",padx=10,command=exit, activebackground="#EFD9D1")
navbtn3.place(x=1300  ,  y=23)


# secondframe = tk.Frame(root,bg="#D8AC9C",height=10)
# secondframe.pack(after=topframe,fill=tk.X)
title=  tk.Label(root, text="Make your day amazing with good fashion ",font="Vivaldi 20 bold", fg="#F4EEED" , bg="#D8AC9C" )
title.place(x=450 ,y=80)

#first line

canv1 = Canvas(root,width=150 ,bg="white",cursor="heart")
canv1.place(x=30,y=130)
item1= PhotoImage(file="pant.gif")
canv1.create_image(1,1, anchor=NW, image=item1)
description1=tk.Label(canv1 , text="Beige Pant", bg="white",fg="#999B84", font="terminal 15 bold")
description1.place(x=20, y=190)
price1=tk.Label(canv1, text="300 DH",bg="white",fg="#999B84", font="terminal 12")
price1.place(x=35 , y=220)


canv2 = Canvas(root,width=150 ,bg="white",cursor="heart")
canv2.place(x=260,y=130)
item2= PhotoImage(file="olivepant.gif")
canv2.create_image(1,1, anchor=NW, image=item2)
description2=tk.Label(canv2 , text="green Pant", bg="white",fg="#999B84", font="terminal 15 bold")
description2.place(x=20, y=190)
price2=tk.Label(canv2, text="350 DH",bg="white",fg="#999B84", font="terminal 12")
price2.place(x=35 , y=220)

canv3 = Canvas(root,width=150 ,bg="white",cursor="heart")
canv3.place(x=500,y=130)
item3= PhotoImage(file="dressb.gif")
canv3.create_image(1,1, anchor=NW, image=item3)
description3=tk.Label(canv3 , text="black dress", bg="white",fg="#999B84", font="terminal 15 bold")
description3.place(x=20, y=190)
price3=tk.Label(canv3, text="750 DH",bg="white",fg="#999B84", font="terminal 12")
price3.place(x=35 , y=220)

canv4 = Canvas(root,width=150 ,bg="white",cursor="heart")
canv4.place(x=730,y=130)
item4= PhotoImage(file="longdress.gif")
canv4.create_image(1,1, anchor=NW, image=item4)
description4=tk.Label(canv4 , text="bluesky dress", bg="white",fg="#999B84", font="terminal 15 bold")
description4.place(x=3, y=190)
price4=tk.Label(canv4, text="400 DH",bg="white",fg="#999B84", font="terminal 12")
price4.place(x=35 , y=220)

canv5 = Canvas(root,width=150 ,bg="white",cursor="heart")
canv5.place(x=960,y=130)
item5= PhotoImage(file="jupe.gif")
canv5.create_image(1,1, anchor=NW, image=item5)
description5=tk.Label(canv5 , text="long skirt ", bg="white",fg="#999B84", font="terminal 15 bold")
description5.place(x=20, y=190)
price5=tk.Label(canv5, text="250 DH",bg="white",fg="#999B84", font="terminal 12")
price5.place(x=35 , y=220)

canv6 = Canvas(root,width=150 ,bg="white",cursor="heart")
canv6.place(x=1190,y=130)
item6= PhotoImage(file="chemise.gif")
canv6.create_image(1,1, anchor=NW, image=item6)
description6=tk.Label(canv6 , text="striped shirt", bg="white",fg="#999B84", font="terminal 15 bold")
description6.place(x=3, y=190)
price6=tk.Label(canv6, text="250 DH",bg="white",fg="#999B84", font="terminal 12")
price6.place(x=35 , y=220)


#second line

canv7 = Canvas(root,width=150 ,bg="white",cursor="heart")
canv7.place(x=30,y=430)
item7= PhotoImage(file="tshirt.gif")
canv7.create_image(1,1, anchor=NW, image=item7)
description7=tk.Label(canv7 , text="green T-shirt", bg="white",fg="#999B84", font="terminal 15 bold")
description7.place(x=3, y=190)
price7=tk.Label(canv7, text="300 DH",bg="white",fg="#999B84", font="terminal 12")
price7.place(x=35 , y=220)

canv8 = Canvas(root,width=150 ,bg="white",cursor="heart")
canv8.place(x=260,y=430)
item8= PhotoImage(file="wedding shoes.gif")
canv8.create_image(1,1, anchor=NW, image=item8)
description8=tk.Label(canv8, text="wedding shoes", bg="white",fg="#999B84", font="terminal 15 bold")
description8.place(x=3, y=190)
price8=tk.Label(canv8, text="300 DH",bg="white",fg="#999B84", font="terminal 12")
price8.place(x=35 , y=220)

canv9 = Canvas(root,width=150 ,bg="white",cursor="heart")
canv9.place(x=500,y=430)
item9= PhotoImage(file="bag.gif")
canv9.create_image(1,1, anchor=NW, image=item9)
description9=tk.Label(canv9 , text="Brown bag ", bg="white",fg="#999B84", font="terminal 15 bold")
description9.place(x=20, y=190)
price9=tk.Label(canv9, text="500 DH",bg="white",fg="#999B84", font="terminal 12")
price9.place(x=35 , y=220)

canv10 = Canvas(root,width=150 ,bg="white",cursor="heart")
canv10.place(x=730,y=430)
item10= PhotoImage(file="hair.gif")
canv10.create_image(1,1, anchor=NW, image=item10)
description10=tk.Label(canv10 , text="hair acces..", bg="white",fg="#999B84", font="terminal 15 bold")
description10.place(x=10, y=190)
price10=tk.Label(canv10, text="120 DH",bg="white",fg="#999B84", font="terminal 12")
price10.place(x=35 , y=220)

canv11 = Canvas(root,width=150 ,bg="white",cursor="heart")
canv11.place(x=960,y=430)
item11= PhotoImage(file="pinkshoes.gif")
canv11.create_image(1,1, anchor=NW, image=item11)
description11=tk.Label(canv11 , text="pink shoes", bg="white",fg="#999B84", font="terminal 15 bold")
description11.place(x=20, y=190)
price11=tk.Label(canv11, text="290 DH",bg="white",fg="#999B84", font="terminal 12")
price11.place(x=35 , y=220)

canv12 = Canvas(root,width=150 ,bg="white",cursor="heart")
canv12.place(x=1190,y=430)
item12= PhotoImage(file="hat.gif")
canv12.create_image(1,1, anchor=NW, image=item12)
description12=tk.Label(canv12 , text="beige hat", bg="white",fg="#999B84", font="terminal 15 bold")
description12.place(x=20, y=190)
price12=tk.Label(canv12, text="150 DH",bg="white",fg="#999B84", font="terminal 12")
price12.place(x=35 , y=220)













root.mainloop()
