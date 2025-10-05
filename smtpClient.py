from socket import *

msg = "\r\nI love computer networks!"
endmsg = "\r\n.\r\n"

# For this lab I am using SMPT4DEV, which is a local mimic of an email server (localhost or 127.0.0.1 on port 25)
# The reason for using this is the specific requirement to not use TLS, which automatically elimiates my existing email accounts (gmail, outlook, etc)
# This is because those email servers require TLS to establish a connection, so hence they cannot be used for this lab

mailserver = ("localhost", 25)  

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response
mailFrom = "MAIL FROM:<nbertoli32572@ucumberlands.edu>\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

# Send RCPT TO command and print server response
rcptTo = "RCPT TO:<nicFer@local.com>\r\n" # using a mock email that I created inside the local smpt4dev server
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)

# Send DATA command and print server response
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)

# Send message data
clientSocket.send(msg.encode())

# Message ends with a single period
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)

# Send QUIT command and get server response
quitCommand = "QUIT\r\n"
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)

clientSocket.close()
