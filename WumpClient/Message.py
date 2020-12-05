import sys

class Message:
        
    def __init__ (self, data ="null|null|0"):  #initiallizing with nulls and a 0
       self.lines = data.split("\n")
       self.parts = self.lines[0].split("|")
       #print(self.parts)
       self.command = self.parts[0]
       self.target = self.parts[1]
       self.numBytes = int(self.parts[2])
       self.messages = ""
       
       if (self.numBytes > 0):
        for x in range(self.lines.len):
            self.messages += self.lines[1] + "\n"
           
    #getters and setters
    #or by action 
    #Nicole -- we need to add 'MOVE', SHOOT, etc...  
    def join(self, name):
        self.command =  "JOIN"
        self.target = name
        self.numBytes = sys.getsizeof(name)
        
    def toString(self):
        return self.command + "|" + self.target + "|" + str(self.numBytes)
        
    