import sys
from Message import Message
from Response import Response

class Play:
    
    playing = True
    
    def play(self, skt, name):
      
        while self.playing:
            #read response from socket
            response = Response(skt.recv(1024).decode('UTF-8'))
            print(response.getMessage())
            
            #store the adjacent rooms
            adjacentRooms = response.getAdjacentRooms()
            print(adjacentRooms)
            
            #init a message to send
            m = Message()
            
            while True:
                try:
                    #get action and room from the user
                    #Nicole - we need to handle 'quit'...will not work if only one input
                    action, room = input("Move or Shoot? (m-s)").split()
            
                    if (action == 'q'): 
                        m.quit(name)
                        break
                    elif(action == 'm'):
                        m.move(room)
                        break
                    elif(action == 's'):
                        m.shoot(room)
                        break
                    else:
                        print("Invalid move. Try again") 
                except ValueError:
                    print("You must enter a move and a room. Try again")
            
            #send it to the server 
            print(m.toString())
            skt.send(bytes(m.toString(), 'UTF-8'))
