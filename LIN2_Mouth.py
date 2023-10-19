import tempfile
from gtts import gTTS
import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

def speak(text, language='en'):
    try:
        # Create a temporary file for each utterance
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            temp_file_name = temp_file.name

        # Create a gTTS object with the text and language
        tts = gTTS(text=text, lang=language)

        # Save the speech to the temporary file
        tts.save(temp_file_name)

        # Load and play the temporary audio file
        pygame.mixer.music.load(temp_file_name)
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

    except Exception as e:
        print("Error:", e)

# Example usage

