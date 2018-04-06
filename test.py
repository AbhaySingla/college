# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/


#https://pythonprogramming.net/tkinter-depth-tutorial-making-actual-program/
#https://gist.github.com/SirRobo/c503014bbb03088bec37a61231036461
#https://blog.devcolor.org/heating-up-with-firebase-tutorial-on-how-to-integrate-firebase-into-your-app-6ce97440175d


import Tkinter as tk
import pyrebase

config = {
    "apiKey": "AIzaSyD3w34u_ldmgK61PaH5TAlQV64jj4ro1l8",
    "authDomain": "superstore-bde7f.firebaseapp.com",
    "databaseURL": "https://superstore-bde7f.firebaseio.com",
    "projectId": "superstore-bde7f",
    "storageBucket": "gs://superstore-bde7f.appspot.com",
    "messageSenderId": "superstore-bde7f.appspot.com",
    "serviceAccount": "/home/pi/Desktop/Sqube_Solutions/SuperStore-5486286531d1.json"
  }

firebase = pyrebase.initialize_app(config)

H1_FONT= ("Verdana", 14)
H2_FONT= ("Helvetica", 12)

class StoreHelpLine(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Search_Page, Call_Help, Product_Details, Wrong_Login):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):
    
    def Sign_In(self):
        
        emailSt = emailEL.get()
        pwordSt = pwordEL.get()
        
        auth = firebase.auth()
        try:
            user = auth.sign_in_with_email_and_password(emailSt, pwordSt)
            #file = open("temp.txt","w")
            #file.write(user)
            #file.close()        
            self.controller.show_frame(Search_Page)
        except:
            self.controller.show_frame(Wrong_Login)
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        global emailEL
        global pwordEL
        
        self.controller = controller
        
        label = tk.Label(self, text="Store HelpLine", font=H1_FONT)
        label.grid(row=0,column=0,sticky="ew")
        
        lable2 = tk.Label(self, text="Sign-In", font=H2_FONT)
        lable2.grid(sticky="ew")

        emailL = tk.Label(self, text='Email: ')
        pwordL = tk.Label(self, text='Password: ')
        emailL.grid(row=2, sticky="w")
        pwordL.grid(row=3, sticky="w")
        
        emailEL = tk.Entry(self) # The entry input
        pwordEL = tk.Entry(self, show='*')
        emailEL.grid(row=2, column=1)
        pwordEL.grid(row=3, column=1)
        
        #        app = fb.FirebaseApplication('https://helpine-de9a7.firebaseio.com/', authentication=None)
        
        button = tk.Button(self, text="Sign-In",
                           command=self.Sign_In)#lambda: controller.show_frame(Search_Page))
        button.grid(columnspan=2, sticky="w")


class Search_Page(tk.Frame):
    
    def search_function(self):
        
        searchSt = searchEL.get()
        
        file = open("temp.txt","a")
        file.write(searchSt)
        file.close()    
		myProduct_Details = Product_Details()
		myProduct_Details.read_file()
        self.controller.show_frame(Product_Details) 

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Store HelpLine", font=H1_FONT)
        label.grid(pady=10,padx=10)
        
        global searchEL
        
        self.controller = controller
        
        searchl = tk.Label(self, text="Search", font=H2_FONT)
        searchl.grid(row=2, sticky="w")
        
        searchEL = tk.Entry(self)
        searchEL.grid(row=2, column=1)
        
        button2 = tk.Button(self, text="Search", command=self.search_function)
        button2.grid(columnspan=2, sticky="w")
       
        button1 = tk.Button(self, text="Sign Out",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(columnspan=2, sticky="w")
                
        button3 = tk.Button(self, text="Request Help",
                            command=lambda: controller.show_frame(Call_Help))
        button3.grid(columnspan=2, sticky="w")
        


class Product_Details(tk.Frame):
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Store HelLine", font=H1_FONT)
        label.grid(pady=10,padx=10)
        
        label2 = tk.Label(self, text="PRODUCT SCREEN",font=H2_FONT)
        label2.grid(row=2)       
        
##        product_pic = gz.Picture(self, image = "download.gif")
##        product_name = Text(app, text="filler", font="Times New Roman", color="Black")
##        product_asile = Text(app, text="filler", font="Times New Roman", color="Black")
##        product_shelf = Text(app, text="filler", font="Times New Roman", color="Black")
##        product_price = Text(app, text="filler", font="Times New Roman", color="Black")
##        AddToCart_button = PushButton(app, command=send_to_database, text="Send to database")
##        GoBack_button = PushButton(app, command=go_back, text="Cancle")
##        call_help_button = PushButton(app, command=call_help, text="Call for help")

        button1 = tk.Button(self, text="Add to Cart")
        button1.grid(columnspan=1, sticky="w")

        button2 = tk.Button(self, text="Cancel",
                            command=lambda: controller.show_frame(Search_Page))
        button2.grid(columnspan=1, column=2, sticky="w")
        
        button3 = tk.Button(self, text="Request Help",
                            command=lambda: controller.show_frame(Call_Help))
        button3.grid(columnspan=2, sticky="w")
        
	def read_file():
		print "\nread file ran\n"
		file = open("temp.txt","r+")
        searchItem = file.readline()
        #searchItem = "12345"
        db = firebase.database()
        searchval = db.child("Items").get()
        labeltest = tk.Label(self, text=searchItem,font=H2_FONT)
        labeltest.grid(row=10)
                    
        for item in searchval.each():
            description = db.child("Items").child(item.key()).get()
            
            for itemdes in description.each():
                if itemdes.key() == "Name":#itemdes.val() == searchItem:
                    #file.write(itemdes.key())
                    labelna = tk.Label(self, text=itemdes.val(),font=H2_FONT)
                    labelna.grid(row=100)
                    
                    if itemdes.key() == "Asile Number":
                        file.write(itemdes.val())
        
        file.close() 
        
class Call_Help(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="StoreHelpLine", font=H1_FONT)
        label.pack(pady=10,padx=10)

        label2 = tk.Label(self, text="Call For Help", font=H2_FONT)
        label2.pack(pady=10,padx=10)
    
        text = tk.Label(self, text="Help is on its way!!")
        text.pack(pady=10,padx=10)
        
        button1 = tk.Button(self, text="OK",
                            command=lambda: controller.show_frame(Search_Page))
        button1.pack(pady=10,padx=10)

class Wrong_Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="StoreHelpLine", font=H1_FONT)
        label.pack(pady=10,padx=10)

        label2 = tk.Label(self, text="Worng Credentials", font=H2_FONT)
        label2.pack(pady=10,padx=10)
    
        button1 = tk.Button(self, text="OK",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=10,padx=10)

app = StoreHelpLine()
app.mainloop()
