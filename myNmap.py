# python3 myNmap.py 127.0.0.1

import sys #access to command line arguments
import ipaddress #ipv4 and ipv6 library
import socket #communicate with the network

# Check that the target was input
argument_input = len(sys.argv) #total length of argument vector

if argument_input > 1: # Ensure there was input
    # Get target IP from cmd line
    target_ip = sys.argv[1] 
    print(f"Input: {target_ip}") 
    
else:
    print(f"Nothing was input.") 
    sys.exit()

# Ensure the ip address format is enforced
try:
    ipaddress.ip_address(address=target_ip) 

except ValueError: #Return a value error if any non-ip is put
    print(f"{target_ip} is not an IP.")
    sys.exit() 

#Attempt a TCP connection
tcp_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 80 #try connecting to a listening port

try:
    tcp_connection.connect((target_ip, port))
    print("your connection succeeded.")

except OSError as TCP_error:
    print(TCP_error)
    sys.exit()
    
# Scan the TCP ports

# Check if target IP can be reached

# Output TCP open ports on target
