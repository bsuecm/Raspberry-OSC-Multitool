import argparse
from pythonosc import udp_client
from gpiozero import Button

switch =         [Button(26, bounce_time=.05),
                  Button(19, bounce_time=.05),
                  Button(13, bounce_time=.05),
                  Button(6 , bounce_time=.05)]

def send_switch1(button_input):
  client.send_message('/switch5', int(button_input.value))
def send_switch2(button_input):
  client.send_message('/switch6', int(button_input.value))
def send_switch3(button_input):
  client.send_message('/switch7', int(button_input.value))
def send_switch4(button_input):
  client.send_message('/switch8', int(button_input.value))
def switches_osc_sender():
  switch[0].when_pressed  = send_switch1
  switch[0].when_released = send_switch1
  switch[1].when_pressed  = send_switch2
  switch[1].when_released = send_switch2
  switch[2].when_pressed  = send_switch3
  switch[2].when_released = send_switch3
  switch[3].when_pressed  = send_switch4
  switch[3].when_released = send_switch4
def create_osc_client(ip, port):
  return udp_client.SimpleUDPClient(ip, port)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="2.69.13.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=8000,
      help="The port the OSC server is listening on")
  args = parser.parse_args()
  client = create_osc_client(args.ip, args.port)
  
  while True:
    switches_osc_sender()