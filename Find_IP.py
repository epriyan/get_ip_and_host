import socket

def host_to_ip():
    try:
        host = input("Enter the host name / host url : ")
        ip = socket.gethostbyname(host)
        print("IP Address of ",host," : ",ip)
    except socket.gaierror:
        print("Unable to resolve host")

def ip_to_url():
    try:
        ip = input("Enter the IP Address: ")
        url = socket.gethostbyaddr(ip)[0]
        print("Host Name of ", ip," : ",url)
    except socket.herror:
        print("No domain associated with this IP")

#Main        
print("Select the options given below")
print()
print("1. Get IP of the host")
print()
print("2. Get Host Name of an IP")
print()
print()

option = 0

try:
    option = int(input("Enter your option: "))
    print()
    print()
except ValueError:
    print("Incorrect option")

if(option==1):
    host_to_ip()
elif(option==2):
    ip_to_url()
else:
    print("Invalid option")
    
    
