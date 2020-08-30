from tkinter import *
from PIL import Image, ImageDraw, ImageFont
import tkinter.messagebox
import random
import operator

class MathCaptcha:
    def __init__(self):
        self.window=Tk()
        self.window.title('Math Captcha')
       #self.window.geometry('600x600')
        self.flag=0
        self.frame1 = Frame(self.window, bg='#3498db', padx=150, pady=150)
        self.frame1.pack()
        self.frame2 = Frame(self.frame1, bg='#ffffff', padx=50, pady=20)
        self.frame2.pack()
        label1 = Label(self.frame2, text='CHECK YOUR DETAILS', bg='#ffffff', font='Times 30 bold')
        label1.grid(row=1,column=1,columnspan=2, pady=20)

        label2 = Label(self.frame2, text='REGISTRATION NO', bg='#ffffff', font='Times 15')
        label2.grid(row=2, column=1)
        
        self.regno = IntVar()
        entry2 = Entry(self.frame2, textvariable=self.regno,justify=RIGHT)
        entry2.grid(row=2,column=2, pady=10, ipady=3, padx=5)

        label3 = Label(self.frame2, text='ENTER YOUR NAME', bg='#ffffff', font='Times 15')
        label3.grid(row=3, column=1)

        self.name = StringVar()
        entry2 = Entry(self.frame2,textvariable=self.name)
        entry2.grid(row=3, column=2, pady=10, ipady=3, padx=5)
 
        button = Button(self.frame2, text="I'M NOT A ROBOT" ,bg='#3498db',activebackground='red', command=self.check_auth)
        button.grid(row=5, column=1,columnspan=2, pady=20)
    
        self.window.mainloop()

    def check_auth(self):
        try:
            if self.name.get() and int(self.regno.get()):
                self.generate_captcha()
            else:
                tkinter.messagebox.showinfo("Warning","Please fill the required details first")
        except:
            tkinter.messagebox.showinfo("Warning","Please fill the required details correctly.")

    def generate_captcha(self):
        self.frame2.pack_forget()
        self.flag=self.flag+1
        if(self.flag<=5):
            cmd = ['x','+','-']
            ops = { "+": operator.add, "-": operator.sub, "x":operator.mul }
            highest=12
            fno=random.randint(5,highest)
            sno=random.randint(5,highest)
            opr = random.randint(0,2)
            base = Image.open('base.png').convert('RGBA')
            txt = Image.new('RGBA', base.size, (255,255,255,0))
            font = ImageFont.truetype("arial.ttf", 72)
            d = ImageDraw.Draw(txt)
            d.text((10,10), "{}{}{}".format(fno,cmd[opr],sno), fill=(86,86,86), font=font)
            out = Image.alpha_composite(base, txt)
            out.save("MathCaptcha.gif")
            print('Answer is {}'.format(ops[cmd[opr]](fno,sno)))
            self.answer=ops[cmd[opr]](fno,sno)
        
            self.display_captcha()
        else:
            self.check_captcha()
        
    
    def display_captcha(self):
        
        self.frame2 = Frame(self.frame1, bg='#ffffff', padx=50, pady=20)
        self.frame2.pack()

        canvas = Canvas(self.frame2, width = 220, height = 100, bg='#ffffff')
        self.captcha_image = PhotoImage(file="MathCaptcha.gif")
        canvas.create_image(0,0, anchor=NW, image=self.captcha_image)
        canvas.grid(row=1,column=1,rowspan=2)
        button1=Button(self.frame2,text='Refresh',font='Times 15',command=self.generate_captcha)
        button1.grid(row=1,column=2)
        label1=Label(self.frame2,text='Enter Code',font='Times 15')
        label1.grid(row=2,column=2)
        self.code=IntVar()
        entry1=Entry(self.frame2,textvariable=self.code,justify=RIGHT)
        entry1.grid(row=3,column=2)
        button2=Button(self.frame2,text='Submit Form',font='Times 15',command=self.check_captcha)
        button2.grid(row=4,column=1)
        label3=Label(self.frame2,text='{} attempts left'.format(6-self.flag),font='Times 15',bg='#ffffff')
        label3.grid(row=5,column=1)

    def check_captcha(self):
        
        try:
            user_ans = int(self.code.get())
        except:
            user_ans = None
        
        if(self.answer==user_ans):
            print('Access granted')
            self.frame2.pack_forget()
            self.frame2 = Frame(self.frame1, bg='#ffffff', padx=50, pady=20)
            self.frame2.pack()
            label1 = Label(self.frame2, text='WELCOME DEAR STUDENT', bg='#ffffff',fg='red', font='Times 30 bold')
            label1.grid(row=1,column=1,columnspan=2, pady=20)

            label2 = Label(self.frame2, text='YOUR DETAILS', bg='#ffffff', font='Times 15')
            label2.grid(row=2,column=1,columnspan=2, pady=20)

            label3 = Label(self.frame2, text='REGISTRATION NO', bg='#ffffff', font='Times 15')
            label3.grid(row=3, column=1)
            label4 = Label(self.frame2,text=self.regno.get(),bg='#ffffff',font='Times 15')
            label4.grid(row=3,column=2)

            label5 = Label(self.frame2, text='NAME', bg='#ffffff', font='Times 15')
            label5.grid(row=4, column=1)     
            label6 = Label(self.frame2,text=self.name.get(),bg='#ffffff',font='Times 15')
            label6.grid(row=4,column=2)

            label3 = Label(self.frame2, text='PROGRAM', bg='#ffffff', font='Times 15')
            label3.grid(row=5, column=1)
            label4 = Label(self.frame2,text='P132:B.tech(CSE)',bg='#ffffff',font='Times 15')
            label4.grid(row=5,column=2)

            label3 = Label(self.frame2, text='INSTITUTE', bg='#ffffff', font='Times 15')
            label3.grid(row=6, column=1)
            label4 = Label(self.frame2,text='Lovely Professional University',bg='#ffffff',font='Times 15')
            label4.grid(row=6,column=2)
        
            
        elif (self.flag<=5):
            tkinter.messagebox.showinfo('WARNING','You have entered wrong CAPTCHA {} attempts left.'.format(5-self.flag))
            self.generate_captcha()
            
        else:   
            print('Access Denied')
            self.frame2.pack_forget()
            self.frame2 = Frame(self.frame1, bg='#ffffff', padx=50, pady=20)
            self.frame2.pack()
            label1 = Label(self.frame2, text='ACCESS DENIED', bg='#ffffff',fg='red', font='Times 30 bold')
            label1.grid(row=1,column=1,columnspan=2, pady=20)
            label2 = Label(self.frame2, text='Too many attempts.', bg='#ffffff', font='Times 15')
            label2.grid(row=2,column=1,columnspan=2, pady=20)
        
MathCaptcha()
