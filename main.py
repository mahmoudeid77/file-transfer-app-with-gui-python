from tkinter import *
from tkinter import messagebox
import socket
import threading
import os

from tkinter import filedialog


root =Tk()
root.title("File Transfer")
root.geometry("450x560+500+200")
root.configure(bg="lightblue")
root.resizable(False,False)

def Send():
    window =Toplevel(root)
    window.title("Send")
    window.geometry("450x560+500+200")
    window.configure(bg="lightblue")
    window.resizable(False,False)

    host =socket.gethostname()
    Label(window,text="IP: "+host,font='arial 15 bold',bg='#fff',fg='#000').place(x=140,y=290)
    Button(window,text="+ select file",height=1,width=10,font='arial 14 bold',bg='#fff',fg='#000',command=select_file).place(x=160,y=150)
    Button(window,text="send",height=1,width=8,font='arial 14 bold',bg='#fff',fg='#000',command=lambda: threading.Thread(target=sender).start()).place(x=300,y=150)

    window.mainloop()

def Receive():
    window =Toplevel(root)
    window.title("receive")
    window.geometry("450x560+500+200")
    window.configure(bg="lightblue")
    window.resizable(False,False)

    def receiver():
        ID =Sender_ID.get()
        filename1 =incoming_file.get()

        s=socket.socket()
        port =8080
        s.connect((ID,port))
        file =open(filename1,'wb')
        file_data=s.recv(1024)
        file.write(file_data)
        file.close()
        s.close()
        messagebox.showinfo("success","file has been received and saved")

    Label(window,text='input sender id',font='arial 15 bold',bg='#fff',fg='#000').place(x=20,y=340)
    Sender_ID =Entry(window,width=30,font='arial 15',bg='white')
    Sender_ID.place(x=20,y=370)
    Sender_ID.focus()

    Label(window,text='file name for incoming file',font='arial 15 bold',bg='#fff',fg='#000').place(x=20,y=420)
    incoming_file =Entry(window,width=30,font='arial 15',bg='white')
    incoming_file.place(x=20,y=450)

    image_icon =PhotoImage(file="images/rc.png")
    rr =Button(window,image=image_icon,borderwidth=0,bg='#fff',activebackground='#fff',width=130,command=receiver)
    rr.place(x=20,y=500)

    window.mainloop()

def select_file():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select File",filetypes=(("all files","*.*"),))

def sender():
    s=socket.socket()
    host=socket.gethostname()
    port =8080
    s.bind((host,port))
    s.listen(1)
    print(host)
    print('Waiting for connection....')
    conn ,addr =s.accept()
    file =open(filename,'rb')
    file_data=file.read(1024)
    conn.send(file_data)
    print('File has been successfully sent')
    file.close()
    s.close()


#icon
image_icon = PhotoImage(file="images/download.png")
root.iconphoto(False,image_icon)

Label(root,text="File Transfer",font="arial 20 bold",bg="lightblue").pack(pady=20)
Frame(root,width=450,height=2,bg="#f3f5f6").place(x=25,y=80)

send_image=PhotoImage(file="images/download.png")
send = Button(root,image=send_image,borderwidth=0,bg="#f4fdfe",activebackground="lightblue",command=Send)
send.place(x=50,y=100)

receive_image=PhotoImage(file="images/receive.png")
receive = Button(root,image=receive_image,borderwidth=0,bg="#f4fdfe",activebackground="lightblue",command=Receive)
receive.place(x=300,y=100)

#label
Label(root,text="Send",font="arial 17 bold",bg="lightblue").place(x=65,y=200)
Label(root,text="Receive",font="arial 17 bold",bg="lightblue").place(x=300,y=200)

background_img = PhotoImage(file="images/bg.png")
Label(root,image=background_img,bg="lightblue").place(x=100,y=323)

root.mainloop()
