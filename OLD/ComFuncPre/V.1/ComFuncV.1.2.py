print("WELCOME TO THE COMFUNC PROJECT!")
print("    ")

import json
import time
import os

try:
    path = "Username_Cache"
    os.mkdir(path)
except FileExistsError:
    pass


def gs_user():
    filename = 'Username_Cache/uc.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def gn_user():
    username = input("What is your name? ")

    filename = 'Username_Cache/uc.json'

    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def g_u():
    username = gs_user()
    if username:
        print("Hello, it looks like you have an account already...")
        print("")
        time.sleep(.5)
        choice = input("Do you want to create a new account? (y/n) ")
        if choice in "y":
            gn_user()
            print("We'll remember you when you come back!")
            print("")
        if choice in "n":
            print("")
            print(f"Welcome Again, {username}!")
            print("")
    else:
        choice = input("Do You Want To Create An Account? (y/n): ")
        if choice in "y":
            username = gn_user()
            print("We'll remember you when you come back!")
            print("")
        if choice in "n":
            print("")
            pass


g_u()

while True:
    import socket
    from msvcrt import getch
    import time

    time.sleep(.8)
    print("This Is The V.1.2 Version!")
    print("    ")

    time.sleep(.5)

    print("Select Your Mode")
    print("0. Exit")
    print("1. CALCULATOR")
    print("2. Triangles")
    print("3. Rectangle-Area CALCULATOR")
    print("4. Games")
    print("5. Useful-Functions")

    choice = input("Enter Mode (0/1/2/3/4/5): ")

    if choice in "0":
        print("EXITING...")

        time.sleep(.8)
        print("DONE")

        time.sleep(1)
        exit()
    else:
        if choice in "1, 2, 3, 4, 5":
            if choice in "1":
                print("WELCOME TO THE CALCULATOR")

                time.sleep(2)


                def add(x, y):
                    return x + y


                def subtract(x, y):
                    return x - y


                def multiply(x, y):
                    return x * y


                def divide(x, y):
                    return x / y


                while True:
                    print("SELECT YOUR MODE")
                    print("0. Exit")
                    print("1. Add")
                    print("2. Subtract")
                    print("3. Multiply")
                    print("4. Divide")

                    Select = input("Enter Mode (0/1/2/3/4): ")

                    if Select in "0":
                        print("EXITING...")

                        time.sleep(.7)
                        print("DONE")

                        time.sleep(1)
                        exit()
                    else:
                        if Select in "1, 2, 3, 4":
                            if Select == "1":
                                num_1 = float(input("Enter The First Number: "))
                                num_2 = float(input("Enter The Second Number: "))
                                answer = (add(num_1, num_2))
                                print("The Answer is %s" % answer)

                                print("Press Any Key To Continue...")
                                getch()
                                exit()
                            if Select == "2":
                                num_1 = float(input("Enter The First Number: "))
                                num_2 = float(input("Enter The Second Number: "))
                                answer = (subtract(num_1, num_2))
                                print("The Answer is %s" % answer)

                                print("Press Any Key To Continue...")
                                getch()
                                exit()
                            if Select == "3":
                                num_1 = float(input("Enter The First Number: "))
                                num_2 = float(input("Enter The Second Number: "))
                                answer = (multiply(num_1, num_2))
                                print("The Answer is %s" % answer)

                                print("Press Any Key To Continue...")
                                getch()
                                exit()
                            if Select == "4":
                                num_1 = float(input("Enter The Dividend: "))
                                num_2 = float(input("Enter The Divisor: "))
                                answer = (divide(num_1, num_2))
                                print("The Answer is %s" % answer)

                                print("Press Any Key To Continue...")
                                getch()
                                exit()
                            break
                        else:
                            print("        ")
                            print("Invalid Input")
                            print("Please Try Again")
                            print("        ")

                            time.sleep(2)
            if choice in "2":
                while True:
                    print("Select Your Mode")
                    print("0. Exit")
                    print("1. Triangle-Area Calculator")
                    print("2. Sticks-Combine-->Triangle")

                    Mode = input("Enter Your Mode(0/1/2): ")

                    if Mode in "0":
                        print("EXITING...")

                        time.sleep(.7)
                        print("DONE")

                        time.sleep(1)
                        exit()
                    else:
                        if Mode in "1, 2":
                            if Mode in "1":
                                print("WELCOME TO THE TRIANGLE-AREA CALCULATOR")

                                time.sleep(2)
                                print("PLEASE ENTER THE BOTTOM-LENGTH")


                                def multiply_and_divide(x, y):
                                    return x * y / 2


                                num_1 = float(input())
                                print("NOW PLEASE ENTER THE HEIGHT")
                                num_2 = float(input())
                                answer = (multiply_and_divide(num_1, num_2))
                                print("THE AREA IS %s" % answer)

                                print("Press Any Key To Continue...")
                                getch()
                                exit()
                            if Mode in "2":
                                print("WELCOME TO THE STICK COMBINER")

                                time.sleep(1)
                                print("    ")

                                Length_1 = float(input("Please Enter The Length of The First Stick:"))
                                Length_2 = float(input("Please Enter The Length of The Second Stick:"))
                                Length_3 = float(input("Please Enter The Length of The Third Stick:"))

                                if Length_1 + Length_2 > Length_3:
                                    if Length_1 + Length_3 > Length_2:
                                        if Length_2 + Length_3 > Length_1:
                                            print("It Is Possible To Make A Triangle")
                                            time.sleep(.5)
                                            print("Press Any Key To Continue...")
                                            getch()
                                            exit()
                                            break
                                        else:
                                            print("It Is Not Possible To Make A Triangle")
                                            time.sleep(.5)
                                            print("Press Any Key To Continue...")
                                            getch()
                                            exit()
                                            break
                                    else:
                                        print("It Is Not Possible To Make A Triangle")
                                        time.sleep(.5)
                                        print("Press Any Key To Continue...")
                                        getch()
                                        exit()
                                        break
                                else:
                                    print("It Is Not Possible To Make A Triangle")
                                    time.sleep(.5)
                                    print("Press Any Key To Continue...")
                                    getch()
                                    exit()
                                    break
                        else:
                            print("        ")
                            print("Invalid Input")
                            print("Please Try Again")
                            print("        ")

                            time.sleep(2)

            if choice in "3":
                print("WELCOME TO THE RECTANGLE-AREA CALCULATOR")

                time.sleep(2)
                print("PLEASE ENTER THE LENGTH")


                def multiply(x, y):
                    return x * y


                num_1 = float(input())
                print("NOW PLEASE ENTER THE WIDTH")
                num_2 = float(input())
                answer = (multiply(num_1, num_2))
                print("THE AREA IS %s" % answer)

                print("Press Any Key To Continue...")
                getch()
                exit()
            if choice in "4":
                while True:
                    print("Select Your Game:")
                    print("0. Exit")
                    print("1. Number-Guess")
                    print("The Second Mode Is Still Under Developing...")

                    choice = input("Chose Your Mode (0/1): ")

                    if choice in ("0", "1"):
                        if choice in "0":
                            print("EXITING...")

                            time.sleep(.8)
                            print("DONE")

                            time.sleep(1)
                            exit()
                        if choice in "1":
                            while True:
                                import random

                                number = random.randint(0, 50)

                                Guess = float(input("I Am Thinking Of A Number! Guess The Number I Am Thinking Of: "))

                                while True:

                                    if Guess > number:
                                        Guess = float(input("Too High! Try Again: "))

                                    if Guess < number:
                                        Guess = float(input("Too Low! Try Again: "))

                                    if Guess == number:
                                        print("Well Done! That's The Number")
                                        print("Press Any Key To Continue...")
                                        getch()
                                        exit()
                                        break
                                break
                    else:
                        print("        ")
                        print("Invalid Input")
                        print("Please Try Again")
                        print("        ")

                        time.sleep(2)

            if choice in "5":
                while True:
                    print("Select Your Mode")
                    print("0. Exit")
                    print("1. Files Download")
                    print("2. Word Count")
                    print("3. IP Checker")
                    print("4. Remember Me")
                    print("5. Simple Text Editor")

                    choice = input("Enter Mode (0/1/2/3/4/5): ")

                    if choice in ("0", "1", "2", "3", "4", "5"):
                        if choice in "0":
                            print("EXITING...")

                            time.sleep(.8)
                            print("DONE")

                            time.sleep(1)
                            exit()
                        if choice in "1":
                            while True:
                                print("Select Your Mode")
                                print("0.Exit")
                                print("1.mp4_Download")
                                print("2.PDF_Download")
                                print("3.Image_Download")
                                print("      ")

                                Mode = input("Enter Your Mode (0/1/2/3): ")

                                if Mode in "0":
                                    print("EXITING...")

                                    time.sleep(.8)
                                    print("DONE")

                                    time.sleep(1)
                                    exit()

                                if Mode in ("1", "2", "3"):
                                    if Mode in "1":
                                        def download_file(url):
                                            import requests
                                            local_filename = url.split('/')[-1]
                                            r = requests.get(url, stream=True)
                                            with open(input("Enter The Name (Also Add The File Extension): "),
                                                      'wb') as f:
                                                for chunk in r.iter_content(chunk_size=1024):
                                                    if chunk:
                                                        f.write(chunk)
                                            return local_filename


                                        try:
                                            download_file(input("Enter Your URL: "))
                                            print("Downloading...")
                                            time.sleep(.5)
                                            print("Done")
                                            print("Press Any Key To Continue...")
                                            getch()
                                            exit()
                                        except:
                                            print("Invalid URL")
                                            print("Press Any Key To Continue...")
                                            getch()
                                            exit()

                                    if Mode in "2":
                                        def DownloadPdf(url):
                                            import requests
                                            from clint.textui import progress
                                            r = requests.get(url, stream=True)
                                            with open(
                                                    input("Enter The Name Of The PDF (Also Add The File Extension): "),
                                                    "wb") as Pypdf:
                                                total_length = int(r.headers.get('content-length'))
                                                for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                                                       expected_size=(total_length / 1024) + 1):
                                                    if ch:
                                                        Pypdf.write(ch)


                                        try:
                                            DownloadPdf(input("Enter Your URL: "))
                                            print("Downloading...")
                                            print("Done")
                                            print("Press Any Key To Continue...")
                                            getch()
                                            exit()
                                        except:
                                            print("Invalid input")
                                            print("Press Any Key To Continue...")
                                            getch()
                                            exit()
                                    if Mode in "3":
                                        import urllib.request

                                        url = input("Please Enter The URL: ")
                                        name = input("Please Enter The Name (Also Add The File Extension): ")

                                        print("Downloading...")
                                        try:
                                            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                                            with open(name, "wb") as f:
                                                with urllib.request.urlopen(req) as r:
                                                    f.write(r.read())
                                            print("Done!")
                                            print("Press Any Key To Continue...")
                                            getch()
                                            exit()
                                        except:
                                            print("Invalid URL")
                                            print("Press Any Key To Continue...")
                                            getch()
                                            exit()
                                    break
                                else:
                                    print("        ")
                                    print("Invalid Input")
                                    print("Please Try Again")
                                    print("        ")

                                    time.sleep(2)

                        if choice in "2":
                            def count_words(filename):
                                try:
                                    with open(filename, encoding='utf-8') as f:
                                        contents = f.read()
                                except FileNotFoundError:
                                    print(f"Sorry, the file {filename} does not exist.")
                                    print("Press Any Key To Continue...")
                                    getch()
                                    exit()
                                else:
                                    words = contents.split()
                                    num_words = len(words)
                                    print(f"The file {filename} has about {num_words} words.")
                                    print("Press Any Key To Continue...")
                                    getch()
                                    exit()


                            filename = input("Enter The File Name: ")
                            count_words(filename)

                        if choice in "3":
                            def get_IP():
                                host_name = socket.gethostname()
                                host_ip = socket.gethostbyname(host_name)
                                print("Computer Hostname:  ", host_name)
                                print("IP Address: ", host_ip)
                                print("Press Any Key To Continue...")
                                getch()
                                exit()


                            get_IP()
                            break

                        if choice in "4":

                            import os

                            try:
                                path = "Username_Cache"
                                os.mkdir(path)
                            except FileExistsError:
                                pass


                            def get_stored_username():
                                filename = 'Username_Cache/username_cache.json'
                                try:
                                    with open(filename) as f:
                                        username = json.load(f)
                                except FileNotFoundError:
                                    return None
                                else:
                                    return username


                            def get_new_username():
                                username = input("What is your name? ")

                                filename = 'Username_Cache/username_cache.json'

                                with open(filename, 'w') as f:
                                    json.dump(username, f)
                                return username


                            def greet_user():
                                username = get_stored_username()
                                if username:
                                    print("Welcome, it looks like you have an account already...")
                                    time.sleep(.3)
                                    choice = input("Do you want to create a new account? (y/n) ")
                                    if choice in "y":
                                        get_new_username()
                                        print("We'll remember you when you come back!")
                                    if choice in "n":
                                        print(f"Welcome back, {username}!")
                                else:
                                    username = get_new_username()
                                    print("We'll remember you when you come back!")


                            greet_user()

                            print("Press Any Key To Continue...")
                            getch()
                            exit()
                            break
                        if choice in "5":
                            import tkinter as tk
                            from tkinter.filedialog import askopenfilename, asksaveasfilename


                            def open_file():
                                """Open a file for editing."""
                                filepath = askopenfilename(
                                    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
                                )
                                if not filepath:
                                    return
                                txt_edit.delete(1.0, tk.END)
                                with open(filepath, "r") as input_file:
                                    text = input_file.read()
                                    txt_edit.insert(tk.END, text)
                                window.title(f"Simple Text Editor - {filepath}")


                            def save_file():
                                """Save the current file as a new file."""
                                filepath = asksaveasfilename(
                                    defaultextension="txt",
                                    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
                                )
                                if not filepath:
                                    return
                                with open(filepath, "w") as output_file:
                                    text = txt_edit.get(1.0, tk.END)
                                    output_file.write(text)
                                window.title(f"Simple Text Editor - {filepath}")


                            window = tk.Tk()
                            window.title("Simple Text Editor")
                            window.rowconfigure(0, minsize=800, weight=1)
                            window.columnconfigure(1, minsize=800, weight=1)

                            txt_edit = tk.Text(window)
                            fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
                            btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
                            btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

                            btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
                            btn_save.grid(row=1, column=0, sticky="ew", padx=5)

                            fr_buttons.grid(row=0, column=0, sticky="ns")
                            txt_edit.grid(row=0, column=1, sticky="nsew")

                            window.mainloop()
                            exit()
                            break
                        break
                    else:
                        print("        ")
                        print("Invalid Input")
                        print("Please Try Again")
                        print("        ")

                        time.sleep(2)
        else:
            print("        ")
            print("Invalid Input")
            print("Please Try Again")
            print("        ")

            time.sleep(2)
