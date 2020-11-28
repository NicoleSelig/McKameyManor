import socket
import sys
from Message import Message

class Client:
    
    playing = True
    
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
                self.quitWumpus()
            
            name = input("Welcome to Hunt the Wumpus! Enter your name: ")
            print("Hi " + name + "!")
            msg = Message()
            msg.join(name)
            self.play()
            
       
    def play(self):
        #send to server
        while self.playing:
            #read response from socket
            
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
        
    #performs a system exit
    def quitWumpus(self):
        sys.exit("Goodbye!")

    #exits the playing loop
    def home(self):
        self.playing = False
        
    #main driver    
    if __name__ == "__main__":
        main()
     


    
    

   

   
    

                