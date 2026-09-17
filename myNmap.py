import sys #access to command line arguments
import ipaddress #ipv4 and ipv6 library
import socket #communicate with the network

# Check that the target was input
argument_input = len(sys.argv) #total length of argument vector

if argument_input > 1: # Ensure there was input
    # Get target IP from cmd line
    target_ip = sys.argv[1] #
    print(f"Input: {target_ip}") 
    
else:
    print(f"Nothing was input.") 
    sys.exit()

# Ensure the ip address format is enforced
try:
    ipaddress.ip_address(address=target_ip)

except ValueError:
    print(f"{target_ip} is not an IP.")
    sys.exit()
    
# Scan the TCP ports

# Check if target IP can be reached

# Output TCP open ports on target
