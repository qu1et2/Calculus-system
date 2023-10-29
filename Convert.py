print("Conversion from the 10th number system to any")
while True:
    calc = int(input("Which calculus system?: ")) #calculus system
    sy = [] #system, list
    n = int(input("Number: "))

    while n > 0:
        b = n%calc  #Remainder
        n = n//calc #Whole
        sy.append(b)
        if n < calc:
            if n == 0:
                break;
            else:
                sy.append(n)
                break;
            
    sy = sy[::-1]
    stringg = ""
    for x in sy:
        stringg += str(x)
    stringg = int(stringg)
    print(stringg)

