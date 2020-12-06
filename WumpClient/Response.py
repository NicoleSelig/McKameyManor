import sys
import re

#constructor for the response from the server
class Response:
    code = 0
    adjacentRooms = []
    bytes = 0
    message = ""
    
    def __init__(self, data):
        self.lines = data.split("\n")
        self.parts = self.lines[0].split("|")
        # print(self.parts) 
        
        self.code = self.parts[0][2:] #ignores the first 2 characters to get just the code number
        print(self.code)
        self.adjacentRooms = self.parts[1].split(",")
        print(self.adjacentRooms)
        
        #splits the bytes from the data
        parts2 = self.parts[2].split('\\')
        self.bytes = parts2[0]
        print(self.bytes)
        
        #stores the message in a variable
        for line in parts2[1:-1]: #skips the first and last element 
            self.message += line[1:]
            self.message += "\n"
    
    def getMessage(self):
        return self.message
    
    def getAdjacentRooms(self):
        return self.adjacentRooms
    
    def getCode(self):
        return self.code
    
    def getBytes(self):
        return self.bytes
        