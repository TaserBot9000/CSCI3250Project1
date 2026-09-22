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
for current_port in range(1, 23): #temporary range, change later
    port_scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_scan.settimeout(1.0)

    try:
        port_scan.connect((target_ip, current_port))
        print(f"Open ports: {current_port}")

    except OSError: #If connection fails dont print it.
        pass

    port_scan.close()

# Check if target IP can be reached

# Output TCP open ports on target
