import pyttsx3

engine = pyttsx3.init(driverName='sapi5')

voices = engine.getProperty('voices')

if not voices:
    print("❌ No voices found. Your system has no TTS voices installed.")
else:
    print("✅ Available Voices:")
    for index, voice in enumerate(voices):
        print(f"{index}: {voice.name} - {voice.id}")

    # Test each voice
    for index, voice in enumerate(voices):
        engine.setProperty('voice', voice.id)
        print(f"🔈 Testing voice {index}: {voice.name}")
        engine.say(f"This is voice number {index}")
        engine.runAndWait()
