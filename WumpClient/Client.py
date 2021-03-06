import socket
import sys
from Message import Message
from Play import Play


class Client:
    
    #main menu loop
    def main():
        while(True):
            server = socket.gethostbyname("localhost")
            port = 9876
            
            #create an INET, STREAMing socket:
            try:
                skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                skt.connect((server, port))
                print("Connected to Wump Server at port " + str(port))
            except TimeoutError:
                print("Connection Timeout")
                print("Goodbye!")
                sys.exit()
            
            #get the players name and send it to the server
            name = input("Welcome to Hunt the Wumpus! Enter your name: ")
            print("Welcome " + name + "!")
            newPlayer = Message()
            newPlayer.join(name)
            skt.send(bytes(newPlayer.toString(), 'UTF-8'))
            
            #start play
            p = Play()
            p.play(skt, name)
        
    #main driver    
    if __name__ == "__main__":
       main()
     


    
    

   

   
    

                