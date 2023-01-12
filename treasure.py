#Rui-jia Meng
#261116408

import random
import treasure_utils


def generate_treasure_map_row(width, boolean):
     """(int, boolean)->str
     Returns a random row of the treasure map as a string according to the width and the boolean
     >>> random.seed(9001)
     >>> generate_treasure_map_row(10, False)
     'vv>vv><^.^'
     >>> random.seed(9001)
     >>> generate_treasure_map_row(10, True)
     'vv>v*><^.^'
     >>> random.seed(9001)
     >>> generate_treasure_map_row(18, True)
     '|v>vv><^.^.<^v^.><'
     """ 
     treasure_map=""
     
     for i in range (width):
         if random.random()<=5/6:
             treasure_map+=treasure_utils.MOVEMENT_SYMBOLS[random.randint(0,3)]
         else:
             treasure_map+=treasure_utils.EMPTY_SYMBOL
    
     if boolean==True and random.random()>0.5:
         treasure_map= treasure_utils.change_char_in_map(treasure_map,0,\
         random.randint(0,(width-1)),treasure_utils.MOVEMENT_SYMBOLS_3D[random.randint(0,1)],width,1)

     return(treasure_map)   


    
def generate_treasure_map(width,height,boolean):
    """(int,int,boolean)->str
    Returns a random tresaure map as a string according to the width, height and boolean. 
    >>> generate_treasure_map(4, 3, False)
    '>v>vv><^.^.<'
    >>> generate_treasure_map(4, 3, True)
    '>v^.>.vv<v>*'
    >>> generate_treasure_map(5, 7, True)
    '>.<^>v<.<^<.<<<^<>>|.^^.**^..<<>^^|'
    """ 
    t_map=""
    for i in range(height):
        t_map+=generate_treasure_map_row(width,boolean)
        
        if i==0:
            t_map=">"+t_map[1:]

    return(t_map)



def generate_3D_treasure_map(width,height,depth):
    """(int,int,int)->str
    Returns a ramdom 3d treasure map as a str according to the width, height and the depth.
    >>> random.seed(9001)
    >>> generate_3D_treasure_map(4, 3, 3)
    '>v|v><^.<<^v>>*>v<|>*.<^><.<^<<<^|>>'
    >>> random.seed(9001)
    >>> generate_3D_treasure_map(4, 4, 4)
    '>v|v><^.<<^v>>*>><|>*.<^v<.<^<<<>|>>v*^^.^..<<<>>>*.<<<v|^v^..<v'
    >>> random.seed(9001)
    >>> generate_3D_treasure_map(2, 2, 4)
    '>v|>>.<<>*<*><v|'
    """ 
    
    treasure_string=""
    for i in range (depth):
        treasure_string+=generate_treasure_map(width,height,True)
    
    return(treasure_string)

def follow_trail(map_string,row,column,index_depth,width,height,depth,n):
    """(str,int,int,int,int,int,int,int,int)->str
    print the number of traveled tiles accoring to the time traveled(n)
    and number tresaure found accoring number of "+" in the string.
    In addition returns a  part of treasure map string modified accoring
    to the map string,row,column,index_depth,width,height,depth and number of times traveled.
    >>> follow_trail('>>v..v..><v', 0, 0, 0, 4, 2, 1, 2)
    Treasures collected: 0
    Symbols visited: 2
    'XXv..v..><v'
    >>> follow_trail('>......v.', 0, 0, 0, 4, 2, 1, 5)
    Treasures collected: 0
    Symbols visited: 5
    'X......v.'
    >>> follow_trail('>+++++v.', 0, 0, 0, 4, 2, 1, 5)
    Treasures collected: 4
    Symbols visited: 5
    'X+++++v.'
    """ 
    treasures_collected=0
    index=(row*width+column)+(width*height*index_depth)
    tiles_traveled=0
    last_position=""
    position="" 
    
    if index_depth>=depth or column>=width or row>=height:
        return(map_string)
    
    while tiles_traveled!=n:
        
        last_position=position
        position=map_string[index]
                 
        if position!=treasure_utils.EMPTY_SYMBOL[0] and position!=treasure_utils.TREASURE_SYMBOL[0]:
            map_string=treasure_utils.change_char_in_3D_map\
            (map_string,row,column,index_depth,treasure_utils.BREADCRUMB_SYMBOL[0],width,height,depth)
        if position==treasure_utils.TREASURE_SYMBOL[0]:
            position=last_position
            treasures_collected+=1
            
        if position==".":
            position=last_position 
        
        if position==treasure_utils.MOVEMENT_SYMBOLS[0]:
            if column+1>width:
                index-=(width-1)
                column-=(width-1)
            else:
                index+=1
                column += 1
        elif position==treasure_utils.MOVEMENT_SYMBOLS[1]:
            if column-1<0:
                index+=(width-1)
                column+=(width-1)
            else:
                index-=1
                column-1
        elif position==treasure_utils.MOVEMENT_SYMBOLS[3]:
            if row-1<0:
                row+=(height-1)
            else:
                row-=1
        elif position==treasure_utils.MOVEMENT_SYMBOLS[2]:
            if row+1>height:
                row-=(height-1)
            else:    
                row+=1
        
        elif position==treasure_utils.MOVEMENT_SYMBOLS_3D[1]:
            if index_depth-1<0:
                index+=(depth-1)*width*height
                index_depth+=depth-1
            else:
                index-=(width*height)
                index_depth-1
        elif position==treasure_utils.MOVEMENT_SYMBOLS_3D[0]:
            if index_depth+1>=depth:
                index-=(depth-1)*width*heigh
                index_depth-=(depth-1)
            else:
                index+=(width*height)
                index_depth+1
        
    
        tiles_traveled+=1
        
        if position=="X":
            break
    print("Treasures collected:",treasures_collected)
    print("Symbols visited:",tiles_traveled)
    return(map_string)

   
    
    
    