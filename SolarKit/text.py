import sys
import time
from art import *
from colorama import Fore, Back, Style

Art=text2art("SolarKit")
print(Fore.GREEN + Art)

def type(text):
  words = text
  for char in words:
    time.sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
type(Fore.GREEN + "Open terminal in SolarKit folder")

def type(text):
  words = text
  for char in words:
    time.sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
type(Fore.GREEN + "\n\nUsage: python main.py --help")

def type(text):
  words = text
  for char in words:
    time.sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
type(Fore.GREEN + "\n\nP.S. install modules using pip install -r requirements.txt\n\n\n")