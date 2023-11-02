from gtts import gTTS
message = ""
tts = gTTS(message)
tts.save("audio.mp3")