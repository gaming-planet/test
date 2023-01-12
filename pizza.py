#Rui-Jia Meng
#ID: 261116408

PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED = 4.0
PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED = 3.0
SPECIAL_INGREDIENT = "guacamole"
SPECIAL_INGREDIENT_COST = 19.99
FAIR = True

import math

def get_pizza_area(diameter):
    """(float)->float
    Returns the area of the pizza by using it's diameter.
    >>>get_pizza_area(4.5)
    15.904312808798327
    >>>get_pizza_area(7.7)
    46.566257107834716
    >>>get_pizza_area(9.2)
    66.47610054996001
    """
    pizza_area=math.pi*(diameter/2)**2
    return pizza_area

def get_fair_quantity(diameter1, diameter2):
    """(float,float)->(int)
  
    returns the fair quantity by using the diameter 1 and diameter 2 to get the area of the bigger and smaller
    pizza, and dividing the bigger area by the smaller area to get the number of times the smaller pizza
    area can be fair with the bigger pizza area. In addition, the return value is rounded up.
  
    >>> get_fair_quantity(3.2,3.4)
    2
    >>> get_fair_quantity(4.5,7.8)
    4
    >>> get_fair_quantity(1.3,17.8)
    188
    """ 
    pizza_area_1=get_pizza_area(diameter1)
    
    pizza_area_2=get_pizza_area(diameter2)
    
    if pizza_area_1 >= pizza_area_2:
        fair_quantity=pizza_area_1//pizza_area_2
        if pizza_area_1%pizza_area_2!=0:
            fair_quantity=fair_quantity+1
    else:
        fair_quantity=pizza_area_2//pizza_area_1
        if pizza_area_1%pizza_area_2!=0:
            fair_quantity=fair_quantity+1        
    
    if not FAIR:
        fair_quantity=int(fair_quantity*1.5)
            
    return round(fair_quantity)

def pizza_formula(d_large, d_small, c_large, c_small, n_small):
    """(float,float,float,float,integer)->float
    returns the missing value replaced by -1 by using the proportion relation of big area pizza cost and small area pizza cost.
    the d_large divided by c_large is equal to n_small multiplied by d_small divided by c_small.    
    >>> pizza_formula(2,5,-1,5,6)
    0.13
    >>> pizza_formula(3,6,2,-1,9)
    72.0
    >>> pizza_formula(2,-1,3.5,3,2)
    0.44

    """  
    if d_large == -1:
        area_large= ((c_large)*(n_small*get_pizza_area(d_small))/c_small)
        d_large=math.sqrt(area_large/math.pi)*2       
        return round(d_large,2)
    elif d_small==-1:
        area_small=c_small*(get_pizza_area(d_large)/c_large)/n_small
        d_small=math.sqrt(area_small/math.pi)*2
        return round(d_small,2)
    elif c_large==-1:
        c_large=c_small*get_pizza_area(d_large)/(n_small*get_pizza_area(d_small))
        return round(c_large,2)
    elif c_small==-1:
        c_small=c_large*(n_small*get_pizza_area(d_small))/get_pizza_area(d_large)
        return round(c_small,2)
    elif n_small==-1:
        n_small=c_small*get_pizza_area(d_large)/c_large/get_pizza_area(d_small)
        return round(n_small,2)
    
def get_pizza_cake_cost(base_diameter, height_per_level):
    """(int,float)->(float)
    Return the cost of the pizza cake by using the base_diameter and height_per level to get the total area
    of the pizza cake and the cost of pizza, cake is defined by multiplying the cost per centimetre cubed  and its total area
    >>>> get_pizza_cake_cost(3,3.5)
    153.94
    >>> get_pizza_cake_cost(2,4)
    62.83
    >>> get_pizza_cake_cost(7,6.4)
    2814.87
    """
    
    pizza_cake_volume=0
    while base_diameter>=1:   
        
        pizza_volume = get_pizza_area(base_diameter)*height_per_level
        pizza_cake_volume += pizza_volume
    
        base_diameter-=1
    pizza_cost=pizza_cake_volume*PIZZA_CAKE_COST_PER_CENTIMETRE_CUBED
    
    if not FAIR:
        return round(pizza_cost*1.5, 2)
    
    return round(pizza_cost,2)
         
def get_pizza_poutine_cost(diameter, height):
    """(int,float)->(float)
    returns the cost of the pizza poutine by using the diameter and height to get the poutine's
    volume according to its volume equation. The cost of the pizza poutine is calculated by multiplying
    the volume of the pizza poutine and the cost per centimetre cubed.  
    >>>get_pizza_poutine_cost(3,3.6)
    76.34
    >>>get_pizza_poutine_cost(2,6.7)
    63,15
    >>>get_pizza_poutine_cost(7,4.3)
    496.45
    """
    poutine_volume=get_pizza_area(diameter)*height
    poutine_cost=poutine_volume*PIZZA_POUTINE_COST_PER_CENTIMETRE_CUBED
    
    if not FAIR:
        return round(poutine_cost*1.5, 2)
    
    return round(poutine_cost,2)   

def display_welcome_menu():
    """()->NoneType
    display the print statement
    >>> display_welcome_menu()
    Welcome To The Best Pizza Place. Our Pizzas Made With 100% Real Pizza.
    Please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    """
    print("Welcome To The Best Pizza Place. Our Pizzas Made With 100% Real Pizza.")
    print("Please choose an option:")
    print("A. Special Orders\nB. Formula Mode\nC. Quantity Mode")




def special_orders():
    """()->NoneType
    display the total cost of the order according to the different choices chosen by the users.
    In addition, the funtion get_pizza_poutine_cost() and get_pizza_cake_cost are use to calculate the value.
    >>> special_orders()
    Would you like the cake or poutine?poutine
    Enter diameter:3
    Enter height:3.6
    Do you want the guacamole?yes
    The cost is $ 96.33
    >>> special_orders()
    Would you like the cake or poutine?cake
    Enter diameter:4
    Enter height:5.6
    Do you want the guacamole?no
    The cost is $ 527.79
    """
    cake_or_poutine=str(input("Would you like the cake or poutine?"))
    
    if cake_or_poutine == "poutine":
        pizza_cost=get_pizza_poutine_cost(int(input("Enter diameter:")),float(input("Enter height:")))
    elif cake_or_poutine == "cake":
        pizza_cost=get_pizza_cake_cost(int(input("Enter diameter:")), float(input("Enter height:")))
           
    total = pizza_cost
    
    SPECIAL_INGREDIENT=input("Do you want the guacamole?")
    
    if SPECIAL_INGREDIENT == "y" or SPECIAL_INGREDIENT=="yes":
        total += SPECIAL_INGREDIENT_COST
    print("The cost is $",total)      
           
def quantity_mode():
    """()->NoneType
    display the number of pizzas to get a fair quantity,
    in which the value is calculated by the function get_fair_quantity()
    >>> quantity_mode()
    Enter diameter 1:5
    Enter diameter 2:9
    you should buy 4 pizza
    >>> quantity_mode()
    Enter diameter 1:9
    Enter diameter 2:20
    you should buy 5 pizza

    """
    number=get_fair_quantity(float(input("Enter diameter 1:")), float(input("Enter diameter 2:")))
    
    print("You should buy",number, "pizzas")

def formula_mode():
    """()->NoneType
    display the missing value replaced by -1 according to the other input values the users provide,
    and the missing value is calculated through the function pizza_formula()
    >>> formula_mode()
    Enter large diameter:5
    Enter small diameter:7
    Enter large price:8
    Enter small price:-1
    Enter small number:3
    the missing value is 47.04
    >>> formula_mode()
    Enter large diameter:4.5
    Enter small diameter:6.3
    Enter large price:-1
    Enter small price:3.4
    Enter small number:5
    The missing value is 0.35
    """
    value=pizza_formula(float(input("Enter large diameter:")), float(input("Enter small diameter:")), float(input("Enter large price:")), \
                        float(input("Enter small price:")), int(input("Enter small number:")) )
    print("The missing value is",value) 

def run_pizza_calculator():
    """()->NoneType
    display the different answer of function special_orders(), formula_mode()
    and quantity_mode() according to the different choices provided that the user choose
    >>> run_pizza_calculator()
    Welcome To The Best Pizza Place. Our Pizzas Made With 100% Real Pizza.
    Please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice:A
    Would you like the cake or poutine?poutine
    Enter diameter:4
    Enter height:4.5
    Do you want the guacamole?no
    The cost is $ 169.65
    >>> run_pizza_calculator()
    Welcome To The Best Pizza Place. Our Pizzas Made With 100% Real Pizza.
    Please choose an option:
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice:B
    Enter large diameter:7
    Enter small diameter:2.3
    Enter large price:8
    Enter small price:-1
    Enter small number:90
    The missing value is 77.73
    """
    display_welcome_menu()
    choice=(input("Your choice:"))
    if choice=="A":
        special_orders()
    elif choice=="B":
        formula_mode()
    elif choice=="C":
        quantity_mode()
    else:
        print("Invalid Mode.")
    

