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
            
            #init a message to send
            m = Message()
            action = None
            room = None
            while True:
                try:
                    #get action and room from the user
                    #Nicole - we need to handle 'quit'...will not work if only one input
                    action = input("Move or Shoot? (m-s)")
            
                    if action == 'q': 
                        m.quit(name)
                        print("You are abandoning the hunt! Goodbye!")
                        sys.exit(0)
                    elif action == 'h':
                        m.help()
                        break
                    elif action == 'm':
                        cave = input("Which cave?")
                        m.move(cave)
                        break
                    elif action == 's':
                        cave = input("Which cave?")
                        m.shoot(cave)
                        break
                    else:
                        print("Invalid move. Try again") 
                except ValueError:
                    print("You must enter a move and a room. Try again")
            
            #send it to the server 
            print(m.toString())
            skt.send(bytes(m.toString(), 'UTF-8'))
