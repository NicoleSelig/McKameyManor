import socket
import sys
import Message 

class Client:
    
    
 if __name__ == "__main__":
     
     msg = Message()
     
     server = "localhost"
     port = 1024
     
     #create an INET, STREAMing socket
     socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     socket.connect((server, port))
     
     name = input("Welcome to Hunt the Wumpus! Enter your name: ")
     
     message = msg.join(name)
     
     #send to server
     
     while True:
         #read response from socket
         
         #if previous action == 'q'
         #quit after reading the response
         
         #create a new Message from it
         #print the messages
         
         #prompt the user for input
         #read the input - moves are chars
         
         #Nicole -- pythons version of a switch
        actionSelect = {
        'h': home,
        'm': move,
        's': shoot,
        'q': quitWumpus
        }
         
        action = input("Move or Shoot? (m-s) ")
        while(action == 'h' or action == 'm' or action == 's'
               or action == 'q'):
             actionSelect[action]()
             
        #turn it into a message
        #send it to the server

   

   
    

                