try:
    import pyuac
except Exception as exp:
    print(exp)
    input()
    exit(1)
print("LOADING......")
try:
    import sys
    import time
    import json
    import os
    import socket
    import time
    import decimal
    import math
    import turtle
    import random
    import requests
    import urllib
    from clint.textui import progress
    from urllib import *
    from tkinter.filedialog import askopenfilename, asksaveasfilename
    import shutil
except Exception as e:
    print(e)
    input()
    exit(1)

try:
    import Functions
except Exception as ex:
    print("IMPORTANT FILE MISSING")
    print("CANNOT PROCEED")
    print(f"Error: {ex}")
    input()
    sys.exit()


def new_user_create():
    source = "main.py"
    s1 = "main.exe"
    filename = "Info.json"
    try:
        with open(filename) as f:
            info = json.load(f)
    except FileNotFoundError:
        print("Where do you want to download it?")
        print("exp: C:\\Program Files\\anyfolder")
        des = input()
        try:
            shutil.copy(s1, des, follow_symlinks=True)
        except FileNotFoundError:
            shutil.copy(source, des, follow_symlinks=True)
        tmp = "1"
        info = "1"
        with open(filename, 'w') as f:
            json.dump(tmp, f)
        tmp = "0"
    if info in "0":
        print("Where do you want to download it?")
        print("exp: C:\\Program Files\\anyfolder")
        des = input()
        try:
            shutil.copy(s1, des, follow_symlinks=True)
        except FileNotFoundError:
            shutil.copy(source, des, follow_symlinks=True)
        tmp = "1"
        with open(filename, 'w') as f:
            json.dump(tmp, f)
        tmp = "0"


def main():
    print(" ")
    print("WELCOME TO THE COMFUNC PROJECT!")
    print(" ")

    try:
        fpath = "Cache"
        os.mkdir(fpath)
    except:
        pass

    try:
        path = "Cache/Username_Cache"
        os.mkdir(path)
    except:
        pass

    Functions.g_u()

    print("This Is The Beta Version!")

    while True:
        print("    ")
        time.sleep(.5)

        print("Select Your Mode")
        print("0. Exit")
        print("1. Calculator")
        print("2. Games")
        print("3. Useful-Functions")

        choice = input("Enter Mode (0/1/2/3): ")

        if choice in ("", " "):
            print("NO INPUT?!")
            time.sleep(.5)
            print("Press Any Key To Continue...")
            input()
            print("")
            del choice
            continue
        if choice in "0":
            print("EXITING...")

            time.sleep(.8)
            print("DONE")

            time.sleep(1)
            sys.exit()
        else:
            if choice in "1, 2, 3":
                if choice in "1":
                    try:
                        apath = "Cache/NUM-CACHE"
                        os.mkdir(apath)
                    except:
                        pass
                    print("")
                    print("Welcome To The Calculator")

                    time.sleep(.5)

                    while True:
                        print("")
                        print("SELECT YOUR MODE")
                        print("0. Exit")
                        print("1. Number-Calculator")
                        print("2. Triangles")
                        print("3. Rectangles")
                        print("4. Circle")
                        print("5. Go Back")
                        Choice = input("Enter Mode (0/1/2/3/4/5): ")
                        print("")
                        if Choice in ("", " "):
                            print("NO INPUT?!")
                            time.sleep(.5)
                            print("Press Any Key To Continue...")
                            input()
                            print("")
                            continue
                        if Choice in "0":
                            print("EXITING...")

                            time.sleep(.7)
                            print("DONE")

                            time.sleep(1)
                            sys.exit()
                        if Choice in "5":
                            break
                        if Choice in "1,2,3,4":
                            if Choice in "1":
                                flagnum = False
                                flag = False
                                sum = 0
                                acache = 0
                                scache = 0
                                mcache = 0
                                dcache = 0
                                while True:
                                    if flag:
                                        break
                                    if flagnum:
                                        break
                                    aname = 'Cache/NUM-CACHE/add.json'
                                    sname = 'Cache/NUM-CACHE/sub.json'
                                    mname = 'Cache/NUM-CACHE/mul.json'
                                    dname = 'Cache/NUM-CACHE/div.json'
                                    try:
                                        with open(aname) as f:
                                            acache = json.load(f)
                                    except:
                                        pass
                                    try:
                                        with open(sname) as f:
                                            scache = json.load(f)
                                    except:
                                        pass
                                    try:
                                        with open(mname) as f:
                                            mcache = json.load(f)
                                    except:
                                        pass
                                    try:
                                        with open(dname) as f:
                                            dcache = json.load(f)
                                    except:
                                        pass
                                    try:
                                        sum = max(max(acache, scache), max(mcache, dcache))
                                    except:
                                        pass
                                    if acache == sum:
                                        if acache > 5:
                                            ans = input("Do you want to add? (y/n) ")
                                            if ans in "y":
                                                num_1 = float(input("Enter The First Number: "))
                                                num_2 = float(input("Enter The Second Number: "))
                                                answer = (Functions.add(num_1, num_2))
                                                print("The Answer is %s" % answer)

                                                try:
                                                    with open(aname) as f:
                                                        cache = json.load(f)
                                                except:
                                                    alname = 0
                                                    with open(aname, 'w') as f:
                                                        json.dump(alname, f)
                                                cache = cache + 1
                                                with open(aname, "w") as f:
                                                    json.dump(cache, f)

                                                choice = input("Do You Want To Try Again?(y/n)")
                                                if choice in "y":
                                                    flag = True
                                                    del choice
                                                    break
                                                else:
                                                    print("Press Any Key To Continue...")
                                                    input()
                                                    sys.exit(0)
                                            if ans in "n":
                                                print("")
                                                pass
                                        else:
                                            pass
                                    else:
                                        if scache == sum:
                                            if scache > 5:
                                                ans = input("Do you want to subtract? (y/n) ")
                                                if ans in "y":
                                                    num_1 = float(input("Enter The First Number: "))
                                                    num_2 = float(input("Enter The Second Number: "))
                                                    answer = (Functions.subtract(num_1, num_2))
                                                    print("The Answer is %s" % answer)

                                                    try:
                                                        with open(sname) as f:
                                                            cache = json.load(f)
                                                    except:
                                                        alname = 0
                                                        with open(sname, 'w') as f:
                                                            json.dump(alname, f)
                                                    cache = cache + 1
                                                    with open(sname, "w") as f:
                                                        json.dump(cache, f)

                                                    choice = input("Do You Want To Try Again?(y/n)")
                                                    if choice in "y":
                                                        flag = True
                                                        del choice
                                                        break
                                                    else:
                                                        print("Press Any Key To Continue...")
                                                        input()
                                                        sys.exit(0)
                                                else:
                                                    print("")
                                                    pass
                                            else:
                                                pass
                                        else:
                                            if mcache == sum:
                                                if mcache > 5:
                                                    ans = input("Do you want to multiply? (y/n) ")
                                                    if ans in "y":
                                                        num_1 = float(input("Enter The First Number: "))
                                                        num_2 = float(input("Enter The Second Number: "))
                                                        answer = (Functions.multiply(num_1, num_2))
                                                        print("The Answer is %s" % answer)

                                                        try:
                                                            with open(mname) as f:
                                                                cache = json.load(f)
                                                        except:
                                                            alname = 0
                                                            with open(mname, 'w') as f:
                                                                json.dump(alname, f)
                                                        cache = cache + 1
                                                        with open(mname, "w") as f:
                                                            json.dump(cache, f)

                                                        choice = input("Do You Want To Try Again?(y/n)")
                                                        if choice in "y":
                                                            del choice
                                                            flag = True
                                                            break
                                                        else:
                                                            print("Press Any Key To Continue...")
                                                            input()
                                                            sys.exit(0)
                                                    else:
                                                        print("")
                                                        pass
                                                else:
                                                    pass
                                            else:
                                                if dcache > 5:
                                                    ans = input("Do you want to divide? (y/n) ")
                                                    if ans in "y":
                                                        num_1 = float(input("Enter The Dividend: "))
                                                        num_2 = float(input("Enter The Divisor: "))
                                                        answer = (Functions.divide(num_1, num_2))
                                                        print("The Answer is %s" % answer)

                                                        try:
                                                            with open(dname) as f:
                                                                cache = json.load(f)
                                                        except:
                                                            alname = 0
                                                            with open(dname, 'w') as f:
                                                                json.dump(alname, f)
                                                        cache = cache + 1
                                                        with open(dname, "w") as f:
                                                            json.dump(cache, f)

                                                        choice = input("Do You Want To Try Again?(y/n)")
                                                        if choice in "y":
                                                            del choice
                                                            flag = True
                                                            break
                                                        else:
                                                            print("Press Any Key To Continue...")
                                                            input()
                                                            sys.exit(0)
                                                    else:
                                                        print("")
                                                        pass
                                                else:
                                                    pass
                                    while True:
                                        print("SELECT YOUR MODE")
                                        print("0. Exit")
                                        print("1. Add")
                                        print("2. Subtract")
                                        print("3. Multiply")
                                        print("4. Divide")
                                        print("5. Power")
                                        print("6. Clear Mode Cache")
                                        print("7. Go Back")

                                        Select = input("Enter Mode (0/1/2/3/4/5/6/7): ")
                                        if Select in ("", " "):
                                            print("NO INPUT?!")
                                            time.sleep(.5)
                                            print("Press Any Key To Continue...")
                                            input()
                                            print("")
                                            continue
                                        if Select in "7":
                                            flagnum = True
                                            break
                                        if Select in "6":
                                            try:
                                                try:
                                                    apath = "Cache\\NUM-CACHE\\add.json"
                                                    os.remove(apath)
                                                except FileNotFoundError:
                                                    pass
                                                try:
                                                    apath = "Cache\\NUM-CACHE\\sub.json"
                                                    os.remove(apath)
                                                except FileNotFoundError:
                                                    pass
                                                try:
                                                    apath = "Cache\\NUM-CACHE\\mul.json"
                                                    os.remove(apath)
                                                except FileNotFoundError:
                                                    pass
                                                try:
                                                    apath = "Cache\\NUM-CACHE\\div.json"
                                                    os.remove(apath)
                                                except FileNotFoundError:
                                                    pass
                                            except Exception as e:
                                                print(e)
                                                input("Press Any Key To Continue...")
                                                input()
                                                exit(0)
                                            print("CACHE DELETED!")
                                            print("Press Any Key To Continue...")
                                            input()
                                            exit(0)
                                        if Select in "0":
                                            print("EXITING...")

                                            time.sleep(.7)
                                            print("DONE")

                                            time.sleep(1)
                                            sys.exit()
                                        else:
                                            if Select in "1, 2, 3, 4, 5":
                                                if Select == "1":
                                                    num_1 = float(input("Enter The First Number: "))
                                                    num_2 = float(input("Enter The Second Number: "))
                                                    answer = (Functions.add(num_1, num_2))
                                                    print("The Answer is %s" % answer)
                                                    cache = 0
                                                    try:
                                                        with open(aname) as f:
                                                            cache = json.load(f)
                                                    except:
                                                        alname = 1
                                                        with open(aname, 'w') as f:
                                                            json.dump(alname, f)
                                                    cache = cache + 1
                                                    with open(aname, "w") as f:
                                                        json.dump(cache, f)

                                                    choice = input("Do You Want To Calculate Again?(y/n)")
                                                    if choice in "y":
                                                        del choice
                                                        break
                                                    else:
                                                        print("Press Any Key To Continue...")
                                                        input()
                                                        sys.exit(0)
                                                if Select == "2":
                                                    num_1 = float(input("Enter The First Number: "))
                                                    num_2 = float(input("Enter The Second Number: "))
                                                    answer = (Functions.subtract(num_1, num_2))
                                                    print("The Answer is %s" % answer)
                                                    cache = 0
                                                    try:
                                                        with open(sname) as f:
                                                            cache = json.load(f)
                                                    except:
                                                        alname = 1
                                                        with open(sname, 'w') as f:
                                                            json.dump(alname, f)
                                                    cache = cache + 1
                                                    with open(sname, "w") as f:
                                                        json.dump(cache, f)

                                                    choice = input("Do You Want To Calculate Again?(y/n)")
                                                    if choice in "y":
                                                        del choice
                                                        break
                                                    else:
                                                        print("Press Any Key To Continue...")
                                                        input()
                                                        sys.exit(0)
                                                if Select == "3":
                                                    num_1 = float(input("Enter The First Number: "))
                                                    num_2 = float(input("Enter The Second Number: "))
                                                    answer = (Functions.multiply(num_1, num_2))
                                                    print("The Answer is %s" % answer)
                                                    cache = 0
                                                    try:
                                                        with open(mname) as f:
                                                            cache = json.load(f)
                                                    except:
                                                        alname = 1
                                                        with open(mname, 'w') as f:
                                                            json.dump(alname, f)
                                                    cache = cache + 1
                                                    with open(mname, "w") as f:
                                                        json.dump(cache, f)

                                                    choice = input("Do You Want To Calculate Again?(y/n)")
                                                    if choice in "y":
                                                        del choice
                                                        break
                                                    else:
                                                        print("Press Any Key To Continue...")
                                                        input()
                                                        sys.exit(0)
                                                if Select == "4":
                                                    num_1 = float(input("Enter The Dividend: "))
                                                    num_2 = float(input("Enter The Divisor: "))
                                                    answer = (Functions.divide(num_1, num_2))
                                                    print("The Answer is %s" % answer)
                                                    cache = 0
                                                    try:
                                                        with open(dname) as f:
                                                            cache = json.load(f)
                                                    except:
                                                        alname = 1
                                                        with open(dname, 'w') as f:
                                                            json.dump(alname, f)
                                                    cache = cache + 1
                                                    with open(dname, "w") as f:
                                                        json.dump(cache, f)

                                                    choice = input("Do You Want To Calculate Again?(y/n)")
                                                    if choice in "y":
                                                        del choice
                                                        break
                                                    else:
                                                        print("Press Any Key To Continue...")
                                                        input()
                                                        sys.exit(0)
                                                if Select == "5":
                                                    a = float(input("Enter The Number: "))
                                                    c = float(input("Enter The Power: "))
                                                    a = math.pow(a, c)
                                                    print("The Answer is %d" % a)
                                                    choice = input("Do You Want To Calculate Again?(y/n)")
                                                    if choice in "y":
                                                        del choice
                                                        break
                                                    else:
                                                        print("Press Any Key To Continue...")
                                                        input()
                                                        sys.exit(0)
                                            else:
                                                print("        ")
                                                print("Invalid Input")
                                                print("Please Try Again")
                                                print("        ")

                                                time.sleep(2)
                            if Choice in "2":
                                while True:
                                    print("SELECT YOUR MODE")
                                    print("0. Exit")
                                    print("1. Triangle-Area Calculator")
                                    print("2. Sticks-Combine-->Triangle")
                                    print("3. Go Back")

                                    Mode = input("Enter Your Mode(0/1/2/3): ")
                                    if Mode in ("", " "):
                                        print("NO INPUT?!")
                                        time.sleep(.5)
                                        print("Press Any Key To Continue...")
                                        input()
                                        print("")
                                        continue

                                    if Mode in "0":
                                        print("EXITING...")

                                        time.sleep(.7)
                                        print("DONE")

                                        time.sleep(1)
                                        sys.exit()
                                    if Mode in "3":
                                        break
                                    else:
                                        if Mode in "1, 2":
                                            if Mode in "1":
                                                print("WELCOME TO THE TRIANGLE-AREA CALCULATOR")

                                                time.sleep(2)
                                                print("PLEASE ENTER THE BOTTOM-LENGTH")

                                                num_1 = float(input())
                                                print("NOW PLEASE ENTER THE HEIGHT")
                                                num_2 = float(input())
                                                answer = (Functions.multiply_and_divide(num_1, num_2))
                                                print("THE AREA IS %s" % answer)

                                                choice = input("Do You Want To Calculate Again?(y/n)")
                                                if choice in "y":
                                                    break
                                                else:
                                                    print("Press Any Key To Continue...")
                                                    input()
                                                    sys.exit(0)
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
                                                            choice = input("Do You Want To Calculate Again?(y/n)")
                                                            if choice in "y":
                                                                break
                                                            else:
                                                                print("Press Any Key To Continue...")
                                                                input()
                                                                sys.exit(0)
                                                        else:
                                                            print("It Is Not Possible To Make A Triangle")
                                                            time.sleep(.5)
                                                            choice = input("Do You Want To Try Again?(y/n)")
                                                            if choice in "y":
                                                                break
                                                            else:
                                                                print("Press Any Key To Continue...")
                                                                input()
                                                                sys.exit(0)
                                                    else:
                                                        print("It Is Not Possible To Make A Triangle")
                                                        time.sleep(.5)
                                                        choice = input("Do You Want To Try Again?(y/n)")
                                                        if choice in "y":
                                                            break
                                                        else:
                                                            print("Press Any Key To Continue...")
                                                            input()
                                                            sys.exit(0)
                                                else:
                                                    print("It Is Not Possible To Make A Triangle")
                                                    time.sleep(.5)
                                                    choice = input("Do You Want To Try Again?(y/n)")
                                                    if choice in "y":
                                                        break
                                                    else:
                                                        print("Press Any Key To Continue...")
                                                        input()
                                                        sys.exit(0)
                                        else:
                                            print("        ")
                                            print("Invalid Input")
                                            print("Please Try Again")
                                            print("        ")
                                            time.sleep(2)
                                            continue

                            if Choice in "3":
                                print("WELCOME TO THE RECTANGLE-AREA CALCULATOR")

                                time.sleep(2)
                                print("PLEASE ENTER THE LENGTH")

                                num_1 = float(input())
                                print("NOW PLEASE ENTER THE WIDTH")
                                num_2 = float(input())
                                answer = (Functions.multiply(num_1, num_2))
                                print("THE AREA IS %s" % answer)

                                choice = input("Do You Want To Try Again?(y/n)")
                                if choice in "y":
                                    break
                                else:
                                    print("Press Any Key To Continue...")
                                    input()
                                    sys.exit(0)
                            if Choice in "4":
                                while True:
                                    print("WELCOME TO CIRCLE CALCULATOR")
                                    print(" ")
                                    print("Select Your Mode:")
                                    print("0. Exit")
                                    print("1. pi")
                                    print("2. Circle-Area")
                                    print("3. Sector-Area")
                                    print("4. Go Back")
                                    mode = input("Enter Your Mode (0/1/2/3/4): ")
                                    if mode in ("", " "):
                                        print("NO INPUT?!")
                                        time.sleep(.5)
                                        print("Press Any Key To Continue...")
                                        input()
                                        print("")
                                        continue

                                    if mode in "0":
                                        print("EXITING...")

                                        time.sleep(.7)
                                        print("DONE")

                                        time.sleep(1)
                                        sys.exit()
                                    if mode in "4":
                                        break
                                    if mode in "1":

                                        dec = int(input("Enter How Many Digit You Want To Calculate: "))
                                        dec = dec + 2
                                        decimal.getcontext().prec = dec
                                        pi = Functions.pi()
                                        print(pi)
                                        print("")
                                        choice = input("Do You Want To Calculate Again?(y/n)")
                                        if choice in "y":
                                            continue
                                        else:
                                            print("Press Any Key To Continue...")
                                            input()
                                            sys.exit(0)
                                    if mode in "2":
                                        pi = 3.1415926
                                        d = float(input("Enter The Diameter of The Circle: "))
                                        r = d / 2
                                        area = float(pi * (r * r))
                                        print("The Area Is About %f" % area)
                                        print("")
                                        choice = input("Do You Want To Calculate Again?(y/n)")
                                        if choice in "y":
                                            continue
                                        else:
                                            print("Press Any Key To Continue...")
                                            input()
                                            sys.exit(0)
                                    if mode in "3":
                                        pi = 3.1415926
                                        d = float(input("Enter The Diameter of The Circle: "))
                                        angle = float(input("Enter The Angle: "))
                                        r = d / 2
                                        areac = float(pi * (r * r))
                                        area = angle / 360 * areac
                                        print("The Area Is About %f" % area)
                                        print("")
                                        choice = input("Do You Want To Calculate Again?(y/n)")
                                        if choice in "y":
                                            continue
                                        else:
                                            print("Press Any Key To Continue...")
                                            input()
                                            sys.exit(0)

                                    else:
                                        print("        ")
                                        print("Invalid Input")
                                        print("Please Try Again")
                                        print("        ")
                                        time.sleep(2)
                                        continue
                        else:
                            print("        ")
                            print("Invalid Input")
                            print("Please Try Again")
                            print("        ")
                            time.sleep(2)
                            continue

                if choice in "2":
                    while True:
                        print("SELECT YOUR MODE:")
                        print("0. Exit")
                        print("1. Number-Guess")
                        print("2. Roll-A-Die")
                        print("3. Go Back")

                        Choice1 = input("Chose Your Mode (0/1/2/3): ")
                        if Choice1 in ("", " "):
                            print("NO INPUT?!")
                            time.sleep(.5)
                            print("Press Any Key To Continue...")
                            input()
                            print("")
                            continue
                        if Choice1 in "3":
                            break
                        if Choice1 in ("0", "1", "2"):
                            if Choice1 in "0":
                                print("EXITING...")

                                time.sleep(.8)
                                print("DONE")

                                time.sleep(1)
                                sys.exit()
                            if Choice1 in "1":
                                gameflag = False
                                while True:
                                    if gameflag:
                                        break
                                    number = random.randint(0, 51)

                                    Guess = float(
                                        input("Can You Guess The Number I Am Thinking Of?: "))

                                    while True:

                                        if Guess > number:
                                            Guess = float(input("Too High! Try Again: "))

                                        if Guess < number:
                                            Guess = float(input("Too Low! Try Again: "))

                                        if Guess == number:
                                            print("Well Done! That's The Number")
                                            choice = input("Do You Want To Try Again?(y/n)")
                                            if choice in "y":
                                                gameflag = True
                                                break
                                            else:
                                                print("Press Any Key To Continue...")
                                                input()
                                                sys.exit(0)
                            if Choice1 in "2":
                                player_one = turtle.Turtle()
                                player_one.color("green")
                                player_one.shape("turtle")
                                player_one.penup()
                                player_one.goto(-200, 100)
                                player_two = player_one.clone()
                                player_two.color("blue")
                                player_two.penup()
                                player_two.goto(-200, -100)

                                player_one.goto(300, 60)
                                player_one.pendown()
                                player_one.circle(40)
                                player_one.penup()
                                player_one.goto(-200, 100)
                                player_two.goto(300, -140)
                                player_two.pendown()
                                player_two.circle(40)
                                player_two.penup()
                                player_two.goto(-200, -100)

                                die = [1, 2, 3, 4, 5, 6]

                                for i in range(20):
                                    if player_one.pos() >= (300, 100):
                                        print("Player One Wins!")
                                        break
                                    elif player_two.pos() >= (300, -100):
                                        print("Player Two Wins!")
                                        break
                                    else:
                                        player_one_turn = input("Press 'Enter' to roll the die ")
                                        die_outcome = random.choice(die)
                                        print("The result of the die roll is: ")
                                        print(die_outcome)
                                        print("The number of steps will be: ")
                                        print(20 * die_outcome)
                                        player_one.fd(20 * die_outcome)
                                        player_two_turn = input("Press 'Enter' to roll the die ")
                                        die_outcome = random.choice(die)
                                        print("The result of the die roll is: ")
                                        print(die_outcome)
                                        print("The number of steps will be: ")
                                        print(20 * die_outcome)
                                        player_two.fd(20 * die_outcome)

                                turtle.bye()
                                choice = input("Do You Want To Calculate Again?(y/n)")
                                if choice in "y":
                                    break
                                else:
                                    print("Press Any Key To Continue...")
                                    input()
                                    sys.exit(0)
                        else:
                            print("        ")
                            print("Invalid Input")
                            print("Please Try Again")
                            print("        ")
                            time.sleep(2)
                            continue

                if choice in "3":
                    flag = False
                    try:
                        path = "Cache/M1-CACHE"
                        os.mkdir(path)
                    except:
                        pass
                    sum = 0
                    fcache = 0
                    wcache = 0
                    icache = 0
                    rcache = 0
                    scache = 0
                    while True:
                        if flag:
                            break
                        fname = 'Cache/M1-CACHE/files.json'
                        wname = 'Cache/M1-CACHE/word.json'
                        iname = 'Cache/M1-CACHE/IP.json'
                        rname = 'Cache/M1-CACHE/remember.json'
                        siname = 'Cache/M1-CACHE/simple.json'
                        try:
                            with open(fname) as f:
                                fcache = json.load(f)
                        except:
                            pass
                        try:
                            with open(wname) as f:
                                wcache = json.load(f)
                        except:
                            pass
                        try:
                            with open(iname) as f:
                                icache = json.load(f)
                        except:
                            pass
                        try:
                            with open(rname) as f:
                                rcache = json.load(f)
                        except:
                            pass
                        try:
                            with open(siname) as f:
                                scache = json.load(f)
                        except:
                            pass
                        try:
                            sum = max(max(fcache, wcache), max(icache, rcache))
                            sum = max(sum, scache)
                        except:
                            pass
                        if fcache == sum:
                            if fcache > 8:
                                ans = input("Do you want to download a file? (y/n) ")
                                if ans in "y":
                                    cache = 0
                                    try:
                                        with open(fname) as f:
                                            cache = json.load(f)
                                    except:
                                        alname = 0
                                        with open(fname, 'w') as f:
                                            json.dump(alname, f)
                                    cache = cache + 1
                                    with open(fname, "w") as f:
                                        json.dump(cache, f)
                                    while True:
                                        print("SELECT YOUR MODE")
                                        print("0.Exit")
                                        print("1. mp4_Download")
                                        print("2. PDF_Download")
                                        print("3. Image_Download")
                                        print("4. Go Back")
                                        print("      ")

                                        Mode = input("Enter Your Mode (0/1/2/3/4): ")
                                        if Mode in ("", " "):
                                            print("NO INPUT?!")
                                            time.sleep(.5)
                                            print("Press Any Key To Continue...")
                                            input()
                                            print("")
                                            continue

                                        if Mode in "0":
                                            print("EXITING...")

                                            time.sleep(.8)
                                            print("DONE")

                                            time.sleep(1)
                                            sys.exit()
                                        if Mode in "4":
                                            break
                                        if Mode in ("1", "2", "3"):
                                            if Mode in "1":

                                                try:
                                                    Functions.download_file(input("Enter Your URL: "))
                                                    print("Downloading...")
                                                    time.sleep(.5)
                                                    print("Done")
                                                    choice = input("Do You Want To Try Again?(y/n)")
                                                    if choice in "y":
                                                        flag = True
                                                        break
                                                    else:
                                                        print("Press Any Key To Continue...")
                                                        input()
                                                        sys.exit(0)
                                                except:
                                                    print("Invalid URL")
                                                    choice = input("Do You Want To Try Again?(y/n)")
                                                    if choice in "y":
                                                        flag = True
                                                        break
                                                    else:
                                                        print("Press Any Key To Continue...")
                                                        input()
                                                        sys.exit(0)

                                            if Mode in "2":
                                                try:
                                                    Functions.DownloadPdf(input("Enter Your URL: "))
                                                    print("Downloading...")
                                                    print("Done")
                                                    choice = input("Do You Want To Try Again?(y/n)")
                                                    if choice in "y":
                                                        flag = True
                                                        break
                                                    else:
                                                        print("Press Any Key To Continue...")
                                                        input()
                                                        sys.exit(0)

                                                except:
                                                    print("Invalid input")
                                                    choice = input("Do You Want To Try Again?(y/n)")
                                                    if choice in "y":
                                                        flag = True
                                                        break
                                                    else:
                                                        print("Press Any Key To Continue...")
                                                        input()
                                                        sys.exit(0)

                                            if Mode in "3":
                                                url = input("Please Enter The URL: ")
                                                name = input("Please Enter The Name (Also Add The File Extension): ")

                                                print("Downloading...")
                                                try:
                                                    req = urllib.request.Request(url,
                                                                                 headers={'User-Agent': 'Mozilla/5.0'})
                                                    with open(name, "wb") as f:
                                                        with urllib.request.urlopen(req) as r:
                                                            f.write(r.read())
                                                    print("Done!")
                                                    choice = input("Do You Want To Try Again?(y/n)")
                                                    if choice in "y":
                                                        flag = True
                                                        break
                                                    else:
                                                        print("Press Any Key To Continue...")
                                                        input()
                                                        sys.exit(0)

                                                except:
                                                    print("Invalid URL")
                                                    choice = input("Do You Want To Try Again?(y/n)")
                                                    if choice in "y":
                                                        flag = True
                                                        break
                                                    else:
                                                        print("Press Any Key To Continue...")
                                                        input()
                                                        sys.exit(0)
                                        else:
                                            print("        ")
                                            print("Invalid Input")
                                            print("Please Try Again")
                                            print("        ")

                                            time.sleep(2)
                                else:
                                    print("")
                                    pass
                            else:
                                pass
                        if wcache == sum:
                            if wcache > 8:
                                ans = input("Do you want to count words? (y/n) ")
                                if ans in "y":
                                    cache = 0
                                    try:
                                        with open(wname) as f:
                                            cache = json.load(f)
                                    except:
                                        alname = 0
                                        with open(wname, 'w') as f:
                                            json.dump(alname, f)
                                    cache = cache + 1
                                    with open(wname, "w") as f:
                                        json.dump(cache, f)

                                    filename = input("Enter The File Name: ")
                                    Functions.count_words(filename)
                                    choice = input("Do You Want To Try Again?(y/n)")
                                    if choice in "y":
                                        flag = True
                                        break
                                    else:
                                        print("Press Any Key To Continue...")
                                        input()
                                        sys.exit(0)

                                else:
                                    print("")
                                    pass
                            else:
                                pass
                        if icache == sum:
                            if icache > 8:
                                ans = input("Do you want to check your IP address? (y/n) ")
                                if ans in "y":
                                    cache = 0
                                    try:
                                        with open(iname) as f:
                                            cache = json.load(f)
                                    except:
                                        alname = 0
                                        with open(iname, 'w') as f:
                                            json.dump(alname, f)
                                    cache = cache + 1
                                    with open(iname, "w") as f:
                                        json.dump(cache, f)

                                    Functions.get_IP()
                                    choice = input("Do You Want To Try Again?(y/n)")
                                    if choice in "y":
                                        flag = True
                                        break
                                    else:
                                        print("Press Any Key To Continue...")
                                        input()
                                        sys.exit(0)

                                else:
                                    print("")
                                    pass
                            else:
                                pass
                        if rcache == sum:
                            if rcache > 8:
                                ans = input("Do you want to use 'remember me'? (y/n) ")
                                if ans in "y":
                                    cache = 0
                                    try:
                                        with open(rname) as f:
                                            cache = json.load(f)
                                    except:
                                        alname = 0
                                        with open(rname, 'w') as f:
                                            json.dump(alname, f)
                                    cache = cache + 1
                                    with open(rname, "w") as f:
                                        json.dump(cache, f)

                                    try:
                                        path = "Cache/Username_Cache"
                                        os.mkdir(path)
                                    except Exception as e:
                                        print(e)
                                        pass

                                    Functions.greet_user()

                                    choice = input("Do You Want To Try Again?(y/n)")
                                    if choice in "y":
                                        flag = True
                                        break
                                    else:
                                        print("Press Any Key To Continue...")
                                        input()
                                        sys.exit(0)

                                else:
                                    print("")
                                    pass
                            else:
                                pass
                        if scache == sum:
                            if scache > 8:
                                ans = input("Do you want to use the text editor? (y/n) ")
                                if ans in "y":
                                    import tkinter as tk

                                    cache = 0
                                    try:
                                        with open(siname) as f:
                                            cache = json.load(f)
                                    except:
                                        alname = 0
                                        with open(siname, 'w') as f:
                                            json.dump(alname, f)
                                    cache = cache + 1
                                    with open(siname, "w") as f:
                                        json.dump(cache, f)

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
                                    choice = input("Do You Want To Try Again?(y/n)")
                                    if choice in "y":
                                        flag = True
                                        break
                                    else:
                                        print("Press Any Key To Continue...")
                                        input()
                                        sys.exit(0)

                                else:
                                    print("")
                                    pass
                            else:
                                pass
                        while True:
                            print("SELECT YOUR MODE")
                            print("0. Exit")
                            print("1. Files Download")
                            print("2. Word Count")
                            print("3. IP Checker")
                            print("4. Remember Me")
                            print("5. Simple Text Editor")
                            print("6. Clear Mode Cache")
                            print("7. Go Back")

                            choice = input("Enter Mode (0/1/2/3/4/5/6/7): ")
                            if choice in ("", " "):
                                print("NO INPUT?!")
                                time.sleep(.5)
                                print("Press Any Key To Continue...")
                                input()
                                print("")
                                continue
                            if choice in "7":
                                flag = True
                                break
                            if choice in "6":
                                try:
                                    try:
                                        a1path = "Cache\\M1-CACHE\\files.json"
                                        os.remove(a1path)
                                    except FileNotFoundError:
                                        pass
                                    try:
                                        a1path = "Cache\\M1-CACHE\\word.json"
                                        os.remove(a1path)
                                    except FileNotFoundError:
                                        pass
                                    try:
                                        a1path = "Cache\\M1-CACHE\\IP.json"
                                        os.remove(a1path)
                                    except FileNotFoundError:
                                        pass
                                    try:
                                        a1path = "Cache\\M1-CACHE\\remember.json"
                                        os.remove(a1path)
                                    except FileNotFoundError:
                                        pass
                                    try:
                                        a1path = "Cache\\M1-CACHE\\simple.json"
                                        os.remove(a1path)
                                    except FileNotFoundError:
                                        pass
                                except Exception as e:
                                    print(e)
                                    input("Press Any Key To Continue...")
                                    input()
                                    exit(0)
                                print("CACHE DELETED!")
                                print("Press Any Key To Continue...")
                                input()
                                exit(0)
                            if choice in ("0", "1", "2", "3", "4", "5"):
                                if choice in "0":
                                    print("EXITING...")

                                    time.sleep(.8)
                                    print("DONE")

                                    time.sleep(1)
                                    sys.exit()
                                if choice in "1":
                                    cache = 0
                                    try:
                                        with open(fname) as f:
                                            cache = json.load(f)
                                    except:
                                        alname = 0
                                        with open(fname, 'w') as f:
                                            json.dump(alname, f)
                                    cache = cache + 1
                                    with open(fname, "w") as f:
                                        json.dump(cache, f)
                                    while True:
                                        print("Select Your Mode")
                                        print("0.Exit")
                                        print("1.mp4_Download")
                                        print("2.PDF_Download")
                                        print("3.Image_Download")
                                        print("4.Go Back")
                                        print("      ")

                                        Mode = input("Enter Your Mode (0/1/2/3/4): ")
                                        if Mode in ("", " "):
                                            print("NO INPUT?!")
                                            time.sleep(.5)
                                            print("Press Any Key To Continue...")
                                            input()
                                            print("")
                                            continue

                                        if Mode in "0":
                                            print("EXITING...")

                                            time.sleep(.8)
                                            print("DONE")

                                            time.sleep(1)
                                            sys.exit()
                                        if Mode in "4":
                                            break
                                        if Mode in ("1", "2", "3"):
                                            if Mode in "1":

                                                try:
                                                    Functions.download_file(input("Enter Your URL: "))
                                                    print("Downloading...")
                                                    time.sleep(.5)
                                                    print("Done")
                                                    choice = input("Do You Want To Try Again?(y/n)")
                                                    if choice in "y":
                                                        break
                                                    else:
                                                        print("Press Any Key To Continue...")
                                                        input()
                                                        sys.exit(0)
                                                except:
                                                    print("Invalid URL")
                                                    choice = input("Do You Want To Try Again?(y/n)")
                                                    if choice in "y":
                                                        flag = True
                                                        break
                                                    else:
                                                        print("Press Any Key To Continue...")
                                                        input()
                                                        sys.exit(0)

                                            if Mode in "2":
                                                try:
                                                    Functions.DownloadPdf(input("Enter Your URL: "))
                                                    print("Downloading...")
                                                    print("Done")
                                                    choice = input("Do You Want To Try Again?(y/n)")
                                                    if choice in "y":
                                                        flag = True
                                                        break
                                                    else:
                                                        print("Press Any Key To Continue...")
                                                        input()
                                                        sys.exit(0)
                                                except:
                                                    print("Invalid input")
                                                    choice = input("Do You Want To Try Again?(y/n)")
                                                    if choice in "y":
                                                        flag = True
                                                        break
                                                    else:
                                                        print("Press Any Key To Continue...")
                                                        input()
                                                        sys.exit(0)
                                            if Mode in "3":

                                                url = input("Please Enter The URL: ")
                                                name = input("Please Enter The Name (Also Add The File Extension): ")

                                                print("Downloading...")
                                                try:
                                                    req = urllib.request.Request(url,
                                                                                 headers={'User-Agent': 'Mozilla/5.0'})
                                                    with open(name, "wb") as f:
                                                        with urllib.request.urlopen(req) as r:
                                                            f.write(r.read())
                                                    print("Done!")
                                                    choice = input("Do You Want To Try Again?(y/n)")
                                                    if choice in "y":
                                                        break
                                                    else:
                                                        print("Press Any Key To Continue...")
                                                        input()
                                                        sys.exit(0)
                                                except:
                                                    print("Something Went Wrong...")
                                                    choice = input("Do You Want To Try Again?(y/n)")
                                                    if choice in "y":
                                                        flag = True
                                                        break
                                                    else:
                                                        print("Press Any Key To Continue...")
                                                        input()
                                                        sys.exit(0)
                                        else:
                                            print("        ")
                                            print("Invalid Input")
                                            print("Please Try Again")
                                            print("        ")

                                            time.sleep(2)

                                if choice in "2":
                                    cache = 0
                                    try:
                                        with open(wname) as f:
                                            cache = json.load(f)
                                    except:
                                        alname = 0
                                        with open(wname, 'w') as f:
                                            json.dump(alname, f)
                                    cache = cache + 1
                                    with open(wname, "w") as f:
                                        json.dump(cache, f)

                                    filename = input("Enter The File Name: ")
                                    Functions.count_words(filename)
                                    choice = input("Do You Want To Try Again?(y/n)")
                                    if choice in "y":
                                        flag = True
                                        break
                                    else:
                                        print("Press Any Key To Continue...")
                                        input()
                                        sys.exit(0)

                                if choice in "3":
                                    cache = 0
                                    try:
                                        with open(iname) as f:
                                            cache = json.load(f)
                                    except:
                                        alname = 0
                                        with open(iname, 'w') as f:
                                            json.dump(alname, f)
                                    cache = cache + 1
                                    with open(iname, "w") as f:
                                        json.dump(cache, f)

                                    Functions.get_IP()
                                    choice = input("Do You Want To Try Again?(y/n)")
                                    if choice in "y":
                                        flag = True
                                        break
                                    else:
                                        print("Press Any Key To Continue...")
                                        input()
                                        sys.exit(0)

                                if choice in "4":
                                    cache = 0
                                    try:
                                        with open(rname) as f:
                                            cache = json.load(f)
                                    except:
                                        alname = 0

                                    cache = cache + 1
                                    with open(rname, "w") as f:
                                        json.dump(cache, f)

                                    try:
                                        path = "Cache/Username_Cache"
                                        os.mkdir(path)
                                    except FileExistsError:
                                        pass
                                    Functions.greet_user()

                                    choice = input("Do You Want To Try Again?(y/n)")
                                    if choice in "y":
                                        flag = True
                                        break
                                    else:
                                        print("Press Any Key To Continue...")
                                        input()
                                        sys.exit(0)
                                if choice in "5":
                                    import tkinter as tk

                                    cache = 0
                                    try:
                                        with open(siname) as f:
                                            cache = json.load(f)
                                    except:
                                        alname = 0
                                        with open(siname, 'w') as f:
                                            json.dump(alname, f)
                                    cache = cache + 1
                                    with open(siname, "w") as f:
                                        json.dump(cache, f)

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
                                    choice = input("Do You Want To Try Again?(y/n)")
                                    if choice in "y":
                                        flag = True
                                        break
                                    else:
                                        print("Press Any Key To Continue...")
                                        input()
                                        sys.exit(0)
                            else:
                                print("        ")
                                print("Invalid Input")
                                print("Please Try Again")
                                print("        ")
                                time.sleep(2)
                                continue
            else:
                print("        ")
                print("Invalid Input")
                print("Please Try Again")
                print("        ")
                time.sleep(2)
                continue


if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:
        new_user_create()
        main()  # Already an admin here.
