import musicalbeeps


class Note:
    """A class to represent a note
    
    insteance attributes
    * duration: float
    * pitch: str
    * octave: int
    * accidental: str    
    """
    
    def __init__(self, duration, pitch, octave= 1, accidental="natural"):
        """(float,str,int,str)->NoneType
        creat a object of type of note
        >>> note = Note(6.0, "C", 5, "natural")
        >>> note.duration
        6.0
        >>> note.pitch
        'C'
        >>> note.accidental
        'natural'
        """
        if type(duration) != float:
            raise AssertionError("duration must be a float")
        elif pitch not in ["A", "B", "C","D", "E", "F","G","R"]  :
            raise AssertionError("pitch must be a string single letter from A to G, or R ")
        elif type(octave) != int or octave < 1.0 or octave > 7.0 :
            raise AssertionError("octave must be between 1 and 7")
        elif accidental not in ["sharp", "flat", "natural"]:
            raise AssertionError("accidental value must be either sharp, flat or natural, in lowercase")
        
        self.duration = duration
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental
        

    def __str__ (self): 
        '''NoneType->NoneType
        return the duration,pitch, octave and the accidental value of the note object
        >>>  note = Note(4.0, "C", 4, "natural")
        >>> print(note)
        4.0 C 4 natural
        
        >>>  note = Note(1.0, "D", 7, "natural")
        >>> print(note)
        1.0 D 7 natural
        
        >>>  note = Note(1.0, "E", 3, "natural")
        >>> print(note)
        1.0 E 3 natural
        '''
        return str(self.duration)+" " + self.pitch + " " + str(self.octave) + " " +self.accidental
    
    
    
    def play(self, player):
        """("player")->NoneType
        diplay the play_note function on the note object.
        """
        if self.pitch=="R":
            player.play_note("pause",self.duration)
        else:
            note_play=self.pitch+str(self.octave)
            if self.accidental=="sharp":
                note_play+="#"
            elif self.accidental=="flat":
                note_play+="b"
            player.play_note(note_play, self.duration)

