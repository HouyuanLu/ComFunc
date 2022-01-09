while True:
    import time
    time.sleep(.3)
    print ("WELCOME TO THE COMBINED VERSION OF CALCULATOR")
    print ("    ")
    import time
    time.sleep (1) 
    print ("Select Your Mode")
    print ("0. Exit")
    print ("1. CALCULATOR")
    print ("2. Triangle-Area")
    print ("3. Rectangle-Area")

    choice = input ("Enter Mode (0/1/2/3)")

    if choice in ("0"):
        print ("EXITING...")
        import time
        time.sleep(.8)
        print ("DONE")
        import time
        time.sleep(1)
        exit()
    else:
        if choice in ("1, 2, 3"):
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
                def wait():
                    while True:
                        import time
                        time.sleep(100000)
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
                        import time
                        time.sleep (.7)
                        print ("DONE")
                        import time
                        time.sleep(1)
                        exit()
                    else: 
                        if Select in ("1, 2, 3, 4"):
                            if Select == "1":
                                num_1 = float (input ("Enter The First Number: "))
                                num_2 = float (input ("Enter The Second Number: "))
                                answer = (add (num_1, num_2))
                                print ("The Answer is %s" % (answer))
                                from msvcrt import getch 
                                print ("Press Any Key To Continue...")
                                getch ()
                            if Select == "2":
                                num_1 = float (input ("Enter The First Number: "))
                                num_2 = float (input ("Enter The Second Number: "))
                                answer = (subtract (num_1, num_2))
                                print ("The Answer is %s" % (answer))
                                from msvcrt import getch 
                                print ("Press Any Key To Continue...")
                                getch ()
                            if Select == "3":
                                num_1 = float (input ("Enter The First Number: "))
                                num_2 = float (input ("Enter The Second Number: "))
                                answer = (multiply (num_1, num_2))
                                print ("The Answer is %s" % (answer))
                                from msvcrt import getch 
                                print ("Press Any Key To Continue...")
                                getch ()
                            if Select == "4":
                                num_1 = float (input ("Enter The Dividend: "))
                                num_2 = float (input ("Enter The Divisor: "))
                                answer = (divide (num_1, num_2))
                                print ("The Answer is %s" % (answer))
                                from msvcrt import getch 
                                print ("Press Any Key To Continue...")
                                getch ()
                                break
                            break
                        else:
                            print ("        ")
                            print ("Invalid Input")
                            print ("Please Try Again")
                            print ("        ")
                            import time
                            time.sleep (2)
            if choice in ("2"):
                print ("WELCOME TO THE TRIANGLE-AREA CALCULATOR")
                import time
                time.sleep (2)
                print ("PLEASE ENTER THE BOTTOM-LENGTH")
                def multiply_and_divide (x, y):
                    return x * y / 2
                num_1 = float (input ())
                print ("NOW PLEASE ENTER THE HEIGHT")
                num_2 = float (input ())
                answer = (multiply_and_divide(num_1, num_2))
                print ("THE AREA IS %s" % (answer))
                from msvcrt import getch 
                print ("Press Any Key To Continue...")
                getch ()
            if choice in ("3"):
                print ("WELCOME TO THE RECTANGLE-AREA CALCULATOR")
                import time
                time.sleep (2)
                print ("PLEASE ENTER THE LENGTH")
                def multiply (x, y):
                    return x * y
                num_1 = float (input ())
                print ("NOW PLEASE ENTER THE WIDTH")
                num_2 = float (input ())
                answer = (multiply (num_1, num_2))
                print ("THE AREA IS %s" % (answer))
                from msvcrt import getch 
                print ("Press Any Key To Continue...")
                getch ()
                break
            break
        else:
            print ("        ")
            print ("Invalid Input")
            print ("Please Try Again")
            print ("        ")
            import time
            time.sleep (2)

