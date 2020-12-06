import sys

#constructor class that handles the message sent by the server
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
           
    #sets a join message
    def join(self, name):
        self.command =  "JOIN"
        self.target = name
        self.numBytes = sys.getsizeof(name)
    
    #sets the quit message
    def quit(self):
        self.command = "QUIT"
        self.target = "null"
        self.numBytes = 0
        
    def help(self):
        self.command = "HELP"
        self.target = "null"
        self.numBytes = 0
    
    #sets a move message
    def move(self, room):
        self.command = "MOVE"
        self.target = room
        self.numBytes = sys.getsizeof(room)
    
    #sets a shoot message
    def shoot(self, room):
        self.command = "SHOOT"
        self.target = room
        self.numBytes = sys.getsizeof(room)
    
    #sets the message to string format for sending to server
    def toString(self):
        return self.command + "|" + self.target + "|" + str(self.numBytes) + "\n"
    
    
        
        
        
    