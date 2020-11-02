import java.io.*;
import java.lang.Runnable;
import java.net.Socket;
import java.util.Date;
import java.nio.charset.StandardCharsets;

class ClientHandler implements Runnable {
    private Socket clientSocket;

    ClientHandler(Socket clientSocket) {
        this.clientSocket = clientSocket;
    }

    public void run() {
        try {
            PrintStream p = new PrintStream(clientSocket.getOutputStream());
            BufferedInputStream bis = new BufferedInputStream( this.clientSocket.getInputStream() ) ;
            BufferedReader br = new BufferedReader( new InputStreamReader(bis, StandardCharsets.UTF_8));

            while (true) {
                String msg = br.readLine();
                System.out.println("received: " + msg);
                p.println(new Date() + ": " + msg);
            }
        } catch (IOException ioe) {
            System.out.println(ioe.toString());
        }
    }
}