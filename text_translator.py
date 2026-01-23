from deep_translator import GoogleTranslator
from gtts import gTTS
import os
from playsound import playsound

def translate_text(input_text, target_lang, output_type="text"):
    translated_text = GoogleTranslator(source="auto", target=target_lang).translate(input_text)

    if output_type == "voice":
        try:
            audio_path = os.path.join(os.getcwd(), "translated_audio.mp3")
            tts = gTTS(text=translated_text, lang=target_lang.split("-")[0])  # just main lang code
            tts.save(audio_path)
            playsound(audio_path)
        except Exception as e:
            return f"Voice output error: {e}"
        return None
    else:
        return translated_text
