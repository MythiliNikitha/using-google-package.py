import socket as s
website = input("Enter website name:")
print("IP address of the website is:",s.gethostbyname(website))
