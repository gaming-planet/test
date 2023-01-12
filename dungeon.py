#Comp 202 assignment 2 part 1
#Rui-Jia meng
#ID:261116408

NAME="Rui jia Meng"
ROOM_NAME="hehehe time kilkler"
PUBLIC= True
    
def start():
    """()->NoneType
    display a print statement for the game intro
    >>> start()
    When you opened your eyes, you were horrified to find that you came to a completely unknown enclosed space.
    The door was locked, and no matter how hard you slammed it, it wouldn't move.Consequently, your only purpose is
    right now is to escape the room! The decoration of the room is very strange,and the tools placed around seem to
    have some purpose. You pick up a piece of paper on the ground with a string of strange  characters written on it...
    You can only tell that they want you to choosea object in the room between a pencil, a book that only has its
    right part and a clock.

    """
    print("When you opened your eyes, you were horrified to find that you came to a completely unknown enclosed space.\
The door was locked, and no matter how hard you slammed it, it wouldn't move.\
Consequently, your only purpose is right now is to escape the room! The decoration of the room is very strange,\
and the tools placed around seem to have some purpose. You pick up a piece of paper on the ground \
with a string of strange  characters written on it...You can only tell that they want you to choose\
a object in the room between a pencil, a book that only has its right part and a clock.")



def success():
    """()->NoneType
    display a print statement for the game succes
    >>> success()
    You put the tresure on altar and suddendly the room starts shaking. You close your eyes and hope for the best.
    After ten sec, the room stop shaking and when you open your eyes, you find yourself outside of the room.

    """
    print("You put the tresure on altar and suddendly the room starts shaking. You close your eyes and hope for the best. \
After ten sec, the room stop shaking and when you open your eyes, you find yourself outside of the room.")
    



#object 1 (clock): 
def box_gold():
    """()->NoneType
    display a different print statement for different commands that the palyer choose
    >>> box_gold()
    altar
    You put the tresure on altar and suddendly the room starts shaking. You close your eyes and hope for the best. After ten sec, the room stop shaking and when you open your eyes, you find yourself outside of the room.
    >>> box_gold()
    exit door
    you walk out of the exit door with the treasure and suddendly the wall crashed on you. You paid for your greedy!!
    >>> box_gold()
    list commands
    altar
    exit door
    """
    which_path=input().lower()
    while ("altar" not in which_path) and ("exit door" not in which_path) and ("list commands" not in which_path):
        print("invalid answer pls re-enter your commends")
        which_path=input().lower()
    if which_path=="list commands":
        print("altar\nexit door")
        return(box_gold())   
    elif "altar"in which_path:
        success()    
    elif "exit door" in which_path:
        print("you walk out of the exit door with the treasure and suddendly the wall crashed on you. You paid for your greedy!!")
    
def box1():
    """()->NoneType
    display a different print statement for different commands that the palyer choose
    >>> box1()
    gold box
    you open the box and find the treasure. You look at the treasure on your hand and dont know what to do.Suddendly,
    the room starts shaking and a altar and a exit door apear in fornt of you.
    altar
    You put the tresure on altar and suddendly the room starts shaking. You close your eyes and hope for the best.
    After ten sec, the room stop shaking and when you open your eyes, you find yourself outside of the room.
    >>> box1()
    gold box
    you open the box and find the treasure. You look at the treasure on your hand and dont know what to do.Suddendly,
    the room starts shaking and a altar and a exit door apear in fornt of you.
    exit door
    you walk out of the exit door with the treasure and suddendly the wall crashed on you. You paid for your greedy!!
    >>> box1()
    silver box
    you open the sliver box and a spider eats your face and before ur death, you realize that you are so stupid because
    you are looking for a yellow box not sliver box.
    """
    box=input().lower().lower()
    while ("gold box"  not in box) and ("silver box" not in box) and ("list commands" not in box):
        print("invalid answer pls re-enter your commends")
        box=input().lower()
    if box=="list commands":
        print("gold box\nsilver box")
        return(box1())   
    elif "gold box" in box:
        print("you open the box and find the treasure. You look at the treasure on your hand and dont know what to do.\
Suddendly, the room starts shaking and a altar and a exit door apear in fornt of you.")
        box_gold()
            
    elif "silver box" in box:
        print("you open the sliver box and a spider eats your face and before ur death, you realize that you are so \
stupid because you are looking for a yellow box not sliver box.")

def object_clock():
   """()->NoneType
   >>> object_clock()
    telephone
    you pick up the telephone and you hear a voice through the phone that tell you to find a compass in a yellowbox in the room, you look around the room and noticed a gold box and a silver box
    silver box
    you open the sliver box and a spider eats your face and before ur death, you realize that you are so stupid because you are looking for a yellow box not sliver box.
    >>> object_clock()
    notebook
     you open the notebook and read that there is a treasure in the room hiding is a yellow space, you look around a find a gold box and a silver box
    gold box
    you open the box and find the treasure. You look at the treasure on your hand and dont know what to do.Suddendly, the room starts shaking and a altar and a exit door apear in fornt of you.
    altar
    You put the tresure on altar and suddendly the room starts shaking. You close your eyes and hope for the best. After ten sec, the room stop shaking and when you open your eyes, you find yourself outside of the room.
    >>> object_clock()
    notebook
     you open the notebook and read that there is a treasure in the room hiding is a yellow space, you look around a find a gold box and a silver box
    gold box
    you open the box and find the treasure. You look at the treasure on your hand and dont know what to do.Suddendly, the room starts shaking and a altar and a exit door apear in fornt of you.
    exit door
    you walk out of the exit door with the treasure and suddendly the wall crashed on you. You paid for your greedy!!   
   """ 
   object1=input().lower()
   while ("telephone"  not in object1) and ("notebook" not in object1) and ("list commands" not in object1):
        print("invalid answer pls re-enter your commends")
        object1=input().lower()
   if "list commands"== object1:
        print("telephone\nnotebook")
        return(object_clock()) 
   elif "telephone" in object1:
        print("you pick up the telephone and you hear a voice through the phone that tell you to find a compass in a yellow\
box in the room, you look around the room and noticed a gold box and a silver box")
        box1()
        
   elif "notebook" in object1:
        print(" you open the notebook and read that there is a treasure in the room hiding is a yellow space, \
you look around a find a gold box and a silver box")
        box1()
#object 2(book)
def book2():
    """()->NoneType
    display a different print statement for different commands that the palyer choose
    >>> book2()
    right box
    you open the right box you find the treasure!!! it is a piece of coin made in gold. You look around and find a altar and a exit door
    altar
    You put the tresure on altar and suddendly the room starts shaking. You close your eyes and hope for the best. After ten sec, the room stop shaking and when you open your eyes, you find yourself outside of the room.
    >>> book2()
    left box
     you open the box and suddendly the door behind you open. You look at in the darkness and a monster kill you
    >>> book2()
    right box
    you open the right box you find the treasure!!! it is a piece of coin made in gold. You look around and find a altar and a exit door
    exit door
    you walk out of the exit door with the treasure and suddendly the wall crashed on you. You paid for your greedy!!
    """
    open_box=input().lower()
    while ("right box"  not in open_box) and ("left box" not in open_box) and ("list commands" not in open_box):
        print("invalid answer pls re-enter your commends")
        open_box=input().lower()
    if "list commands"== open_box:
        print("right box\nleft box")
        return(book2())     
    if "right box" in open_box:
        print("you open the right box you find the treasure!!! it is a piece of coin made in gold. You look around and find a altar and a exit door")
        box_gold()
        
    elif "left box" in open_box:
         print(" you open the box and suddendly the door behind you open. You look at in the darkness and a monster kill you")

#object 3(pencil)

def even_odd():
    """()->NoneType
    display a different print statement for different commands that the palyer choose
    >>> even_odd()
    even
     you choose even and congrat it is answer that the skeleton want, consequently the skeleton set you free from the escape room
    >>> even_odd()
    odd
     you choose odd and you realize that it is not the answer that the skeleton want!! But it is too late, you see the skeleton run at you and you just regret that you didnt listen in your elementary school math class 
    >>> even_odd()
    list commands
    even
    odd
    even
    you choose even and congrat it is answer that the skeleton want, consequently the skeleton set you free from the escape room
    """
    even_or_odd=input().lower()
    while ("even" not in even_or_odd) and ("odd" not in even_or_odd) and ("list commands" not in even_or_odd):
        print("invalid commands!! pls re-enter your commands")
        even_or_odd=input().lower()
    if "list commands"== even_or_odd:
        print("even\nodd")
        return(even_odd())
    elif "even" in even_or_odd:
        print(" you choose even and congrat it is answer that the skeleton want, consequently the skeleton set you free from the escape room")
    elif "odd" in even_or_odd:
        print("you choose odd and you realize that it is not the answer that the skeleton want!! \
But it is too late, you see the skeleton run at you and you just regret that you didnt listen in your elementary school math class ")

def place1():
   """()->NoneType
    display a different print statement for different commands that the palyer choose
    >>> place1()
    alter
    You put the tresure on altar and suddendly the room starts shaking. You close your eyes and hope for the best. After ten sec, the room stop shaking and when you open your eyes, you find yourself outside of the room.
    >>> place1()
    skeleton
     you put the coin in the hand of the skeleton and suddendly the skeleton became alive!!!! he ask you if 6/2(2+1) is even, if it is even you must to to the right door and if you choose odd he will force you to the left door.
    odd
    you choose odd and you realize that it is not the answer that the skeleton want!! But it is too late, you see the skeleton run at you and you just regret that you didnt listen in your elementary school math class 
    >>> place1()
    skeleton
     you put the coin in the hand of the skeleton and suddendly the skeleton became alive!!!! he ask you if 6/2(2+1) is even, if it is even you must to to the right door and if you choose odd he will force you to the left door.
    even
     you choose even and congrat it is answer that the skeleton want, consequently the skeleton set you free from the escape room  
   """
   place=input().lower()
   while ("alter" not in place) and ("skeleton" not in place) and ("list commands" not in place):
       print("invalid commands!! pls re-enter your commands")
       place=input().lower()
   if "list commands"== place:
       print("alter\nskeleton")
       return(place1())
   if "alter" in place:
       success()
   elif "skeleton" in place:
       print(" you put the coin in the hand of the skeleton and suddendly the skeleton became alive!!!! he ask you if 6/2(2+1) is even, \
if it is even you must to to the right door and if you choose odd he will force you to the left door.")
       even_odd()

def pencil3():
    """()->NoneType
    display a different print statement for different commands that the palyer choose
    >>> pencil3()
    yellow wallet
    you open the wallet and find a gold coin inside and a alter with a skeleton apears in front of you.
    You look at the coin and you realize that the coin could be place on the altar in front of you or in the hand of skeleton
    alter
    You put the tresure on altar and suddendly the room starts shaking. You close your eyes and hope for the best.
    After ten sec, the room stop shaking and when you open your eyes, you find yourself outside of the room.
    >>> pencil3()
    silver wallet
    you open ths silver wallet and realize that theres nothing inside... You turn ur head and you got kill by a skeleton 
    >>> pencil3()
    yellow wallet
    you open the wallet and find a gold coin inside and a alter with a skeleton apears in front of you. You look at the coin and
    you realize that the coin could be place on the altar in front of you or in the hand of skeleton
    skeleton
     you put the coin in the hand of the skeleton and suddendly the skeleton became alive!!!! he ask you if 6/2(2+1) is even,
     if it is even you must to to the right door and if you choose odd he will force you to the left door.
    odd
    you choose odd and you realize that it is not the answer that the skeleton want!! But it is too late, you see the skeleton run
    at you and you just regret that you didnt listen in your elementary school math class 
    """
    object3=input().lower()
    while ("yellow wallet" not in object3) and ("silver wallet" not in object3) and ("list commands" not in object3):
       print("invalid commands!! pls re-enter your commands")
       object3=input().lower()
    if "list commands"== object3:
       print("yellow wallet\nsilver wallet")
       return(pencil3())
    elif "yellow wallet" in object3:
       print("you open the wallet and find a gold coin inside and a alter with a skeleton apears in front of you\
. You look at the coin and you realize that the coin could be place on the altar in front of you or in the hand of skeleton")
       place1()                
    if "silver wallet" in object3:
            print("you open ths silver wallet and realize that theres nothing inside... You turn ur head and you got kill by a skeleton ")


def start1():
    """()->NoneType
    display a different print statement for different commands that the palyer choose
        >>> start1()
    book
    you open the book and read that there is a tresure in the room hinding in one of the box at the left and right,
    however you only have one chance to guess which is the right box. (think about how the book looks like) 
    left box
     you open the box and suddendly the door behind you open. You look at in the darkness and a monster kill you
    >>> start1()
    pencil
    you take the pencil and you realize that it is just a normal pencil with the words: I dont like silver on it. In addition,
    the two ends of the pencil point you to two things, a intact yellow wallet and a broken silver wallet.
    silver wallet
    you open ths silver wallet and realize that theres nothing inside... You turn ur head and you got kill by a skeleton 
    >>> start1()
    clock
    OOOOOOh You accidentally click a mysterious button on the alarm clock, and suddenly you find that the dilapidated room
    you are in is slowly changing, the dilapidated furniture has become very new, and the cracks in the walls have all disappeared.
    You find that the button you just touched has set the chamber back in time. In addition youfind a telephone and notebook on the ground
    telephone
    you pick up the telephone and you hear a voice through the phone that tell you to find a compass in a yellowbox in the room,
    you look around the room and noticed a gold box and a silver box
    silver box
    you open the sliver box and a spider eats your face and before ur death, you realize that you are so stupid because
    you are looking for a yellow box not sliver box.

    """        
    examine_object=(input().lower())
        
    while ("clock" not in examine_object) and ("book"not in examine_object) and ("pencil" not in examine_object) and ("list commands" not in examine_object):
        print("invalid commands!! pls re-enter your commands")
        examine_object=input().lower()
    
    if examine_object=="list commands":
        print("examine book\nexamine clock\nexamine pencil")
        return(start1())   
    
    elif "clock" in examine_object:
        print("OOOOOOh You accidentally click a mysterious button on the alarm clock, and suddenly you \
find that the dilapidated room you are in is slowly changing, the dilapidated furniture has become very new, and the cracks \
in the walls have all disappeared. You find that the button you just touched has set the chamber back in time. In addition you\
find a telephone and notebook on the ground")
        object_clock()
      

            
    elif "book" in examine_object:
        print("you open the book and read that there is a tresure in the room hinding in one of the box at \
the left and right, however you only have one chance to guess which is the right box. (think about how the book looks like) ")
        book2()
        
            
    elif "pencil" in examine_object:
        print("you take the pencil and you realize that it is just a normal pencil with the words: I dont like silver on it.\
In addition, the two ends of the pencil point you to two things, a intact yellow wallet and a broken silver wallet.")
        pencil3()

 
 
def escape_room(): 
    """()->NoneType
    >>> escape_room()
    When you opened your eyes, you were horrified to find that you came to a completely unknown enclosed space.
    The door was locked, and no matter how hard you slammed it, it wouldn't move.Consequently, your only purpose is
    right now is to escape the room! The decoration of the room is very strange,and the tools placed around seem to
    have some purpose. You pick up a piece of paper on the ground with a string of strange  characters written on it...
    You can only tell that they want you to choosea object in the room between a pencil, a book that only has its right
    part and a clock.
    clock
    OOOOOOh You accidentally click a mysterious button on the alarm clock, and suddenly you find that the dilapidated
    room you are in is slowly changing, the dilapidated furniture has become very new, and the cracks in the walls have all
    disappeared. You find that the button you just touched has set the chamber back in time. In addition youfind a telephone
    and notebook on the ground
    telephone
    you pick up the telephone and you hear a voice through the phone that tell you to find a compass in a yellowbox in the room,
    you look around the room and noticed a gold box and a silver box
    silver box
    you open the sliver box and a spider eats your face and before ur death, you realize that you are so stupid because
    you are looking for a yellow box not sliver box.
    >>> escape_room()
    When you opened your eyes, you were horrified to find that you came to a completely unknown enclosed space.The door was locked,
    and no matter how hard you slammed it, it wouldn't move.Consequently, your only purpose is right now is to escape the room!
    The decoration of the room is very strange,and the tools placed around seem to have some purpose. You pick up a piece of paper
    on the ground with a string of strange  characters written on it...You can only tell that they want you to choosea object in
    the room between a pencil, a book that only has its right part and a clock.
    pencil
    you take the pencil and you realize that it is just a normal pencil with the words: I dont like silver on it.In addition,
    the two ends of the pencil point you to two things, a intact yellow wallet and a broken silver wallet.
    yellow wallet
    you open the wallet and find a gold coin inside and a alter with a skeleton apears in front of you. You look at the coin and
    you realize that the coin could be place on the altar in front of you or in the hand of skeleton
    skeleton
     you put the coin in the hand of the skeleton and suddendly the skeleton became alive!!!! he ask you if 6/2(2+1) is even,
     if it is even you must to to the right door and if you choose odd he will force you to the left door.
    even
     you choose even and congrat it is answer that the skeleton want, consequently the skeleton set you free from the escape room
    >>> escape_room()
    When you opened your eyes, you were horrified to find that you came to a completely unknown enclosed space.The door was locked,
    and no matter how hard you slammed it, it wouldn't move.Consequently, your only purpose is right now is to escape the room! The
    decoration of the room is very strange,and the tools placed around seem to have some purpose. You pick up a piece of paper on
    the ground with a string of strange  characters written on it...You can only tell that they want you to choosea object in the room
    between a pencil, a book that only has its right part and a clock.
    bookg
    you open the book and read that there is a tresure in the room hinding in one of the box at the left and right, however you only
    have one chance to guess which is the right box. (think about how the book looks like) 
    right
    invalid answer pls re-enter your commends
    right box
    you open the right box you find the treasure!!! it is a piece of coin made in gold. You look around and find a altar and a exit door
    alter
    invalid answer pls re-enter your commends
    altar
    You put the tresure on altar and suddendly the room starts shaking. You close your eyes and hope for the best. After ten sec,
    the room stop shaking and when you open your eyes, you find yourself outside of the room.
    """
    start()        
    start1()
    
     
escape_room()