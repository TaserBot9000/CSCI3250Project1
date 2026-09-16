import sys #access to command line arguments
import socket #communicate with the network

# Check that the target was input
argument_input = len(sys.argv) #total length of argument vector

if argument_input > 1: # Ensure there was input
    # Get target IP from cmd line
    target_ip = sys.argv[1] #
    print(f"Input: {target_ip}") 
    
else:
    print("Nothing was input.") 

# Scan the TCP ports

# Check if target IP can be reached

# Output TCP open ports on target
