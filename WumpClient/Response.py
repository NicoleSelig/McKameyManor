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
        parts = data.split("|")
        #print(parts) 
        self.code = parts[0].strip()
        print(self.code)
        self.adjacentRooms = parts[1].split(",")
        #print(self.adjacentRooms)
        self.bytes = int(re.search(r'\d+', parts[2]).group(0)) #finds the first number in the string 
        #print(self.bytes)
        self.message = data[-self.bytes:]
         
    def getMessage(self):
        return self.message
    
    def getAdjacentRooms(self):
        return self.adjacentRooms
    
    def getCode(self):
        return self.code
    
    def getBytes(self):
        return self.bytes
        