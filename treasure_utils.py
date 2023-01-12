#Comp 202 assignment 2 part 2
#Rui-Jia Meng
#ID 26116408


MOVEMENT_SYMBOLS = '><v^'
EMPTY_SYMBOL = '.'
TREASURE_SYMBOL = '+'
BREADCRUMB_SYMBOL = 'X'
MOVEMENT_SYMBOLS_3D = '*|'



def get_nth_row_from_map(map_string,n,width,height):
    """(str,int,int,int)->str
    returns the nth row of the map as a string according to the whole map string,
    its width, height and the row wanted(n) .
    >>> get_nth_row_from_map('^>>>>>..v', 2, 3, 3)
    '..v'
    >>> get_nth_row_from_map('^>>.....v', 1, 3, 3)
    '...'
    >>> get_nth_row_from_map('^>>.....v', 0, 3, 3)
    """
    if n>=height:
        nth=""
    elif n==0:
        nth=map_string[0:width]
    elif n!=0:
        nth=map_string[n*width:(n*width)+width]
    
    return(nth)
    
    
def print_treasure_map(map_string,width,height):
    """(str,int,int)->NoneType
    prints a tresure map in different row accoring to its width and height.
    >>> print_treasure_map('<...vv..', 4, 2)
    <...
    vv..
    >>> print_treasure_map('<>.<vv..', 2, 4)
    <>
    .<
    vv
    ..
    >>> print_treasure_map('<>.<vv..>', 3, 3)
    <>.
    <vv
    ..>
    """
    i=0
    for j in range(height):
        treasure_map=map_string[i:i+width]
        j+=1
        i+=width
        print(treasure_map)
        
def change_char_in_map(map_string,row,column,c,width,height):
    """(str,int,int,str,int,int)->str
    returns a new string by changing a string in the old map string,
    in addition the position of the string changed is define by the row, column, width and the height.
    >>> change_char_in_map('.........<><', 2, 2, 'X', 4, 3)
    '.........<X<'
    >>> change_char_in_map('.........', 1, 2, 'X', 3, 3)
    '.....X...'
    >>> change_char_in_map('.........<><', 1, 1, 'X', 4, 3)
    '.....X...<><'
    """ 
    if row>=height or column>=width:
        return("")
    new_map_string= map_string[:(row*width)+column]+c+map_string[(row*width)+column+1:]    
    return(new_map_string)

    
def get_proportion_travelled(map_string):
    """(str)->float
    returns the proporton of "X" in the string
    >>> get_proportion_travelled('.XXXX.XX.')
    0.67
    >>> get_proportion_travelled('...XXX')
    0.5
    >>> get_proportion_travelled('...XXX.')
    0.43  
    """ 
    s=map_string.count(BREADCRUMB_SYMBOL[0]) 
    proportion=s/len(map_string)    
    return(round(proportion,2))
    

def get_nth_map_from_3D_map(map_string,n,width,height,depth):
    """(str,int,int,int,int)->str
    >>> get_nth_map_from_3D_map('.X.XXX.X..v.vXv.v.23', 4, 2, 2, 5)
    'v.23'
    >>> get_nth_map_from_3D_map('.X.XXX.X..v.vXv.v.', 0, 3, 3, 2)
    '.X.XXX.X.'
    >>> get_nth_map_from_3D_map('.X.XXX.X..v.vXv.v.', 1, 2, 3, 2)
    '.v.vXv.v.'
    """ 
    space=width*height
    if n>=depth:
        nth3d=""
    if n==0:
        nth3d=map_string[0:space]
    if n!=0:
        nth3d=map_string[n*space:(n*space)+space]
    return(nth3d)
    
    
    
def print_3D_treasure_map(map_string, width, height,depth):
    """(str,int,int,int)->str
    print the 3D treasure map as a string according to the
    print_3D_treasure_map('.X.XXX.X..v.vXv.v.', 3, 3, 2)wight height and depth
    >>> print_3D_treasure_map('.X.XXX.X..v.vXv.v...', 2, 5, 2)
    .X
    .X
    XX
    .X
    ..

    v.
    vX
    v.
    v.
    ..
    >>> print_3D_treasure_map('.X.XXX.X..v.vXv.v.>>', 5, 2, 2)
    .X.XX
    X.X..

    v.vXv
    .v.>>
    >>> print_3D_treasure_map('.X.XXX.X..v.vXv.v.>><><..<.', 3, 3, 3)
    .X.
    XXX
    .X.

    .v.
    vXv
    .v.

    >><
    ><.
    .<.
    """

    for i in range(depth):
        print_treasure_map(map_string, width, height)
        map_string = map_string[width*height:]
        
        if i != depth-1:
            print("")


def change_char_in_3D_map(map_string,row,column,index_depth,c,width,height,depth):
    """(str,int,int,int,str,int,int,int)->str
    >>> change_char_in_3D_map('.XxXXX.X.vvvvXv.v.', 1, 1, 0, 'O', 3, 3, 2)
    '.XxXOX.X.vvvvXv.v.'
    >>> change_char_in_3D_map('.XxXXX.X.vvvvXv.v.', 2, 1, 0, 'C', 3, 3, 2)
    '.XxXXX.C.vvvvXv.v.'
    >>> change_char_in_3D_map('.XxXXX.X.vvvvXv.v.', 2, 1, 1, 'C', 3, 3, 2)
    '.XxXXX.X.vvvvXv.C.'
    """
    if row>=height or column>=width or index_depth>=depth:
        return("")
    new_string= map_string[:(row*width+column)+(index_depth*width*height)]+c+map_string[(row*width+column)+(index_depth*width*height)+1:] 
    return(new_string)
        
        