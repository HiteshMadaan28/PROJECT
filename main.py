from tkinter import *
from tkinter import messagebox
from tkinter import Toplevel,Menu,ttk
from PIL import Image,ImageTk
import oracledb
import random
import datetime
import tkinter as tk

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)
def generate_ticket_number():
    ticket_number = ''
    for i in range(3):
        ticket_number += str(random.randint(0, 9))
    TICKET_NO='T'+ticket_number
    return TICKET_NO
def cost():
    cost=random.randint(4000, 11000)
    return cost
def book_tickets():
    book_window = Toplevel(root)
    book_window.title('Book Tickets Form')
    book_window.state('zoomed')
    book_window.title("Book tickets")
    book_window.configure(bg="#fff")
    heading = Label(book_window, text="Book Tickets",bg="white",fg = "black", font = ("Microsoft Yahei UI Light",20))
    heading.place(x=800, y=30)
    label = Label(book_window, text = "AVAILABLE TRAINS",bg="white",fg = "green", font = ("Castellar",25))
    label.place(x=700,y=150)
    label_frame = Frame(book_window,width=400,height=700,bg="white",highlightthickness=4,highlightbackground="light cyan")
    label_frame.place(x=30,y=60)
    label = Label(label_frame, text = "Passenger Details",bg="white",fg = "green", font = ("Castellar",20))
    label.place(x=15,y=30)
    label = Label(label_frame, text = "Passenger ID",bg="white",fg = "green", font = ("Castellar",15))
    label.place(x=20,y=120)
    Idstring=tk.StringVar()
    Id=Entry(label_frame,textvariable=Idstring,width=15,fg='black',border=1,bg='white',font=("Microsoft Yahei UI Light",15))
    Id.place(x=20,y=160)
    label = Label(label_frame, text = "Passenger Name",bg="white",fg = "green", font = ("Castellar",15))
    label.place(x=20,y=210)
    NAMES=tk.StringVar()
    pname=Entry(label_frame,textvariable=NAMES,width=15,fg='black',border=1,bg='white',font=("Microsoft Yahei UI Light",15))
    pname.place(x=20,y=250)
    label = Label(label_frame,text = "PhoneNumber",bg="white",fg = "green", font = ("Castellar",15))
    label.place(x=20,y=300)
    PHONENO=tk.StringVar()
    pnumber=Entry(label_frame,textvariable=PHONENO,width=15,fg='black',border=1,bg='white',font=("Microsoft Yahei UI Light",15))
    pnumber.place(x=20,y=340)
    label = Label(label_frame, text = "Address",bg="white",fg = "green", font = ("Castellar",15))
    label.place(x=20,y=390)
    PADD=tk.StringVar()
    address=Entry(label_frame,textvariable=PADD,width=15,fg='black',border=1,bg='white',font=("Microsoft Yahei UI Light",15))
    address.place(x=20,y=430)
    label = Label(label_frame, text = "Train ID",bg="white",fg = "green", font = ("Castellar",15))
    label.place(x=20,y=480)

    TID=tk.StringVar()
    train_id=Entry(label_frame,textvariable=TID,width=15,fg='black',border=1,bg='white',font=("Microsoft Yahei UI Light",15))
    train_id.place(x=20,y=520)
    def enter():
        conn=oracledb.connect(user="python",password="coder",dsn="Localhost:1521/orcl")
        cur=conn.cursor()

        sql=f"SELECT * FROM AVAILABLE_TRAINS where train_id='{train_id.get()}'"
        cur.execute(sql)
        rows=cur.fetchone()

        for i in rows:
            print(i)

        z1=rows[0]
        z2=rows[1]

        z3=rows[2]
        z4=rows[3]

        z5=rows[4]
        date1 = z4.strftime('%d-%b-%Y')
        date2 = z5.strftime('%d-%b-%Y')
        print(date1)
        print(date2)

        TFROM=tk.StringVar()
        TFROM.set(rows[1])

        TTO=tk.StringVar()
        TTO.set(rows[2])

        TD=tk.StringVar()
        TD.set(rows[3])

        TA=tk.StringVar()
        TA.set(rows[4])

        TCID=tk.StringVar()
        TCID.set(generate_ticket_number())

        TCOST=tk.IntVar()
        TCOST.set(cost())
        sql1=f"INSERT INTO PASSENGER VALUES('{Id.get()}','{pname.get()}','{pnumber.get()}','{address.get()}')"
        cur.execute(sql1)

        conn.commit()
        messagebox.showinfo( "Result", "Record ADDED Successfully")
        cur.close()
        conn.close()

        def lastpage():
            lastpage= Toplevel(root)
            lastpage.title('Book Tickets Form')
            
            lastpage.state('zoomed')
            lastpage.title("Book tickets")
           
            lastpage.configure(bg="#fff")

            heading = Label(lastpage, text="CONFIRM YOUR DETAILS AND BOOK YOUR TICKET",bg="white",fg = "black", font = ("Microsoft Yahei UI Light",20))
            heading.place(x=500, y=30)

            Label(lastpage, text = "Passenger ID",bg="white",fg = "green", font = ("Castellar",20)).place(x=200,y=130)
            Label(lastpage, text = "Name",bg="white",fg = "green", font = ("Castellar",20)).place(x=200,y=180)
            Label(lastpage, text = "Phone No.",bg="white",fg = "green", font = ("Castellar",20)).place(x=200,y=230)
            Label(lastpage, text = "Address",bg="white",fg = "green", font = ("Castellar",20)).place(x=200,y=280)
            Label(lastpage, text = "Train ID",bg="white",fg = "green", font = ("Castellar",20)).place(x=200,y=330)
            Label(lastpage, text = "FROM",bg="white",fg = "green", font = ("Castellar",20)).place(x=200,y=380)
            Label(lastpage, text = "TO",bg="white",fg = "green", font = ("Castellar",20)).place(x=200,y=430)
            Label(lastpage, text = "ARRIVAL",bg="white",fg = "green", font = ("Castellar",20)).place(x=200,y=480)
            Label(lastpage, text = "DEPARTURE",bg="white",fg = "green", font = ("Castellar",20)).place(x=200,y=530)
            Label(lastpage, text = "TICKET ID",bg="white",fg = "green", font = ("Castellar",20)).place(x=200,y=580)
            Label(lastpage, text = "Train COST",bg="white",fg = "green", font = ("Castellar",20)).place(x=200,y=630)

            
            Label(lastpage, textvariable=Idstring ,bg="white",fg = "black", font = ("Microsoft Yahei UI Light",20)).place(x=600,y=130)
            Label(lastpage, textvariable=NAMES ,bg="white",fg = "black", font = ("Microsoft Yahei UI Light",20)).place(x=600,y=180)
            Label(lastpage, textvariable=PHONENO ,bg="white",fg = "black", font = ("Microsoft Yahei UI Light",20)).place(x=600,y=230)
            Label(lastpage, textvariable=PADD ,bg="white",fg = "black", font = ("Microsoft Yahei UI Light",20)).place(x=600,y=280)
            Label(lastpage, textvariable=TID ,bg="white",fg = "black", font = ("Microsoft Yahei UI Light",20)).place(x=600,y=330)
            Label(lastpage, textvariable=TFROM ,bg="white",fg = "black", font = ("Microsoft Yahei UI Light",20)).place(x=600,y=380)
            Label(lastpage, textvariable=TTO ,bg="white",fg = "black", font = ("Microsoft Yahei UI Light",20)).place(x=600,y=430)
            Label(lastpage, textvariable=TD ,bg="white",fg = "black", font = ("Microsoft Yahei UI Light",20)).place(x=600,y=480)
            Label(lastpage, textvariable=TA ,bg="white",fg = "black", font = ("Microsoft Yahei UI Light",20)).place(x=600,y=530)
            Label(lastpage, textvariable=TCID ,bg="white",fg = "black", font = ("Microsoft Yahei UI Light",20)).place(x=600,y=580)
            Label(lastpage, textvariable=TCOST ,bg="white",fg = "black", font = ("Microsoft Yahei UI Light",20)).place(x=600,y=630)

            def SUBMIT():
                conn=oracledb.connect(user="python",password="coder",dsn="Localhost:1521/orcl")
                cur=conn.cursor()
                C=0
                INSET_INTO_TRAVEL=f"INSERT INTO TRAVEL VALUES('{Id.get()}','{z2}','{z3}','{date1}','{date2}','{z1}')"
                cur.execute(INSET_INTO_TRAVEL)
                conn.commit()
                C=1
                if C==1:
                    INSERT_INTO_TICKET=f"INSERT INTO TICKET VALUES('{TCID.get()}','{Id.get()}',{TCOST.get()})"
                    cur.execute(INSERT_INTO_TICKET)
                    conn.commit()
                messagebox.showinfo( "Result", "YOUR TICKET HAS BEEN BOOKED")
                cur.close()
                conn.close()
                               
            Button(lastpage,width=20,pady=7,text='BOOK TICKET',bg='#57a1f8',fg='white',border=0,command=SUBMIT).place(x=1000,y=700)
            
        Button(book_window,width=20,pady=7,text='Next',bg='#57a1f8',fg='white',border=0,command=lastpage).place(x=1000,y=700)
  
    Button(label_frame,width=20,pady=7,text='Enter',bg='#57a1f8',fg='white',border=0,command=enter).place(x=100,y=600)    
        
    conn=oracledb.connect(user="python",password="coder",dsn="Localhost:1521/orcl")
    cur=conn.cursor()
    print(conn.version)

    sql="SELECT * FROM AVAILABLE_TRAINS"
    cur.execute(sql)
    rows=cur.fetchall()

    frame=Frame(book_window,width=1000,height=300,bg="light cyan")

    frame.place(x=460,y=210)

    tv=ttk.Treeview(frame,columns=(1,2,3,4,5),show="headings",height="15")
    tv.grid(row=1,column=1,columnspan=2,padx=10,pady=10)
    tv.column(1 ,anchor=CENTER,width=30)
    tv.heading(1,text="TRAIN ID")
    tv.column(2, anchor=CENTER, width=170)
    tv.heading(2,text="FROM")
    tv.column(3, anchor=CENTER, width=170)
    tv.heading(3,text="TO")
    tv.column(1, anchor=CENTER, width=170)
    tv.heading(4,text="Departure")
    tv.column(5, anchor=CENTER, width=170)
    tv.heading(5, text="Arival")

    for i in rows:
        tv.insert('','end',values=i)

    style=ttk.Style(book_window)
    style.theme_use('clam')
    
    style.configure("Treeview",background="grey",foreground="black",font=("Times",12,'normal'),rowheight=30,fieldbackground="white")
    style.configure("Treeview.Heading",background='white')

def view_tickets():
    book_window = Toplevel(root)
    book_window.title('View Tickets')
    book_window.state('zoomed')
    book_window.title("View tickets")
    book_window.configure(bg="#fff")

    heading = Label(book_window, text="View Tickets",bg="white",fg = "black", font = ("Microsoft Yahei UI Light",20))
    heading.place(x=650, y=30)
    # form input
    label = Label(book_window, text = "Passenger ID",bg="white",fg = "green", font = ("Castellar",30))
    label.place(x=300,y=150)

    enter=Entry(book_window,width=35,fg='black',border=1,bg='white',font=("Microsoft Yahei UI Light",20))

    enter.place(x=650,y=160)

    value=enter.get()

    def show():
        conn=oracledb.connect(user="python",password="coder",dsn="Localhost:1521/orcl")
        cur=conn.cursor()
        print(conn.version)

        sql=f"select PASSENGER.p_id,PASSENGER.p_name,PASSENGER.p_number,PASSENGER.p_address,TRAVEL.train_id,TRAVEL.l_from,TRAVEL.l_to,TRAVEL.arival,TRAVEL.departure,TICKET.ticket_no,TICKET.cost from PASSENGER,TRAVEL,ticket where PASSENGER.p_id=TRAVEL.p_id and PASSENGER.p_id=ticket.p_id and PASSENGER.p_id='{enter.get()}'"
        cur.execute(sql)
        rows=cur.fetchall()
        frame=Frame(book_window,width=800,height=300,bg="light cyan")

        frame.place(x=100,y=350)

        tv=ttk.Treeview(frame,columns=(1,2,3,4,5,6,7,8,9,10,11),show="headings",height="13")
        tv.grid(row=1,column=1,columnspan=2,padx=0,pady=10)
        tv.column(1 ,anchor=CENTER,width=30)
        tv.heading(1,text="Passenger Id")
        tv.column(2, anchor=CENTER, width=170)
        tv.heading(2,text="Name")
        tv.column(3, anchor=CENTER, width=150)
        tv.heading(3,text="Number")
        tv.column(1, anchor=CENTER, width=140)
        tv.heading(4,text="Address")
        tv.column(5, anchor=CENTER, width=100)
        tv.heading(5, text="Train Id")
        tv.column(6, anchor=CENTER, width=100)
        tv.heading(6, text="From", anchor=CENTER)
        tv.column(7, anchor=CENTER, width=100)
        tv.heading(7, text="to")
        tv.column(8, anchor=CENTER, width=120)
        tv.heading(8, text="Arival")
        tv.column(9, anchor=CENTER, width=120)
        tv.heading(9, text="Departure")
        tv.column(10, anchor=CENTER, width=100)
        tv.heading(10, text="Ticket_NO")
        tv.column(11, anchor=CENTER, width=100)
        tv.heading(11, text="Cost")
        
        for i in rows:
            tv.insert('','end',values=i)

        style=ttk.Style(book_window)
        style.theme_use('clam')
        
        style.configure("Treeview",background="grey",foreground="black",font=("Times",12,'normal'),rowheight=30,fieldbackground="white")
        style.configure("Treeview.Heading",background='white')


    Button(book_window,width=20,pady=7,text='Enter',bg='#57a1f8',fg='white',border=0,command=show).place(x=900,y=205)

    

    conn=oracledb.connect(user="python",password="coder",dsn="Localhost:1521/orcl")
    cur=conn.cursor()
    print(conn.version)

    sql="select PASSENGER.p_id,PASSENGER.p_name,PASSENGER.p_number,PASSENGER.p_address,TRAVEL.train_id,TRAVEL.l_from,TRAVEL.l_to,TRAVEL.arival,TRAVEL.departure,TICKET.ticket_no,TICKET.cost from PASSENGER,TRAVEL,ticket where PASSENGER.p_id=TRAVEL.p_id and PASSENGER.p_id=ticket.p_id"
    cur.execute(sql)
    rows=cur.fetchall()

    frame=Frame(book_window,width=1000,height=300,bg="light cyan")

    frame.place(x=100,y=350)

    tv=ttk.Treeview(frame,columns=(1,2,3,4,5,6,7,8,9,10,11),show="headings",height="13")
    tv.grid(row=1,column=1,columnspan=2,padx=0,pady=10)
    tv.column(1 ,anchor=CENTER,width=30)
    tv.heading(1,text="Passenger Id")
    tv.column(2, anchor=CENTER, width=170)
    tv.heading(2,text="Name")
    tv.column(3, anchor=CENTER, width=150)
    tv.heading(3,text="Number")
    tv.column(1, anchor=CENTER, width=140)
    tv.heading(4,text="Address")
    tv.column(5, anchor=CENTER, width=100)
    tv.heading(5, text="Train Id")
    tv.column(6, anchor=CENTER, width=100)
    tv.heading(6, text="From", anchor=CENTER)
    tv.column(7, anchor=CENTER, width=100)
    tv.heading(7, text="to")
    tv.column(8, anchor=CENTER, width=120)
    tv.heading(8, text="Arival")
    tv.column(9, anchor=CENTER, width=120)
    tv.heading(9, text="Departure")
    tv.column(10, anchor=CENTER, width=100)
    tv.heading(10, text="Ticket_NO")
    tv.column(11, anchor=CENTER, width=100)
    tv.heading(11, text="Cost")
    
    for i in rows:
        tv.insert('','end',values=i)

    style=ttk.Style(book_window)
    style.theme_use('clam')
    
    style.configure("Treeview",background="grey",foreground="black",font=("Times",12,'normal'),rowheight=30,fieldbackground="white")
    style.configure("Treeview.Heading",background='white')

def update_tickets():

    book_window = Toplevel(root)
    book_window.title('Update Tickets')
    book_window.state('zoomed')
    book_window.title("Update tickets")
    book_window.configure(bg="#fff")

    heading = Label(book_window, text="Update Tickets",bg="white",fg = "black", font = ("Microsoft Yahei UI Light",20))
    heading.place(x=800, y=30)
    label = Label(book_window, text = "Passenger ID",bg="white",fg = "green", font = ("Castellar",30))
    label.place(x=400,y=85)

    enter=Entry(book_window,width=35,fg='black',border=1,bg='white',font=("Microsoft Yahei UI Light",20))
    enter.place(x=750,y=90)
    label = Label(book_window, text = "Name",bg="white",fg = "green", font = ("Castellar",20))
    label.place(x=350,y=185)
    name=Entry(book_window,width=35,fg='black',border=1,bg='white',font=("Microsoft Yahei UI Light",15))
    name.place(x=450,y=190)  
    label = Label(book_window, text = "Number",bg="white",fg = "green", font = ("Castellar",20))
    label.place(x=850,y=185)
    number=Entry(book_window,width=35,fg='black',border=1,bg='white',font=("Microsoft Yahei UI Light",15))
    number.place(x=990,y=190)
    value=enter.get()

    def up():
        if name.get()=='':
            conn=oracledb.connect(user="python",password="coder",dsn="Localhost:1521/orcl")
            cur=conn.cursor()

            sql=f"update PASSENGER set p_number='{number.get()}' where p_id='{enter.get()}'"
            cur.execute(sql)
            conn.commit()
            messagebox.showinfo('Success', 'YOUR NAME HAS BEEN UPDATED')
            cur.close()
            conn.close()
        if number.get()=='':
            conn=oracledb.connect(user="python",password="coder",dsn="Localhost:1521/orcl")
            cur=conn.cursor()

            sql=f"update PASSENGER set p_name='{name.get()}' where p_id='{enter.get()}'"
            cur.execute(sql)
            conn.commit()
            messagebox.showinfo('Success', 'YOUR NUMBER HAS BEEN UPDATED')
            cur.close()
            conn.close()
        if name.get()!='' and number.get()!='':
            conn=oracledb.connect(user="python",password="coder",dsn="Localhost:1521/orcl")
            cur=conn.cursor()

            sql=f"update PASSENGER set p_number='{number.get()}',p_name='{name.get()}' where p_id='{enter.get()}'"
            cur.execute(sql)
            conn.commit()
            messagebox.showinfo('Success', 'YOUR NAME AND NAME HAS BEEN UPDATED')
            cur.close()
            conn.close()

    def show():
        conn=oracledb.connect(user="python",password="coder",dsn="Localhost:1521/orcl")
        cur=conn.cursor()
        print(conn.version)

        sql=f"select PASSENGER.p_id,PASSENGER.p_name,PASSENGER.p_number,PASSENGER.p_address,TRAVEL.train_id,TRAVEL.l_from,TRAVEL.l_to,TRAVEL.arival,TRAVEL.departure,TICKET.ticket_no,TICKET.cost from PASSENGER,TRAVEL,ticket where PASSENGER.p_id=TRAVEL.p_id and PASSENGER.p_id=ticket.p_id and PASSENGER.p_id='{enter.get()}'"
        cur.execute(sql)
        rows=cur.fetchall()
        frame=Frame(book_window,width=1000,height=300,bg="light cyan")

        frame.place(x=100,y=300)

        tv=ttk.Treeview(frame,columns=(1,2,3,4,5,6,7,8,9,10,11),show="headings",height="20")
        tv.grid(row=1,column=1,columnspan=2,padx=0,pady=10)
        tv.column(1 ,anchor=CENTER,width=30)
        tv.heading(1,text="Passenger Id")
        tv.column(2, anchor=CENTER, width=170)
        tv.heading(2,text="Name")
        tv.column(3, anchor=CENTER, width=150)
        tv.heading(3,text="Number")
        tv.column(1, anchor=CENTER, width=140)
        tv.heading(4,text="Address")
        tv.column(5, anchor=CENTER, width=100)
        tv.heading(5, text="Train Id")
        tv.column(6, anchor=CENTER, width=100)
        tv.heading(6, text="From", anchor=CENTER)
        tv.column(7, anchor=CENTER, width=100)
        tv.heading(7, text="to")
        tv.column(8, anchor=CENTER, width=120)
        tv.heading(8, text="Arival")
        tv.column(9, anchor=CENTER, width=120)
        tv.heading(9, text="Departure")
        tv.column(10, anchor=CENTER, width=100)
        tv.heading(10, text="Ticket_NO")
        tv.column(11, anchor=CENTER, width=100)
        tv.heading(11, text="Cost")
        
        for i in rows:
            tv.insert('','end',values=i)

        style=ttk.Style(book_window)
        style.theme_use('clam')
        
        style.configure("Treeview",background="grey",foreground="black",font=("Times",12,'normal'),rowheight=30,fieldbackground="white")
        style.configure("Treeview.Heading",background='white')

    Button(book_window,width=20,pady=7,text='Enter',bg='#57a1f8',fg='white',border=0,command=show).place(x=900,y= 135)
    Button(book_window,width=20,pady=7,text='Update',bg='#57a1f8',fg='white',border=0,command=up).place(x=800,y= 230)
    conn=oracledb.connect(user="python",password="coder",dsn="Localhost:1521/orcl")
    cur=conn.cursor()
    print(conn.version)
    sql="select PASSENGER.p_id,PASSENGER.p_name,PASSENGER.p_number,PASSENGER.p_address,TRAVEL.train_id,TRAVEL.l_from,TRAVEL.l_to,TRAVEL.arival,TRAVEL.departure,TICKET.ticket_no,TICKET.cost from PASSENGER,TRAVEL,ticket where PASSENGER.p_id=TRAVEL.p_id and PASSENGER.p_id=ticket.p_id"
    cur.execute(sql)
    rows=cur.fetchall()
    frame=Frame(book_window,width=1000,height=300,bg="light cyan")
    frame.place(x=100,y=300)

    tv=ttk.Treeview(frame,columns=(1,2,3,4,5,6,7,8,9,10,11),show="headings",height="20")
    tv.grid(row=1,column=1,columnspan=2,padx=0,pady=10)
    tv.column(1 ,anchor=CENTER,width=30)
    tv.heading(1,text="Passenger Id")
    tv.column(2, anchor=CENTER, width=170)
    tv.heading(2,text="Name")
    tv.column(3, anchor=CENTER, width=150)
    tv.heading(3,text="Number")
    tv.column(1, anchor=CENTER, width=140)
    tv.heading(4,text="Address")
    tv.column(5, anchor=CENTER, width=100)
    tv.heading(5, text="Train Id")
    tv.column(6, anchor=CENTER, width=100)
    tv.heading(6, text="From", anchor=CENTER)
    tv.column(7, anchor=CENTER, width=100)
    tv.heading(7, text="to")
    tv.column(8, anchor=CENTER, width=120)
    tv.heading(8, text="Arival")
    tv.column(9, anchor=CENTER, width=120)
    tv.heading(9, text="Departure")
    tv.column(10, anchor=CENTER, width=100)
    tv.heading(10, text="Ticket_NO")
    tv.column(11, anchor=CENTER, width=100)
    tv.heading(11, text="Cost")
    
    for i in rows:
        tv.insert('','end',values=i)

    style=ttk.Style(book_window)
    style.theme_use('clam')
    
    style.configure("Treeview",background="grey",foreground="black",font=("Times",12,'normal'),rowheight=30,fieldbackground="white")
    style.configure("Treeview.Heading",background='white')

def cancel_ticket():
    cancel_window = Toplevel(root)
    cancel_window.state('zoomed')
    cancel_window.title('Cancel Ticket')
    cancel_window.configure(bg="#fff")
    
    heading = Label(cancel_window, text="CANCEL Tickets",bg="white",fg = "black", font = ("Microsoft Yahei UI Light",20))
    heading.place(x=800, y=30)
    
    label_id = Label(cancel_window, text="Enter Passenger Id",bg="white",fg = "green", font = ("Castellar",30))
    label_id.place(x=420, y=120)
    input_id = Entry(cancel_window,width=25,fg='black',border=1,bg='white',font=("Microsoft Yahei UI Light",20))
    input_id.place(x=900, y=130)

    def show_passenger():
        conn =oracledb.connect(user="python",password="coder",dsn="Localhost:1521/orcl")
        cur = conn.cursor()
        print(conn.version)
        try:
            sql = "SELECT * FROM PASSENGER WHERE p_id= :input_e"
            cur.execute(sql, {'input_e': input_id.get()})
            row = cur.fetchone()

        # Record Not found
            if row:
                print(row)
                return True
            else:
                messagebox.showinfo("No Records Found", "No records were found for the given search value.")
                return False
        except oracledb.DatabaseError as e:
            # display the error message to the user
            messagebox.showerror("Database Error", str(e))
            cur.close()
        conn.close()

    def show_travel():
        
        con =oracledb.connect(user="python",password="coder",dsn="Localhost:1521/orcl")
        c = con.cursor()
        sql = "SELECT * FROM TRAVEL WHERE p_id= :input_e"
        c.execute(sql, {'input_e': input_id.get()})
        rows = c.fetchall()
        frame = Frame(cancel_window, width=500, height=200, bg="light cyan")
        frame.place(x=250, y=300)

        tv = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6),show="headings", height="20")
        tv.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        tv.column(1, anchor=CENTER, width=30)
        tv.heading(1, text="Passenger Id")
        tv.column(2, anchor=CENTER, width=170)
        tv.heading(2, text="FROM")
        tv.column(3, anchor=CENTER, width=170)
        tv.heading(3, text="TO")
        tv.column(1, anchor=CENTER, width=170)
        tv.heading(4, text="Arrival date")
        tv.column(5, anchor=CENTER, width=170)
        tv.heading(5, text="Departure date")
        tv.column(6, anchor=CENTER, width=170)
        tv.heading(6, text="Train Id")

        for i in rows:
            tv.insert('', 'end', values=i)

        style = ttk.Style(cancel_window)
        style.theme_use('classic')
        style.configure("Treeview", background="gray86", foreground="black", font=("Times", 12, 'normal'), rowheight=30, fieldbackground="white")
        style.configure("Treeview.Heading", background='white')

        c.close()
        con.close()

    def cancellation():
        record = show_passenger()

        if record:
            show_travel()
            conn =oracledb.connect(user="python",password="coder",dsn="Localhost:1521/orcl")
            cur = conn.cursor()
            sql = "DELETE FROM TRAVEL WHERE p_id =:input_e"
            cur.execute(sql, {'input_e': input_id.get()})

            print("RECORD DELETED")
            conn.commit()
            messagebox.showinfo( "Result", "Record Deleted Successfully")
            
            cur.close()
            conn.close()

    button = Button(cancel_window, text="ENTER", command=cancellation,width=20,pady=7,bg='#57a1f8',fg='white',border=0)
    button.place(x=770, y=200)

            
    con =oracledb.connect(user="python",password="coder",dsn="Localhost:1521/orcl")
    c = con.cursor()
    sql = "SELECT * FROM TRAVEL"
    c.execute(sql)
    rows = c.fetchall()
    frame = Frame(cancel_window, width=500, height=200, bg="light cyan")
    frame.place(x=250, y=300)

    tv = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6),show="headings", height="8")
    tv.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    tv.column(1, anchor=CENTER, width=30)
    tv.heading(1, text="Passenger Id")
    tv.column(2, anchor=CENTER, width=170)
    tv.heading(2, text="FROM")
    tv.column(3, anchor=CENTER, width=170)
    tv.heading(3, text="TO")
    tv.column(1, anchor=CENTER, width=170)
    tv.heading(4, text="Arrival date")
    tv.column(5, anchor=CENTER, width=170)
    tv.heading(5, text="Departure date")
    tv.column(6, anchor=CENTER, width=170)
    tv.heading(6, text="Train Id")

    for i in rows:
        tv.insert('', 'end', values=i)

    style = ttk.Style(cancel_window)
    style.theme_use('classic')
    style.configure("Treeview", background="gray86", foreground="black", font=("Times", 12, 'normal'), rowheight=30, fieldbackground="white")
    style.configure("Treeview.Heading", background='white')
   

def mainpage():
    main=Toplevel(root)
    main.title('Railway Reservation System')
    main.state('zoomed')
    main.configure(bg='#fff')
    main.resizable(True,True)
    root.withdraw()

    bg = ImageTk.PhotoImage( file = "train.jpg")
  
    # Show image using label
    label1 = Label( main, image = bg)
    label1.place(x = -200,y =-200)
    button = Button(main, text="Book tickets", command=book_tickets,width=20,pady=7,bg='#57a1f8',fg='white',font=("Times", 20, 'normal'),border=0)
    button.place(x=970, y=300)
    button = Button(main, text="View Ticket", command=view_tickets,width=20,pady=7,bg='#57a1f8',fg='white',font=("Times", 20, 'normal'),border=0)
    button.place(x=970, y=400)
    button = Button(main, text="Update Ticket", command=update_tickets,width=20,pady=7,bg='#57a1f8',font=("Times", 20, 'normal'),fg='white',border=0)
    button.place(x=970, y=500)
    button = Button(main, text="Cancel Ticket", command=cancel_ticket,width=20,pady=7,bg='#57a1f8',font=("Times", 20, 'normal'),fg='white',border=0)
    button.place(x=970, y=600)

    menubar=Menu(main)

    menubar = Menu(main)
    menup = Menu(menubar, tearoff=0)
    menup.add_command(label="Book tickets", command=book_tickets)
    menup.add_command(label="View Ticket", command=view_tickets)
    menup.add_command(label="Update Ticket", command=update_tickets)
    menup.add_command(label="Cancel Ticket", command=cancel_ticket)

    menup.add_separator()  
    menup.add_command(label="exit", command=main.quit)  
    menubar.add_cascade(label="Menu", menu=menup)  
    def logout():
        main.destroy()
        root.deiconify()
    Logout= Menu(menubar, tearoff=0)  
    Logout.add_command(label="Log_out",command=logout)  
    menubar.add_cascade(label="Log_out", menu=Logout)  

    main.config(menu=menubar)
    main.mainloop()

def signup():
    
    def signedup():

        username = users.get()
        upassword = password1.get()
        cpassword = password2.get()
        username = user.get()

        if username == '':
            messagebox.showerror("Altert", "Singned UP Congratularion")
        if upassword == '':
            messagebox.showerror("Altert", "Singned UP Congratularion")
        if cpassword == '':
            messagebox.showerror("Altert", "Singned UP Congratularion")
        if cpassword != upassword:
            messagebox.showerror("Invalid", "Password Should be same")
        password = password2.get()
        con = oracledb.connect(user="python",password="coder",dsn="Localhost:1521/orcl")
        c = con.cursor()
        query1 = "SELECT COUNT(*) FROM USERID WHERE user_id = :username"
        c.execute(query1, {"username": users.get()})
        result1 = c.fetchone()[0]

        query2 = "SELECT COUNT(*) FROM ADMIN WHERE a_i= :username "
        c.execute(query2, {"username": users.get()})
        result2 = c.fetchone()[0]
        if result1 > 0 or result2 > 0:
            messagebox.showinfo(
                "Alert", "Username already exits!!")

        elif username!="" and cpassword==upassword:
            query3 = "INSERT INTO USERID(USER_ID,PASSWORD)VALUES(:username , :cpassword)"
            c.execute(query3, {"username": users.get(),
                      "cpassword": password2.get()})
            con.commit()
            messagebox.showinfo(
                "Alert", "Username added successfully")
    
        c.close()
        con.close()

    window = Toplevel(root)
    window.title('Signup')
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False, False)
    image = Image.open("image.png")
    imgs = ImageTk.PhotoImage(image)
    Label(window, image=imgs, bg='white').place(x=5, y=20)

    frames = Frame(window, width=350, height=350, bg="white")
    frames.place(x=530, y=70)
    headings = Label(frames, text="Sign UP", fg="#57a1f8",bg="white", font=("Microsoft Yahei UI Light", 23, 'bold'))
    headings.place(x=110, y=5)

    def on_enter(e):
        users.delete(0, 'end')
    def on_leave(e):
        name = users.get()
        if name == '':
            users.insert(0, 'Username')

    users = Entry(frames, width=25, fg='black', border=0,bg='white', font=("Microsoft Yahei UI Light", 11))
    users.place(x=30, y=80)
    users.insert(0, 'Enter UserName')
    users.bind('<FocusIn>', on_enter)
    users.bind('<FocusOut>', on_leave)
    Frame(frames, width=295, height=2, bg='black').place(x=25, y=107)
    def on_enter(e):
        password1.delete(0, 'end')
        password1.config(show="*")
    def on_leave(e):
        name = password1.get()
        if name == '':
            password1.insert(0, 'Enter Password')

    password1 = Entry(frames, width=25, fg='black', border=0, bg='white', font=("Microsoft Yahei UI Light", 11))
    password1.place(x=30, y=140)
    password1.insert(0, 'Enter Password')
    password1.bind('<FocusIn>', on_enter)
    password1.bind('<FocusOut>', on_leave)
    Frame(frames, width=295, height=2, bg='black').place(x=25, y=168)
    def on_enter(e):
        password2.delete(0, 'end')
        password2.config(show="*")
    def on_leave(e):
        name = password2.get()
        if name == '':
            password2.insert(0, 'Confirm Password')

    password2 = Entry(frames, width=25, fg='black', border=0,bg='white', font=("Microsoft Yahei UI Light", 11))
    password2.place(x=30, y=205)
    password2.insert(0, 'Confirm Password')
    password2.bind('<FocusIn>', on_enter)
    password2.bind('<FocusOut>', on_leave)
    Frame(frames, width=295, height=2, bg='black').place(x=25, y=230)
    Button(frames, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=signedup).place(x=35, y=250)
    window.mainloop()

def signin():
    username = user.get()
    passcode = password.get()

    con = oracledb.connect(
        user="python",password="coder",dsn="Localhost:1521/orcl")
    c = con.cursor()
    query1 = "SELECT COUNT(*) FROM USERID WHERE user_id = :username AND password=:password"
    c.execute(query1, {"username": user.get(), "password": password.get()})
    result1 = c.fetchone()[0]

    query2 = "SELECT COUNT(*) FROM ADMIN WHERE a_i= :username AND password=:password"
    c.execute(query2, {"username": user.get(), "password": password.get()})
    result2 = c.fetchone()[0]
    if result1 > 0 or result2 > 0:

        mainpage()
    else:
        messagebox.showinfo("Try again", "Username Or password is incorrect")
    c.close()
    con.close()

image = Image.open("photo.png")
img = ImageTk.PhotoImage(image)

Label(root, image=img, bg='white').place(x=5, y=20)
frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=530, y=70)
heading = Label(frame, text="Sign In", fg="#57a1f8", bg="white",font=("Microsoft Yahei UI Light", 23, 'bold'))
heading.place(x=110, y=5)
def on_enter(e):

    user.delete(0, 'end')
def on_leave(e):

    name = user.get()

    if name == '':

        user.insert(0, 'Username')
user = Entry(frame, width=25, fg='black', border=0,bg='white', font=("Microsoft Yahei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
def on_enter(e):

    password.delete(0, 'end')
    password.config(show="*")

def on_leave(e):

    name = password.get()

    if name == '':

        password.insert(0, 'Password')

password = Entry(frame, width=25, fg='black', border=0,bg='white', font=("Microsoft Yahei UI Light", 11))
password.place(x=30, y=160)
password.insert(0, 'Password')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=187)
Button(frame, width=39, pady=7, text='Sign In', bg='#57a1f8',fg='white', border=0, command=signin).place(x=35, y=208)
label = Label(frame, text="Don't have any account?", fg='black',bg='white', font=("Microsoft Yahei UI Light", 9))
label.place(x=80, y=250)
sign_up = Button(frame, width=6, text='Sign up', border=0,bg='white', cursor='hand2', fg="#57a1f8", command=signup)
sign_up.place(x=223, y=250)
root.mainloop()



