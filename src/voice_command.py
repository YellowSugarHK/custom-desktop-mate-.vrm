import speech_recognition as sr

def listen_to_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return None

if __name__ == "__main__":
    command = listen_to_command()
    if command == "wave":
        print("Mate is waving!")
