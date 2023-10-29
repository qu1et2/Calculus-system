print("Conversion from the 10th number system to any")
while True:
    calc = int(input("Which calculus system?: ")) #Calculus system created by qu1et2
    sy = [] 
    n = int(input("Number: "))

    while n > 0:
        b = n%calc  #Remainder
        n = n//calc #Whole 
        sy.append(b)
        if n < calc: 
            if n == 0: #Exception
                break;
            else:
                sy.append(n) #Add to list
                break;
            
    sy = sy[::-1] #Reversing the list
    stringg = ""
    for x in sy:
        stringg += str(x)
    stringg = int(stringg)
    print(stringg)

