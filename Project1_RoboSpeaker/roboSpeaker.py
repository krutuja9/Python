# import os 

# if __name__ == '__main__':
#   print("Welcone to RoboSpeaker 1.1. Created by Rutuja")
#   x = input("Enter what you want me to pronounce")
#   command = f"say {x}"
#   os.system(command) 


import pyttsx3

if __name__ == "__main__":
  print ("welcome to RoboSpeaker 1.1 Created by RUtuja")
  while True:
    text_to_speak = input("Enter what you want me to pronounce\n")
    if text_to_speak == 'q':
      break
    engine = pyttsx3.init()
  
    engine.say(text_to_speak)
    engine.runAndWait()