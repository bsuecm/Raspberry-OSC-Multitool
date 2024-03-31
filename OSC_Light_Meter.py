import argparse
import board
from adafruit_bh1750 import BH1750
from pythonosc import udp_client
from gpiozero import Button
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="2.69.13.6",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=8000,
      help="The port the OSC server is listening on")
  parser.add_argument("--lux", type=float, default = 5.0,
      help="The threshold value in lux")
  args = parser.parse_args()
  client = udp_client.SimpleUDPClient(args.ip, args.port)
  i2c = board.I2C()
  lux_reading = BH1750(i2c).lux
  last_lux_reading = lux_reading
  osc_address = '/flash'
  
  def normal_operation():
    global lux_reading, last_lux_reading
    lux_reading = BH1750(i2c).lux
    if last_lux_reading <= args.lux and lux_reading >= args.lux:
      client.send_message(osc_address, 100)
    elif last_lux_reading >= args.lux and lux_reading <= args.lux:
      client.send_message(osc_address, 0)
    last_lux_reading = lux_reading

  while True:
    normal_operation()