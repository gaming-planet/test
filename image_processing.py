#assignment 3 
#Rui-ia Meng
#261116408


def is_valid_image(PGM_image):
    '''(list)->Bool
    Return a boolean according if the nested list represents a valid
    non-Compressed PGM image matrix
    >>> is_valid_image([[0,0,4], [0, 0,5]])
    True
    >>> is_valid_image([["0x4", "20x2"], ["411x7"]])
    False
    >>> is_valid_image([[0,4], [0, 0,5]])
    False
    '''
    if PGM_image==[]:
        return False
    for elmt in PGM_image:
        for i in elmt:
            if type(i)!=int:
                return False
            elif i>255:
                return False
            elif i<0:
                return False
        if len(elmt)!=len(PGM_image[0]):
            return False
        else:
            continue     
    return True
    
def is_valid_compressed_image(image):
    '''(list)->Bool
    Return a boolean according if the nested list represents a valid
    Compressed PGM image matrix
    >>> is_valid_compressed_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    False
    >>> is_valid_compressed_image([["3", "3", "3"], ["3","4","5"], ["4", "6","9"]])
    False
    >>> is_valid_compressed_image([["6x5", "20x2"], ["56x7"]])
    '''
    repeat=[]
    C=0
    B=0
    
    if image==[]:
        return False
    for elmt in range(len(image)):
        C=B
        B=0
        for i in image[elmt]:
            if type(i) != str:
                return False
            elif "x" not in i:
                return False
            elif not i.split("x")[0].isdecimal():
                return False
            elif not i.split("x")[1].isdecimal(): 
                return False
            elif int(i.split("x")[0])>255 or int(i.split("x")[0])<0:
                return False
            elif int(i.split("x")[1])<0:
                return False
            elif len(i.split("x"))!=2:
                return False
            
            B+=int(i.split("x")[1])

        if C!=B and elmt!=0:
            return False
    
    return True
        
def load_regular_image(PGM_image_file):
    """(str)->list<list<int>
    Take a file name as input and load the file. Output it
    as a nested list in the non compressed PGM matrix form
    if it is the right filetype. Otherwise an assertion error will raise.
    
    >>> save_image([[2, 1], [1,1]], "test.pgm")
    >>> load_regular_image("test.pgm")
    [[2, 1], [1, 1]]
    
    >>> save_image([[2,5,5,5, 1], [14,4,4,4,1]], "test.pgm")
    >>> load_regular_image("test.pgm")
    [[2, 5, 5, 5, 1], [14, 4, 4, 4, 1]]
    
    >>> save_compressed_image([["6x5", "7x5"], ["111x10"]], "test.pgm.compressed")
    >>> load_regular_image("test.pgm.compressed")
    Traceback (most recent call last):
    AssertionError: Wrong file type
    
    """
    imagefile=[]
    int_number=[]
   
    image=open(PGM_image_file, 'r')
   
    
    for line in image:
        row=line.split()
        imagefile.append(row)
    image.close()
    
    
    for i in range (3):
        image2=imagefile.pop(0)   
    
    PGM_file=[]
        
    for i in range(len(imagefile)):
        for j in range(len(imagefile[i])):
            imagefile[i][j] = int(imagefile[i][j])
    
    if not is_valid_image(imagefile):
         raise AssertionError("Wrong file type")
    
    return(imagefile)
    
def load_compressed_image(PGM_compressed_image):
    """(str)->list<list<str>
    Take a file name as input and load the file. Output it
    as a nested list in the compressed PGM matrix form
    if it is the right filetype. Otherwise an assertion error will raise.
    
    >>> save_image([["0x5", "30x2"], ["111x7"]], "test.pgm.compressed")
    >>> load_compressed_image("test.pgm.compressed")
    [['0x5', '30x2'], ['111x7']]
    
    >>> save_image([["10x5", "200x3"], ["151x8"]], "test.pgm.compressed")
    >>> load_compressed_image("test.pgm.compressed")
    [['10x5', '200x3'], ['151x8']]
    
    >>> save_image([[2, 1], [1,1]], "test.pgm")
    >>> load_compressed_image("test.pgm")
    Traceback (most recent call last):
    AssertionError: Wrong file type    
    """
    imagefile_compressed=[]
    image=open(PGM_compressed_image, 'r')
   
    for line in image:
        row=line.split()
        imagefile_compressed.append(row)
    for i in range(3):
        remove=imagefile_compressed.pop(0)
    
    if not is_valid_compressed_image(imagefile_compressed):
        raise AssertionError("Wrong file type")
    
    image.close()
    
    return(imagefile_compressed)   
    
def load_image(PGM_image):
    """(str)->(list<list>)
    Take a filename as the input and according to if the file is a compressed or
    non-compressed PGM_image. It will output the nested list according to the tyoe of
    file. In addition, a assertion error will raise, if the file is not the right type.
    
    >>> save_regular_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    >>> load_image("test.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    >>> save_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> load_image("test.pgm.compressed")
    [['0x5', '200x2'], ['111x7']]
    
    >>> save_image([["0x5", "30x2"], ["111x7"]], "test.pgm.compressed")
    >>> load_image("test.pgm.compressed")
    [['0x5', '30x2'], ['111x7']]
    
    """
    image_PGM=[]
    image=open(PGM_image, 'r')
    for line in image:
        row=line.split()
        image_PGM.append(row)
   
    if image_PGM[0][0]=='P2C':
        return(load_compressed_image(PGM_image))
    elif image_PGM[0][0]=='P2':
        return(load_regular_image(PGM_image))
    
    if not is_valid_image(load_regular_image(PGM_image)) and not is_valid_compressed_image(load_compressed_image(PGM_image)):
         raise AssertionError("Wrong file type")   
    
    image.close()
    
def save_regular_image(nested_list, filename):
    """(list<list<int>,str)->NonType
    Take a nested list and a filename as input, and if the nested list is a
    valid image matrix, it will write it in a file. otherwise, a assertion error will raise.
    >>> %Run image_processing.py
    >>> save_regular_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    >>> fobj = open("test.pgm", 'r')
    >>> fobj.read()
    'P2\n10 3\n255\n0 0 0 0 0 0 0 0 0 0\n255 255 255 255 255 255 255 255 255 255\n0 0 0 0 0 0 0 0 0 0\n'
    >>> fobj.close()
    
    >>> save_regular_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    >>> image2=load_image("test.pgm")
    >>> image1=[[0]*10, [255]*10, [0]*10]
    >>> image2!=image1
    False
    
    >>> save_regular_image([[0]*10, [255]*10, ["0"]*10], "test.pgm")
    Traceback (most recent call last):
    AssertionError: Wrong file type
    """
    fobj=open(filename,'w')
    text=""
    lenght=str(len(nested_list[0]))
    height=str(len(nested_list))
    for s in nested_list:
        for i in range(len(s)):
            text+=(str(s[i]))
            
            if i != len(s)-1:
                text+=" "
            
        text+="\n"
    fobj.write("P2\n"+lenght+" "+height+"\n255\n"+text)

    if not is_valid_image(nested_list):
         raise AssertionError("Wrong file type")
     
def save_compressed_image(nested_list, filename):
    """(list<list<str>,str)->NonType
    Take a nested list and a filename as input, and if the nested list is a
    valid compressed image matrix, it will write it in a file. Otherwise, a
    assertion error will raise.
    >>> save_compressed_image([["6x5", "20x2"], ["1110000x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\n7 2\n255\n6x5 20x2\n1110000x7\n'
    >>> fobj.close()
    
    >>> save_compressed_image([["6x5", "200"], ["111x7"]], "test.pgm.compressed")
    Traceback (most recent call last):
    IndexError: list index out of range
    
    >>> save_compressed_image([["6x5", "7x5"], ["111x10"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\n10 2\n255\n6x5 7x5\n111x10\n'
    >>> fobj.close()
    
    """
    fobj=open(filename, 'w')
    text=""
    for elmt in nested_list:
        B=0
        for i in elmt:
            B+=int(i.split("x")[1])
        lenght=str(B)
    height=str(len(nested_list))
    for s in nested_list:
        for i in range(len(s)):
            text+=(str(s[i]))
            if i!=len(s)-1:
                text+=" "
        text+="\n"
        
    fobj.write("P2C\n"+lenght+" "+height+"\n255\n"+text)

def save_image(nested_list, filename):
    """(list<list>,str)-> NonType
    Take a nested list and a filename as input, and if the nested list is a
    valid compressed image matrix or a valid non- compressed image matrix, it will write
    it in a file with the according form. Otherwise, an assertion error will raise.
    
    >>> save_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\n7 2\n255\n0x5 200x2\n111x7\n'
    >>> fobj.close()
    
    >>> save_image([[2, 1], [1,1]], "test.pgm")
    >>> fobj = open("test.pgm", 'r')
    >>> fobj.read()
    'P2\n2 2\n255\n2 1\n1 1\n'
    >>> fobj.close()
    
    >>> save_image([["0x5", "202"], ["111x7"]], "test.pgm.compressed")
    Traceback (most recent call last):
    AssertionError: wrong file type
    """
    if is_valid_compressed_image(nested_list):
        return(save_compressed_image(nested_list, filename))
    elif is_valid_image(nested_list):
        return(save_regular_image(nested_list, filename))
    if not is_valid_compressed_image(nested_list) and not is_valid_image(nested_list):
        raise AssertionError("wrong file type")
        
def invert(non_compressed_PGM):
    """list<int>->list<int>
    Invert a non compressed image matrix. And raise a assertion 
    error if the file is not a non-compressed image.
    >>> image = [[100, 100, 150], [100, 100, 200], [255, 255, 255]]
    >>> invert(image)
    [[155, 155, 105], [155, 155, 55], [0, 0, 0]]
    >>> image = [[100, 100, 150], [100, 100, 200], [255, 255, 2755]]
    >>> invert(image)
    Traceback (most recent call last):
    AssertionError: wrong file type
    >>> image = [[100, 100, 150], [1, 1, 20], [2, 5, 5]]
    >>> invert(image)
    [[155, 155, 105], [254, 254, 235], [253, 250, 250]]
    """
    
    if not is_valid_image (non_compressed_PGM):
        raise AssertionError("wrong file type")
    return [[255-i for i in elmt] for elmt in non_compressed_PGM]
    
def flip_horizontal(non_compressed_PGM):
    """list<int>->list<int>
    Filp the non compressd PGM matrix horizontally.
    Raise a assertion error is it is not a non compressed PGM
    >>>  image = [[2, 2, 3, 3, 3], [0, 0, 0, 1, 1], [5, 5, 5, 5, 5]]
    >>> flip_horizontal(image)
    [[3, 3, 3, 2, 2], [1, 1, 0, 0, 0], [5, 5, 5, 5, 5]]
    >>>  image = [[2, 2, 3, 3, 30000], [0, 0, 0, 1, 1], [1, 5, 1, 5, 1]]
    >>> flip_horizontal(image)
    [[30000, 3, 3, 2, 2], [1, 1, 0, 0, 0], [1, 5, 1, 5, 1]]
    >>>  image = [['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']]
    >>> flip_horizontal(image)
    Traceback (most recent call last):
    AssertionError: wrong file type
    """
    flip_image=[]
    
    if not is_valid_image(non_compressed_PGM):
        raise AssertionError("wrong file type")
    
    for elmt in non_compressed_PGM:
        flip_image.append(elmt[::-1])
    
    return flip_image



def flip_vertical(non_compressed_PGM):
    """(list<int))->list<int>
    flip a (non-compressed) PGM image matrix vertically
    >>>  image = [[1, 3, 3, 4, 5], [0, 0, 5, 5, 5], [5, 5, 5, 5, 5]]
    >>> flip_vertical(image)
    [[5, 5, 5, 5, 5], [0, 0, 5, 5, 5], [1, 3, 3, 4, 5]]
    >>>  image = [[1, 4, 5], [0, 0, 5, 5, 5], [5, 5, 5, 5, 5]]
    >>> flip_vertical(image)
    Traceback (most recent call last):
    AssertionError: wrong file type
    >>>  image = [[1, 4,6,6, 5], [0, 10000, 5, 5, 5], [5, 5, 5, 5, 5]]
    >>> flip_vertical(image)
    [[5, 5, 5, 5, 5], [0, 10000, 5, 5, 5], [1, 4, 6, 6, 5]]
    """
    if not is_valid_image(non_compressed_PGM):
        raise AssertionError("wrong file type")
    
    flip_image=non_compressed_PGM[::-1]
    return flip_image
    
def crop(non_compressed_PGM,x1,x2,y1,y2):
    """(list,int,int,int,int)->list
    crop a non compressed image matrix according to the given coordinates.
    >>> crop([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]], 1, 3, 2, 1)
    [[7], [11]]
    >>> crop([[1, 2, 3, 4], [4, 500, 600, 7000], [8, 9, 10, 11]], 0, 3, 2, 1)
    [[4], [7000]]
    >>> crop([[5, 5, 5], [5, 6, 6], [6, 6, 7]], 2, 2, 1, 1)
    [[7]]
    """
    crop_image=[]
    if not is_valid_image(non_compressed_PGM):
        raise AssertionError("must be a non commpressed PGM" )
    
    for crop1 in range(x1,x1+y1):
        crop_list=[]
        for crop2 in range(x2, x2+y2):
            crop_list.append(non_compressed_PGM[crop1][crop2])
        crop_image.append(crop_list)
    
    return(crop_image) 
  
def find_end_of_repetition(list_of_interger, index_interger, target_number):
    """(list, int,int)->int
    Return a interger that represent the index before the repetition of the target number end.
    In addition it start at the given index.
    >>> find_end_of_repetition([5, 3, 5, 5, 5, 5, 0], 2, 5)
    5
    >>> find_end_of_repetition([1, 7, 7, 4, 5, 6, 7], 1, 7)
    2
    >>> find_end_of_repetition([1, 1, 1, 1, 1, 1, 8], 0, 1)
    5
    """
    for i in list_of_interger[index_interger:]:
        
        if i!=target_number:
            return list_of_interger.index(i)-1
        if list_of_interger.index(i)==len(list_of_interger)-1 and i==target_number:
            return list_of_interger.index(i)
    
def compress(non_compressed_PGM):
    """(list<list<int>)->list<list>  
    Return the non-compressed PGM matrix as a conpressed PGM matrix
    Raise a assertion eror if it is not a non compressed PGM.
    >>> compress([[11, 11, 11, 11, 11], [5, 5, 5, 5, 5], [255, 255, 255, 255, 255]])
    [['11x5'], ['5x5'], ['255x5']]
    >>> compress(([['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']]))
    Traceback (most recent call last):
    AssertionError: wrong file type
    >>> compress([[ 11, 11], [5, 5, 5, 5, 5], [255, 255, 255, 255, 255]])
    Traceback (most recent call last):
    AssertionError: wrong file type
    """
    compress_list=[]
    last=0
    if not is_valid_image(non_compressed_PGM):
        raise AssertionError("wrong file type")
    
    for elmt in non_compressed_PGM:
        new_row=[]
        count=1
        for i in range(len(elmt)):
            last=elmt[i]
            if i+1==len(elmt):
                new_row.append(str(elmt[i])+"x"+str(count))
                count=1
            elif elmt[i+1]==last:
                 count+=1
            else:
                new_row.append(str(elmt[i])+"x"+str(count))
                count=1      
        compress_list.append(new_row)          
    return(compress_list)
        
def decompress(compressed_PGM):
    """(list<list<str>)->list<list>  
    Return the compressed PGM matrix as a non-conpressed PGM matrix.
    Raise an asserction error is it is not a compressd PGM
    >>> decompress([['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']])
    [[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]]
    >>> decompress([[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]])
    Traceback (most recent call last):
    AssertionError: must be a compresssed PGM
    >>> decompress([['11x6'], ['1x1', '5x3', '7x2'], ['255x4', '0x1', '255x1']])
    [[11, 11, 11, 11, 11, 11], [1, 5, 5, 5, 7, 7], [255, 255, 255, 255, 0, 255]]
    """
    decompress_PGM=[]
    
    if not is_valid_compressed_image(compressed_PGM):
        raise AssertionError("must be a compresssed PGM")
    for elmt in compressed_PGM:
        elmt_split=[]
        for i in elmt:
            for x in range(int(i.split("x")[1])):
                elmt_split.append(int((i.split("x")[0])))
        decompress_PGM.append(elmt_split)
    
    return decompress_PGM

def process_command(image):
    """list->NoneType

    >>> process_command("LOAD<comp.pgm> CP SAVE<comp.pgm.compressed>")
    >>> load_compressed_image("comp.pgm.compressed")
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1']
    , ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1',
    '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1'
    , '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4',
    '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1',
    '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1',
    '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    
    >>> process_command("LOAD<comp.pgm.compressed> DC SAVE<comp.pgm>")
    >>> load_image("comp.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187,
    187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0,
    187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0,
    119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119,
    0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51,
    0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    >>> process_command("LOAD<comp.pgm> Fv FH INV SAVE<comp.pgm>")
    >>> load_image("comp.pgm")
    [[255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 0, 0, 0, 0, 255, 68, 68, 68,
    68, 68, 255, 136, 136, 136, 136, 136, 255, 204, 204, 204, 204, 204, 255], [255,
    0, 255, 255, 0, 255, 68, 255, 68, 255, 68, 255, 136, 255, 255, 255, 136, 255, 255,
    255, 255, 255, 204, 255], [255, 0, 0, 0, 0, 255, 68, 255, 68, 255, 68, 255, 136,
    255, 255, 255, 136, 255, 255, 255, 255, 255, 204, 255], [255, 255, 255, 255, 0, 255,
    68, 255, 68, 255, 68, 255, 136, 255, 255, 255, 136, 255, 255, 255, 255, 255, 204,
    255], [255, 255, 255, 255, 0, 255, 68, 255, 68, 255, 68, 255, 136, 136, 136, 136,
    136, 255, 204, 204, 204, 204, 204, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]]
    """
    split_image=image.split()
    
    matrix=[]
    for elmt in split_image:
        
        if "LOAD" in elmt:
            matrix=load_image(elmt[elmt.index("<")+1:-1])
        elif "SAVE" in elmt: 
            save_image(matrix,elmt[elmt.index("<")+1:-1])
        elif "INV" in elmt:
            matrix=invert(matrix)
        elif "FH" in elmt:
            matrix=flip_horizontal(matrix)
        elif "FV" in elmt:
            matrix=flip_vertical(matrix)
        elif "CR" in elmt:
            matrix=crop(matrix,int(elmt[elmt.index(">")+1]),int(elmt[elmt.index("<")+3]),int(elmt[elmt.index(">")+5],int(elmt[elmt.index(">")+7])) )
        elif "CP" in elmt and is_valid_image(matrix):
            matrix=compress(matrix)
        elif "DC" in elmt and is_valid_compressed_image(matrix) :
            matrix=decompress(matrix)


