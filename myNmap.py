import sys #access to command line arguments
import ipaddress #ipv4 and ipv6 library
import socket #communicate with the network

# Check that the target was input
argument_input = len(sys.argv) #total length of argument vector

if argument_input > 1: # Ensure there was input
    # Get target IP from cmd line
    target_ip = sys.argv[1] 
    print(f"Ip address: {target_ip}") 
    
else:
    print(f"Nothing was input.") 
    sys.exit()

# Ensure the IP address format is enforced
try:
    ipaddress.ip_address(address=target_ip) 

except ValueError: #handle invalid IP address
    print(f"{target_ip} is not an IP address.")
    sys.exit() 

#Attempt a TCP connection
tcp_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_connection.settimeout(1.0)
port = 8000 #test default http.server port (may need to be changed for extended port scanning)

#Try connecting to the target ip and port
try:
    tcp_connection.connect((target_ip, port))
    print(f"your connection succeeded. Port {port} reached.")

except OSError as TCP_error: 
    print(TCP_error) 
    sys.exit()

# Scan the TCP ports

# Check if target IP can be reached

# Output TCP open ports on target
