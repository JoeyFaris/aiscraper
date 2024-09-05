import platform

def text_to_speech(text):
    """
    Convert the given text to speech using the appropriate TTS engine for the platform.
    
    Args:
    text (str): The text to be converted to speech.
    """
    try:
        if platform.system() == 'Darwin':
            print("Using macOS TTS engine")
            import subprocess
            subprocess.call(['say', text])
        else:
            import pyttsx3
            print("Initializing pyttsx3 engine")
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.setProperty('volume', 0.9)
            engine.say(text)
            engine.runAndWait()
        
        print("Text-to-speech conversion completed successfully.")
    except Exception as e:
        print(f"An error occurred during text-to-speech conversion: {str(e)}")
