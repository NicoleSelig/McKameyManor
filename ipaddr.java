//ipv4 addresses are 32-bits
//typically write them in dotted-quad notation, eg 159.242.4.87
//each segment is one byte (0-255)
//netmask is  32-bit value, 1s then 0s

//159.242.0.0/22
//159       242     00000001 00000001
//11111111 11111111 11111100 00000000
//159       242     00000000 00000000


//159.131.12.5/24 //cidr notation -- ip address thats in the network 
//10.131.12.0 - 10.131.12.255

public class ipaddr {

    int address;
    int netmask;

    public ipaddr(int addr){

    }

    public ipaddr(String cidr){
        String[] parts = cidr.split("/");
        this.setMask(Integer.parseInt(parts[1]));
        this.setAddress(parts[0]);
    }

    void setAddress(String ip){
        String [] octets = ip.split("."); //get 4 separate values
        int o = 0;
        for (int i = 0; i < 4; i ++) {
            o = Integer.parseInt(octets[0]);
        }
        //use bitwise shift again to slide it into the correct position
        this.address = this.address << 8;
        this.address += o;
    }

    // 0000 0000
    // 0000 0001
    // 0000 0010
    // 0000 0011
    // 0000 0110
    void setMask(int nm){
        for (int i = 0; i < nm; i++){
            this.netmask = this.netmask << 1; // << - bitwise shift to the left
            this.netmask += 1;
        }
        this.netmask = this.netmask << (32 - nm - 1);
        this.printHex(this.netmask);

    }

    void printHex(int i) {
        System.out.println(String.format("0x%08X", i)); //prints 8 hex digits 
    }

    @Override
    public String toString(){
        return "";
    }

    //work on a function to reverse that process
    public void reverseShift(){

    }
    
}
