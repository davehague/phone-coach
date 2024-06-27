from google.cloud import speech
import pyaudio

def record_audio():
    # Audio recording parameters
    RATE = 16000
    CHUNK = int(RATE / 10)  # 100ms

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Recording...")
    frames = []

    try:
        while True:
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        pass
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

    print("Recording stopped.")
    return b''.join(frames)

def speech_to_text():
    client = speech.SpeechClient()
    audio_content = record_audio()

    audio = speech.RecognitionAudio(content=audio_content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US"
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        return result.alternatives[0].transcript

    return ""

if __name__ == "__main__":
    print("Please speak something...")
    text = speech_to_text()
    print(f"Recognized text: {text}")
