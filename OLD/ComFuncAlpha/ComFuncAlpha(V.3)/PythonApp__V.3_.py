print ("Select Your Mode")
print ("0. Exit")
print ("1. CALCULATOR")
print ("2. Triangle")
print ("3. Rectangle")

choice = input ("Enter Mode (0/1/2/3)")

if choice in ("0"):
    print ("EXITING...")
    GeneratorExit
    SystemExit
    exit
    print ("DONE")
if choice in ("1"):

    print ("WELCOME TO THE CALCULATOR")
    import time
    time.sleep (2)

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
if choice in ("2"):
    print ("WELCOME TO THE TRIANGLE-AREA CONCULATOR")
    import time
    time.sleep (2)
    print ("PLEASE ENTER THE LENGTH")
    def mutiply_and_divide (x, y):
        return x * y / 2
    num_1 = float (input ())
    print ("NOW PLEASE ENTER THE HIGHT")
    num_2 = float (input ())
    answer = (mutiply_and_divide(num_1, num_2))
    print ("THE AREA IS %s" % (answer))
if choice in ("3"):
    print ("WELCOME TO THE RECTANGLE-AREA CONCULATOR")
    import time
    time.sleep (2)
    print ("PLEASE ENTER THE LENGTH")
    def mutiply (x, y):
        return x * y
    num_1 = float (input ())
    print ("NOW PLEASE ENTER THE WIDTH")
    num_2 = float (input ())
    answer = (mutiply (num_1, num_2))
    print ("THE AREA IS %s" % (answer))