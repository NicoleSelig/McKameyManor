import sys
import re

#constructor for the response from the server
class Response:
    code = 0
    adjacentRooms = []
    bytes = 0
    message = ""
    
    def __init__(self, data):
        # print(data)
        self.lines = data.split("\n")
        self.parts = self.lines[0].split("|")
        # print(self.parts) #not sure why, but this has extra \\'s in the message -- Nicole
        self.code = self.parts[0]
        # print(self.code)
        self.adjacentRooms = self.parts[1].split(",")
        # print(self.adjacentRooms)
        parts2 = self.parts[2].split('\\')
        # print(parts2)
        self.bytes = parts2[0]
        # print(self.bytes)
       
        #Prints the response Message -- not sure there is a need to store this in a variable
        for line in parts2[1:-1]: #skips the first and last element 
            print(line[1:]) #removes the n's
        