import sys #access to command line arguments
import ipaddress #ipv4 and ipv6 library
import socket #communicate with the network
import subprocess #run system commands

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

#See if IP is reachable 
reachable = False 
test_ping = subprocess.run(["ping",target_ip]) #use a ping to reach IP

if test_ping.returncode == 0: #command successful
    reachable = True

if not reachable:
    print(f"{target_ip} is not reachable")
    sys.exit()

#try to connect
openPorts = 0

#Attempt a TCP connection
for current_port in range(1, 1001): 
    port_scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_scan.settimeout(0.3)
    try:
        port_scan.connect((target_ip, current_port))
        print(f"Port: {current_port} is listening.")
        openPorts += 1

    except OSError: #If connection fails dont print it.
        pass

    finally:
        port_scan.close()


# print how many open ports
print(f"\nScan finished! {openPorts} open ports found.")

