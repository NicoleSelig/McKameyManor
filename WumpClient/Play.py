import sys
from Message import Message
from Response import Response

class Play:
    
    playing = True
    
    def play(self, skt):
        # print("Playing....")
    #send to server
        while self.playing:
            #read response from socket
            joinResponse = Response(str(skt.recv(1024)))
            print(joinResponse.message)
          
            
            
            #if previous action == 'q'
            #quit after reading the response
            
            #create a new Message from it
            #print the messages
            
            #prompt the user for input
            #read the input - moves are chars
            
            #Nicole -- pythons version of a switch
            actionSelect = {
            'h': "home",
            'm': "msg.move",
            's': "msg.shoot",
            'q': "quitWumpus"
            }
            
            action = input("Move or Shoot? (m-s) ")
            while(action == 'h' or action == 'm' or action == 's'
                or action == 'q'):
                actionSelect[action]()
                
            #turn it into a message
            #send it to the server 
    
    #exits the playing loop
    def home(self):
        self.playing = False