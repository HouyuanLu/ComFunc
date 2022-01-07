def add (x,y):
    return x + y
def subtract (x,y):
    return x - y
def multiply (x,y):
    return x * y
def divide (x, y):
    return x / y

print ("SELECT")
print ("0. Exit")
print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Divide")

Select = input ("Enter Select (0/1/2/3/4): ")

if Select in ("0"):
    exit
else: 
    if Select in ("1, 2, 3, 4"):
        num_1 = float (input ("Enter The First Number: "))
        num_2 = float (input ("Ender The Second Number: "))

        if Select == "1":
            answer = (add (num_1, num_2))
            print ("%s" % (answer))
        if Select == "2":
            answer = (subtract (num_1, num_2))
            print ("%s" % (answer))
        if Select == "3":
            answer = (multiply (num_1, num_2))
            print ("%s" % (answer))
        if Select == "4":
            answer = (divide (num_1, num_2))
            print ("%s" % (answer))
    else:
        print ("Invaild Input")