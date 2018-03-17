# import tkinter as tk
#
# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack()
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.grid(row=1,column=1)
#
#         e1 = tk.Entry(self)
#         e2 = tk.Entry(self)
#
#         e1.grid(row=1,column=3)
#         e2.grid(row=1,column=4)
#
#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=root.destroy)
#         self.quit.grid(row=1,column=2)
#
#     def say_hi(self):
#         print("hi there, everyone!")
#
# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()

import requests
import json
import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import *
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Register_User, Dashboard):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="DMAIL Client", font=controller.title_font)
        # label.pack(side="top", fill="x", pady=10)
        label.grid(column=1, row=1)

        group = tk.LabelFrame(self, text="Login", padx=10, pady=10)
        group.grid(column=1, row=2, padx=(10,10))



        private_key_label = tk.Label(group, text="Private Key").grid(row=2,column=1)
        private_key_entry = tk.Entry(group).grid(row=2,column=2)

        button2 = tk.Button(group, text="Login",
                            command=lambda: controller.show_frame("Dashboard"))
        button2.grid(row=3, column=2, pady=(10,10), command= lambda: StartPage.get_user(private_key_entry.text))

        button1 = tk.Button(self, text="Create Account",
                            command=lambda: controller.show_frame("Register_User"))


        button1.grid(row=4,column=1, pady=(20,20))

    @staticmethod
    def get_user(public_key):


        url = "https://dmail-hack-mit.herokuapp.com/finduser"

        payload = {"pub_key": public_key}

        payload = json.dumps(payload)
        headers = {
            'Content-Type': "application/json",
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)




class Register_User(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # label = tk.Label(self, text="Create Account", font=controller.title_font)
        # label.(side="top", fill="x", pady=10)
        username_label = tk.Label(self, text="Username")
        username_label.grid(row=1,column=1)

        username_entry = tk.Entry(self).grid(row=1, column=2)

        public_key_label = tk.Label(self, text="Public Key").grid(row=2,column=1)

        public_key_entry = tk.Entry(self).grid(row=2, column=2)

        register_button = tk.Button(self, text="Register")
        register_button.grid(row=3, column=1)

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=4,column=1)


class Dashboard(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Main Page", font=controller.title_font)
        label.grid(row=1, column=1)

        button_group = tk.LabelFrame(self, text="", padx=10, pady=10)
        button_group.grid(column=1, row=2, padx=(10, 10), sticky=W)


        send_email_button = tk.Button(button_group, text="Send Email").grid(row=2, column=1)
        fetch_emails_button = tk.Button(button_group, text="Fetch Email").grid(row=2, column=2)

        group = tk.LabelFrame(self, text="Emails", padx=10, pady=10)
        group.grid(column=1, row=3, padx=(10, 10))

        Dashboard.populate_emails(group)





        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=10, column=1)

    @staticmethod
    def populate_emails(root):
        public_key = "key--eins"
        emails = Dashboard.get_emails_from_end_point(public_key)

        row = 0
        for email in emails:
            box = tk.LabelFrame(root,text="",padx=10,pady=10)
            box.grid(column=1, row=row, sticky=W)

            email_label = tk.Label(box, text=email.generate_email_title())
            email_label.grid(row=1, column=1)
            row +=1


    @staticmethod
    def get_emails_from_end_point(public_key):
        email1 = Email_Object("sender-kaan", "receiver-Harsh", "Hello Kaan How are things")

        email2 = Email_Object("sender-Harsh", "receiver-Kaan", "Kaan everything is great, I love Georgia Tech!")

        email3 = Email_Object("sender-Kaan", "receiver-Harsh", "It is great to hear Harsh! I hope you become a professor at Tech")

        return [email1,email2,email3]

class Email_Object(object):

    def __init__(self,sender,receiver,content):

        self.sender = sender
        self.receiver =receiver
        self.content = content

    def generate_email_title(self):
        return "From: " + self.sender + " " + self.content



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()