import argparse
from pythonosc import udp_client
from gpiozero import Button
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="2.69.13.6",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=8000,
      help="The port the OSC server is listening on")
  args = parser.parse_args()
  client = udp_client.SimpleUDPClient(args.ip, args.port)
  switch_osc_map = {Button(26, bounce_time=.05): '/switch1',
                    Button(19, bounce_time=.05): '/switch2',
                    Button(13, bounce_time=.05): '/switch3',
                    Button(6 , bounce_time=.05): '/switch4'}
  def send_switch(switch):
    client.send_message(switch_osc_map[switch], switch.value)
  def switches_osc_sender():
    for switch in switch_osc_map:
      switch.when_pressed  = send_switch
      switch.when_released = send_switch
  def normal_operation():
    switches_osc_sender()
  while True:
    normal_operation()