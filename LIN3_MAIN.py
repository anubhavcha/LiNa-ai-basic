from LIN1_Ear import listen
from LIN2_Mouth import speak
from brain import search_brain
from open_operation import open_youtube
from open_operation import open_code
from open_operation import open_chrome
from open_operation import open_insta
from open_operation import open_telegram
from open_operation import open_whatsapp
import webbrowser
import pyautogui as gui
from wish import wish
import threading
from brain import load_qa_data
from brain import print_animated_message
import time
from playmusic import play_music_on_youtube


qa_file_path = "C:\\Users\\Anubhav\\Desktop\\LiNa\\qna_logbook.txt"
qa_dict = load_qa_data(qa_file_path)



def main():
    wish()
    while True:
          text = listen().lower()

          if text.startswith(("who is ", "what is ", "how to ")):
            search_brain(text)

          elif "open youtube" in text or "open tube in text" in text:
              open_youtube()

          elif "open telegram" in text or "open telegram app" in text :
              open_telegram()

          elif "open instagram" in text or "open insta" in text:
              open_insta()

          elif "open chrome" in text or "open google" in text :
              open_chrome()

          elif "open whatsapp" in text or "open what'sapp" in text or "open whats app" in text or "open what's app" in text :
              open_whatsapp()

          elif "open vs code" in text or "open code editor" in text :
              open_code()


          elif "open google classroom" in text :
                  webbrowser.open("https://classroom.google.com/u/0/")

          elif "close" in text or "close this" in text or "close tab" in text:
              speak("closing the current display screen")
              gui.hotkey('alt', 'f4')

          elif text in qa_dict:
              ans = qa_dict[text]
              animate_thread = threading.Thread(target=print_animated_message, args=(ans,))
              # Create a thread for speaking the message
              speak_thread = threading.Thread(target=speak, args=(ans,))

              # Start both threads concurrently
              animate_thread.start()
              speak_thread.start()

              # Wait for both threads to finish
              animate_thread.join()
              speak_thread.join()
          elif "shutdown" in text or "shut down" in text:
            gui.hotkey('win','d')
            time.sleep(1)
            gui.hotkey('alt', 'f4')
            time.sleep(1)
            gui.press('enter')
            
          elif "good morning" in text or "good evening" in text or "good night" in text:
            wish()  

          elif "minimise" in text or "minimise the window" in text:
            gui.hotkey('win','d')

          elif "play music" in text or "play music on youtube" in text:
            speak("sir Whitch song do you want to play?")
            song_name = listen().lower()
            play_music_on_youtube(song_name)  
            
if __name__ == '__main__':
    main()
                 