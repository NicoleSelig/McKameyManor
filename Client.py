import socket
import sys
from Message import Message
from Play import Play


class Client:
    
    #main menu loop
    def main():
        p = Play()
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
            
            name = input("Welcome to Hunt the Wumpus! Enter your name: ")
            print("Hi " + name + "!")
            newPlayer = Message()
            newPlayer.join(name)
            print(newPlayer.toString())
            skt.sendall(bytes(newPlayer.toString(), 'UTF-8'))
            print("socket sent")
            joinresponse = skt.recv(1024)
            print(str(joinresponse))
        
    #main driver    
    if __name__ == "__main__":
       main()
     


    
    

   

   
    

                