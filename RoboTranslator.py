from gtts import gTTS
import os
from playsound3 import playsound
import pygame
from googletrans import Translator


def translate_and_speak(text, dest_language='en'):
    # Initialize translator
    translator = Translator()

    # Translate text
    translated_text = translator.translate(text, dest=dest_language).text

    # Convert translated text to speech
    tts = gTTS(text=translated_text, lang=dest_language)
    tts.save("translated_audio.mp3")

    # Play the translated audio
    playsound("translated_audio.mp3")

    # Delete the temporary audio file
    os.remove("translated_audio.mp3")


if __name__ == "__main__":
    print("Top 10 language abbreviations:")
    print("1. English: en")
    print("2. Spanish: es")
    print("3. French: fr")
    print("4. German: de")
    print("5. Mandarin Chinese: zh-CN")
    print("6. Hindi: hi")
    print("7. Arabic: ar")
    print("8. Russian: ru")
    print("9. Portuguese: pt")
    print("10. Bengali: bn")

    while True:
        text_to_translate = input("Enter the text to translate (or enter '$$$' to exit): ")
        if text_to_translate == "$$$":
            break

        print("Enter the destination language abbreviation (e.g., 'fr' for French, 'es' for Spanish): ")
        destination_language = input()

        translate_and_speak(text_to_translate, destination_language)
