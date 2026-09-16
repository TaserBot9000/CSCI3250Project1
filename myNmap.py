import sys #access to command line arguments
import socket #communicate with the network

# Check that the target was input
argument_input = len(sys.argv) #total length of argument vector

if argument_input > 1:
    print(f"Input: {sys.argv[1]}") #temporary test
else:
    print("Nothing was input.")

# Get target IP from cmd line

# Scan the TCP ports

# Check if target IP can be reached
