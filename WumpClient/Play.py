import sys
from Message import Message
from Response import Response

class Play:
    
    playing = True
    
    def play(self, skt, name):
        # print("Playing....")
    #send to server
        while self.playing:
            #read response from socket
            response = Response(str(skt.recv(1024)))
            print(response.getMessage())
            
            adjacentRooms = response.getAdjacentRooms()
            print(adjacentRooms)
            #create a new Message from it
            #print the messages
            
            #prompt the user for input
            #read the input - moves are chars
            #turn it into a message
            m = Message()
            action, room = input("Move or Shoot? (m-s)").split()
            print(action)
            print(room)
            while(action == 'm' or action == 's' or action == 'q'):
                if (action == 'q'):
                    m.quit(name)
                if (action == 'm'):
                    m.move(room)
                if (action == 's'):
                    m.shoot(room)

            #send it to the server 
            print(m.toString())
            skt.send(bytes(m.toString()), 'UTF-8')
