#DataFlair Python Image Stegangraphy project
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox,StringVar,dialog
from PIL import ImageTk
from PIL import Image
from io import BytesIO
from getpass import getpass
import os
securePass="secure"
class IMG_Stegno:
    password=""
    # main frame or start page
    def main(self, root):
        root.title('ImageSteganography by Maida and Hira')
        root.geometry('500x600')
        root.resizable(width =False, height=False)
        root.config(bg = '#e3f4f1')
        frame = Frame(root)
        frame.grid()
        
        title = Label(frame,text='MH Image Steganography')
        title.config(font=('Times new roman',25, 'bold'),bg = '#e3f4f1')
        title.grid(pady=10)
        title.grid(row=1)

        encode = Button(frame,text="Encode",command= lambda :self.encode_frame3(frame), padx=14,bg = '#e3f4f1' )
        encode.config(font=('Helvetica',14), bg='#e8c1c7')
        encode.grid(row=2)
        decode = Button(frame, text="Decode",command=lambda :self.decode_frame3(frame), padx=14,bg = '#e3f4f1')
        decode.config(font=('Helvetica',14), bg='#e8c1c7')
        decode.grid(pady = 12)
        decode.grid(row=3)

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

    # Back function to loop back to main screen
    def back(self,frame):
        frame.destroy()
        self.main(root)

    # frame for encode page
    def encode_frame1(self,F):
        F.destroy()
        F2 = Frame(root)
        label1= Label(F2,text='Select the Image in which \n you want to hide text :')
        label1.config(font=('Times new roman',25, 'bold'),bg = '#e3f4f1')
        label1.grid()

        button_bws = Button(F2,text='Select',command=lambda : self.encode_frame2(F2))
        button_bws.config(font=('Helvetica',18), bg='#e8c1c7')
        button_bws.grid()
        button_back = Button(F2, text='Cancel', command=lambda : IMG_Stegno.back(self,F2))
        button_back.config(font=('Helvetica',18),bg='#e8c1c7')
        button_back.grid(pady=15)
        button_back.grid()
        F2.grid()
    
    # frame for decode page
    def decode_frame1(self,F):
        F.destroy()
        d_f2 = Frame(root)
        label1 = Label(d_f2, text='Select Image with Hidden text:')
        label1.config(font=('Times new roman',25,'bold'),bg = '#e3f4f1')
        label1.grid()
        label1.config(bg = '#e3f4f1')
        button_bws = Button(d_f2, text='Select', command=lambda :self.decode_frame2(d_f2))
        button_bws.config(font=('Helvetica',18), bg='#e8c1c7')
        button_bws.grid()
        button_back = Button(d_f2, text='Cancel', command=lambda : IMG_Stegno.back(self,d_f2))
        button_back.config(font=('Helvetica',18), bg='#e8c1c7')
        button_back.grid(pady=15)
        button_back.grid()
        d_f2.grid()

    # function to encode image
    def encode_frame2(self,e_F2):
        
        e_pg= Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            my_img = Image.open(myfile)
            new_image = my_img.resize((300,200))
            img = ImageTk.PhotoImage(new_image)
            label3= Label(e_pg,text='Selected Image')
            label3.config(font=('Helvetica',14,'bold'))
            label3.grid() 
            board = Label(e_pg, image=img)
            board.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = my_img.size
            board.grid()
            label2 = Label(e_pg, text='Enter the message')
            label2.config(font=('Helvetica',14,'bold'))
            label2.grid(pady=15)
            text_a = Text(e_pg, width=50, height=10)
            text_a.grid()
            encode_button = Button(e_pg, text='Cancel', command=lambda : IMG_Stegno.back(self,e_pg))
            encode_button.config(font=('Helvetica',14), bg='#e8c1c7')
            data = text_a.get("1.0", "end-1c")
            button_back = Button(e_pg, text='Encode', command=lambda : [self.enc_fun(text_a,my_img,self.password),IMG_Stegno.back(self,e_pg)])
            button_back.config(font=('Helvetica',14), bg='#e8c1c7')
            button_back.grid(pady=15)
            encode_button.grid()
            e_pg.grid(row=1)
            e_F2.destroy()

       # function to verify password
    def verify_password(self, password):
        # You can implement your own logic for password verification
        # For simplicity, let's use a hardcoded password for demonstration purposes
        print("hello")
        return password == "hello" 
         
    def encode_frame3(self,e_F3):
        
        e_pg= Frame(root)
        label3= Label(e_pg,text='Enter Password')
        label3.config(font=('Helvetica',14,'bold'))
        label3.grid()

        password_var = StringVar()
        password_entry = Entry(e_pg, show="*",textvariable=password_var,width=20)
        password_entry.grid()

        p=password_var.get()
        print(p)
        

        def on_enter_button_click():
        # Retrieve the password when the "Enter" button is clicked
            entered_password = password_var.get()
            if entered_password != securePass:
                messagebox.showinfo("Error", "Incorrect password")
                return
            
            print("Entered password:", entered_password)
            # Add your logic to handle the entered password
            self.password=entered_password
            # Destroy the frame or perform any other actions
            self.encode_frame1(e_pg)

        button_back =Button(e_pg, text='Enter', command=on_enter_button_click)
        button_back.config(font=('Helvetica',14), bg='#e8c1c7')
        button_back.grid(pady=15)
        e_pg.grid(row=1)
        e_F3.destroy()
    
    # function to decode image
    def decode_frame2(self,d_F2):
        d_F3 = Frame(root)
        myfiles = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfiles:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            my_img = Image.open(myfiles, 'r')
            my_image = my_img.resize((300, 200))
            img = ImageTk.PhotoImage(my_image)
            label4= Label(d_F3,text='Selected Image :')
            label4.config(font=('Helvetica',14,'bold'))
            label4.grid()
            board = Label(d_F3, image=img)
            board.image = img
            board.grid()
            hidden_data = self.decode(my_img)
            label2 = Label(d_F3, text='Hidden data is :')
            label2.config(font=('Helvetica',14,'bold'))
            label2.grid(pady=10)
            text_a = Text(d_F3, width=50, height=10)
            text_a.insert(INSERT, hidden_data)
            text_a.configure(state='disabled')
            text_a.grid()
            button_back = Button(d_F3, text='Cancel', command= lambda :self.Page_3(d_F3))
            button_back.config(font=('Helvetica',14),bg='#e8c1c7')
            button_back.grid(pady=15)
            button_back.grid()
            d_F3.grid(row=1)
            d_F2.destroy()
        
    def decode_frame3(self,e_F3):
        
        e_pg= Frame(root)
        label3= Label(e_pg,text='Enter Password')
        label3.config(font=('Helvetica',14,'bold'))
        label3.grid()

        password_var = StringVar()
        password_entry = Entry(e_pg, show="*",textvariable=password_var,width=20)
        password_entry.grid()
        

        def on_enter_button_click():
        # Retrieve the password when the "Enter" button is clicked
            entered_password = password_var.get()
            if entered_password != securePass:
                messagebox.showinfo("Error", "Incorrect password")
                return
            
            print("Entered password:", entered_password)
            # Add your logic to handle the entered password
            self.password=entered_password
            # Destroy the frame or perform any other actions
            self.decode_frame1(e_pg)

        button_back =Button(e_pg, text='Enter', command=on_enter_button_click)
        button_back.config(font=('Helvetica',14), bg='#e8c1c7')
        button_back.grid(pady=15)
        e_pg.grid(row=1)
        e_F3.destroy()
    
    #function to decode data
    def decode(self, image):
        image_data = iter(image.getdata())
        data = ''
 
        while (True):
            pixels = [value for value in image_data.__next__()[:3] +
                      image_data.__next__()[:3] +
                      image_data.__next__()[:3]]
            # string of binary data
            binary_str = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binary_str += '0'
                else:
                    binary_str += '1'
 
            data += chr(int(binary_str, 2))
            if pixels[-1] % 2 != 0:
                return data
 
#function to generate data in binary 
    def generate_Data(self,data):
        # list of binary codes of given data
        new_data = []
 
        for i in data:
            new_data.append(format(ord(i), '08b'))
        return new_data
    #function to modify the pixels of image
    def modify_Pix(self,pix, data):
        dataList = self.generate_Data(data)
        dataLen = len(dataList)
        imgData = iter(pix)
        for i in range(dataLen):
            pix = [value for value in imgData.__next__()[:3] +
                   imgData.__next__()[:3] +
                   imgData.__next__()[:3]]
            for j in range(0, 8):
                if (dataList[i][j] == '0') and (pix[j] % 2 != 0):
                    if (pix[j] % 2 != 0):
                        pix[j] -= 1
                elif (dataList[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
                    if (i == dataLen - 1):
                        if (pix[-1] % 2 == 0):
                            pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1
 
            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]
    #function to enter the data pixels in image
    def encode_enc(self,newImg, data,password):
        
        w = newImg.size[0]
        (x, y) = (0, 0)
 
        for pixel in self.modify_Pix(newImg.getdata(), data):
 
            # Putting modified pixels in the new image
            newImg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1
    
    # function to enter hidden text
    def enc_fun(self,text_a,myImg,password):
        data = text_a.get("1.0", "end-1c")
        if (len(data) == 0):
            messagebox.showinfo("Alert","Kindly enter text in TextBox")
        else:
            newImg = myImg.copy()
            self.encode_enc(newImg, data,password)
            my_file = BytesIO()
            temp=os.path.splitext(os.path.basename(myImg.filename))[0]
            newImg.save(tkinter.filedialog.asksaveasfilename (initialfile=temp, filetypes = ([('png', '*.png')]), defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w,self.d_image_h = newImg.size
            messagebox.showinfo("Success","Encoding Successful\nFile is saved as Image_with_hiddentext.png in the same directory")
 
    def frame_3(self,frame):
        frame.destroy()
        self.main(root)


root = Tk()
o = IMG_Stegno()
o.main(root)
root.mainloop()

#https://data-flair.training/blogs/python-image-steganography-project/

#https://www.geeksforgeeks.org/image-based-steganography-using-python/

