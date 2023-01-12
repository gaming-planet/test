from note import *



class Melody:
    """A class to represent a note
    
    insteance attributes
    * title:
    * pitch: str
    * octave: int
    * accidental: str    
    """
    
    def __init__(self, filename):
        """
        creat a object of type of Melody
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.author
        'Patty and Mildred J. Hill'
        >>> happy_birthday.title
        'Happy Birthday'
        >>> happy_birthday.notes
        [<note.Note object at 0x0000029811F95FF0>, <note.Note object at 0x0000029811F95F90>,
        <note.Note object at 0x0000029811F95F30>, <note.Note object at 0x0000029811F95ED0>,
        <note.Note object at 0x0000029811F95E70>, <note.Note object at 0x0000029811F95D80>,
        <note.Note object at 0x0000029811F95D20>, <note.Note object at 0x0000029811F95CC0>,
        <note.Note object at 0x0000029811F95C60>, <note.Note object at 0x0000029811F96230>,
        <note.Note object at 0x0000029811F96290>, <note.Note object at 0x0000029811F962F0>,
        <note.Note object at 0x0000029811F96350>, <note.Note object at 0x0000029811F963B0>,
        <note.Note object at 0x0000029811F96410>, <note.Note object at 0x0000029811F96470>,
        <note.Note object at 0x0000029811F964D0>, <note.Note object at 0x0000029811F96530>,
        <note.Note object at 0x0000029811F96590>, <note.Note object at 0x0000029811F965F0>,
        <note.Note object at 0x0000029811F96650>, <note.Note object at 0x0000029811F966B0>,
        <note.Note object at 0x0000029811F96710>, <note.Note object at 0x0000029811F96770>,
        <note.Note object at 0x0000029811F967D0>]
        """
        note_string=""
        song_list1=[]
        song_list=[]
        note_list=[]
        list_of_self=[]
        new_list=[]
        music=open(filename, "r")
        
        for line in music:
            row=line.split()
            song_list1.append(row)
        music.close()
        
        self.title= " ".join(song_list1[0])
        self.author=" ".join(song_list1[1])
        
        for i in range(2):
            song_list1.pop(0) 
        
        repeat=True
        
        for elmt in song_list1:
            song_list.append(elmt)
            
            
            if elmt[-1]=="true" and repeat or elmt[-1] == "false" and not repeat:
                new_list.append(elmt)
                repeat=False
            elif elmt[-1]=="true" and  not repeat:
                new_list.append(elmt)
                song_list+=new_list
                new_list=[]
                repeat=True
            

        for elmt in song_list:
            
            if str(elmt[1])=="R":
                note_string=str(elmt[0])+" "+str(elmt[1])
            else:
                note_string=str(elmt[0])+" "+str(elmt[1])+" "+str(elmt[2])+" "+str(elmt[3])
            note_list.append(note_string)
        
        for i in range (len(note_list)):
            list_note=note_list[i].split(" ")
            if str(list_note[1])=="R":
                note=Note(float(list_note[0]), str(list_note[1]))
            else:
                note=Note(float(list_note[0]), str(list_note[1]),int(list_note[2]), str(list_note[3]).lower())
            list_of_self.append(note)
        
        
        self.notes=list_of_self
        
    def play(self, player):
        """(player)->none
        play the melody with the play funtion of note object
        """
        for note in self.notes:
            note.play(player)
    
    def get_total_duration(self):
        """(none)->float
        return the total duartion of the whole melody by adding up the duration
        of each note
        
        >>>  happy_birthday = Melody("birthday.txt")
        >>>  happy_birthday.get_total_duration()
        13.0
        
        >>> hot_cross_buns = Melody("hotcrossbuns.txt")
        >>>  hot_cross_buns.get_total_duration()
        8.0
        """
        total_duration=0
        for note in self.notes:
            total_duration+=note.duration
        return(total_duration)
        
    def lower_octave(self):
        """(NoneTyoe)->bool
        return a boolean that indicate if the octave is in its range if we decrese it.
        if it is in range, all the octave in the melody will decraese of 1
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.lower_octave()
        True
        >>> happy_birthday = Melody("birthday.txt")
        >>> happy_birthday.lower_octave()
        True
        >>> happy_birthday.lower_octave()
        True
        >>> happy_birthday.lower_octave()
        True
        >>> happy_birthday.lower_octave()
        False
        
        >>>  hot_cross_buns = Melody("hotcrossbuns.txt")
        >>>  hot_cross_buns.lower_octave()
        True   
        """
        for note in self.notes:
            if note.octave<2:
                return False
        for note in self.notes:
            if note.pitch=="R":
                continue
            note.octave=note.octave-1
        return(True)
        
    def upper_octave(self):
        """(NoneType)->Bool
        return a boolean that indicate if the octave is in its range if we increse it.
        if it is in range, all the octave in the melody will incraese of 1
        >>> happy_birthday = Melody("birthday.txt")
        >>>  happy_birthday.upper_octave()
        True
        >>>  happy_birthday.upper_octave()
        True
        >>>  happy_birthday.upper_octave()
        False
        >>> happy_birthday = Melody("birthday.txt")
        >>>  happy_birthday.upper_octave()
        True
        >>>  happy_birthday.upper_octave()
        True
        >>> happy_birthday.notes[5].octave
        6
        >>> happy_birthday = Melody("birthday.txt")
        >>>  happy_birthday.upper_octave()
        True
        """
        for note in self.notes:
            if note.octave>6:
                return(False)
        for note in self.notes:
            if note.pitch=="R":
                continue
            note.octave=note.octave+1  
        return(True)
            
    def change_tempo(self, float_number):
        """(float)->NoneType
        change the duration of the note by multiplying it by the  input float
        >>> happy_birthday = Melody("birthday.txt")
        >>>  happy_birthday.change_tempo(50)
        >>>  happy_birthday.get_total_duration()
        650.0
        >>> happy_birthday = Melody("birthday.txt")
        >>>  happy_birthday.change_tempo(0.01)
        >>>  happy_birthday.get_total_duration()
        0.13000000000000003
        >>> happy_birthday = Melody("birthday.txt")
        >>>  happy_birthday.change_tempo(2)
        >>>  happy_birthday.get_total_duration()
        26.0
        """
        for note in self.notes:
            note.duration=note.duration*float_number
        
