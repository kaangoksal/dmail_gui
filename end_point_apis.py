import requests
import json
import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import *
from tkinter import messagebox

from encryption import encryption_api



class end_point_apis():

    @staticmethod
    def get_user(private_key, controller):

        # Fucking gnupg library doesn't work

        # command = lambda: controller.show_frame("Dashboard")
        # print("I received the private key ", private_key.encode())

        # file = open('privatekey.key', 'r')
        # private_key = file.read()
        # file.close()
        #
        # print("I found the private key ", private_key.encode())
        # imported_key = gpg.import_keys(private_key)
        #
        # public_key = gpg.export_keys(imported_key)

        file = open('publickey.key', 'r')
        public_key = file.read()
        file.close()

        url = "https://dmail-hack-mit.herokuapp.com/finduser"

        payload = {"pub_key": public_key}

        payload = json.dumps(payload)
        headers = {
            'Content-Type': "application/json",
        }
        print("Here is the payload ", payload)
        response = requests.request("POST", url, data=payload, headers=headers)

        parsed_json = response.json()

        if "username" in parsed_json:
            controller.show_frame("Dashboard")
        else:
           messagebox.showinfo("Error", "Authentication Error, no user exists")

        print(response.text)

    @staticmethod
    def register_user(self, username, public_key):
        print("Registering User ", username)

        url = "https://dmail-hack-mit.herokuapp.com/register"

        payload = {"pub_key": public_key, "username": username}

        payload = json.dumps(payload)
        headers = {
            'Content-Type': "application/json",
        }
        print("Here is the payload ", payload)
        response = requests.request("POST", url, data=payload, headers=headers)

        parsed_json = response.json()

        if "pub_key" in parsed_json:
            messagebox.showinfo("Success", "User Created Successfully")

        else:
            messagebox.showinfo("Error", "Register error: " + str(parsed_json["message"]))

        print("Here is the response ", response.text)

    @staticmethod
    def send_email(body, to_pub_key, sender):
        import requests

        url = "https://dmail-hack-mit.herokuapp.com/send"

        encrypted_message = encryption_api.encrypt_message(body, to_pub_key)

        encrypted_message_hash = encrypted_message

        payload = {"pub_key": to_pub_key, "sender": sender, "email_hash": encrypted_message_hash}
        payload = json.dumps(payload)

        headers = {
            'Content-Type': "application/json",
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)

