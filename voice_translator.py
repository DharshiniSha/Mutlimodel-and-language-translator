import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
from playsound import playsound

recognizer = sr.Recognizer()

def translate_voice(target_lang, output_type="text"):
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = recognizer.listen(source)

    try:
        original_text = recognizer.recognize_google(audio)
        translated_text = GoogleTranslator(source="auto", target=target_lang).translate(original_text)

        if output_type == "voice":
            try:
                audio_path = os.path.join(os.getcwd(), "translated_voice.mp3")
                tts = gTTS(text=translated_text, lang=target_lang.split("-")[0])
                tts.save(audio_path)
                playsound(audio_path)
            except Exception as e:
                return f"Voice output error: {e}"
            return None
        else:
            return translated_text

    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Speech recognition error: {e}"
