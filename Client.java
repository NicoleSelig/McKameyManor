import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class Client {
    //create a socket
    Socket theSocket = new Socket(hostname, port);
    DataOutputStream dos = new DataOutputStream(theSocket.getInputStream());

    BufferedInputStream bis = new BufferedInputStream(theSocket.getInputStream());
    BufferedReader br = new BufferedReader(new InputStreamReader(bis, StandardCharsets.UTF_8));

    Scanner scanner = new Scanner(System.in);
    String message = "";
    //connect to the server IP + Port
    
    //sock.getOutputStream()
    //sock.getInputStream()


    boolean playing = true;

    while(playing){
        // prompt the user for input and read it (sc.readLine())
        System.out.println("Enter Message: ");
        message = scanner.nextLine();
        dos.writeBytes(message + "\n");

        String msg = br.readLine();
        // send a message to the server (format the message)
        // wait/recieve a response from the server
        // print the response
        if (message == "quit") { playing = false;}
        //if msg = "quit" {sock.close(); System.exit(0);}
        System.out.println("[" + hostname + "]:" + msg);
    }
    while (!message.equals("quit")){

    }
    theSocket.close();
}


// //move or shoot? (m-s) m
// to room? 5

// join 
// move|5
// shoot|6
// quit


//Response:
//adjacent rooms
//game state (dead, hunted the wumpus, something else)
//Message -- what's nearby
