# Finger Exercise 
'''Write a program that examines three variables—x, y, and z—and
prints the largest odd number among them. If none of them are odd, it should
print a message to that effect.'''


x = int (input("Enter the X number: "))
y = int (input("Enter the Y number: "))
z = int (input("Enter the Z number: ")) 


if x%2 == 0 and y%2 == 0 and z%2 == 0:
    print("X =",x ,"Y = ",y, "and Z = ",z ,"all numbers are even ,none of the them are odd")

else:
    #  case 111
    if x%2 == 1 and y%2 == 1 and z%2 == 1:
        print(("X =",x ,"Y = ",y, "and Z = ",z ,"all numbers are odd")
        if x > y and x > z:
            print("X is the greatest odd number")
        elif y > z:
            print ("y is the greatest odd among all the numbers")
        else:
            print ("z is the greatest odd number")
      #  case 000
    elif x%2 == 0 and y%2 == 0 and z%2 == 0:
        print(("X =",x ,"Y = ",y, "and Z = ",z ,"all numbers are even")
        if x > y and x > z:
            print("X is the greatest odd number")
        elif y > z:
            print ("y is the greatest odd among all the numbers")
        else:
            print ("z is the greatest odd number")
    


          #  case 100
    elif x%2 == 1 and y%2 == 0 and z%2 == 0:
        #print(("X =",x ,"Y = ",y, "and Z = ",z ,"all numbers are even")
        if x > y and x > z:
            print("X is the greatest odd number")
        elif y > z:
            print ("y is the greatest odd among all the numbers")
        else:
            print ("z is the greatest odd number")
    #   110
    elif x%2 == 1 and y%2 == 1 and z%2 == 0:
        #print(("X =",x ,"Y = ",y, "and Z = ",z ,"all numbers are even")
        if x > y and x > z:
            print("X is the greatest odd number")
        elif y > z:
            print ("y is the greatest odd among all the numbers")
        else:
            print ("z is the greatest odd number")

    #   011
    elif x%2 == 0 and y%2 == 1 and z%2 == 1:
        #print(("X =",x ,"Y = ",y, "and Z = ",z ,"all numbers are even")
        if x > y and x > z:
            print("X is the greatest odd number")
        elif y > z:
            print ("y is the greatest odd among all the numbers")
        else:
            print ("z is the greatest odd number")    
    #   010
    elif x%2 == 0 and y%2 == 1 and z%2 == 1:
        #print(("X =",x ,"Y = ",y, "and Z = ",z ,"all numbers are even")
        if x > y and x > z:
            print("X is the greatest odd number")
        elif y > z:
            print ("y is the greatest odd among all the numbers")
        else:
            print ("z is the greatest odd number")

    #   101
    elif x%2 == 1 and y%2 == 0 and z%2 == 1:
        #print(("X =",x ,"Y = ",y, "and Z = ",z ,"all numbers are even")
        if x > y and x > z:
            print("X is the greatest odd number")
        elif y > z:
            print ("y is the greatest odd among all the numbers")
        else:
            print ("z is the greatest odd number")
    #   001
    elif x%2 == 0 and y%2 == 0 and z%2 == 1:
        #print(("X =",x ,"Y = ",y, "and Z = ",z ,"all numbers are even")
        if x > y and x > z:
            print("X is the greatest odd number")
        elif y > z:
            print ("y is the greatest odd among all the numbers")
        else:
            print ("z is the greatest odd number")