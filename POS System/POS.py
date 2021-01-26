from tkinter import *
import time, re, random, os
from tkinter import messagebox
from deals import Deal1, Deal2, Deal3





class POSSystem(Deal1, Deal2, Deal3):
    
    
    
    def __init__(self, window):
        self.window = window
        self.window.geometry("1350x700+0+0")
        self.window.title("Subway POS System")
        bg_color = "#2b7c5d"
        title = Label(self.window, text = "SUBWAY SANDWICH POS SYSTEM", bd = 12, relief = GROOVE, bg = bg_color, fg = "black", font = ("broadway", 30, "bold"), pady=2).pack(fill = X)            
        
        #=================variables
        
        self.chBBQ = IntVar()
        self.BMTit = IntVar()
        self.chTK = IntVar()
        self.tunaDel = IntVar()
        self.steak = IntVar()
        self.turkB = IntVar()
        
        self.ck = IntVar()
        self.chp = IntVar()
        self.dK = IntVar()
        self.cFF = IntVar()
        self.T = IntVar()
        self.chS = IntVar()
        
        self.chBUF = IntVar()
        self.veg = IntVar()
        self.chTPT = IntVar()

        
        
        #====================customer
        self.cname = StringVar()
        self.cphone = StringVar()
        
        self.bill_no = StringVar()
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
        
        
        #=====================Total Product
        self.sub_total = StringVar()
        
        self.tax = StringVar()
        
        
        
        
        #================Customer Details Frame
        F1 = LabelFrame(self.window, bd =10, relief = GROOVE, text = "Customer Details", font = ("Lucida Bright", 15, "bold"), fg = "gold", bg = bg_color)
        F1.place(x = 0, y = 80, relwidth = 1)
        
        cname_lbl = Label(F1, text = "Customer Name:", font = ("Helvetica", 15, "bold"),bg = bg_color, fg = "white").grid(row = 0, column = 0, padx = 20, pady = 5)
        cname_txt = Entry(F1, width = 15, textvariable = self.cname, font = "corbel 15", bd = 7, relief = SUNKEN).grid(row = 0, column = 1, pady=5, padx=10)        

        cphone_lbl = Label(F1, text = "Phone Number:", font = ("Helvetica", 15, "bold"),bg = bg_color, fg = "white").grid(row = 0, column = 2, padx = 20, pady = 5)
        cphone_txt = Entry(F1, width = 15, textvariable =self.cphone, font = "corbel 15", bd = 7, relief = SUNKEN).grid(row = 0, column = 3, pady=5, padx=10)    
        
        cbill_lbl = Label(F1, text = "Bill Number:", font = ("Helvetica", 15, "bold"),bg = bg_color, fg = "white").grid(row = 0, column = 4, padx = 20, pady = 5)
        cbill_txt = Entry(F1, width = 15, textvariable = self.search_bill, font = "corbel 15", bd = 7, relief = SUNKEN).grid(row = 0, column = 5, pady=5, padx=10)    


        bill_btn = Button(F1, image = img0,command=self.find_bill, bg="black", width =35, height=25, bd= 7).grid(row = 0, column = 6, padx=1, pady=1 )
        
        #=================Sandwich
        F2 = LabelFrame(self.window, bd =10, relief = GROOVE, text = "Regulars", font = ("Lucida Bright", 15, "bold"), fg = "gold", bg = bg_color)
        F2.place(x = 5, y = 180, width = 325, height= 380)
        
        chBBQ_lbl = Label(F2, text = "BBQ Chicken", font=("Helvetica", 12, "bold"), bg = bg_color , fg = "lightgreen").grid(row = 0, column =0, padx= 10, pady=10, sticky="w" )
        chBBQ_txt = Entry(F2, width = 10, textvariable =self.chBBQ, font=("Helvetica", 14, "bold"),bd = 5, relief = SUNKEN).grid(row=0, column=1, padx = 10, pady=10)
        
        BMTit_lbl = Label(F2, text = "BMT Italian", font=("Helvetica", 12, "bold"), bg = bg_color , fg = "lightgreen").grid(row = 1, column =0, padx= 10, pady=10, sticky="w" )
        BMTit_txt = Entry(F2, width = 10,textvariable =self.BMTit, font=("Helvetica", 14, "bold"),bd = 5, relief = SUNKEN).grid(row=1, column=1, padx = 10, pady=10)

        chTK_lbl = Label(F2, text = "Chicken Tikka", font=("Helvetica", 12, "bold"), bg = bg_color , fg = "lightgreen").grid(row = 2, column =0, padx= 10, pady=10, sticky="w" )
        chTK_txt = Entry(F2, width = 10, textvariable =self.chTK, font=("Helvetica", 14, "bold"),bd = 5, relief = SUNKEN).grid(row=2, column=1, padx = 10, pady=10)

        tunaDel_lbl = Label(F2, text = "Tuna Delight", font=("Helvetica", 12, "bold"), bg = bg_color , fg = "lightgreen").grid(row = 3, column =0, padx= 10, pady=10, sticky="w" )
        tunaDel_txt = Entry(F2, width = 10, textvariable =self.tunaDel, font=("Helvetica", 14, "bold"),bd = 5, relief = SUNKEN).grid(row=3, column=1, padx = 10, pady=10)
        
        
        steak_lbl = Label(F2, text = "Cheese Steak", font=("Helvetica", 12, "bold"), bg = bg_color , fg = "lightgreen").grid(row = 4, column =0, padx= 10, pady=10, sticky="w" )
        steak_txt = Entry(F2, width = 10, textvariable =self.steak, font=("Helvetica", 14, "bold"),bd = 5, relief = SUNKEN).grid(row=4, column=1, padx = 10, pady=10)
        
        
        turkB_lbl = Label(F2, text = "Turkey Breast", font=("Helvetica", 12, "bold"), bg = bg_color , fg = "lightgreen").grid(row = 5, column =0, padx= 10, pady=10, sticky="w" )
        turkB_txt = Entry(F2, width = 10, textvariable =self.turkB, font=("Helvetica", 14, "bold"),bd = 5, relief = SUNKEN).grid(row=5, column=1, padx = 10, pady=10)
       
        #=================Sides and Extras
        F3 = LabelFrame(self.window, bd =10, relief = GROOVE, text = "Sides, Drinks & Extras", font = ("Lucida Bright", 15, "bold"), fg = "gold", bg = bg_color)
        F3.place(x = 340, y = 180, width = 325, height= 380)
        
        ck_lbl = Label(F3, text = "Fresh Cookies", font=("Helvetica", 12, "bold"), bg = bg_color , fg = "lightgreen").grid(row = 0, column =0, padx= 10, pady=10, sticky="w" )
        ck_txt = Entry(F3, width = 10, textvariable = self.ck, font=("Helvetica", 14, "bold"),bd = 5, relief = SUNKEN).grid(row=0, column=1, padx = 10, pady=10)
        
        chp_lbl = Label(F3, text = "Regular Chips", font=("Helvetica", 12, "bold"), bg = bg_color , fg = "lightgreen").grid(row = 1, column =0, padx= 10, pady=10, sticky="w" )
        chp_txt = Entry(F3, width = 10, textvariable = self.chp, font=("Helvetica", 14, "bold"),bd = 5, relief = SUNKEN).grid(row=1, column=1, padx = 10, pady=10)

        dK_lbl = Label(F3, text = "Cold Drinks", font=("Helvetica", 12, "bold"), bg = bg_color , fg = "lightgreen").grid(row = 2, column =0, padx= 10, pady=10, sticky="w" )
        dK_txt = Entry(F3, width = 10, textvariable = self.dK, font=("Helvetica", 14, "bold"),bd = 5, relief = SUNKEN).grid(row=2, column=1, padx = 10, pady=10)

        cFF_lbl = Label(F3, text = "Hot Coffee", font=("Helvetica", 12, "bold"), bg = bg_color , fg = "lightgreen").grid(row = 3, column =0, padx= 10, pady=10, sticky="w" )
        cFF_txt = Entry(F3, width = 10, textvariable = self.cFF, font=("Helvetica", 14, "bold"),bd = 5, relief = SUNKEN).grid(row=3, column=1, padx = 10, pady=10)
        
        
        T_lbl = Label(F3, text = "Warm Tea", font=("Helvetica", 12, "bold"), bg = bg_color , fg = "lightgreen").grid(row = 4, column =0, padx= 10, pady=10, sticky="w" )
        T_txt = Entry(F3, width = 10, textvariable = self.T, font=("Helvetica", 14, "bold"),bd = 5, relief = SUNKEN).grid(row=4, column=1, padx = 10, pady=10)
        
        
        chS_lbl = Label(F3, text = "Cheese Slice", font=("Helvetica", 12, "bold"), bg = bg_color , fg = "lightgreen").grid(row = 5, column =0, padx= 10, pady=10, sticky="w" )
        chS_txt = Entry(F3, width = 10, textvariable = self.chS , font=("Helvetica", 14, "bold"),bd = 5, relief = SUNKEN).grid(row=5, column=1, padx = 10, pady=10)
        
        #=================Make-it-a-Meal
        F4 = LabelFrame(self.window, bd =10, relief = GROOVE, text = "Make-it-Meal", font = ("Lucida Bright",15,"bold"), fg = "gold", bg = bg_color)
        F4.place(x = 680, y = 180, width = 325, height= 380)
        
        chBUF_lbl = Label(F4, text = "Buffalo Chicken", font=("Forte", 14, "bold"), bg = bg_color , fg = "orange").grid(row = 0, column =0, padx= 5, pady=10, sticky="w" )
        chBUF_txt = Entry(F4, width = 8, textvariable = self.chBUF, font=("Helvetica", 14, "bold"),bd = 5, relief = SUNKEN).grid(row=0, column=1, padx = 5, pady=10)
        
        veg_lbl = Label(F4, text = "Veggie Delight", font=("Forte", 14, "bold"), bg = bg_color , fg = "orange").grid(row = 1, column =0, padx= 5, pady=10, sticky="w" )
        veg_txt = Entry(F4, width = 8, textvariable = self.veg, font=("Helvetica", 14, "bold"),bd = 5, relief = SUNKEN).grid(row=1, column=1, padx = 5, pady=10)

        chTPT_lbl = Label(F4, text = "Chatpata Chickpea", font=("Forte", 14, "bold"), bg = bg_color , fg = "orange").grid(row = 2, column =0, padx= 5, pady=10, sticky="w" )
        chTPT_w_txt = Entry(F4, width = 8, textvariable = self.chTPT, font=("Helvetica", 14, "bold"),bd = 5, relief = SUNKEN).grid(row=2, column=1, padx = 5, pady=10)

        F4_mini = Frame(F4, bd=7, bg = bg_color, relief = GROOVE)
        F4_mini.place(x=0, y=200, width=305, height=140)
        
        txt1 = Label(F4_mini, fg= "white", text = "*Meals include a 250ml Drink, Cookies and Chips.", font=("Lucida Bright", 8, "bold"), bg=bg_color).grid(row =0, column=0, sticky="w")
        txt2 = Label(F4_mini, fg= "white", text = "**Meals add Rs. 150/= to the cost of the burger.", font=("Lucida Bright", 8, "bold"), bg=bg_color).grid(row=1, column=0, sticky="w")
      
        #=================Bill Area
        F5 = LabelFrame(self.window, bd =10, relief = GROOVE)
        F5.place(x = 1020, y = 180, width = 320, height= 380)
        bill_title = Label(F5, text = "BILL AREA", font = ("Stencil", 15, "bold"), bd = 7, relief = GROOVE).pack(fill = X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand= scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand = 1)
        
        #=================Button Frame
        F6 = LabelFrame(self.window, bd =10, relief = GROOVE, text = f"Deal Menu\t\t\t\t\t\t           Operations\t\t\t     Sub-Total", font = ("Lucida Bright", 15, "bold"), fg = "gold", bg = bg_color)
        F6.place(x = 0, y = 560, relwidth = 1, height= 140)
        

        btn_ = Frame(F6, bd=7, bg = "gold", relief = GROOVE )
        btn_.place(x=0, width=740, height=105)

        btn_F = Frame(F6,  bd=7, bg="black", relief=GROOVE)
        btn_F.place(x=740, width=585, height=105)
        
        btn_FF = Frame(F6, bd=7,bg=bg_color, relief=GROOVE)
        btn_FF.place(x=1090, width=250, height=105)
        

        
        total_lbl = Label(btn_FF, text = "Sub-Total:", bg = bg_color, fg="black", font=("Lucida Bright", 10, "bold")).grid(row=0, column=0, padx=1, pady=1, sticky="w")
        total_txt = Entry(btn_FF, width=20, textvariable = self.sub_total,font="helvetica 10 bold", bd = 7, relief = SUNKEN).grid(row =0, column =1, padx= 1, pady=1)
        
        taxT = Label(btn_FF, text = "13% Tax:", bg = bg_color, fg="black", font=("Lucida Bright", 10, "bold")).grid(row=1, column=0, padx=1, pady=1, sticky="w")
        taxT_txt = Entry(btn_FF, width=20, textvariable = self.tax,font="helvetica 10 bold", bd = 7, relief = SUNKEN).grid(row =1, column =1, padx= 1, pady=1)
        
        #===================Operations
        Total_btn = Button(btn_F, image = img1 , command=self.calctotal, bd=0,width=72, height=75).grid(row=0, column=0, padx=6, pady=6)
        Bill_btn = Button(btn_F, image = img2, command=self.bill_area, bd=0, width=72, height=75).grid(row=0, column=1, padx=6, pady=6)
        Clear_btn = Button(btn_F, image = img3, command=self.clear_data, bd=0, width=72, height=75).grid(row=0, column=2, padx=6, pady=6)
        Exit_btn = Button(btn_F, image = img4, command=self.exitpos, bd=0,width=72, height=75).grid(row=0, column=3, padx=6, pady=6)
        
        #===================Deals
        Meal1_btn = Button(btn_, image = img5 , bg="orange", command=self.add1, bd = 3, width = 192, height=72, font = "helvetica 20 bold").grid(padx=20, pady=5, row = 0, column=0)         
        Meal2_btn = Button(btn_, image = img7 , bg="orange", command=self.add2, bd = 3, width = 192, height=72, font = "helvetica 20 bold").grid(padx=20, pady=5, row = 0, column=1)
        Meal3_btn = Button(btn_, image = img6 , bg="orange", command=self.add3, bd = 3, width = 192, height=72, font = "helvetica 20 bold").grid(padx=20, pady=5, row = 0, column=2)
        
        self.bill_screen()       

                
        
        
        
        
        
        
        
        
        


    #===================Funtionality
        
        
        
    # def verify(self):
    #     try:
        
    #         self.chBBQ_p = self.chBBQ.get()*510
    #         self.BMTit_p = self.BMTit.get()*645
    #         self.chTK_p = self.chTK.get()*405
    #         self.tunaDel_p = self.tunaDel.get()*485
    #         self.steak_p = self.steak.get()*645
    #         self.turkB_p = self.turkB.get()*645
            
    #         self.ck_p = self.ck.get()*130 
    #         self.chp_p = self.chp.get()*50
    #         self.dK_p = self.dK.get()*110
    #         self.cFF_p = self.cFF.get()*80
    #         self.T_p = self.T.get()*60
    #         self.chS_p = self.chS.get()*55
            
    #         self.chBUF_p = self.chBUF.get()*600
    #         self.veg_p = self.veg.get()*450
    #         self.chTPT_p = self.chTPT.get()*450
            
    #         self.total_item_p = float((self.chBBQ_p)+                                                       
    #                                       (self.BMTit_p)+            
    #                                       (self.chTK_p)+            
    #                                       (self.tunaDel_p)+            
    #                                       (self.steak_p)+
    #                                       (self.turkB_p)+            
    #                                       (self.ck_p)+            
    #                                       (self.chp_p)+            
    #                                       (self.dK_p)+            
    #                                       (self.cFF_p)+
    #                                       (self.T_p)+            
    #                                       (self.chS_p)+            
    #                                       (self.chBUF_p)+            
    #                                       (self.veg_p)+            
    #                                       (self.chTPT_p))
        
    #         self.sub_total.set("Rs. "+str(self.total_item_p))
    #         self.item_tax = round((self.total_item_p*0.13),2)
    #         self.tax.set("Rs. "+str(self.item_tax))
            
            
    #         self.Total_bill = float(self.total_item_p+
    #                                 self.item_tax)
            
    #     except Exception:
    #         self.error()
        
    #     except FloatingPointError:
    #         self.error()        

    #===================Funtionality
        
    def error(self):
        messagebox.showerror("Error", "Please enter correctly.")    
        
    # def conflict(self):
    #     messagebox.showerror("Error", "Bill already exists. Try Again.") 
        
    def calctotal(self):
        for i in os.listdir("bills/"):
            file = i.split('.')
            if self.search_bill.get() == str(file[0]):
                self.conflict()               
        try:
        
            self.chBBQ_p = self.chBBQ.get()*510
            self.BMTit_p = self.BMTit.get()*645
            self.chTK_p = self.chTK.get()*405
            self.tunaDel_p = self.tunaDel.get()*485
            self.steak_p = self.steak.get()*645
            self.turkB_p = self.turkB.get()*645
            
            self.ck_p = self.ck.get()*130 
            self.chp_p = self.chp.get()*50
            self.dK_p = self.dK.get()*110
            self.cFF_p = self.cFF.get()*80
            self.T_p = self.T.get()*60
            self.chS_p = self.chS.get()*55
            
            self.chBUF_p = self.chBUF.get()*600
            self.veg_p = self.veg.get()*450
            self.chTPT_p = self.chTPT.get()*450
            
            self.total_item_p = float((self.chBBQ_p)+                                                       
                                          (self.BMTit_p)+            
                                          (self.chTK_p)+            
                                          (self.tunaDel_p)+            
                                          (self.steak_p)+
                                          (self.turkB_p)+            
                                          (self.ck_p)+            
                                          (self.chp_p)+            
                                          (self.dK_p)+            
                                          (self.cFF_p)+
                                          (self.T_p)+            
                                          (self.chS_p)+            
                                          (self.chBUF_p)+            
                                          (self.veg_p)+            
                                          (self.chTPT_p))
        
            self.sub_total.set("Rs. "+str(self.total_item_p))
            self.item_tax = round((self.total_item_p*0.13),2)
            self.tax.set("Rs. "+str(self.item_tax))
            
            
            self.Total_bill = float(self.total_item_p+
                                    self.item_tax)
            
        except Exception:
            self.error()
        
        except FloatingPointError:
            self.error()
    
    def bill_screen(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END,"\t\tSUBWAY\n" )
        self.txtarea.insert(END,"\tSindh, Karachi, Pakistan.")
        self.txtarea.insert(END,"\n=================================\n")
        self.txtarea.insert(END,time.strftime('%b/%d/%y\t\t\t%I:%M %p', time.localtime()))
        self.txtarea.insert(END,f"\nBill Number:   \t{self.bill_no.get()}" )
        self.txtarea.insert(END,f"\nCustomer Name: \t{self.cname.get()}" )
        self.txtarea.insert(END,f"\nPhone Number:  \t{self.cphone.get()}" )
        self.txtarea.insert(END,"\n=================================")
        self.txtarea.insert(END,"\n Products\t\tQTY\tPrice")
        self.txtarea.insert(END,"\n=================================")
    
                
    def bill_area(self):

        # if self.cname.get() and self.sub_total.get() and self.tax.get() != str():
        #     self.error()
        
        if self.cname.get() == "" or self.cphone.get() == "":
            messagebox.showerror("Error", "Customer details are required.")
        
        elif self.sub_total.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No product selected.")
        
        else:
            
            self.bill_screen()
            if self.chBBQ.get() !=0:
                #=======Chicken BBQ Sandwich
                self.txtarea.insert(END,f"\n Chicken BBQ\t\t{self.chBBQ.get()}\t{self.chBBQ_p}")
            if self.BMTit.get() !=0:
                #=======BMT Italian Sandwich
                self.txtarea.insert(END,f"\n BMT Italian\t\t{self.BMTit.get()}\t{self.BMTit_p}")
            if self.chTK.get() !=0:
                #=======Chickn Tikka Sandwich
                self.txtarea.insert(END,f"\n Chicken Tikka\t\t{self.chTK.get()}\t{self.chTK_p}")
            if self.tunaDel.get() !=0:
                #=======Tuna Delight Sandwhich
                self.txtarea.insert(END,f"\n Tuna Delight\t\t{self.tunaDel.get()}\t{self.tunaDel_p}")
            if self.steak.get() !=0:
                #=======Steak and Cheese Sandwich
                self.txtarea.insert(END,f"\n Cheese Steak\t\t{self.steak.get()}\t{self.steak_p}")
            if self.turkB.get() !=0:
                #=======Turkey Breast Sandwich
                self.txtarea.insert(END,f"\n Turkey Breast\t\t{self.turkB.get()}\t{self.turkB_p}")
            
            
            if self.ck.get() !=0:
                #=======Cookies
                self.txtarea.insert(END,f"\n Fresh Cookies\t\t{self.ck.get()}\t{self.ck_p}")
            if self.chp.get() !=0:
                #=======Chips
                self.txtarea.insert(END,f"\n Regular Chips\t\t{self.chp.get()}\t{self.chp_p}")
            if self.dK.get() !=0:
                #=======Drinks
                self.txtarea.insert(END,f"\n Cold Drinks\t\t{self.dK.get()}\t{self.dK_p}")
            if self.cFF.get() !=0:
                #=======Coffee
                self.txtarea.insert(END,f"\n Hot Coffee\t\t{self.cFF.get()}\t{self.cFF_p}")
            if self.T.get() !=0:
                #=======Tea
                self.txtarea.insert(END,f"\n Warm Tea\t\t{self.T.get()}\t{self.T_p}")
            if self.chS.get() !=0:
                #=======Cheese
                self.txtarea.insert(END,f"\n Cheese Slice\t\t{self.chS.get()}\t{self.chS_p}")
            
            if self.chBUF.get() !=0:
                #=======Deal 1
                self.txtarea.insert(END,f"\n Deal 1\t\t{self.chBUF.get()}\t{self.chBUF_p}")
            if self.veg.get() !=0:
                #=======Deal 2
                self.txtarea.insert(END,f"\n Deal 2\t\t{self.veg.get()}\t{self.veg_p}")
            if self.chTPT.get() !=0:
                #=======Deal 3
                self.txtarea.insert(END,f"\n Deal 3\t\t{self.chTPT.get()}\t{self.chTPT_p}")            
            
    
            if self.tax.get()!="Rs. 0.0":        
                self.txtarea.insert(END,"\n---------------------------------")
                self.txtarea.insert(END,f"\n Total Tax\t\t{self.tax.get()}")
                self.txtarea.insert(END,"\n---------------------------------")
            
            self.txtarea.insert(END,f"\n Total Bill\t\tRs. {self.Total_bill}")
            self.txtarea.insert(END,"\n=================================\n")
            self.txtarea.insert(END,"~Thank You for choosing SUBWAY!~")
            self.txtarea.insert(END,"\n~~~Created By: Muhammad Nasir~~~")
            self.save_bill()
            

    def save_bill(self):
        op = messagebox.askyesno("SAVE BILL", "Do you want to save the bill?")
        
        if op>0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill {self.bill_no.get()} has been saved.")
        else:
            return
    
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            file = i.split('.')
            if self.search_bill.get() == str(file[0]):
                present="Yes"
                f1 = open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for j in f1:
                    
                    self.txtarea.insert(END, j)
                f1.close()
                
                
        if present == "no":
            messagebox.showerror("Error", "Invalid bill number")


    
    def clear_data(self):
        op = messagebox.askyesno("Exit", "Do you really want to clear data?")
        
        if op>0:
        
        
            self.chBBQ.set(0)
            self.BMTit.set(0)
            self.chTK.set(0)
            self.tunaDel.set(0)
            self.steak.set(0)
            self.turkB.set(0)
            
            self.ck.set(0)
            self.chp.set(0)
            self.dK.set(0)
            self.cFF.set(0)
            self.T.set(0)
            self.chS.set(0)
            
            self.chBUF.set(0)
            self.veg.set(0)
            self.chTPT.set(0)

             
            
             
            #====================customer
            self.cname.set("")
            self.cphone.set("")
            
            self.bill_no.set("")
            x = random.randint(1000,9999)
            self.bill_no.set(str(x))
            
            self.search_bill.set("")
            
            
            #=====================Total Product
            self.sub_total.set("")
            
            self.tax.set("")
            self.bill_screen()
        
    def exitpos(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op>0:
            self.window.destroy()
                    


try:

    window = Tk()
    img0 = PhotoImage(file = "search.png")
    img1 = PhotoImage(file = "total.png")
    img2 = PhotoImage(file = "bill.png")
    img3 = PhotoImage(file = "clear.png")
    img4 = PhotoImage(file = "exit.png")
    img5 = PhotoImage(file = "d1.png")
    img6 = PhotoImage(file = "d2.png")
    img7 = PhotoImage(file = "d3.png")
    
    obj = POSSystem(window)
    window.mainloop()
     
except:
    pass


    







