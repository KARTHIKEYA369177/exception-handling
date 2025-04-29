try:
    print("window")
except:
    print("you have done something wrong")
finally:
    print("program over")
    
    
try:
    age=int(input("enter the child age"))
    if age<3:
        raise ValueError
    elif age>15:
        print("not allowed")
    else:
        print("you can come")
except ValueError:
    print("your child is very small")
finally:
    print("program over")