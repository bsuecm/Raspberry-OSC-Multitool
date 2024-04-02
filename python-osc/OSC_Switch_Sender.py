import argparse
from pythonosc import udp_client
from gpiozero import Button

def send_switch(switch_number):
  client.send_message(switch_osc_map[switch_number], switch_number.value)
def switches_osc_sender():
  for switch in switch_osc_map:
    switch.when_pressed  = send_switch
    switch.when_released = send_switch
def create_osc_client(ip, port):
  return udp_client.SimpleUDPClient(ip, port)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="2.69.13.6",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=8000,
      help="The port the OSC server is listening on")
  args = parser.parse_args()
  client = create_osc_client(args.ip, args.port)
  switch_osc_map = {Button(26, bounce_time=.05): '/switch1',
                    Button(19, bounce_time=.05): '/switch2',
                    Button(13, bounce_time=.05): '/switch3',
                    Button(6 , bounce_time=.05): '/switch4'}
  while True:
    switches_osc_sender()