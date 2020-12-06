import sys
import re

#constructor for the response from the server
class Response:
    code = 0
    #what the response codes indicate:
    #200 - moved to a room with no wumpus
    #300 - wumpus is in your destination and you are eaten
    #500 - player entered a room that is too large, or they hit a wall
    #100 - player shoots the wumpus
    #99 - the arrows are eaten
    #SHOOTing - The arrow can't find a way from 3 to 19 and flys randomly into room #!
    #101 - help menu
    #0 - remove player
    
    adjacentRooms = []
    bytes = 0
    message = ""
    
    def __init__(self, data):
        self.parts = data.split("|")
        print(self.parts) 
        
        self.code = self.parts[0] 
        print(self.code)
        self.adjacentRooms = self.parts[1].split(",")
        print(self.adjacentRooms)
        self.bytes = self.parts[2] 
        print(self.bytes)
        
        # #stores the message in a variable
        # for line in parts2[1:-1]: #skips the first and last element 
        #     self.message += line[1:]
        #     self.message += "\n"
        # #print(self.message)
    
    def getMessage(self):
        return self.message
    
    def getAdjacentRooms(self):
        return self.adjacentRooms
    
    def getCode(self):
        return self.code
    
    def getBytes(self):
        return self.bytes
        