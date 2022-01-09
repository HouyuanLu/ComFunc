import sys
import json
import socket
import time
import decimal
import requests
from clint.textui import progress


def gs_user():
    filename = 'Cache/Username_Cache/uc.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def gn_user():
    username = input("What is your name? ")

    filename = 'Cache/Username_Cache/uc.json'

    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def g_u():
    username = gs_user()
    if username:
        print("Hello, it looks like you have an account already...")
        print("")
        choice = input("Do you want to create a new account? (y/n) ")
        if choice in ("y", "n"):
            if choice in "y":
                gn_user()
                print("We'll remember you when you come back!")
                print("")
            if choice in "n":
                print("")
                print(f"Welcome Again, {username}!")
                print("")
        else:
            print("Invalid Input")
            print("Press any key to continue...")
            input()
            exit(0)
    else:
        choice = input("Do You Want To Create An Account? (y/n): ")
        if choice in ("y", "n"):
            if choice in "y":
                username = gn_user()
                print("We'll remember you when you come back!")
                print("")
                pass
            if choice in "n":
                print("")
                pass
        else:
            print("Invalid Input")
            print("Press any key to continue...")
            input()
            sys.exit()


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def multiply_and_divide(x, y):
    return x * y / 2


def pi():
    decimal.getcontext().prec += 2  # extra digits for intermediate steps
    three = decimal.Decimal(3)  # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    decimal.getcontext().prec -= 2
    return +s  # unary plus applies the new precision


def download_file(url):
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(input("Enter The Name (Also Add The File Extension): "),
              'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return local_filename


def DownloadPdf(url):
    r = requests.get(url, stream=True)
    with open(
            input(
                "Enter The Name Of The PDF (Add The File Extension): "),
            "wb") as Pypdf:
        total_length = int(r.headers.get('content-length'))
        for ch in progress.bar(r.iter_content(chunk_size=2391975),
                               expected_size=(total_length / 1024) + 1):
            if ch:
                Pypdf.write(ch)


def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


def get_IP():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print("Computer Hostname:  ", host_name)
    print("IP Address: ", host_ip)


def get_stored_username():
    filename = 'Cache/Username_Cache/1username_cache.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What is your name? ")

    filename = 'Cache/Username_Cache/1username_cache.json'

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
