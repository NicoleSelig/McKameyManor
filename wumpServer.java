import java.io.IOException;
import java.net.ServerSocket;

public class wumpServer {
    private static final int port = 10101;
    private static ServerSocket serverSocket;
    private static ClientHandler clientHandler;
    private static Thread thread;

    public static void main(String[] args) throws IOException {
        serverSocket = new ServerSocket(port);

        while(true) {
            clientHandler = new ClientHandler(serverSocket.accept());  // Accept the connection
            thread = new Thread(clientHandler);  // create a new Thread
            thread.start();  // call the run() method
        }
    }
}