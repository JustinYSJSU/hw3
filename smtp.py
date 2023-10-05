#follow the format for SMTP messages in the book. remember each command ends with \r\n
import socket

endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.freesmtpservers.com"
smtp_port = 25

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((mailserver, smtp_port)) #connect to the mail server on port 25 (usually for smtp)
recv = clientSocket.recv(1024).decode()
print(recv)

if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
mail_from = "MAIL FROM: <justin.yamamoto@sjsu.edu>\r\n"
clientSocket.send(mail_from.encode())
recv_2 = clientSocket.recv(1024).decode()
print(f"mail from:  {recv_2}")

# Send RCPT TO command and print server response.
rcpt_to = "RCPT TO: <jyamamoto2002@gmail.com>\r\n"
clientSocket.send(rcpt_to.encode())
recv_3 = clientSocket.recv(1024).decode()
print(f"rcpt to:  {recv_3}")

# Send DATA command and print server response.
data = "DATA\r\n"
clientSocket.send(data.encode())
recv_4 = clientSocket.recv(1024).decode()
print(f"data: {recv_4}")

# Send message data. msg includes header, subject, body, and period with line endings
msg_data = "To: me <jyamamoto2002@gmail.com>\r\n"
msg_data += "From: me <justin.yamamoto@sjsu.edu\r\n"
msg_data += "Subject: cmpe148 yay!\r\n"
msg_data += "\r\n"
msg_data += "this is for cmpe148, which is obviously the best class ever\r\n"
msg_data += endmsg

clientSocket.send(msg_data.encode())
recv_5 = clientSocket.recv(1024).decode()
print(f"send msg: {recv_5}")

# Send QUIT command and get server response.
quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv_6 = clientSocket.recv(1024).decode()
print(f"quit: {recv_6}")

clientSocket.close()