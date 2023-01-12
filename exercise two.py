x=int(input("choose a number for x shabi:"))
y=int(input("choose a number for y retard:"))

x_difference = (10 - x)
y_difference = (10 - y) 


if x_difference < 0:
    x_difference = abs(x_difference) + x 

if y_difference < 0:
    y_difference = abs(y_difference) + y 

    
if x==y:
    print("0")
elif x_difference < y_difference:
    print(x)
elif y_difference < x_difference:
    print(y)
else:
    print("codedoesnt work")