import sys

class Message:
    
    command = ""
    target = ""
    numBytes = 0
    message = ""
        
    def __init__ (self, data ="null|null|0"):  #initiallizing with nulls and a 0
       self.lines = data.split("\n")
       self.parts = self.lines[0].split("|")
       #print(self.parts)
       self.command = self.parts[0]
       self.target = self.parts[1]
       self.numBytes = int(self.parts[2])
       self.message = ""
       
       if (self.numBytes > 0):
        for x in range(self.lines.len):
            self.message += self.lines[1] + "\n"
           
    #getters and setters
    #or by action 
    #Nicole -- we need to add 'MOVE', SHOOT, etc...  
    def join(self, name):
        self.command =  "JOIN"
        self.target = name
        self.numBytes = sys.getsizeof(name)
    
    def quit(self, name):
        self.command = "QUIT"
        self.target = name
        self.numBytes = sys.getsizeof(name)
    
    def move(self, room):
        self.command = "MOVE"
        self.target = room
        self.numBytes = sys.getsizeof(room)
    
    def shoot(self, room):
        self.command = "SHOOT"
        self.target = room
        self.numBytes = sys.getsizeof(room)
        
    def toString(self):
        return self.command + "|" + self.target + "|" + str(self.numBytes) + "\n"
    
    
        
        
        
    