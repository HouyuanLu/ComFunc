print ("WELCOME TO THE CALCULATOR")

def add (x,y):
    return x + y
def subtract (x,y):
    return x - y
def multiply (x,y):
    return x * y
def divide (x, y):
    return x / y

print ("SELECT YOUR MODE")
print ("0. Exit")
print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Divide")

Select = input ("Enter Mode (0/1/2/3/4): ")

if Select in ("0"):
    print ("EXITING...")
    exit
    print ("DONE")
else: 
    if Select in ("1, 2, 3, 4"):
        num_1 = float (input ("Enter The First Number: "))
        num_2 = float (input ("Ender The Second Number: "))

        if Select == "1":
            answer = (add (num_1, num_2))
            print ("The Answer is %s" % (answer))
        if Select == "2":
            answer = (subtract (num_1, num_2))
            print ("The Answer is %s" % (answer))
        if Select == "3":
            answer = (multiply (num_1, num_2))
            print ("The Answer is %s" % (answer))
        if Select == "4":
            answer = (divide (num_1, num_2))
            print ("The Answer is %s" % (answer))
    else:
        print ("        ")
        print ("Invaild Input")
        print ("Please Try Again")
        print ("        ")
        import time
        time.sleep (2)
        while True:
            print ("SELECT YOUR MODE")
            print ("0. Exit")
            print ("1. Add")
            print ("2. Subtract")
            print ("3. Multiply")
            print ("4. Divide")

            Select = input ("Enter Mode (0/1/2/3/4): ")

            if Select in ("0"):
                print ("EXITING...")
                GeneratorExit
                SystemExit
                exit
                print ("DONE")
            else: 
                if Select in ("1, 2, 3, 4"):
                    num_1 = float (input ("Enter The First Number: "))
                    num_2 = float (input ("Ender The Second Number: "))

                    if Select == "1":
                        answer = (add (num_1, num_2))
                        print ("The Answer is %s" % (answer))
                    if Select == "2":
                        answer = (subtract (num_1, num_2))
                        print ("The Answer is %s" % (answer))
                    if Select == "3":
                        answer = (multiply (num_1, num_2))
                        print ("The Answer is %s" % (answer))
                    if Select == "4":
                        answer = (divide (num_1, num_2))
                        print ("The Answer is %s" % (answer))
                        break
                    break
                else:
                    print ("        ")
                    print ("Invaild Input")
                    print ("Please Try Again")
                    print ("        ")
                    import time
                    time.sleep (2)